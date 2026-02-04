saldo = 0
pemasukan = []
pengeluaran = []

def tambah_pemasukan():
    global saldo, pemasukan
    jumlah = int(input("Masukkan jumlah pemasukan: "))
    saldo = saldo + jumlah
    pemasukan.append(jumlah)
    print(f"Pemasukan {jumlah} berhasil ditambahkan!")

def tambah_pengeluaran():
    global saldo, pengeluaran
    jumlah = int(input("Masukkan jumlah pengeluaran: "))
    if jumlah > saldo:
        print("Peringatan: Saldo tidak cukup!")
    else:
        saldo = saldo - jumlah
        pengeluaran.append(jumlah)
        print(f"Pengeluaran {jumlah} berhasil dikurangi dari saldo!")

def lihat_saldo():
    print("=" * 30)
    print(f"Saldo saat ini: Rp {saldo:,.0f}")
    print("=" * 30)

def lihat_laporan():
    total_pemasukan = sum(pemasukan)
    total_pengeluaran = sum(pengeluaran)
    
    print("\n" + "=" * 40)
    print("LAPORAN UANG SAKU")
    print("=" * 40)
    print(f"Total Pemasukan  : Rp {total_pemasukan:,.0f}")
    print(f"Total Pengeluaran: Rp {total_pengeluaran:,.0f}")
    print(f"Saldo Akhir      : Rp {saldo:,.0f}")
    print("=" * 40)
    
    if pemasukan:
        print(f"\nDetail Pemasukan ({len(pemasukan)} transaksi):")
        for i, nilai in enumerate(pemasukan, 1):
            print(f"  {i}. Rp {nilai:,.0f}")
    
    if pengeluaran:
        print(f"\nDetail Pengeluaran ({len(pengeluaran)} transaksi):")
        for i, nilai in enumerate(pengeluaran, 1):
            print(f"  {i}. Rp {nilai:,.0f}")
    
    if not pemasukan and not pengeluaran:
        print("\nBelum ada transaksi.")
    print()

def menu():
    print("\n=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Lihat laporan")
    print("5. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pemasukan()
    elif pilihan == "2":
        tambah_pengeluaran()
    elif pilihan == "3":
        lihat_saldo()
    elif pilihan == "4":
        lihat_laporan()
    elif pilihan == "5":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid")