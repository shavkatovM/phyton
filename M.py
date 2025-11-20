otam = {
    "ismi": "Mavlutdin",
    "tugilgan_yili": 1954,
    "tugilgan_joyi": "Samarqand viloyati"
}

# Ma'lumotni matn ko'rinishida chiqarish
print(f"Otamning ismi {otam['ismi']}, {otam['tugilgan_yili']}-yilda, {otam['tugilgan_joyi']}da tug'ilgan.")
sevimli_taomlar = {
    "Ali": "osh",
    "Vali": "manti",
    "Hasan": "sho'rva",
    "Husan": "lag'mon",
    "Madina": "shashlik"
}

# Kamida uch kishining taomini chiqarish
print(f"Alining sevimli taomi {sevimli_taomlar['Ali']}")
print(f"Valining sevimli taomi {sevimli_taomlar['Vali']}")
print(f"Hasanning sevimli taomi {sevimli_taomlar['Hasan']}")
python_lugati = {
    "integer": "butun son",
    "float": "o'nlik son",
    "string": "matn",
    "list": "ro'yxat",
    "dict": "lug'at",
    "if": "agar sharti",
    "else": "aks holda",
    "for": "takrorlash operatori",
    "while": "shartli sikl",
    "function": "funksiya"
}
soz = input("Biror Python atamasini kiriting: ").lower()

if soz in python_lugati:
    print(f"'{soz}' so'zining tarjimasi: {python_lugati[soz]}")
else:
    print("Bunday so'z mavjud emas.")
