import streamlit as st
from translator import translate_text

# Configuration de la page
st.set_page_config(page_title="Traducteur Darija", layout="centered")

st.title("Traducteur Darija")
st.write("Traduisez des phrases en Darija (dialecte marocain) en Arabe, Français et Anglais.")

# Entrée utilisateur
darija_text = st.text_area("Entrez une phrase en Darija :")

if st.button("Traduire"):
    if darija_text:
        arabic_translation = translate_text(darija_text, "Arabic")
        french_translation = translate_text(darija_text, "French")
        english_translation = translate_text(darija_text, "English")

        st.subheader("Traductions :")
        st.write(f"**Arabe :** {arabic_translation['choices'][0]['message']['content'].strip()}")
        st.write(f"**Français :** {french_translation['choices'][0]['message']['content'].strip()}")
        st.write(f"**Anglais :** {english_translation['choices'][0]['message']['content'].strip()}")
    else:
        st.error("Veuillez entrer une phrase en Darija.")
