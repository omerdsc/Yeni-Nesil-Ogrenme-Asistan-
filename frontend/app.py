import streamlit as st
import requests

st.set_page_config(page_title="Kişisel Öğrenme Asistanı", layout="wide")
st.title("📚 Yeni Nesil Öğrenme Asistanı")

# Dosya yükleme
uploaded_file = st.file_uploader("Not dosyanızı yükleyin (.txt)", type=["txt"])

if uploaded_file:
    # Dosyayı backend'e gönder
    files = {"file": uploaded_file}
    response = requests.post("http://localhost:8000/upload", files=files)

    if response.status_code == 200:
        st.success("✅ Dosya başarıyla yüklendi.")
    else:
        st.error("❌ Dosya yüklenemedi.")

# Soru sorma
question = st.text_input("Bir soru sorun:")

if st.button("Sor") and question:
    res = requests.post("http://localhost:8000/ask", json={"user_input": question})
    if res.status_code == 200:
        st.write("**Cevap:**")
        st.success(res.json()["answer"])
    else:
        st.error("Sunucudan cevap alınamadı.")
