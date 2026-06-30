import random
def topla():
    print("1.sayıyı giriniz:")
    sayi1 = int(input())
    print("2.sayıyı giriniz:")
    sayi2 = int(input())
    toplam = sayi1 + sayi2
    print(sayi1, "+", sayi2, "=", toplam)
    return toplam

def cikar():
    print("1.sayıyı giriniz:")
    sayi1 = int(input())
    print("2.sayıyı giriniz:")
    sayi2 = int(input())
    cikarim = sayi1 - sayi2
    print(sayi1, "-", sayi2, "=", cikarim)
    return cikarim

def carp(): 
    
    print("1.sayıyı giriniz:")
    sayi1 = int(input())
    print("2.sayıyı giriniz:")
    sayi2 = int(input())
    carpim = sayi1 * sayi2
    print(sayi1, "*", sayi2, "=", carpim)
    return carpim

def bolme():
    print("1.sayıyı giriniz:")
    sayi1 = int(input())
    print("2.sayıyı giriniz:")
    sayi2 = int(input())
    bolme = sayi1 / sayi2
    print(sayi1, "/", sayi2, "=", bolme)
    return bolme

topla()

cikar()

carp()

bolme()


def main():
    print("1.topla")
    print("2.cikar")
    print("3.carp")
    print("4.bolme")
    print("5.çıkış")
    secenek = int(input())
    if secenek == 1:
        topla()
    elif secenek == 2:
        cikar()
    elif secenek == 3:
        carp()
    elif secenek == 4:
        bolme()
    elif secenek == 5:
        print("Çıkış Yapıldı")
        exit()
    else:
        print("Geçersiz İşlem")
        exit()

main()
