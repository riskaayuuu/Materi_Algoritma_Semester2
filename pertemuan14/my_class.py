class Bank:
    def __init__(self,saldo):
        self.__saldo = saldo

    def getSaldo(self):  # cara mengakses class yang private (.__)
        return self.__saldo
    
    def setSaldo(self,money):
        self.__saldo = money

bank1 = Bank(100)
bank1.setSaldo (9000)
print(bank1.getSaldo())     

bank1._Bank__saldo = 1000  
print(bank1.getSaldo())

print(bank1.__dict__)