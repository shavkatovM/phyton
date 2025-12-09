#Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
Taomlar = []

print("novvi zakas baras!")

while True:
    menyu = ["shashlik", "somsa", "barak"]
    print("Menyuda bor taomlar:", menyu)

    buyurtma = input("Qaysi taomni tanlaysiz? ")
    Taomlar.append(buyurtma)

    shunda = input("Yana narsa aytasizmi? (ha/yo‘q): ")
    if shunda.lower() != "yo'q":
        break

print(f"Sizning buyurtmalaringiz: {Taomlar}")

#e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
mahsulotlar = []
while True:
    mahsulot = input('Mahsulot nomini ayting:')
    narx = input(f"{mahsulot.title()}ning narxi: ")
    mahsulotlar[mahsulot] = narx
    javob = input("yana mahsulot qo'shasiz bormi?(ha/yo'q)")
    if javob != 'ha':
        break
    #Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
    buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':45,
               'shaftoli':45,
               'tarvuz':35,
               'uzum':28}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")