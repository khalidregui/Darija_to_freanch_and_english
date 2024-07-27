import os
import openai

# Récupérer la clé API depuis les variables d'environnement
openai.api_key = os.getenv("OPENAI_API_KEY")

def translate_text(text, target_language):
    """
    Utilise l'API OpenAI pour traduire le texte en langue cible.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100
    )
    translation = response.choices[0].message['content'].strip()
    return translation
