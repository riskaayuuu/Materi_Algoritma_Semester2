person = [
    {'nama' : 'ecan', 'umur' : '24'},
    {'nama' : 'njun', 'umur' : '24'},
    {'nama' : 'icung', 'umur' : '22'}
]

person_new = {'nama' : 'lala','umur':'19'}
person.append(person_new)

for i in person:
    print('-',i['nama'],i['umur'])

