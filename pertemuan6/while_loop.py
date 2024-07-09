# i = 1
# while i <= 10:
#     print('Mari berhitung ', i)
#     i += 1

# total_perulangan = 0
# while True:
#     main = input('Ingin keluar atau tidak? [Ya/Tidak]: ').lower()
#     if main == 'ya':
#         break
#     total_perulangan += 1
# print('Total perulangan : ',total_perulangan)    

while True:
    angka = int(input('Masukkan Angka : '))
    if angka % 2 == 0:
        print(angka,'adalah bilangan genap')
    else:
        print(angka,'adalah bilangan ganjil')    


