import streamlit as st
import requests

st.set_page_config(page_title="CareerAgent - AI Recruitment Assistant", page_icon="🚀", layout="centered")

st.title(" CareerAgent")
st.subheader("Ton assistant IA autonome pour la recherche de stages et d'emplois")

WEBHOOK_URL = "YOUR_N8N_WEBHOOK_URL"

uploaded_file = st.file_uploader("📂 Importe ton CV (PDF) pour commencer :", type=["pdf"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Écris ta demande (ex: Je cherche un stage...) :"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("CareerAgent analyse ton profil et ta demande..."):
            try:
                # Préparation des données à envoyer en multipart
                data = {"chatInput": prompt}
                files = None
                
                if uploaded_file is not None:
                    # On envoie le fichier directement en binaire sous le nom 'data'
                    files = {"data": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}

                # Envoi de la requête au webhook n8n
                response = requests.post(WEBHOOK_URL, data=data, files=files)
                
                if response.status_code == 200:
                    try:
                        res_data = response.json()
                        agent_reply = res_data.get("output", res_data.get("text", str(res_data)))
                    except:
                        agent_reply = response.text
                else:
                    agent_reply = f"Erreur de communication avec n8n (Code {response.status_code})"
                
                st.markdown(agent_reply)
                st.session_state.messages.append({"role": "assistant", "content": agent_reply})
            
            except Exception as e:
                st.error(f"Impossible de joindre le webhook n8n : {e}")