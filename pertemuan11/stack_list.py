# Deklarasi stack 
stack = []

# Tambah data stack
stack.append('lord alul')
stack.append('iqbal')
stack.append('husain')
stack.append('mbape')

for index,value in enumerate(stack):
    print(f'{index} : {value}')

stack.pop() #elemen terakhir langsung otomatis terhapus
print('====================')
for index,value in enumerate(stack):
    print(f'{index} : {value}')

#mengecek dataa elemen Top/Peek
print(f'Data Stack Top : {stack[-1]}')    

print('Stack Kosong : ')
print(f'Ya' if len(stack) == 0 else 'Tidak') #untuk mengecek apakah stack is empty    

print(f'Jumlah Elemen Stack : {len(stack)}') #untuk menampilka jumlah elemen didalamnya





