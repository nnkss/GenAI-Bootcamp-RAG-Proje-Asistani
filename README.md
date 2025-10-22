# ✨ Global AI Hub/Akbank GenAI Bootcamp: RAG Proje Asistanı


**Global AI Hub/Akbank GenAI Bootcamp** için geliştirilmiş, **üretime hazır** ve **Retrieval-Augmented Generation (RAG)** özellikli bir proje asistanı chatbot.

Bu uygulama, bootcamp'e ait proje kurallarını ve teknik gereksinimleri indeksliyor; **ChromaDB** ile en alakalı bilgileri çekiyor ve **Google Gemini** kullanarak sadece veri kaynağına dayanan, doğru ve faydalı yanıtlar üretiyor.


## 3. Elde Edilen Sonuçlar ve Temel Özellikler (Features)
Projenizin temel özellikleri ve kazanımları şunlardır:

* **Basit RAG Pipeline:** Öbekleme (Chunking), Yerleştirme (Embedding), Depolama, Alma (Retrieve) ve Oluşturma (Generate) adımlarını içeren temiz bir akış.
* Yanıt oluşturma için **Google Gemini 2.5 Flash** kullanılmıştır.
* **Türkçe uyumlu embedding modeli** (`paraphrase-multilingual-MiniLM-L12-v2`) kullanılmıştır.
* **Streamlit UI** (Kullanıcı Arayüzü), Markdown oluşturma ve kalıcı Chroma vektör deposu kullanılmıştır.
* API anahtarı yönetimi için güvenli dosya tabanlı çözüm uygulanmıştır.


* ## 2. Teknik Yığın (Tech Stack)

| Teknoloji | Amaç / Model | Sizin Projenizdeki Karşılığı |
| :--- | :--- | :--- |
| **Arka uç / UI** | Flask | **Streamlit** |
| **RAG** | LangChain, Chroma | LangChain, ChromaDB |
| **LLM** | Google Gemini (gemini-2.5-flash) | Google Gemini (gemini-2.5-flash) |
| **Yerleştirmeler** | Google `models/text-embedding-004` | **`paraphrase-multilingual-MiniLM-L12-v2`** |
| **Veri** | Markdown Soru-Cevap | **GenAI Bootcamp Projesi.pdf** |


### Gereksinimler

* Python 3.10+
* Gemini modellerine erişimi olan **geçerli bir Google API anahtarı** (Colab Secrets'a kaydedilmelidir.)
* Proje dosyaları (Kod, `requirements.txt`, ve `GenAI Bootcamp Projesi.pdf`)


#### 1. Ortamı Hazırlayın

1.  **Gerekli Dosyalar:** Tüm proje dosyalarını (kod ve veri) bir Colab oturumuna yükleyin.
2.  **API Anahtarını Kaydedin:** Google API anahtarınızı, Colab'ın Gizli Anahtarlar (🔑) bölümüne **`GEMINI_API_KEY`** adıyla kaydedin.
3.  **Çalıştırma Zamanı:** Donanım hızlandırıcıyı **T4 GPU** olarak ayarlayın.

#### 2. Çalıştırma

`RAG_Chatbot_Projesi.ipynb` dosyasını açın ve tüm kod bloklarını sırasıyla çalıştırın.

| Adım | Açıklama |
| :--- | :--- |
| **Kod Bloğu 1** | Bağımlılıkları yükler. **(Çalıştırdıktan sonra Oturumu Yeniden Başlatın)** |
| **Kod Bloğu 2/3** | Vektör veritabanını oluşturur (Veri okuma, Parçalama, Vektörleştirme). |
| **Kod Bloğu 4** | `app.py` dosyasını oluşturur. |
| **Kod Bloğu 5** | Uygulamayı başlatır ve Cloudflare Tünelini açarak **Canlı URL** verir. |

### Çalıştırma Kılavuzu (Hızlı Başlangıç)

Bu proje, Colab ortamında çalıştırılmak üzere tasarlanmıştır.

#### 1. Ortamı Hazırlayın

1.  **Gerekli Dosyalar:** GitHub'daki tüm proje dosyalarını (kod ve veri) bir Colab oturumuna yükleyin.
2.  **API Anahtarını Kaydedin:** Google API anahtarınızı, Colab'ın Gizli Anahtarlar (🔑) bölümüne **`GEMINI_API_KEY`** adıyla kaydedin.
3.  **Çalıştırma Zamanı:** Donanım hızlandırıcıyı **T4 GPU** olarak ayarlayın.

#### 2. Çalıştırma

`RAG_Chatbot_Projesi.ipynb` dosyasını açın ve tüm kod bloklarını sırasıyla çalıştırın.

| Adım | Açıklama |
| :--- | :--- |
| **Kod Bloğu 1** | Bağımlılıkları yükler. **(Çalıştırdıktan sonra Oturumu Yeniden Başlatın)** |
| **Kod Bloğu 2/3** | Vektör veritabanını oluşturur (Veri okuma, Parçalama, Vektörleştirme). |
| **Kod Bloğu 4** | `app.py` dosyasını oluşturur. |
| **Kod Bloğu 5** | Uygulamayı başlatır ve Cloudflare Tünelini açarak **Canlı URL** verir. |

#### 3. Uygulamayı Açın

Daha sonra tarayıcınızı, Kod Bloğu 5'in çıktısı olan **URL adresinden** açın.

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


#### 3. Uygulamayı Açın

Daha sonra tarayıcınızı, Kod Bloğu 5'in çıktısı olan **URL adresinden** açın.


### Yapılandırma (Varsayılanlar)

Projemiz için kullanılan teknik parametreler aşağıdadır:

* **Üretken Model (LLM):** `gemini-2.5-flash` (Bizim projede kullanılan, kararlılık için `temperature=0.2` ayarlanmıştır.)
* **Gömme Modeli (Embedding):** `paraphrase-multilingual-MiniLM-L12-v2`
* **Parçalama (Chunking):** 1000 karakter (`chunk_size`), 200 karakter örtüşme (`chunk_overlap`).
* **Geri Alma k (Retrieval k):** 3 (Sorgu başına Vektör Veritabanından çekilen en alakalı metin parçasının sayısı.)


### Proje Yapısı

GenAI-Bootcamp-RAG-Proje-Asistani/
├── GenAI Bootcamp Projesi.pdf   # Veri kaynağı
├── app.py                      # Streamlit arayüzü ve RAG sorgu akışı
├── RAG_Chatbot_Projesi.ipynb   # Çalışma Kılavuzu ve Geliştirme Notları
├── requirements.txt            # Python bağımlılıkları
└── README.md                   # Bu dosya
