#1Masala
#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar  = ["O'ZBEKISTON", "AMERICA", "KOREYA", "TURKIYA"]

#2Masala
#Ro'yxatning uzunligini konsolga chiqaring
davlatlar  = ["O'ZBEKISTON", "AMERICA", "KOREYA", "TURKIYA"]
print("DAVLATLAR UZUNLIGI:",len(davlatlar))

#3MASAlA
#sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
davlatlar  = ["O'ZBEKISTON", "AMERICA", "KOREYA", "TURKIYA"]
sorted(davlatlar)
print(davlatlar)

#4MASALA
#sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
davlatlar  = ["O'ZBEKISTON", "AMERICA", "KOREYA", "TURKIYA"]
print(sorted(davlatlar , reverse=True))

#5MASALA
#Asl ro'yxatni qaytadan konsolga chiqaring
davlatlar  = ["O'ZBEKISTON", "AMERICA", "KOREYA", "TURKIYA"]
print("Asl ro'yxat:",davlatlar)

#6MASALA
#reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar  = ["O'ZBEKISTON", "AMERICA", "KOREYA", "TURKIYA"]
davlatlar.reverse()
print(davlatlar)

#7MASALA
#sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
davlatlar  = ["O'ZBEKISTON", "AMERICA", "KOREYA", "TURKIYA"]
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

#8MASALA
#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
sonlar = list(range(120,1200))
print(sonlar)


#9MASALA
#Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring

print("sonlar yigindisi: {sum(sonlar)}")

