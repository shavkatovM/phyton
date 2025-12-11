#def daraja(x,y):
#  print(x ** y)

# daraja(4,8)
# daraja(9,6)
# daraja(5,7)


#Amaliyot
#Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.

# from datetime import datetime

# def yosh_hisobla(ism, familiya, tugilgan_yil):
#     hozirgi_yil = datetime.now().year
#     yosh = hozirgi_yil - tugilgan_yil
#     return f"{ism} {familiya} {yosh} yoshda"

# ism = input("Ismingizni kiriting: ")
# familiya = input("Familiyangizni kiriting: ")
# tugilgan_yil = int(input("Tug'ilgan yilingizni kiriting: "))

# natija= yosh_hisobla(ism, familiya, tugilgan_yil)
# print(natija)


#Amaliyot2
#Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.

def kvadrat_va_kub():
    son = float(input("Son kiriting: "))
    
    kvadrat = son ** 2
  
    kub = son ** 3
    print("Kvadrati:", kvadrat)
    print("Kubi:", kub)( )


