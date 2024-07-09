class Hewan:
    def __init__(self, inputNama, inputJenis ):
        self.nama = inputNama
        self.jenis = inputJenis

    def info_hewan(self):
        return f'Nama : {self.nama} , Jenis : {self.jenis}'    

class Fish(Hewan):
    def __init__(self,nama,jenis,makanan):
        super().__init__(nama,jenis)
        Hewan.__init__(self,nama,jenis)
        self.makanan = makanan

    def info_fish(self):
        return f'{self.info_hewan()}, Makanan : {self.makanan}'

mujaer = Fish('Mujaer','Ikan Air Tawar','Lumut')
print(mujaer.info_fish())        

