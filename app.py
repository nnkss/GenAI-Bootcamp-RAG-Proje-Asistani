
import streamlit as st
import os
import shutil
# Gerekli RAG Kütüphaneleri
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from google.colab import userdata # API Anahtarını çekmek için


# --- RAG SİSTEMİ KURULUMU (Önbellekte Tutulur) ---
@st.cache_resource
def setup_rag_system():
    # API Anahtarını geçici dosyadan okuma
    api_key_path = "GEMINI_API_KEY_TEMP"
    if os.path.exists(api_key_path):
        with open(api_key_path, 'r') as f:
            gemini_api_key = f.read().strip()
    else:
        st.error("KRİTİK HATA: API Anahtarı Streamlit ortamında bulunamadı. Lütfen Colab'da Adım 2'yi kontrol edin.")
        return None

    # --- Diğer RAG kurulum kodlarınız buraya gelir (Kod Bloğu 2 ile aynı mantık) ---
    pdf_path = "GenAI Bootcamp Proje Dosyası.pdf"
    if not os.path.exists(pdf_path):
        st.error(f"HATA: '{pdf_path}' dosyası bulunamadı. Lütfen Colab'a tekrar yükleyin.")
        return None

    reader = PdfReader(pdf_path)
    raw_text = ''.join(page.extract_text() + "\n" for page in reader.pages if page.extract_text())
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, length_function=len)
    texts = text_splitter.create_documents([raw_text])

    model_name = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    model_kwargs = {'device': 'cuda'}
    embeddings = HuggingFaceEmbeddings(model_name=model_name, model_kwargs=model_kwargs)
    vectorstore = Chroma.from_documents(documents=texts, embedding=embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # RAG Zincirini Kurma
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2, api_key=gemini_api_key)

    # KRİTİK DÜZELTME: PROMPT METNİ EKLENDİ
    template = """Sen, Global AI Hub/Akbank GenAI Bootcamp Proje ve Kural Asistanısın.
    Yalnızca sağlanan bağlam (context) bilgisine dayanarak kullanıcı sorularını cevapla.
    Eğer bağlamda yeterli bilgi yoksa, "Veri setimde bu konuyla ilgili yeterli bilgi bulunmamaktadır." diye cevap ver.

    Bağlam (Context): {context}
    Soru: {question}
    Cevap:
    """
    prompt = ChatPromptTemplate.from_template(template)
    rag_chain = ({"context": retriever, "question": RunnablePassthrough()} | prompt | llm | StrOutputParser())

    return rag_chain

# --- STREAMLIT ARAYÜZÜ ---
st.set_page_config(page_title="Bootcamp Proje Asistanı", layout="wide")
st.title("✨ GenAI Bootcamp Proje ve Kural Asistanı")
st.markdown("Merhaba! Bana projeniz, kurallar, veri setleri veya teslimat hakkında sorular sorabilirsiniz.")

# Yorum satırını kaldırıyoruz ki, web sitesindeki hata mesajı yerine RAG sistemi kurulsun.
rag_chain = setup_rag_system()

if rag_chain:
    query = st.text_input("Sorunuzu buraya yazın:", placeholder="README.md dosyasında neler olmalı?")
    if query:
        with st.spinner(f"'{query}' için cevap aranıyor..."):
            try:
                response = rag_chain.invoke(query)
                st.info(response)
            except Exception as e:
                st.error(f"Chatbot bir hata ile karşılaştı: {e}")
