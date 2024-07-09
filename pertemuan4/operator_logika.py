a = True
b = False
print(a and b)
print(a or b)
print(not a)
print(not b)

bayar = False
absensi = 66

bayar_IN = (input('apakah sudah bayar? (true/false) :'))
bayar = (bayar_IN.lower() == 'true')
bayar = (bayar_IN.lower() == 'false')
absensi = (input('presentasi kehadiran:')) 
if bayar == True or absensi >= 70:
    print('Boleh Ujian')
else:
    print('Tidak Boleh Ujian') 


    


