print('========== Program Manipulasi String ==========')
print('pilihan menu: ')
print('1. Hitung kata')
print('2. Ubah kata')

pilihan=int(input('Pilihan anda: '))

kalimat=input('Masukan sebuah kalimat/kata: ')

def hitung_kata():
    a=input('Masukan kata yang ingin di hitung: ')
    x.count(a)
    print('terdapat sebanyak',x,'kata',a,'di dalam kalimat')

def ubah_kata():
    b=input('Masukan kata yang ingin di ubah: ')
    c=input('Masukan kata pengganti: ')
    d=c.replace(b,c)
    print('String berhasil diubah menjadi: ',d)

if pilihan=='1':
    Hitung_kata()

elif kalimat=='2':
    ubah_kata()

else:
    print('kata yang di input tidak terdaftar')
