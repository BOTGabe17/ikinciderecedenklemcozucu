from math import sqrt

a = 0
b = 0
c = 0

x = input("değişken giriniz:")
soru_sayac = int(input("kaç değişken girelecek?"))

terimler = []
katsayılar = []
katsayı = "" 
kod = 0

for n in range(soru_sayac):
    terim = input("terim giriniz.")
    terimler.insert(1,terim)

for n in range(soru_sayac):
     terim = terimler[n]
     for i in range(len(terim)):
        if terim[i] == x:
           if len(terim) - 1 != i:
                katsayı = terim[:i]
                if katsayı == '':
                    a = 1
                    katsayılar.insert(1,a)
                    break
                if katsayı == '-':
                    a = -1
                    katsayılar.insert(1,a)
                    break
                a += int(katsayı)
                katsayılar.insert(1,katsayı)
                break
           else:
                katsayı = terim[:i]
                if katsayı == '':
                    b = 1
                    katsayılar.insert(1,b)
                    break
                if katsayı == '-':
                    b = -1
                    katsayılar.insert(1,b)
                    break
                b += int(katsayı)
                katsayılar.insert(1,katsayı)
                break

        elif len(terim) - 1 == i:
            katsayı = terim
            c += int(katsayı)
            katsayılar.insert(1,katsayı)


delta = b**2 - 4*a*c

if(delta < 0):
    print("denklemin reel kökü yoktur")
elif(a == 0):
    print("denklem 2. derece değil.")
else:

    diskriminant1 = (-b + sqrt(delta))/ (2*a)
    diskriminant2 = (-b - sqrt(delta))/ (2*a)
    
    print(diskriminant1,diskriminant2)
