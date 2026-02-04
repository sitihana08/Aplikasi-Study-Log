catatan = []
target_harian = 0  # Target waktu belajar harian dalam menit

def tambah_catatan():
    """Menambahkan catatan belajar baru ke dalam list"""
    print("\n--- Tambah Catatan Belajar ---")
    mapel = input("Masukkan nama mapel: ").strip()
    topik = input("Masukkan topik yang dipelajari: ").strip()
    
    try:
        durasi = int(input("Masukkan durasi belajar (menit): "))
        if durasi <= 0:
            print("⚠️  Durasi harus lebih dari 0 menit!")
            return
    except ValueError:
        print("⚠️  Masukkan angka yang valid untuk durasi!")
        return
    
    # Menyimpan data ke dalam list dengan struktur yang mudah dipahami
    catatan_baru = {
        "mapel": mapel,
        "topik": topik,
        "durasi": durasi
    }
    catatan.append(catatan_baru)
    print("✓ Catatan belajar berhasil ditambahkan!\n")

def lihat_catatan():
    """Menampilkan semua catatan belajar dengan rapi"""
    print("\n--- Daftar Catatan Belajar ---")
    
    if not catatan:
        print("📝 Belum ada catatan belajar. Mulai tambahkan catatan baru!\n")
        return
    
    print(f"{'No':<4} {'Mapel':<15} {'Topik':<25} {'Durasi (menit)':<15}")
    print("-" * 60)
    
    for i, item in enumerate(catatan, 1):
        mapel = item["mapel"][:14]  # Batasi panjang teks
        topik = item["topik"][:24]
        durasi = item["durasi"]
        print(f"{i:<4} {mapel:<15} {topik:<25} {durasi:<15}")
    
    print()

def total_waktu():
    """Menghitung total durasi belajar dari semua catatan"""
    print("\n--- Total Waktu Belajar ---")
    
    if not catatan:
        print("📝 Belum ada catatan. Total waktu: 0 menit\n")
        return
    
    total = sum(item["durasi"] for item in catatan)
    jam = total // 60
    menit = total % 60
    
    print(f"Total waktu belajar: {total} menit ({jam} jam {menit} menit)")
    
    if target_harian > 0:
        persen = (total / target_harian) * 100
        print(f"Target harian: {target_harian} menit")
        print(f"Pencapaian: {persen:.1f}%")
        if persen >= 100:
            print("🎉 Selamat! Anda sudah mencapai target harian!\n")
        else:
            kurang = target_harian - total
            print(f"⏳ Masih perlu {kurang} menit lagi untuk mencapai target.\n")
    else:
        print()

def atur_target_harian():
    """Mengatur target waktu belajar harian"""
    global target_harian
    print("\n--- Atur Target Harian ---")
    
    try:
        target = int(input("Masukkan target waktu belajar harian (menit): "))
        if target < 0:
            print("⚠️  Target tidak boleh negatif!")
            return
        target_harian = target
        print(f"✓ Target harian berhasil diatur menjadi {target} menit!\n")
    except ValueError:
        print("⚠️  Masukkan angka yang valid!")
        print()

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Atur target harian")
    print("5. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "4":
        atur_target_harian()
    elif pilihan == "5":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")
