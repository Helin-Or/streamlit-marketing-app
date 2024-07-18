import streamlit as st

def app():
    st.title('Produktinformationen erfassen')

    # Eingabefelder für grundlegende Informationen des Produkts
    with st.form(key='product_form'):
        produktname = st.text_input("Produktname", "Guess Noelle Shoulder Bag")
        kategorie = st.text_input("Kategorie", "Handtasche")
        preis = float(st.text_input("Preis (€)", value='124.95'))
        vorteile = st.text_area("Vorteile des Produkts", "Reißverschlussfach hinten, abnehm- und längenverstellbarer Tragehenkel, drei Kartensteckfächer sowie ein Reißverschlussfach innen")
        zielgruppen = st.text_area("Zielgruppen", "Damen")
        artikelnummer = st.text_input("Artikelnummer", "GU151H4ZZ-Q11")
        farbe = st.text_input("Farbe", "Schwarz")
        groesse = st.text_area("Größe", "Höhe: 18 cm\nBreite: 29 cm\nTiefe: 6 cm\nLänge: 63 cm")
        material = st.text_area("Material", "Obermaterial: Polyurethan\nFutter: Textil\nMaterialkonstruktion: Kunstleder")
        pflegehinweise = st.text_area("Pflegehinweise", "Nicht bügeln\nNicht waschen\nNicht bleichen\n")

        # Knopf zum Absenden des Formulars
        submit_button = st.form_submit_button("Produktdaten speichern")

        if submit_button:
            # Speichern der Produkt-Daten im session_state
            st.session_state['produkt_informationen'] = {
                'Produktname': produktname,
                'Kategorie': kategorie,
                'Preis': preis,
                'Vorteile': vorteile,
                'Zielgruppen': zielgruppen,
                'Artikelnummer': artikelnummer,
                'Farbe': farbe,
                'Groesse': groesse,
                'Material': material,
                'Pflegehinweise': pflegehinweise
            }

            st.success("Produktinformationen gespeichert.")

# Dieser Teil ist für Testzwecke, wenn Sie dieses Skript einzeln laufen lassen.
if __name__ == "__main__":
    app()