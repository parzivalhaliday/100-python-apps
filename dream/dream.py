import os
from datetime import datetime

# Notunuzu alın
notunuz = input("Notunuzu yazın: ")

# Dosya adını isteyin
dosya_adi = input("Dosya adını girin: ")

# Tarih bilgisini alın
tarih = datetime.now().strftime("%Y-%m-%d")

# Dosya adını ve tarihi kullanarak dosya adını oluşturun
dosya_adi = f"{dosya_adi} - {tarih}.txt"

# Dosyayı açın ve notu yazın
with open(dosya_adi, "w") as dosya:
    dosya.write(notunuz)

print(f"Notunuz {dosya_adi} adlı dosyaya kaydedildi.")
