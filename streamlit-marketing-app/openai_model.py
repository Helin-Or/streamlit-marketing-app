 # Importing required packages
import streamlit as st
import openai
import uuid
import time
from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
from assistant import OPENAI_ASSISTANT



def app():
    st.title('Produktbeschreibung generieren')

    # Initialize OpenAI client
    client = OpenAI()


    # Initialize session state variables
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())

    if "run" not in st.session_state:
        st.session_state.run = {"status": None}

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "retry_error" not in st.session_state:
        st.session_state.retry_error = 0


# Initialize OpenAI assistant
    if "assistant" not in st.session_state:
        openai.api_key = os.getenv('OPENAI_API_KEY')
        st.session_state.assistant = openai.beta.assistants.retrieve(OPENAI_ASSISTANT)
        st.session_state.thread = client.beta.threads.create(
            metadata={'session_id': st.session_state.session_id}
     )

# Display chat messages
    elif hasattr(st.session_state.run, 'status') and st.session_state.run.status == "completed":
        st.session_state.messages = client.beta.threads.messages.list(
            thread_id=st.session_state.thread.id
     )
        for message in reversed(st.session_state.messages.data):
            if message.role in ["user", "assistant"]:
                with st.chat_message(message.role):
                    for content_part in message.content:
                        message_text = content_part.text.value
                        st.markdown(message_text)


# Vorbereiten des initialen Prompts
    if 'produkt_informationen' in st.session_state:
        produkt_informationen = st.session_state['produkt_informationen']

        # Extract size information
        groesse_info = produkt_informationen['Groesse'].split('\n')
        groesse_dict = {item.split(': ')[0]: item.split(': ')[1] for item in groesse_info if ': ' in item}
        
        # Extract material information
        material_info = produkt_informationen['Material'].split('\n')
        material_dict = {item.split(': ')[0]: item.split(': ')[1] for item in material_info if ': ' in item}

        # Extract pflegehinweise information
        pflegehinweise_lines = produkt_informationen['Pflegehinweise'].split('\n')
        pflegehinweise_formatted = "\n".join(f"    - {line}" for line in pflegehinweise_lines if line) #macht Bindestrich vor jedem Pflegehinweis
        


        
    # Konvertieren der Daten in einen lesbaren String
        #produkt_informationen_str = "\n".join([f"{key}: {value}" for key, value in produkt_informationen.items()])

        initial_prompt = f"""# Schritt 1: Generiere den ersten Abschnitt der Produktbeschreibung
    
Erstelle eine detaillierte Produktbeschreibung basierend auf den folgenden Produktinformationen: 
        
# Context
Das Produkt ist eine {produkt_informationen['Kategorie']} namens {produkt_informationen['Produktname']}.

# Objective
Unser Ziel ist es, die die einzigartigen Vorteile und Merkmale der 
{produkt_informationen['Produktname']} hervorzuheben, um potenzielle Käufer zu überzeugen.

# Mode
Adoptiere eine professionelle und ansprechende Persona, die das Vertrauen und das Interesse 
der Kunden weckt.

# People of Interest
Die Zielgruppe dieses Produkts sind hauptsächlich {produkt_informationen['Zielgruppen']}, die Wert auf Qualität und Design legen.

# Attitude 
Der emotionale Ton der Beschreibung sollte freundlich, informativ und einladend sein.

# Style 
Verwende einen klaren, prägnanten und überzeugenden Schreibstil, der die Vorzüge und Besonderheiten der {produkt_informationen['Produktname']} überzeugend kommuniziert.

# Specifications
Preis: {produkt_informationen['Preis']}
Farbe: {produkt_informationen['Farbe']}
Größe: 
    - Höhe: {groesse_dict.get('Höhe', 'N/A')}
    - Breite: {groesse_dict.get('Breite')}
    - Tiefe: {groesse_dict.get('Tiefe')}
    - Länge: {groesse_dict.get('Länge')}

Material: 
    - Obermaterial: {material_dict.get('Obermaterial')}
    - Futter: {material_dict.get('Futter', 'N/A')}
    - Materialkonstruktion: {material_dict.get('Materialkonstruktion')}

Pflegehinweise: 
{pflegehinweise_formatted}

Vorteile: {produkt_informationen['Vorteile']}
Artikelnummer: {produkt_informationen['Artikelnummer']} 
        
# Schritt 2: Bitte geben Sie Feedback zur generierten Produktbeschreibung: Entspricht sie Ihren Anforderungen und Erwartungen? Falls Änderungen oder Anpassungen notwendig sind, lassen Sie es mich wissen.
"""
        
    else:
         initial_prompt = "Bitte geben Sie Produktinformationen ein."

# Anzeigen des initialen Prompts
    st.text_area("Initialer Prompt (kopieren und bei Bedarf bearbeiten):", initial_prompt, height=100)


# Chat input and message creation with file ID
    if prompt := st.chat_input("Was kann ich für Sie tun?"):
        with st.chat_message('user'):
            st.write(prompt)

        message_data = {
            "thread_id": st.session_state.thread.id,
            "role": "user",
            "content": prompt
        }

    # Include file ID in the request if available
        if "file_id" in st.session_state:
            message_data["file_ids"] = [st.session_state.file_id]

        st.session_state.messages = client.beta.threads.messages.create(**message_data)

        st.session_state.run = client.beta.threads.runs.create(
            thread_id=st.session_state.thread.id,
         assistant_id=st.session_state.assistant.id,
        )
        if st.session_state.retry_error < 3:
            time.sleep(1)
            st.rerun()

# Handle run status
    if hasattr(st.session_state.run, 'status'):
        if st.session_state.run.status == "running":
            placeholder = st.empty()
            with placeholder.container():
                with st.chat_message('assistant'):
                    st.write("Thinking ......")

        elif st.session_state.run.status == "failed":
            st.session_state.retry_error += 1
            with st.chat_message('assistant'):
                if st.session_state.retry_error < 3:
                    st.write("Run failed, retrying ......")
                    time.sleep(3)
                    st.rerun()
                else:
                    st.error("FAILED: The OpenAI API is currently processing too many requests. Please try again later ......")

        elif st.session_state.run.status != "completed":
            st.session_state.run = client.beta.threads.runs.retrieve(
                thread_id=st.session_state.thread.id,
                run_id=st.session_state.run.id,
         )
            if st.session_state.retry_error < 3:
                time.sleep(3)
                st.rerun()


if __name__ == "__main__":
    app()