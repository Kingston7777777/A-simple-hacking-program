#A simple Hacking program written by Kingsley which is me
x = input("Enter your name?: ")
z = "Thanks for visiting"
if x == x:
   print(x.replace(x,"Hacked"))

y = input("To return your information back type Y?: ")

if y == "Y":
    print(x.replace("Hacked",x))
else:
    print(x.replace(x, "Hacked"))

print(z)