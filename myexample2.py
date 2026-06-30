"""
gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
gunler.append("Salertesi")
gunler[7] = gunler[0]
del gunler[7]
print(f"{len(gunler)} tane eleman vardır")
for x in gunler[:]:
    print(x)

if "Salıertesi" not in gunler:
    print("Böyle bir eleman bulunmamaktadır")
"""

"""
numbers = [5, -9, 15.82, 87, -87]
numbers.sort()
print(numbers)
"""

"""
sayilar = []
x = 0
for x in range(10):
    if x%2 != 0:
        sayilar.append(x)
    x+=1

print(sayilar)
"""

"""
start, end = 4, 19
for num in range(start, end+1):
    if num % 2 != 0:
        print(num , end = " ")
"""

