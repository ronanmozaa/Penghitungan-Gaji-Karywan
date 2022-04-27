kondisi = False
gol = [1, 6]

while not kondisi:
    print("---------------------------------")
    print("    Perhitungan Gaji Karyawan    ")
    print("---------------------------------")
    print("")

    nama     = str(input("Masukkan Nama                : "))
    nip      = int(input("Masukkan Nomor Induk Pegawai : "))
    anak     = int(input("Masukkan Jumlah Anak         : "))
    jam      = int(input("Masukkan Waktu Lembur        : "))
    gol      = int(input("Pilih Golongan Anda          : "))

    if   gol == 1:
        jab        = "Manajer"
        gapok      = 6000000
        lembur     = 7200000
        tun        = 500000
        gator      = int(gapok) + int(lembur) + int(tun)
        gasih      = int(gator) - ((int(gator) * 5) / 100)
        pajak      = int(gapok) * 0.2
    elif gol == 2:
        jab        = "Direktur"
        gapok      = 5000000 
        lembur     = 6000000 
        tun        = 500000
        gator      = int(gapok) + int(lembur) + int(tun)
        gasih      = int(gator) - ((int(gator) * 5) / 100)
        pajak      = int(gapok) * 0.2
    elif gol == 3:
        jab        = "Karyawan"
        gapok      = 4000000 
        lembur     = 4800000 
        tun        = 500000
        gator      = int(gapok) + int(lembur) + int(tun)
        gasih      = int(gator) - ((int(gator) * 5) / 100)
        pajak      = int(gapok) * 0.2
    elif gol == 4:
        jab        = "Sekretaris"
        gapok      = 3000000
        lembur     = 3600000 
        tun        = 500000
        gator      = int(gapok) + int(lembur) + int(tun)
        gasih      = int(gator) - ((int(gator) * 5) / 100) 
        pajak      = int(gapok) * 0.2
    elif gol == 5:
        jab        = "Supervisor"
        gapok      = 2000000 
        lembur     = 2400000 
        tun        = 500000
        gator      = int(gapok) + int(lembur) + int(tun)
        gasih      = int(gator) - ((int(gator) * 5) / 100) 
        pajak      = int(gapok) * 0.2
    while True:
        tindakan = input("apakah data yang anda inputkan sudah benar? [y]/[t]")
        if tindakan == "y" or tindakan == "t" :
            break
    if tindakan.lower() == "y" :
        kondisi = True

print("")
print("------------------------------------")
print("             Gaji Karyawan")
print("------------------------------------")
print("Nama                 : {} \nNomor Induk Pegawai  : {} \nJumlah anak          : {}anak \nJumlah Lembur        : {}jam \n".format(nama, nip, anak, jam))
print("Jabatan           : {} \nGaji Pokok        : Rp.{} \nGaji Lembur       : Rp.{} \nTunjangan         : Rp.{}".format(jab, gapok, lembur, tun))
print("Gaji Kotor        : Rp.{} \nGaji Bersih       : Rp.{} \nPajak Penghasilan : Rp.{}".format(gator, gasih, pajak))