def embed_zip_in_png(png_file, zip_file, output_file):
    """
    PNG dosyasına ZIP dosyasını gömer.
    
    Args:
        png_file (str): Orijinal PNG dosyasının yolu
        zip_file (str): Gömülecek ZIP dosyasının yolu
        output_file (str): Oluşturulacak yeni PNG dosyasının yolu
    """
    # PNG ve ZIP dosyalarının içeriğini okuyoruz
    with open(png_file, 'rb') as png:
        png_data = png.read()
    
    with open(zip_file, 'rb') as zip:
        zip_data = zip.read()
    
    # Özel bir işaret ekleyerek ZIP verisini PNG'ye ekliyoruz
    # Bu işaret, daha sonra ZIP dosyasını çıkarmak için kullanılacak
    marker = b'--ZIPSTART--'
    
    # Yeni dosyayı oluşturuyoruz (PNG + İşaret + ZIP)
    with open(output_file, 'wb') as output:
        output.write(png_data)
        output.write(marker)
        output.write(zip_data)
    
    print(f"ZIP dosyası başarıyla PNG'ye gömüldü: {output_file}")


def extract_zip_from_png(embedded_png, output_zip):
    """
    PNG dosyasına gömülmüş ZIP dosyasını çıkarır.
    
    Args:
        embedded_png (str): ZIP gömülmüş PNG dosyasının yolu
        output_zip (str): Çıkarılacak ZIP dosyasının yolu
    """
    # Gömülmüş dosyanın içeriğini okuyoruz
    with open(embedded_png, 'rb') as file:
        data = file.read()
    
    # İşareti kullanarak ZIP verisini bölüyoruz
    marker = b'--ZIPSTART--'
    if marker in data:
        # İşaretten sonraki veri ZIP dosyasıdır
        zip_start = data.find(marker) + len(marker)
        zip_data = data[zip_start:]
        
        # ZIP dosyasını oluşturuyoruz
        with open(output_zip, 'wb') as zip_file:
            zip_file.write(zip_data)
        
        print(f"ZIP dosyası başarıyla çıkarıldı: {output_zip}")
    else:
        print("Bu PNG dosyasında gömülü ZIP bulunamadı.")


