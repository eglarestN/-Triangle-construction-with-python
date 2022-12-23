kenar_uzunlugu = int(input("üçgeniniz kenar uzunluklari ne kadar olsun: "))

for k in range(kenar_uzunlugu):
    for i in range(k + 1):
        print("*", end='')
    print()

uzun_kenar = int(input("dikdörgenin uzun kenarini giriniz: "))
kisa_kenar = int(input("dikdörtgenin kisa kenarini giriniz: "))

for k in range(uzun_kenar):
    for i in range(kisa_kenar):
        print("*", end='')
    print()