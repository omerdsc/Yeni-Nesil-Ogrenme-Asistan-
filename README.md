Projenin Amacı:

Kullanıcının kendi yüklediği notlardan doğal dilde sorular sorarak cevap almasını sağlamak

Bireysel öğrenmeyi hızlandıran, etkileşimli bir yapay zeka destekli sistem geliştirmek

Terminalden
   Backend’i şu komutla başlat: uvicorn app.main:app --reload ve tarayıcıdan http://127.0.0.1:8000/docs la fastapiye ekranına ulaşırız 
  Frontend’i şu komutla başlat: streamlit run frontend/app.py otomatikmen tarayıcı ekranı açılması lazım eğer açılmaz ise http://localhost:8501 local adresi ile tarayıcıdan açabiliriz
  
Ama başlatmadan önce .env dosyası içerisine bir tane OPENAI_API_KEY amahtarı tanımlamalısınız eğer tanımlanmazsa herhangi bir sonuç döndürmeyecektir

![Ekran görüntüsü 2025-05-05 165318](https://github.com/user-attachments/assets/0159ce17-7fac-4f7d-ae04-7855ec5d5fe1)

![Ekran görüntüsü 2025-05-05 164923](https://github.com/user-attachments/assets/3f59be29-d8d3-4fd1-873c-51895e26679a)

