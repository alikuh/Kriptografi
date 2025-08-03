from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet
import hashlib
import base64

window = Tk()
window.title("Kriptografi")
window.minsize(400, 600)

try:
    photo = PhotoImage(file="Kriptografi1.png", width=200, height=200)
    label = Label(window, image=photo)
    label.PhotoImage = photo
    label.pack(padx=5, pady=20)
except:
    label= Label(window, text="🔐 KRİPTOGRAFİ 🔐", font=("Arial", 16))
    label.pack(padx=5, pady=20)
#TİTLE
label1 = Label(window, text="Enter your title")
label1.pack(padx=5, pady=5)
entry_title = Entry(width=30)
entry_title.pack(padx=5, pady=5)

# SECRET TEXT
label2 = Label(window, text="Enter your secret")
label2.pack()
text_secret = Text(width=30,height=10)
text_secret.pack(padx=5, pady=5)

# MASTER KEY
label3 = Label(window, text="Enter your masterkey")
label3.pack(padx=5, pady=5)
entry_key = Entry(width=30)
entry_key.pack(padx=5, pady=5)

# İmza
imza = Label( text="Ali Kuh",fg="blue")
imza.place(relx=1.0, rely=1.0, anchor="se")

ENCRYPTED_FILE = "data.txt"

def generate_key_from_password(password):  # normal şifreyi önce SHA-256 ile hashleyip sonra Base64 ile okunur hale getiren fonskiyon
    # Parolayı SHA-256 ile hash'le
    password_hash = hashlib.sha256(password.encode()).digest()
    # Base64 encode ile metin haline getir
    key = base64.urlsafe_b64encode(password_hash)
    return key

def Encrypt():
    try:
        # girilen verieleri aldık
        title = entry_title.get()
        secret_text = text_secret.get("1.0","end-1c")
        master_key = entry_key.get()

        # Boş alan kontrolü
        if not title:
            messagebox.showerror("Error","Please enter a title")
            return
        if not secret_text:
            messagebox.showerror("Error","Please enter a secret")
            return
        if not master_key:
            messagebox.showerror("Error","Please enter a masterkey")
            return

        # Şifreleme anahtarı oluştur
        key = generate_key_from_password(master_key)
        fernet = Fernet(key)

        # Metni şifrele
        encrypted_text = fernet.encrypt(secret_text.encode())

        # Base64 ile kodladık txt dosyasına yazdırabilmek için
        encrypted_text_b64 = base64.b64encode(encrypted_text).decode()

        # Yeni şifrelenmiş veri
        new_entry =f"TİTLE:{title}\nENCRYPTED: {encrypted_text_b64}\n" + "="*50 + "\n"

        # Ana dosyaya ekleme işlemi
        with open(ENCRYPTED_FILE,"a",encoding="utf-8") as file:
            file.write(new_entry)

        # Text alanını şifreli metinle doldur
        text_secret.delete("1.0", "end")
        text_secret.insert("1.0", encrypted_text_b64)

        messagebox.showinfo("Success", f"Text encrypted and saved to {ENCRYPTED_FILE}!")

    except Exception as error:
        messagebox.showerror("Error", f"Encryption failed:{str(error)}")
def Decrypt():
    try:
        # Girilen verileri al
        encrypted_text_b64 = text_secret.get("1.0","end-1c")
        master_key = entry_key.get()

        # Boş alan Kontrolü
        if not encrypted_text_b64:
            messagebox.showerror("Error","Please enter encrypted text")
            return
        if not master_key:
            messagebox.showerror("Error","Please enter a masterkey")
            return

        #Gizlenmiş keyi çözme anahtarı oluştur
        key = generate_key_from_password(master_key)
        fernet = Fernet(key)

        #Base64 ten decode etme
        encrypted_text = base64.b64decode(encrypted_text_b64.encode())

        # Şifreyi ÇÖZ
        decrypted_text = fernet.decrypt(encrypted_text).decode()

        # Text alanına çözülmüş şifreyi yazacaz
        text_secret.delete("1.0", "end")
        text_secret.insert("1.0", decrypted_text)

        messagebox.showinfo("Success", "Text decrypted successfully!")
    except Exception as error:
        messagebox.showerror("Error", f"Decryption failed!\nWrong password or corrupted text. {str(error)}")


button1 = Button(window, text="Save & Encrypt",command=Encrypt)
button1.pack(padx=5, pady=5)

button2 = Button(window, text="Decrypt",command=Decrypt)
button2.pack(padx=5, pady=5)
window.mainloop()