# Tkinter GUI ekleyerek kullanıcı dostu arayüz oluşturuyoruz
if __name__ == "__main__":
    import tkinter as tk
    from tkinter import filedialog, ttk, messagebox
    import os
    
    def select_png_file():
        file_path = filedialog.askopenfilename(
            title="PNG Dosyası Seçin",
            filetypes=[("PNG Dosyaları", "*.png")]
        )
        if file_path:
            png_entry.delete(0, tk.END)
            png_entry.insert(0, file_path)
    
    def select_zip_file():
        file_path = filedialog.askopenfilename(
            title="ZIP Dosyası Seçin",
            filetypes=[("ZIP Dosyaları", "*.zip")]
        )
        if file_path:
            zip_entry.delete(0, tk.END)
            zip_entry.insert(0, file_path)
    
    def select_output_file():
        file_path = filedialog.asksaveasfilename(
            title="Çıktı Dosyasını Seçin",
            defaultextension=".png",
            filetypes=[("PNG Dosyaları", "*.png")]
        )
        if file_path:
            output_entry.delete(0, tk.END)
            output_entry.insert(0, file_path)
    
    def select_embedded_png():
        file_path = filedialog.askopenfilename(
            title="Gömülü PNG Dosyası Seçin",
            filetypes=[("PNG Dosyaları", "*.png")]
        )
        if file_path:
            embedded_entry.delete(0, tk.END)
            embedded_entry.insert(0, file_path)
    
    def select_extract_output():
        file_path = filedialog.asksaveasfilename(
            title="Çıkarılacak ZIP Dosyasını Seçin",
            defaultextension=".zip",
            filetypes=[("ZIP Dosyaları", "*.zip")]
        )
        if file_path:
            extract_output_entry.delete(0, tk.END)
            extract_output_entry.insert(0, file_path)
    
    def do_embed():
        png_file = png_entry.get()
        zip_file = zip_entry.get()
        output_file = output_entry.get()
        
        if not png_file or not zip_file or not output_file:
            messagebox.showerror("Hata", "Lütfen tüm dosya yollarını belirtin.")
            return
        
        try:
            embed_zip_in_png(png_file, zip_file, output_file)
            messagebox.showinfo("Başarılı", f"ZIP dosyası başarıyla PNG'ye gömüldü:\n{output_file}")
        except Exception as e:
            messagebox.showerror("Hata", f"İşlem sırasında bir hata oluştu:\n{str(e)}")
    
    def do_extract():
        embedded_png = embedded_entry.get()
        output_zip = extract_output_entry.get()
        
        if not embedded_png or not output_zip:
            messagebox.showerror("Hata", "Lütfen tüm dosya yollarını belirtin.")
            return
        
        try:
            extract_zip_from_png(embedded_png, output_zip)
            messagebox.showinfo("Başarılı", f"ZIP dosyası başarıyla çıkarıldı:\n{output_zip}")
        except Exception as e:
            messagebox.showerror("Hata", f"İşlem sırasında bir hata oluştu:\n{str(e)}")
    
    # Ana pencere oluşturuyoruz
    root = tk.Tk()
    root.title("PNG ZIP Gizleyici")
    root.geometry("500x400")
    root.resizable(False, False)
    
    # Notebook (sekmeli arayüz) oluşturuyoruz
    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Gömme sekmesi
    embed_frame = ttk.Frame(notebook)
    notebook.add(embed_frame, text="ZIP Göm")
    
    # Çıkarma sekmesi
    extract_frame = ttk.Frame(notebook)
    notebook.add(extract_frame, text="ZIP Çıkar")
    
    # Gömme sekmesi içeriği
    ttk.Label(embed_frame, text="PNG Dosyası:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
    png_entry = ttk.Entry(embed_frame, width=50)
    png_entry.grid(row=0, column=1, padx=5, pady=5)
    ttk.Button(embed_frame, text="Gözat", command=select_png_file).grid(row=0, column=2, padx=5, pady=5)
    
    ttk.Label(embed_frame, text="ZIP Dosyası:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
    zip_entry = ttk.Entry(embed_frame, width=50)
    zip_entry.grid(row=1, column=1, padx=5, pady=5)
    ttk.Button(embed_frame, text="Gözat", command=select_zip_file).grid(row=1, column=2, padx=5, pady=5)
    
    ttk.Label(embed_frame, text="Çıktı Dosyası:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
    output_entry = ttk.Entry(embed_frame, width=50)
    output_entry.grid(row=2, column=1, padx=5, pady=5)
    ttk.Button(embed_frame, text="Gözat", command=select_output_file).grid(row=2, column=2, padx=5, pady=5)
    
    ttk.Button(embed_frame, text="ZIP Dosyasını PNG'ye Göm", command=do_embed).grid(row=3, column=1, padx=5, pady=20)
    
    # Çıkarma sekmesi içeriği
    ttk.Label(extract_frame, text="Gömülü PNG:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
    embedded_entry = ttk.Entry(extract_frame, width=50)
    embedded_entry.grid(row=0, column=1, padx=5, pady=5)
    ttk.Button(extract_frame, text="Gözat", command=select_embedded_png).grid(row=0, column=2, padx=5, pady=5)
    
    ttk.Label(extract_frame, text="Çıktı ZIP:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
    extract_output_entry = ttk.Entry(extract_frame, width=50)
    extract_output_entry.grid(row=1, column=1, padx=5, pady=5)
    ttk.Button(extract_frame, text="Gözat", command=select_extract_output).grid(row=1, column=2, padx=5, pady=5)
    
    ttk.Button(extract_frame, text="ZIP Dosyasını Çıkar", command=do_extract).grid(row=2, column=1, padx=5, pady=20)
    
    # Bilgi etiketi
    info_label = ttk.Label(root, text="PNG dosyalarına ZIP dosyalarını güvenli bir şekilde gömün ve çıkarın.", 
                           wraplength=400, justify=tk.CENTER)
    info_label.pack(side=tk.BOTTOM, pady=10)
    
    root.mainloop() 