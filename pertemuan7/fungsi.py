def cetak_string():
    print('Ini fungsi string')
cetak_string()

def sapaan(ucapan):
    print(ucapan)
sapaan("ini fungsi")


def penjumlahan(a,b):
    hasil = a + b
    print(hasil)

penjumlahan(5,10) 

def pengurangan(a,b):
    return a - b

print(pengurangan(10,5))

def bilangan(angka):
    if angka % 2 == 0:
        return 'Genap'
    else:
        return'Ganjil'

angka = int(input("Masukkan angka : "))   #jika ingin menambahkan inputan maka tambahkan xseperti baris 27 
print(bilangan(8))    

nama = 'ecan'

def cetak():
    nama = 'jamal'
    print(nama)

cetak()    
 

