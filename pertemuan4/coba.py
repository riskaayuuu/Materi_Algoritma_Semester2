print('============== KONVERSI BILANGAN DESIMAL ==============')
decimal = int(input("Masukkan angka desimal yang akan dikonversi: "))
biner = bin(decimal)[2:].replace("0b", "")
nama_biner = "Biner"

octal = oct(decimal)[2:].replace("0o", "")
nama_octal = "Octal"

hexadesimal = hex(decimal)[2:].replace("0x", "")
nama_hexadesimal = "Hexadesimal"

print(f"{decimal} dalam {nama_biner} adalah {biner}")
print(f"{decimal} dalam {nama_octal} adalah {octal}")
print(f"{decimal} dalam {nama_hexadesimal} adalah {hexadesimal}")
print('============== KONVERSI BILANGAN SELESAI ==============')


