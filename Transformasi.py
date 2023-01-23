
def dilatasi_a_b():
   x = float(input("x = "))
   y = float(input("y = "))
   k = float(input("k = "))
   a = float(input("a = "))
   b = float(input("b = "))
   print(k * (x - a)+a, k * (y - b)+b)
   #print(k * (y - b)+b)

def dilatasi():
   x = float(input("x = "))
   y = float(input("y = "))
   k = float(input("k = "))
   print(x * k, y * k)

jawab = input("Coba? y/n \n")
while jawab == "y":
   jawab2 = input("pilih rumus: \n 1.dilatasi AB \n 2.dilatasi \n 3.refleksi y=mx \n")
   if int(jawab2) == 1:
      dilatasi_a_b()
   elif int(jawab2) == 2:
      dilatasi()
   elif int(jawab2) == 3:
      print("Belum Tersedia")
   jawab = input("Coba lagi? y/n \n")