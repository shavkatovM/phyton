car_0 = {
        'model':'GENTRA',
        'rang':'oq',
        'yil':2018,
        'narh':13000,
        'km':50000,
        'korobka':'avtomat'
        }

car_1 = {
        'model':'SPARK',
        'rang':'qora',
        'yil':2015,
        'narh':9000,
        'km':89000,
        'korobka':'mexanika'
        }

car_2 = {
        'model':'MALIBU 2',
        'rang':'qizil',
        'yil':2019,
        'narh':15000,
        'km':20000,
        'korobka':'mexanika'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
        }
mashinalar = [car_0,car_1,car_2 ]
print(mashinalar[1])
for car in mashinalar:
    print(f"{car_0['model'].title()}, ")
    print(f"{car_1['rang'].title()}, ")
    print(f"{car_2['yil']}-yil, {car['narh']}")
    
#keyinki masala
#Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
shaxslar = [
    {
        "ism": "Abu Ali Ibm Sino",
        "soha": "Ilm-Fan";
        "Tavsif":"Buyuyk shifokor,olim,o'zbekiston og'loni" 
    },
    {
        "ism": "Alisher Navai",
        "soha": "Adabiyot",
        "Tavsifi": "Buyuk shoir, buyuk ajdodimiz, gazal mulki sultoni"
    }
]




for shaxs in shaxslar:
   print(f"ism: {shaxs['ism']}")
   print(f"soha: {shaxs['soha']}")
   print(f"Tavsif: {shaxs['Tavsif']}/n")         