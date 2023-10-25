print("#"*10," Välikoe ", "#"*10)
print()

#ehtorakenne1
kengankoko = int(input("Anna kengän koko: "))
if kengankoko < 30:
    print("Jalkasi on todella pieni!")
elif kengankoko < 36:
    print("Jalkasi on pieni")
elif kengankoko < 40:
    print("Jalkasi on normaalikokoinen")
elif kengankoko < 45:
    print("Jalkasi on suuri")
else:
    print("Jalkasi on todella todella suuri")
print()
print("#"*10," Seuraava tehtävä ", "#"*10)
#ehtorakenne2
ika = int(input("Kerro ikäsi: "))
if ika < 18 or ika > 65:
    print("Voit relata!")
else:
    print("Töihin siitä!")

print()
print("#"*10," Seuraava tehtävä ", "#"*10)
#while-silmukka1
mista = int(input("Anna eka luku: "))
mihin = int(input("Anna toinen luku: "))
while mista <= mihin:
    print(mista)
    mista+=1

print()
print("#"*10," Seuraava tehtävä ", "#"*10)
#while-silmukka2
while True:
    mjono = input("Anna merkkijono, 0 lopettaa: ")
    if mjono == "0":
        break
    print(mjono[-2:])

print()
print("#"*10," Seuraava tehtävä ", "#"*10)
#for-silmukka1
print(f"Anna viisi lukua: ")
luvut = []
for i in range(5):
    luvut.append(int(input()))
    if len(luvut) < 5:
        print("Seuraava!")
print()
print("Numerot ovat:")
for numero in range(len(luvut)):
    print(luvut[numero])

print()
print("#"*10," Seuraava tehtävä ", "#"*10)
#funktiot1
def tervehdi():
    print("Terveiset funktiosta!")
tervehdi()

print()
print("#"*10," Seuraava tehtävä ", "#"*10)
#funktiot2
def summa(x: int, y: int):
    vastaus = x+y
    return vastaus

def main():
    print("Anna kaksi lukua: ")
    luvut = []
    for i in range(2):
        luku = int(input())
        luvut.append(luku)
    vastaus = summa(luvut[0], luvut[1])
    print(f"Lukujen {luvut[0]} ja {luvut[1]} summa on {vastaus}")
    
if __name__ == "__main__":
    main()
print()
print("#"*10," Ohjelma päättyy ","#"*10)