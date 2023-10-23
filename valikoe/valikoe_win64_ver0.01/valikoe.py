otsikko = "Välikoe"
seuraava = "Seuraava tehtävä"
def seuraava_tehtava(): # Funktio tulostaa sanat "Seuraava tehtävä" risuaitoihin
    print()             # ennen tehtävää
    print("#","#"*len(seuraava),"#", sep='')
    print(f"#{seuraava}#")
    print("#","#"*len(seuraava),"#", sep='')
    print()

def virhe():
    print()
    print("Virhe: Et syöttänyt kokonaislukua.")
    while True:
        takaisin = input("Haluatko kokeilla uudestaan. (k)yllä/(e)i: ")
        if takaisin == "k":
            return True     # Palauttaa funktiota kutsuvalle ohjelmalle arvon True, ja
                            # käyttäjä siirtyy takaisin kyseisen ohjelman silmukan alkuun
        elif takaisin == "e":
            return False    # Palauttaa funktiota kutsuvalle ohjelmalle arvon False, ja
                            # käyttäjä siirtyy seuraavaan tehtävään
        else:
            print("Virhe: Syötä joko (k)yllä tai (e)i")


print()
print("#","#"*len(otsikko),"#", sep='')
print(f"#{otsikko}#")
print("#","#"*len(otsikko),"#", sep='')
print()

#ohjelmat alkavat
#ehtorakenne1
while True:
    try:
        kengankoko = int(input("Anna kengän koko: "))
        if kengankoko < 30:
            print()
            print("Jalkasi on todella pieni!")
        elif kengankoko < 36:
            print()
            print("Jalkasi on pieni")
        elif kengankoko < 40:
            print()
            print("Jalkasi on normaalikokoinen")
        elif kengankoko < 45:
            print()
            print("Jalkasi on suuri")
        else:
            print()
            print("Jalkasi on todella todella suuri")
        break
    except ValueError:
        if not virhe():
            break

seuraava_tehtava()

#ehtorakenne2
while True:
    try:
        ika = int(input("Kerro ikäsi: "))
        if ika < 18 or ika > 65:
            print()
            print("Voit relata!")
        else:
            print()
            print("Töihin siitä!")
        break
    except ValueError:
        if not virhe():
            break

seuraava_tehtava()

#while-silmukka1
while True:
    try:
        mista = int(input("Anna eka luku: "))
        mihin = int(input("Anna toinen luku: "))
        print()
        while mista <= mihin:
            print(mista)
            mista+=1
        break
    except ValueError:
        if not virhe():
            break

seuraava_tehtava()

#while-silmukka2
while True:
    mjono = input("Anna merkkijono, 0 lopettaa: ")
    if mjono == "0":
        break
    print(mjono[-2:])

seuraava_tehtava()

#for-silmukka1
while True:
    try: 
        print(f"Anna viisi lukua: ")
        luvut = []
        for i in range(5):
            luvut.append(int(input()))
            if len(luvut) < 5:
                print()
                print("Seuraava!")
        for numero in range(len(luvut)):
            if i == 4:
                i = 3
                print("#"*18)
                print()
            print(luvut[numero])
    except ValueError:
        if not virhe():
            break

seuraava_tehtava()

#funktiot1
def tervehdi():
    print("Terveiset funktiosta!")
tervehdi()

seuraava_tehtava()

#funktiot2
def summa(x: int, y: int):
    vastaus = x+y
    return vastaus

def main():
    while True:
        print("Anna kaksi lukua: ")
        luvut = []
        try:
            for i in range(2):
                luku = int(input())
                luvut.append(luku)
                if i == 0:
                    print("Anna toinen luku")
            vastaus = summa(luvut[0], luvut[1])
            print()
            print(f"Lukujen {luvut[0]} ja {luvut[1]} summa on {vastaus}")
            break
        except ValueError:
            if not virhe():
                break
if __name__ == "__main__":
    main()
#ohjelmat päättyvät

print()
print("#"*10," Ohjelma päättyy ","#"*10)
print()

loppu = "Syötä mitä tahansa lopettaaksesi ohjelman"
print("#","#"*len(loppu),"#", sep='')
print(f"#{loppu}#") 
print("#","#"*len(loppu),"#", sep='')
end = input()
