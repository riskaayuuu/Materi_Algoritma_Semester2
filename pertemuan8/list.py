person = ['dimas','bagas','idris','izat']

person.append('wildan') #menambahkan data didalam akhir elemen list
print(person)

person.insert(1,'dulah') #menambahkan data diantara elemen list
print(person)

person.remove('dimas') #menghapus data dengan cara sebutkan kalimatnya
print(person) 

del person[4] # menghapus data tertentu dalam list
print(person) 

person.pop() # kalau tidak mengisi yg didalam kurung otomatis menghapus data yg paling terakhir
print(person) 

person1 = ['wildan','dimas','izat','iwan','izat']

print(person1[3]) # mengecek index ke 3 itu berisi data apa

print(person1.index('izat')) # mengecek izat itu di index ke berapa

print(person1.count('izat')) # mengecek ada berapa izat di list misal 2/3

person2 = ['cindy','bagas','adel','zaenal']

person2.sort() # mengurutkan sesuai abjad?
print(person2)

person2.reverse() # membalik data akhir menjadi data awal posisinya
print(person2)

print(len(person2))
