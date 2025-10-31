import json
import ollama
import psycopg2



model = "llama3.1:latest"
model2 = "gpt-oss:20b"




def calcule_mtn(id_contrat=292418):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        
        cur = conn.cursor()
        cur.execute("select * from gescli.fc_montant_total(%s)", (id_contrat,))
        result = cur.fetchone()[0]
        cur.close()
        conn.close()
        return f"Le montant total du contrat {id_contrat} est {result}."
    except Exception as e:
        return "Veuillez reesaye"


def compter_factures(id_contrat=311149):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    query = """
        select * from fc_nombre_total_facture(%s)
    """
    cur.execute(query, (id_contrat,))
    result = cur.fetchone()[0] or 0
    cur.close()
    conn.close()
    return f"Le contrat {id_contrat} contient {result} facture(s)."


def resilie(id_contrat=311149):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute("select * from gescli.fc_resiliation(%s)", (id_contrat,))
        result = cur.fetchone()[0]
        cur.close()
        conn.close()
        return result
    except Exception as e:
        return "Veuillez reesaye "



TOOL_EXECUTORS = {
    "calcule_mtn": calcule_mtn,
    "compter_factures": compter_factures,
    "resilie": resilie,
}



TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "calcule_mtn",
            "description": "Permet d'obtenir le solde total du client.",
            "parameters": {
                "type": "object",
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "compter_factures",
            "description": "Compte le nombre de factures pour un contrat donné.",
            "parameters": {
                "type": "object",
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "resilie",
            "description": "Récupère les informations sur la résiliation pour un contrat donné.",
            "parameters": {
                "type": "object",
                
            }
        }
    }
]


def chatbot_edd_id_contrat_(user_msg: str):
    messages = [
        {
            "role": "system",
            "content": (
                "Tu es un assistant francophone. "
                "Utilise l’outil lorsque c’est approprié. "
                "Répond uniquement aux questions qui nécessitent un outil ; sinon dis « je ne sais pas ». "
                " Ne repond pas a une question qui neccessite pas un outil "
                "Après un appel d’outil, retourne le résultat de la fonction ET ajoute un message bienveillant personnalisé pour calme  le client."
            )
        },
        {"role": "user", "content": user_msg}
    ]

    while True:
        response = ollama.chat(
            model=model2,
            messages=messages,
            tools=TOOLS,
           
        )

        msg = response["message"]
        tool_calls = msg.get("tool_calls", [])

        
        if not tool_calls:
            return msg.get("content", "")

        # Ajouter la demande d'outils de l'assistant au fil
        #messages.append({
        #    "role": "assistant",
        #    "content": msg.get("content", ""),
        #    "tool_calls": tool_calls,
        #})

        # Exécuter chaque tool demandé
        for call in tool_calls:
            fn = call["function"]
            name = fn["name"]
            args = fn.get("arguments", {})

           
            if isinstance(args, str) and args.strip():
                try:
                    args = json.loads(args)
                except Exception:
                    args = {}

            if not isinstance(args, dict):
                args = {}

        
            #args["id_contrat"] = m_contrat

            # Appeler la fonction Python
            try:
                result = TOOL_EXECUTORS[name](**args)
            except TypeError as e:
                result = f"Arguments invalides pour {name}: {e}"
            except Exception as e:
                result = f"Erreur lors de l'exécution de {name}: {e}"
            
            messages.append({
                "role": "assistant",
                "content": f"Voici le résultat brut de l’outil **{name}** :\n\n{result}"
            })
            # Retourner le résultat de l’outil au modèle (contenu en texte/JSON)
            messages.append({
                "role": "tool",
                "tool_call_id": call.get("id", name),
                "name": name,
                "content": json.dumps({"result": result}, ensure_ascii=False)
            })





