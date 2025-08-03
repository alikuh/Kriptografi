# 🔐 Kriptografi - Python & Tkinter

Bu proje, **Python** ve **Tkinter** kullanılarak geliştirilmiş bir masaüstü uygulamasıdır.  
Kullanıcı, girdiği metni kendi belirlediği **parola** ile güvenli şekilde şifreleyebilir ve aynı parola ile tekrar çözebilir.  
Şifrelenmiş veriler **data.txt** dosyasında saklanır.

---

## ✨ Özellikler
- 📌 Kullanıcıdan başlık (title) alma
- 📌 Kullanıcıdan metin (secret) alma
- 📌 Kullanıcıdan şifreleme/deşifreleme için parola alma
- 📌 Fernet algoritması ile güvenli şifreleme
- 📌 Base64 ile okunabilir formatta dosyaya kaydetme
- 📌 Tek tıkla şifreleme (Encrypt) ve çözme (Decrypt)
- 📌 Kullanıcı dostu Tkinter arayüzü
- 📌 Yanlış parola girildiğinde uyarı mesajı

---

## 📷 Ekran Görüntüsü
![Uygulama Ekran Görüntüsü](ekran.png)

---

## 🔑 Kullanım
1. **Enter your title** alanına kaydın başlığını yazın.  
2. **Enter your secret** alanına şifrelemek istediğiniz metni yazın.  
3. **Enter your masterkey** alanına belirleyeceğiniz parolayı yazın.  
4. **Save & Encrypt** butonuna basarak şifreleyip kaydedin.  
5. Çözmek için aynı başlığı ve doğru parolayı girip **Decrypt** butonuna tıklayın.

---

## 🔧 Teknik Detaylar

### 📦 Bağımlılıklar
- **cryptography** → Python için gelişmiş kriptografik kütüphane  
- **tkinter** → Yerleşik GUI framework (Python ile birlikte gelir)  
- **hashlib** → Kriptografik hash fonksiyonları (yerleşik)  
- **base64** → Base64 kodlama/çözme işlemleri (yerleşik)  

---

### 🔐 Şifreleme Süreci
1. **Düz Metin** → UTF-8 Kodlama →
2. **AES-256 tabanlı Fernet Şifreleme** →
3. **Base64 Kodlama** → 
4. **data.txt dosyasına kaydetme**

---
