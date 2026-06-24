import csv
from collections import deque

FILE = "data_barang.csv"

# =============================
# LOAD DATA (HASHMAP)
# =============================
def load_data():
    data = {}
    try:
        with open(FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data[row['id']] = row
    except FileNotFoundError:
        pass
    return data

# =============================
# SAVE DATA
# =============================
def save_data(data):
    with open(FILE, mode='w', newline='') as file:
        fieldnames = ['id', 'nama', 'stok', 'harga']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in data.values():
            writer.writerow(item)

# =============================
# CREATE (QUEUE)
# =============================
def tambah_barang(data):
    q = deque()

    id = input("ID: ")
    nama = input("Nama: ")
    stok = input("Stok: ")
    harga = input("Harga: ")

    q.append({'id': id, 'nama': nama, 'stok': stok, 'harga': harga})

    item = q.popleft()
    data[item['id']] = item

    save_data(data)
    print("Barang berhasil ditambahkan!")

# =============================
# READ
# =============================
def lihat_barang(data):
    for item in data.values():
        print(item)

# =============================
# UPDATE
# =============================
def update_barang(data):
    id = input("Masukkan ID: ")
    if id in data:
        data[id]['nama'] = input("Nama baru: ")
        data[id]['stok'] = input("Stok baru: ")
        data[id]['harga'] = input("Harga baru: ")
        save_data(data)
        print("Data diupdate!")
    else:
        print("Tidak ditemukan!")

# =============================
# DELETE
# =============================
def hapus_barang(data):
    id = input("Masukkan ID: ")
    if id in data:
        del data[id]
        save_data(data)
        print("Data dihapus!")
    else:
        print("Tidak ditemukan!")

# =============================
# SEARCHING (LINEAR SEARCH)
# =============================
def cari_barang(data):
    keyword = input("Cari nama: ")
    for item in data.values():
        if keyword.lower() in item['nama'].lower():
            print(item)

# =============================
# SORTING
# =============================
def sorting_barang(data):
    sorted_data = sorted(data.values(), key=lambda x: x['nama'])
    for item in sorted_data:
        print(item)

# =============================
# MAIN PROGRAM
# =============================
def main():
    data = load_data()

    while True:
        print("\n=== MENU ===")
        print("1. Tambah")
        print("2. Lihat")
        print("3. Update")
        print("4. Hapus")
        print("5. Cari")
        print("6. Sorting")
        print("0. Keluar")

        pilih = input("Pilih: ")

        if pilih == '1':
            tambah_barang(data)
        elif pilih == '2':
            lihat_barang(data)
        elif pilih == '3':
            update_barang(data)
        elif pilih == '4':
            hapus_barang(data)
        elif pilih == '5':
            cari_barang(data)
        elif pilih == '6':
            sorting_barang(data)
        elif pilih == '0':
            break
        else:
            print("Pilihan salah!")

main()