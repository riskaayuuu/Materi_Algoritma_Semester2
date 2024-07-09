def penjumlahan(a,b):
    return a + b

def pengurangan(a,b):
    return a - b

def pembagian(a,b):
    return a / b

def perkalian(a,b):
    return a* b

def pangkat(a,b):
    return a**b

def bilangan(angka):
    if angka % 2 == 0:
        return 'Genap'
    else:
        return 'Ganjil'
    
def menu():
    print("Pilih operasi matematika")
    print('1. Penjumlahan')
    print('2. Pengurangan')
    print('3. Perkalian')   

def operasi():
   pilihan = input('masukkan pilihan anda: ')
   a = int(input('Masukkan bilangan pertama: '))
   b = int(input('Masukkan bilangan kedua: '))
   if pilihan == '1': 
      print(penjumlahan(a,b))
   elif pilihan == '2':
       print(pengurangan(a,b))
   else:
       print(perkalian(a,b)) 


       
          
