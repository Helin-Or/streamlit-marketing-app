# feedback_page.py

import streamlit as st

def app():
    st.title('Feedback geben')

    st.write("""
    ### Feedback zur App-Nutzung

    Teilen Sie uns Ihre Erfahrungen mit der Nutzung der Anwendung mit.
    Wir schätzen Ihr Feedback, um unsere App kontinuierlich zu verbessern.


    """)

    # Eingabefelder für das Feedback
    with st.form(key='app_feedback_form'):
        st.subheader("Bitte geben Sie Ihr Feedback ein:")
        
        experience_rating = st.selectbox("Wie würden Sie Ihre Erfahrung mit der App bewerten?", ["Sehr gut", "Gut", "Durchschnittlich", "Schlecht"])

        improvement_suggestions = st.text_area("Welche Verbesserungsvorschläge haben Sie für die App?")
        
        st.subheader("Bitte geben Sie Ihre Kontaktdaten an (optional, aber hilfreich für Rückfragen):")
        name = st.text_input("Ihr Name:")
        company_department = st.text_input("Unternehmen/Abteilung:")
        contact_info = st.text_input("Kontaktinformationen:")

        privacy_policy = st.checkbox("Ich stimme den Datenschutzbestimmungen zu.")

        # Knopf zum Absenden des Formulars
        submit_button = st.form_submit_button("Feedback absenden")

        if submit_button:
            # Speichern der Feedback-Daten oder weiterverarbeiten
            feedback_data = {
                'experience_rating': experience_rating,
                'improvement_suggestions': improvement_suggestions,
                'name': name,
                'company_department': company_department,
                'contact_info': contact_info
            }

            # Hier könntest du die Feedback-Daten weiterverarbeiten oder speichern
            st.success("Vielen Dank für Ihr Feedback!")

    # Hinweise zur Nutzung der Feedbackseite
    st.write("""
    #### Hinweise zur Nutzung der Feedbackseite:

    - Geben Sie konstruktives Feedback, um uns bei der Verbesserung der App zu helfen.
    - Ihre Rückmeldungen sind anonym, es sei denn, Sie geben freiwillig Ihren Namen und Ihre Kontaktinformationen an.
    - Wir schätzen Ihr Feedback und nutzen es zur kontinuierlichen Verbesserung unserer Anwendung.
    """)

if __name__ == "__main__":
    app()