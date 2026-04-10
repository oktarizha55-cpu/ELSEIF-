# =========================
# 1. BIAYA LISTRIK 
# =========================
kwh = int(input("Masukkan total KWH: "))
biaya = 0

if kwh <= 100:
    biaya = kwh * 500
elif kwh <= 300:
    biaya = (100 * 500) + ((kwh - 100) * 1000)
else:
    biaya = (100 * 500) + (200 * 1000) + ((kwh - 300) * 2000)

print("Total biaya listrik:", biaya)


# =========================
# 2. GANJIL / GENAP
# =========================
angka = int(input("\nMasukkan angka: "))

if angka % 2 == 0:
    print("Genap")
else:
    print("Ganjil")


# =========================
# 3. LULUS / PERBAIKAN 
# =========================
nilai = int(input("\nMasukkan nilai: "))

if nilai > 75:
    print("Lulus")
elif nilai >= 50:
    print("Perbaikan")
else:
    print("Tidak lulus")


# =========================
# 4. LULUS / PERBAIKAN yang ke 2 
# =========================
nilai2 = int(input("\nMasukkan nilai: "))
absensi = int(input("Masukkan absensi: "))

if nilai2 > 70 and absensi > 50:
    print("Lulus")
elif (nilai2 < 70 and absensi > 70) or (nilai2 > 70 and absensi < 50):
    print("Perbaikan")
else:
    print("Tidak lulus")