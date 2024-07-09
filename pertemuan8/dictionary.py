person = {'name' : 'jay', 'umur' : '40', 'city' : 'seoul'}

person['fav'] = 'mie' # menambahkan label value
print(person)

person['umur'] = '24' # mengganti isi value dari 40 menjadi 24
print(person)

del person['city'] #menghapus label city
print(person)

print(person['name']) #menampilkan salah satu value

