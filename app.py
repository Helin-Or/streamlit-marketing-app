 # Importing required packages
import streamlit as st
import produktinformationen
import openai_model
import produktdaten
import feedback
import anleitung


# To use this app, you need an .env file with the OPENAI API
# and you need to fill in the ID in the assistant.py file

PAGES = {
    "Produktinformationen": produktinformationen,
    "Produktdaten": produktdaten,
    "Produktbeschreibung generieren": openai_model,
    "Feedback": feedback,
    "Anleitung": anleitung,
  

}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page.app()