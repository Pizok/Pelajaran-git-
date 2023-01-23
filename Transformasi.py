
def function ():
   x = float(input("x = "))
   y = float(input("y = "))
   k = float(input("k = "))
   a = float(input("a = "))
   b = float(input("b = "))
   print(k * (x - a)+a)
   print(k * (y - b)+b)

jawab = input("Coba? y/n \n")
while jawab == "y":
    function()
    jawab = input("Coba lagi? y/n \n")