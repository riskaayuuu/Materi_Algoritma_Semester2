nama = input('nama:')
umur = int(input('umur:'))
pekerjaam_ortu = str(input('pekerjaan:'))
gaji_ortu = int(input('gaji ortu:'))
ipk = float(input('ipk:'))

pekerjaan_pengecualian = ['PNS', 'DOKTER','POLISI']

if (pekerjaam_ortu not in  pekerjaan_pengecualian) and (gaji_ortu <= 1000000) and (ipk >= 2.7) and (umur <25):
    print('SELAMAT KM DPT!')
else: 
    print('YAHH BLM DPT')    