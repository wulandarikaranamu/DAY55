print("\n"+"PROFRAM PESANAN MINUMAN"+"\n"+20*"=")

pesanan = ["air mineral","jus","kopi","teh"]
jenis_ruangan = input("fasilitas ruangan paling ternyaman :")
no_meja = int(input("nomor mrja sipemesan :"))

print("\n"+"minuman yang tersedia"+"\n"+20*"=")

for x in (pesanan):
    print(x)

kategori_minuman = int(input("masukkan kategori (1-4) :"))
meja_istimewah = int(input("masukkan no meja terfavorit :"))

if(kategori_minuman) == 1:
    jenis_minuman = "air_mineral"
    harga = 100000
elif(kategori_minuman) == 2:
    jenis_minuman = "jus"
    harga = 200000
elif(kategori_minuman) == 3:
    jenis_minuman = "kopi"
    harga = 250000
elif(kategori_minuman) == 4:
    jenis_minuman = "jus"
    harga = 300000
total_biaya = meja_istimewah*harga

print(f"minuman {jenis_minuman} : Rp. {harga}")
print("total biaya : Rp.",total_biaya)

bayar = int(input("total bayar : Rp."))
ansuran = bayar-total_biaya
print(f"ansuran : Rp. {ansuran}")

print("\n"+"TERIMAKSIH SELAMAT MENIKMATI"+"\n"+20*"=")
