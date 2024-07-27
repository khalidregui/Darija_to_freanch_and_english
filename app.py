import streamlit as st
from translator import translate_text

# Configuration de la page
st.set_page_config(page_title="Traducteur Darija", layout="centered")

# Affichage de l'image de fond
st.image("moroccobg.jpj", use_column_width=True)

st.title("Traducteur Darija")
st.write("Traduisez des phrases en Darija (dialecte marocain) en Arabe, Français et Anglais.")

# Entrée utilisateur
darija_text = st.text_area("Entrez une phrase en Darija :")

if st.button("Traduire"):
    if darija_text:
        french_translation = translate_text(darija_text, "French")
        english_translation = translate_text(darija_text, "English")

        st.subheader("Traductions :")
        st.write(f"**Français :** {french_translation}")
        st.write(f"**Anglais :** {english_translation}")
    else:
        st.error("Veuillez entrer une phrase en Darija.")
