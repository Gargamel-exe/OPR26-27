print("Hellooo♥")

# intiger - celo število
x = 10
y = -10
#operacije inta
print(x+y)
print(x-y)
print(x/y)
print(x*y)

# celoštevilsko deljenje
print(x//y)
print(int(x/y))

#deljenje z ostankom
print(x%y)

#preveri type
print(type("sks"))

#spreminjanje tipa
x = "12"
x = int(x) # float(x)
print(x+1)

print("rožle"*10) #edina operacija med str in int

# string - nizi znakov
a = "abc"
b = "def"

print(a+b)
#indeksiranje
print(a[0])
#print(a[10]) #index out of range

#rezine
#string[od:do:korak]
print(a[0:1])
print(a[::-1]) #od konca do začetka

print(len(a))
#f string
ime = "Jozef"
print(f"pozdravljen {ime}")