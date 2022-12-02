#test case 1
kata = input("Masukkan kata:")
def left(kata):
    y=kata[2:5]
    return y
x=left(kata)
print("Huruf yang diambil pada kata", kata ,'adalah', x)



#Test case 2
kata = input("Masukkan kata:")
def left(kata):
    y=kata[0:3]
    return y
x=left(kata)
def left(kata):
    z=kata[5:8]
    return z
y=left(kata)
print("Huruf yang diambil pada kata", kata ,'adalah', x ,'dan', y)
