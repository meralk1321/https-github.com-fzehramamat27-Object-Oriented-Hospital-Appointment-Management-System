import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from kullanici import Doktor
from veritabani import HastaneDB


class HastaneGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Hastane Randevu Sistemi")
        self.root.geometry("700x500")
        self.root.configure(bg="#f0f4f7")

        self.db = HastaneDB()

        baslik = tk.Label(
            root,
            text="HASTANE RANDEVU SİSTEMİ",
            font=("Arial", 18, "bold"),
            bg="#f0f4f7",
            fg="#1f4e79"
        )
        baslik.pack(pady=10)

        self.frame_doktor = tk.LabelFrame(
            root,
            text="Doktor Ekle",
            padx=10,
            pady=10
        )
        self.frame_doktor.pack(fill="x", padx=20, pady=10)

        tk.Label(self.frame_doktor, text="Ad").grid(row=0, column=0)
        tk.Label(self.frame_doktor, text="Soyad").grid(row=1, column=0)
        tk.Label(self.frame_doktor, text="Uzmanlık").grid(row=2, column=0)

        self.entry_ad = tk.Entry(self.frame_doktor)
        self.entry_soyad = tk.Entry(self.frame_doktor)
        self.entry_uzmanlik = tk.Entry(self.frame_doktor)

        self.entry_ad.grid(row=0, column=1, padx=5, pady=5)
        self.entry_soyad.grid(row=1, column=1, padx=5, pady=5)
        self.entry_uzmanlik.grid(row=2, column=1, padx=5, pady=5)

        btn_ekle = tk.Button(
            self.frame_doktor,
            text="Doktor Ekle",
            command=self.doktor_ekle,
            bg="#1f77b4",
            fg="white"
        )
        btn_ekle.grid(row=3, column=0, columnspan=2, pady=10)

        self.frame_randevu = tk.LabelFrame(
            root,
            text="Randevu Oluştur",
            padx=10,
            pady=10
        )
        self.frame_randevu.pack(fill="x", padx=20, pady=10)

        tk.Label(self.frame_randevu, text="Hasta Adı").grid(row=0, column=0)

        self.entry_hasta = tk.Entry(self.frame_randevu)
        self.entry_hasta.grid(row=0, column=1)

        tk.Label(self.frame_randevu, text="Doktor").grid(row=1, column=0)

        self.combo_doktor = ttk.Combobox(self.frame_randevu)
        self.combo_doktor.grid(row=1, column=1)

        btn_randevu = tk.Button(
            self.frame_randevu,
            text="Randevu Oluştur",
            command=self.randevu_olustur,
            bg="#28a745",
            fg="white"
            


        )
        btn_randevu.grid(row=2, column=0, columnspan=2, pady=10)
        self.frame_liste = tk.LabelFrame(
        root,
        text="Randevular",
        padx=10,
        pady=10
        )
        self.frame_liste.pack(fill="both", expand=True, padx=20, pady=10)

        self.tree = ttk.Treeview(
        self.frame_liste,
        columns=("ID", "Hasta", "Doktor"),
        show="headings"
        )

        self.tree.heading("ID", text="ID")
        self.tree.heading("Hasta", text="Hasta")
        self.tree.heading("Doktor", text="Doktor")

        self.tree.pack(fill="both", expand=True)

        self.doktorlari_yukle()
        self.randevulari_goster()

    def doktor_ekle(self):

        ad = self.entry_ad.get()
        soyad = self.entry_soyad.get()
        uzmanlik = self.entry_uzmanlik.get()

        if  ad == "" or soyad == "" or uzmanlik == "":
         messagebox.showerror("Hata", "Tüm alanları doldurun")
         return

        doktor = Doktor(ad, soyad, "11111111111", uzmanlik)

        self.db.doktor_ekle(doktor)

        messagebox.showinfo("Başarılı", "Doktor eklendi")

        self.entry_ad.delete(0, tk.END)
        self.entry_soyad.delete(0, tk.END)
        self.entry_uzmanlik.delete(0, tk.END)

        self.doktorlari_yukle()

    def doktorlari_yukle(self):

        doktorlar = self.db.doktorlari_getir()

        liste = []

        for doktor in doktorlar:
            liste.append(f"{doktor[0]} - {doktor[1]}")

        self.combo_doktor["values"] = liste

    def randevu_olustur(self):

        hasta_ad = self.entry_hasta.get()
        secilen = self.combo_doktor.get()

        if hasta_ad == "" or secilen == "":
         messagebox.showerror("Hata", "Bilgileri doldurun")
         return

        doktor_id = int(secilen.split(" - ")[0])

        self.db.randevu_al(hasta_ad, doktor_id)

        messagebox.showinfo("Başarılı", "Randevu oluşturuldu")

        self.entry_hasta.delete(0, tk.END)

        self.randevulari_goster()

    def randevulari_goster(self):

       for item in self.tree.get_children():
        self.tree.delete(item)

        liste = self.db.randevulari_getir()

    def randevulari_goster(self):
        # Önce listedeki eski verileri temizle (opsiyonel ama iyidir)
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # HATA BURADA: 'liste' değişkenini tanımlaman lazım!
        # Veritabanından randevuları çekiyoruz:
        liste = self.db.randevulari_getir()
        for randevu in liste:
         self.tree.insert("", tk.END, values=randevu)