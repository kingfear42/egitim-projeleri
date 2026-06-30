def topla():
    print("1.sayıyı giriniz:") 
    sayi1=int(input())
    print("2.sayıyı giriniz:")
    sayi2=int(input())
    toplam=sayi1+sayi2
    print(toplam)

def cikar():
    print("1.sayıyı giriniz:") 
    sayi1=int(input())
    print("2.sayıyı giriniz:")
    sayi2=int(input())
    cikar=sayi1-sayi2
    print(cikar)

def carp():
    print("1.sayıyı giriniz:") 
    sayi1=int(input())
    print("2.sayıyı giriniz:")
    sayi2=int(input())
    carp=sayi1*sayi2
    print(carp)

def bol():
    print("1.sayıyı giriniz:") 
    sayi1=int(input())
    print("2.sayıyı giriniz:")
    sayi2=int(input())
    bol=sayi1/sayi2
    print(bol)

print("Aşağıdaki işlemlerden hangisini yapmak istersiniz")
print("1.Topla")
print("2.Çıkar")
print("3.Çarp")
print("4.Böl")
print("Yukarıdakilerden bir tanesini seçiniz:")
secenek=int(input())

if secenek==1:
    topla()
elif secenek==2:    
    cikar()
elif secenek==3:
    carp()
elif secenek==4:
    bol()
else:
    print("Hatalı secenek girdiniz")
