#1amaliyot
ismlar = ["SHIROKI", "BEGI PO", "BUXARSKIY"]
print(f"{ismlar[0]} ishlar qalay")
#2amaliyot 
#sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 
sonlar = [1,90,-20,534,999]
print(sonlar)
#3amaliyot 
#Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 
sonlar = [1,90,-20,534,999]
print(sonlar[0] + sonlar[4])
#4amliyot
#t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 
t_shaxslar = ["Jaloliddin Manguberdi", "IMOM AL-Buxoriy", "Amir Temur"]
z_shaxslar = ["Bobur Nurmetov", "YARIIY", "GREEN 71"]
#5amaliyot
#Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
JADIDLAR = t_shaxslar.pop(2)
z_shaxs =  z_shaxslar.pop(1)
print("MAN" + JADIDLAR + " SHU INSONNI YAXSHI TANIYMAN ")
print("BU" + z_shaxs + " INSONNI JUDA HURMAT QILAMAN ")