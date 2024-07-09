#Deklarasi queue
queue = []

# fungsi Tambah data
def enqueue(item):
    queue.append(item)

# fungsiHapus Data
def dequeue():
    queue.pop(0)

# fungsiHapus Data jika data kosong
def dequeue():
    if len(queue) == 0:
        print('Data Kosong : Tidak Bisa Hapus')
    else:
        queue.pop(0)

# fungsi Panggil data pertama
def front():
    return queue[0]

#fungsi untuk menjalankan jika data pertama kosong 
def front():
    if len(queue) < 1:
        return 'Queue Kosong'
    else:
        return queue[0]
    
# fungsi untuk menampilkan data terakhir 
def tail():
    if len(queue) < 1:
        return 'Queue Kosong'
    else:
         return queue[-1]
    
#Fungsi untuk menampilkan data kosong atau tidak 
def isEmpty():
    if len(queue) == 0:
        return ' Queue Kosong'
    else:
        return 'Queue Tidak Kosong'

# Panggil Fungsi enqueue
enqueue('ABC')
enqueue('DEF')
enqueue('GHI')

#Panggil Fungsi dequeue
dequeue()
dequeue()

print(queue)
print(f'Data Front : {front()}')
print(f'Data Terakhir : {tail()}')
print(f'apakah data kosong atau tidak : {isEmpty()}')