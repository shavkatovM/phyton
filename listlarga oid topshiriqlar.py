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
 
 #6amaliyot
 #friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 
friends = []
friends.append("SHOXZOD")
friends.append("ZAVOHIR")
friends.append("DIYOR")
friends.append("ISROIL")
friends.append("BEKMUROT")
 #7amaliyot
 #Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
 
friends = ["SHOXZOD" , "JAVOHIR" , "ISROIL", "BEKMUROT"  ]
friends.remove("JAVOHIR")
 
 #8amaliyot
 #Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends = ["SHOXZOD" , "JAVOHIR" , "ISROIL", "BEKMUROT"  ]
friends.insert(1, "IBRAT USTOZ ")
friends.insert(0, "SHABNAM")
friends.insert(2,"SHOXRUXXON ")
#9AMALIYOT
#Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar = []
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(0))
print("\nKelgan mehmonlar: ", mehmonlar)
