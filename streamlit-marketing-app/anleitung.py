import streamlit as st

def app():
    st.title('Anleitung zur Nutzung der App')

    st.write("""
    Herzlich Willkommen. Diese App hilft Ihnen dabei, detaillierte und ansprechende Produktbeschreibungen zu erstellen.
    
    Im Folgenden finden Sie eine Schritt-für-Schritt-Anleitung zur Nutzung der App:""")

    st.header('Schritt 1: Produktinformationen eingeben')

             
    st.write("""
    Gehen Sie zur Seite 'Produktinformationen' und füllen Sie die Felder mit den relevanten Daten für Ihr Produkt aus.
    Dazu gehören:
    - Produktname
    - Kategorie
    - Preis
    - Vorteile des Produkts
    - Zielgruppen
    - Artikelnummer
    - Farbe
    - Größe
    - Material
    - Pflegehinweise

    Nachdem Sie alle Informationen eingegeben haben, klicken Sie auf 'Produktdaten speichern'.
    """)

    st.header('Schritt 2: Produktdaten anzeigen')
    st.write("""
    Wechseln Sie zur Seite 'Produktdaten', um eine Übersicht der eingegebenen Produktinformationen zu sehen.
    Sie können die Daten auch als .txt-Datei herunterladen.
    """)
    st.write("Zusätzlich können Sie die angezeigten Informationen kopieren, indem Sie auf das Kopieren-Symbol oben rechts klicken.")

    st.header('Schritt 3: Produktbeschreibung generieren')
    st.write("""
    Gehen Sie zur Seite 'Produktbeschreibung generieren', um die automatisch geladenen Produktinformationen zu überprüfen und den initialen Prompt für die Produktbeschreibung anzupassen. Kopieren Sie den initialen Prompt aus dem Textfeld und fügen Sie ihn im Chatfenster ein, um die Generierung der Produktbeschreibung zu starten. Nach der Generierung können Sie die erstellte Produktbeschreibung überprüfen und bei Bedarf anpassen. Stellen Sie sicher, dass alle wichtigen Details korrekt wiedergegeben werden und der Stil der Beschreibung Ihren Erwartungen entspricht.
    """)

    st.header('Feedback geben')
    st.write("""
    Möchten Sie uns Feedback zur App geben? Besuchen Sie die Seite 'Feedback' und teilen Sie uns Ihre Erfahrungen mit der Nutzung der Anwendung mit. Wir schätzen Ihr Feedback, um unsere App kontinuierlich zu verbessern.
    """)

    st.header('Hinweis')
    st.write("""
    Stellen Sie sicher, dass Sie alle erforderlichen Informationen korrekt eingegeben haben, um eine präzise und 
    ansprechende Produktbeschreibung zu erhalten.
    \n Falls die API überlastet ist, versuchen Sie es bitte später erneut.
    """)

if __name__ == "__main__":
    app()