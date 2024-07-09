import random

angka_acak = random.randint(1,10)
print(angka_acak)

while True:
    angka = int(input('Masukkan angka acak : '))
    if angka <=10 :
        print('tebakan benar')
    elif angka >=10:
        print('Tebakan terlalu tinggi')
    else:
        print('Tebakan terlalu rendah')        




