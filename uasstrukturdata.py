peminjam = []

while True:
    print("\nProgram Peminjaman Sepeda Listrik")
    print("1. Tambah Peminjam")
    print("2. Cari Peminjam")
    print("3. Tampilkan Peminjam")
    print("4. Ubah Data Peminjam")
    print("5. Hapus Data Peminjam")
    print("6. Keluar")
    pilihan = input("Pilih opsi (1/2/3/4/5/6): ")

    if pilihan == '1': # Tmbah Peminjam
        nama = input("Masukkan nama peminjam: ")
        sepeda = input("Masukkan nomor sepeda listrik: ")
        durasi = input("Masukkan durasi peminjaman (jam): ")
        peminjam.append([nama, sepeda, durasi])
        print("Data peminjam berhasil ditambahkan.\n")

    elif pilihan == '2': #cari peminjam
        if not peminjam:
            print("Tidak ada data peminjaman untuk dicari.\n")
        else:
            nama_cari = input("Masukkan nama peminjam yang dicari: ")
            ditemukan = False
            print("hasil pencarian: ")
            for data in peminjam:
                if nama_cari.lower() in data[0].lower(): # Mencari nama (case insensitive)
                    print(f"Nama: {data[0]}, Sepeda: {data[1]}, Durasi: {data[2]} jam")
                    ditemukan = True
            if not ditemukan:
                print("Peminjam tidak ditemukan.\n")

    elif pilihan == '3': #Tampilkan Peminjaman
        if not peminjam:
            print("Tidak ada data peminjaman.\n")
        else:
            # Bubble sort berdasarkan nama peminjam
            for i in range(len(peminjam)):
                for j in range(0, len(peminjam) - i - 1):
                    if peminjam[j][0] > peminjam[j + 1][0]: #Membandingkan nama peminjam
                        peminjam[j], peminjam[j + 1] = peminjam[j + 1], peminjam[j] # Tukar posisi

        print("Daftar peminjaman (diurutkan berdasarkan nama):")
        for i, data in enumerate(peminjam, start=1):
             print(f"{i}. Nama: {data[0]}, Sepeda: {data[1]}, Durasi: {data[2]} jam")
            print()

    elif pilihan == '4':  # Ubah Data Peminjam
        if not peminjam:
            print("Tidak ada data peminjaman untuk diubah.\n")
        else:
            for i, data in enumerate(peminjam, start=1):
                print(f"{i}. Nama: {data[0]}, Sepeda: {data[1]}, Durasi: {data[2]} jam")
            indeks = int(input("Masukkan nomor peminjam yang ingin diubah: ")) - 1
            if 0 <= indeks < len(peminjam):
                nama = input("Masukkan nama baru: ")
                sepeda = input("Masukkan nomor sepeda baru: ")
                durasi = input("Masukkan durasi baru (jam): ")
                peminjam[indeks] = [nama, sepeda, durasi]
                print("Data peminjam berhasil diubah.\n")
            else:
                print("Nomor peminjam tidak valid.\n")

    elif pilihan == '5':  # Hapus Data Peminjam
        if not peminjam:
            print("Tidak ada data peminjaman untuk dihapus.\n")
        else:
            for i, data in enumerate(peminjam, start=1):
                print(f"{i}. Nama: {data[0]}, Sepeda: {data[1]}, Durasi: {data[2]} jam")
            indeks = int(input("Masukkan nomor peminjam yang ingin dihapus: ")) - 1
            if 0 <= indeks < len(peminjam):
                peminjam.pop(indeks)
                print("Data peminjam berhasil dihapus.\n")
            else:
                print("Nomor peminjam tidak valid.\n")
                
    elif pilihan == '6':  # Keluar
        print("Terima kasih telah menggunakan program ini.")
        break
    
    else:
        print("Pilihan tidak valid. Silakan coba lagi.\n")

