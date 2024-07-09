for i in range(2,5):
    print('Ayo berhitung ',i)

fruits = ['apel', 'durian', 'kiwi', 'pisang']
numbers = [1,4,5,6,7,8]
print('\n') #untuk memberi jarak 

for fruit in fruits:
    print(fruit)
print('\n')  

for index,fruit in enumerate(fruits):
    print(index,fruit)
print('\n')

for number,fruit in zip(numbers,fruits):  #untuk menggabungkan dan menampilkan fruits dan numbers 
   print(number,fruit)
print('\n')

names = 'Riska Ayu Meilani'
for name in names:
    print(name)    

biodata = {'Nama':'Riska Ayu Meilani', 'NIM':'23090153'}    
for data in biodata: #menampikan labelnya saja seperti Nama dan NIM
    print(data)
print('\n')

for value in biodata.values(): #perintah untuk menampilkan value 
    print(value)    
print('\n')

for label,value in biodata.items(): #untuk menampilkan label dan value
    print(label,":",value)    
print('\n')    

for i in range (1,11):
    if i % 2 == 0:
        print(i, 'adalah bilangan genap')
    else:
        print(i, 'adalah bilangan ganjil')