import streamlit as st

def app():
    st.title('Produktdaten anzeigen')

    # Check if product_informationen is available in session state
    if 'produkt_informationen' in st.session_state:
        produkt_informationen = st.session_state['produkt_informationen']

        # Format product data as a plain text string
        produkt_informationen_txt = "\n".join([f"{key}: {value}" for key, value in produkt_informationen.items()])

        # Display product data using markdown for better readability
        st.text("Produktinformationen")
        st.markdown(f"```\n{produkt_informationen_txt}\n```")

        # Create a button to download the product data as a .txt file
        st.download_button(
            label="Produktinformationen herunterladen",
            data=produkt_informationen_txt,
            file_name='produktinformationen.txt',
            mime='text/plain',
        )
    else:
        st.warning("Keine Produktinformationen gefunden. Bitte erstellen Sie die Produktinformationen auf der ersten Seite.")

if __name__ == "__main__":
    app()