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

## 4. Çalıştırma Kılavuzu (Setup)

Bu proje **Colab ortamında çalıştırılmak üzere** tasarlanmıştır. Tüm kurulum ve veritabanı oluşturma adımları not defteri içinde otomatiktir.

### A. Ortamı Hazırlayın

1.  **Gerekli Dosyalar:** Tüm proje dosyalarını (kod ve veri) bir Colab oturumuna yükleyin.
2.  **API Anahtarını Kaydedin:** Gizli Anahtarlar (🔑) bölümüne **`GEMINI_API_KEY`** adıyla anahtarınızı kaydedin.
3.  **Çalıştırma Zamanı:** Donanım hızlandırıcıyı **T4 GPU** olarak ayarlayın.

### B. Çalıştırma

`RAG_Chatbot_Projesi.ipynb` dosyasını açın ve **tüm kod bloklarını yukarıdan aşağıya, sırasıyla** çalıştırın. Not defteri, tüm kütüphaneleri kuracak ve uygulamayı başlatacaktır.

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

**ÖNEMLİ NOT:** Colab oturumu kapalı olduğu için bu link şu an pasif olabilir. Projeyi kontrol edecek ekibin, `RAG_Chatbot_Projesi.ipynb` dosyasındaki son bloğu çalıştırarak linki kendilerinin aktif etmesi gerekmektedir.
