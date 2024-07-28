import streamlit as st
import openai
import os

# Charger la clé API OpenAI depuis les variables d'environnement
openai.api_key = os.getenv("OPENAI_API_KEY")

# Configuration de la page Streamlit
st.set_page_config(page_title="Traducteur Darija", page_icon="🌍", layout="centered")

# Titre de l'application
st.title("Traducteur Darija 🌍")
st.markdown("### Traduisez des phrases en Darija vers le Français et l'Anglais")

# Saisie de la phrase en Darija
darija_text = st.text_area("Entrez une phrase en Darija:")

# Bouton de traduction
if st.button("Traduire"):
    if darija_text:
        # Appel à l'API OpenAI pour la traduction
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=f"Traduisez cette phrase en Darija en Français et en Anglais:\n\nDarija: {darija_text}\n\nFrançais:\n\nAnglais:",
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5,
        )
        
        # Extraction des traductions
        translations = response.choices[0].text.strip().split("\n\n")
        french_translation = translations[0].replace("Français:", "").strip()
        english_translation = translations[1].replace("Anglais:", "").strip()
        
        # Affichage des résultats
        st.markdown("### Traduction en Français")
        st.write(french_translation)
        
        st.markdown("### Traduction en Anglais")
        st.write(english_translation)
    else:
        st.error("Veuillez entrer une phrase en Darija.")
