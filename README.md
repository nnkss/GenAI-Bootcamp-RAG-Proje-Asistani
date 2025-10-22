# ✨ Global AI Hub/Akbank GenAI Bootcamp: RAG Proje Asistanı

**Global AI Hub/Akbank GenAI Bootcamp** için geliştirilmiş, **üretime hazır** ve **Geri Alma-Artırılmış Üretim (RAG)** özellikli bir proje asistanı chatbot.

Bu uygulama, bootcamp'e ait proje kurallarını ve teknik gereksinimleri indeksliyor; **ChromaDB** ile en alakalı bilgileri çekiyor ve **Google Gemini** kullanarak sadece veri kaynağına dayanan, doğru ve faydalı yanıtlar üretiyor.

## 1. Temel Özellikler (Features)

* Basit RAG Pipeline: Öbekleme (Chunking) → Yerleştirme (Embedding) → Depolama → Alma → Oluşturma adımlarını içerir.
* Yanıt oluşturma için **Google Gemini 2.5 Flash** kullanılmıştır.
* **Streamlit UI**, Markdown oluşturma ve kalıcı Chroma vektör deposu kullanılmıştır.
* API anahtarı yönetimi için güvenli dosya tabanlı çözüm uygulanmıştır.

## 2. Teknik Yığın (Tech Stack)

| Teknoloji | Amaç / Model | Not |
| :--- | :--- | :--- |
| **Arka uç / UI** | Streamlit | Kod: app.py |
| **RAG** | LangChain (LCEL), ChromaDB | |
| **LLM** | Google Gemini (`gemini-2.5-flash`) | |
| **Yerleştirmeler (Embeddings)** | `paraphrase-multilingual-MiniLM-L12-v2` | Türkçe uyumlu model |
| **Veri** | GenAI Bootcamp Projesi (*.pdf) | |

---

## 3. Gereksinimler

* Python 3.10+
* Gemini modellerine erişimi olan **geçerli bir Google API anahtarı** (Colab Secrets'a kaydedilmelidir).

---

### Proje Çalıştırma Talimatları (Yerel Ortam - Local Setup)

Bu talimatlar, projeyi kendi bilgisayarında (yerel ortamda) çalıştırmak isteyen bir geliştirici için tasarlanmıştır.

1.  **Depoyu Klonlayın:** Proje dosyalarını yerel bilgisayarınıza indirin.
    ```bash
    git clone [https://github.com/nnkss/GenAI-Bootcamp-RAG-Proje-Asistani.git](https://github.com/nnkss/GenAI-Bootcamp-RAG-Proje-Asistani.git)
    cd GenAI-Bootcamp-RAG-Proje-Asistani
    ```
2.  **Bağımlılıkları Yükleyin:** Gerekli tüm kütüphaneleri `requirements.txt` dosyasından yükleyin.
    ```bash
    pip install -r requirements.txt
    ```
3.  **Yapılandırma:** Yerel ortamda **`GOOGLE_API_KEY`** adlı bir ortam değişkeni ayarlayın veya projenin kök dizinine API anahtarınızı içeren bir **`.env`** dosyası oluşturun.
4.  **Uygulamayı Başlatın:** Streamlit uygulamasını başlatın.
    ```bash
    streamlit run app.py
    ```
    Daha sonra tarayıcınızı **`http://localhost:8501`** adresinden açın.

---

## 5. Yapılandırma (Varsayılanlar)

Projeniz için kullanılan kritik teknik parametreler aşağıdadır:

* **Üretken Model (LLM):** `gemini-2.5-flash` (Kararlılık için `temperature=0.2` ayarlanmıştır.)
* **Gömme Modeli (Embedding):** `paraphrase-multilingual-MiniLM-L12-v2`
* **Parçalama (Chunking):** 1000 karakter, 200 karakter örtüşme.
* **Geri Alma k (Retrieval k):** 3 (Sorgu başına çekilen en alakalı metin parçası sayısı.)

---

## 6. Proje Yapısı

GenAI-Bootcamp-RAG-Proje-Asistani/ 

├── GenAI Bootcamp Projesi.pdf # Veri kaynağı (GitHub'a yüklenmiştir) 

├── app.py # Streamlit arayüzü ve RAG sorgu akışı 

├── RAG_Chatbot_Projesi.ipynb # Çalışma Kılavuzu, RAG Kurulumu ve Geliştirme Notları

├── requirements.txt # Python bağımlılıkları 

└── README.md # Bu dosya

## Canlı Proje Linki

> **Canlı Proje Linki:**  https://structural-scoop-senior-jane.trycloudflare.com

**ÖNEMLİ NOT:** Colab oturumu kapalı olduğu için bu link şu an pasif olabilir. Projeyi kontrol edecek ekibin, `GenAI_Bootcamp_RAG_Proje_Asistani.ipynb` dosyasındaki son bloğu çalıştırarak linki kendilerinin aktif etmesi gerekmektedir.
