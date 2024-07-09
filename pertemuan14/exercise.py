class Book:
    def __init__(self,judul,penulis,tahun):
        self.__judul = judul
        self.__penulis = penulis
        self.__tahun = tahun

    def getJudul(self):
        return self.__judul
    def getPenulis(self):
        return self.__penulis
    def getTahun(self):
        return self.__tahun
    
    def Informasi(self):
        return f'Judul : {self.getJudul()}, Penulis : {self.getPenulis()}, Tahun Terbit : {self.getTahun}'
    
class Ebook(Book):
    def __init__(self,ukuran,judul,penulis,tahun):
        Book.__init__(self,judul,penulis,tahun)
        self.__ukuran = ukuran

    def info(self):
        return f'{self.Informasi()}, Ukuran file : {self.__ukuran}' 
    

        

    