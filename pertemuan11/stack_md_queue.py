from queue import LifoQueue

# Deklarasi stack
stack = LifoQueue()

# Tambah data stack (QUEUE PAKE PUT)
stack.put('Abdul')
stack.put('Lasso')
stack.put('Husain')
stack.put('Iqbal')

# Display Stack
print(stack.queue)

# Menampilkan top elemen stack
print(f'Top/Peek Stack : {stack.queue[-1]}')

# Hapus elemen stack
stack.get()
print(stack.queue)

# Mengecek stack kosong / tidak
print(f'Stack Kosong/Tidak : {stack.empty()}')

print(f'Stack Full/Tidak : {stack.full()}')

# Menentukan jumlah elemen stack
print(f'Jumlah Stack : {stack.qsize()}')
