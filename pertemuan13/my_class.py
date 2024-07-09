class Mobil:
    def __init__(self,merk,model,tahun):
        self.merk = merk
        self.model = model
        self.tahun = tahun

mobil1 = Mobil('Honda','Ayla',2019) 
print(mobil1.__dict__)

mobil2 = Mobil('Ducati','A4',2020)
print(mobil2.__dict__)

class PersegiPanjang:
    def __init__(self,panjang,lebar):
        self.panjang = panjang
        self.lebar = lebar

    def get_luas(self):
        return self.panjang * self.lebar
    
persegi1 = PersegiPanjang(90,10)
print(persegi1.get_luas())

persegi2 = PersegiPanjang(5,10)
print(persegi2.get_luas())    

