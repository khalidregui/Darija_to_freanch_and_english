import streamlit as st
from translator import translate_text

# Configuration de la page
st.set_page_config(page_title="Traducteur Darija", layout="centered")

# CSS pour définir l'image de fond
page_bg_img = '''
<style>
.stApp {
  background-image: url("moroccobg.jpg");
  background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Traducteur Darija")
st.write("Traduisez des phrases en Darija (dialecte marocain) en Français et Anglais.")

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
