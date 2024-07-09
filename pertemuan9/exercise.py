import numpy as np

array = []
def nilai(): 
    jumlah_siswa = int(input("Masukkan Jumlah Siswa : "))
    for i in range(jumlah_siswa):
        nilai_ujian_akhir = float(input(f"Masukkan nilai ujian akhir siswa ke {i+1} : "))
        array.append(nilai_ujian_akhir)

    rata_rata = np.mean(array)


    print(f"Nilai Rata-rata kelas : {rata_rata}")
    print(f"Nilai Tertinggi : {np.max(array)}")
    print(f"Nilai Terendah : {np.min(array)}")
    print(f"Jumlah siswa yang mendapatkan nilai diatas rata-rata : {np.sum(array > rata_rata)}")
    array.sort()
    print(f"Urutan nilai terendah ke nilai yang terbesar : {array}")
    array.reverse()
    print(f"nilai ujian siswa yang berada di per ingkat ketiga tertinggi : {array[2]}")
nilai()





