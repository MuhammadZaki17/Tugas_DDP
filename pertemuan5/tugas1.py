kendaraan=["Avanza","mobil","toyota","1500cc"]
kendaraan.append("hitam")
kendaraan.append("300_juta")
kendaraan.insert(2,"roda empat")
kendaraan.remove("mobil")
print(kendaraan)
print()
pilihan  = int(input("""Silahkan pilih nomor dibawah ini
untuk menggunakan tools dibawah ini
==================================
Pilihan
==================================
1. Pertambahan
2. Pengurangan
3. Pembagian
=================================
Pilihan mu? """))
match pilihan:
    case 1:
        print("menghitung luas persegi")
        sisi = int(input("masukan sisi?"))
        luasP = int(sisi*sisi)
        print("luas persegi adalah", luasP)
    case "2":
        print(" menghitung luas lingkaran ")
        jari = float(input("masukan jari-jari "))
        luasL = float(3.14*jari*jari)
        print("luas lingkaran adalah", luasL)
    case "3":
        print ("Menghitung luas segitiga ")
        alas =int(input("masukan alas"))
        tinggi =int(input("masukan tinggi "))
        luas =int(alas*tinggi/2)
        print ("luas segitiga adalah", luasS)
