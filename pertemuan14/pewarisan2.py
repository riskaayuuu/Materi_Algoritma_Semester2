class Hewan:
    def __init__(self,nama):
        self.__nama = nama

    def getNama(self):
        return self.__nama
class Fish:
    def __init__(self,jenis):
        self.__jenis = jenis

    def getJenis(self):
        return self.__jenis    

class Lele(Hewan,Fish):
    def __init__(self, nama,jenis,makanan):
        Hewan.__init__(self,nama)
        Fish.__init__(self,jenis)
        self.__makanan = makanan

    def info(self):
        return f'Nama : {self.getNama()} , Jenis : {self.getJenis()} , Makanan : {self.__makanan}' 
    
object1 = Lele('Lele','Air Tawar','Pulut')
print(object1.info())    

