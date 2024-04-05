def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas

def main():
    print("Program Menghitung Luas Persegi Panjang")
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))

    luas = hitung_luas_persegi_panjang(panjang, lebar)
    print("Luas persegi panjang adalah:", luas)

if __name__ == "__main__":
    main()
