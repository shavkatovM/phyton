#1masala
#Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 


izohli_lugati = {
    "background-color" : "orqa fon o'zgartirish",
    'title' : 'sarlavha qoyish uchun ishlariladi',
    'font-size' : 'bu matn olchami'
}
print(izohli_lugati)

#2masala
#Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring. 

# Davlatlar va poytaxtlar lug'ati
davlatla = {
    "O'zbekiston": "Toshkent",
    "Qozog'iston": "Astana",
    "Qirg'iziston": "Bishkek",
    "Tojikiston": "Dushanbe",
}

# Davlatlarni alifbo tartibida chiqarish
print("Davlatla")
for country in sorted(davlatla.keys()):
    print(country)

print("\nPoytaxtlar")
# Poytaxtlarni alifbo tartibida chiqarish
for capital in sorted(davlatla.values()):
    print(capital)

