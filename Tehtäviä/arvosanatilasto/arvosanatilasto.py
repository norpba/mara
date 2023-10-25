# Kirjoita ratkaisu tähän
def kysely():
    pisteet_ja_maara = []
    while True:
        koekysely = (input("Koepisteet ja harjoitusten määrä: ")) # yksi syöte on yhden opiskelijan
        if koekysely == "":                                       # koepisteet ja harjoitusten määrä
            data = pisteet_ja_maara
            print("Tilasto:")
            return data
        pisteet_ja_maara.append(koekysely)

def listan_jakaminen(lista: list):
    koepisteet = []
    harjoitusten_lkmr = []
    for i in lista:
        jako = i.split()
        for osa in range(len(jako)):
            if osa % 2 == 0:
                koepisteet.append(int(jako[osa]))   
            else:
                harjoitusten_lkmr.append(int(jako[osa]))
    return koepisteet, harjoitusten_lkmr
    
def harjoituspisteet(lista: list):
    pisteet = []
    for luku in range(len(lista)):
        pisteraja = 10
        pisteita_per_harjoitus = 0
        while lista[luku] >= pisteraja:
            pisteraja+=10
            pisteita_per_harjoitus+=1
            if pisteraja > lista[luku]:
                pisteet.append(pisteita_per_harjoitus)
        if lista[luku] < 10:
            pisteet.append(pisteita_per_harjoitus)
    return pisteet

def karvo(koepisteet, harjoituspisteet: list):                                  # pisteiden keskiarvo saadaan jakamalla
    keskiarvo = (sum(koepisteet) + sum(harjoituspisteet)) / len(koepisteet)     # koepisteiden ja harjoituspisteiden summa
    print(f"Pisteiden keskiarvo: {keskiarvo:.1f}")                              # oppilaiden lukumäärällä

def hyv_prosentti_ja_pisteiden_summa(koepisteet, harjoituspisteet: list):
    kokonaispisteet = []
    for luku in range(len(koepisteet)):
        x = koepisteet[luku]
        y = harjoituspisteet[luku]
        kokonaispisteet.append(x+y)

    koe_lapi = []
    for pistemaara in range(len(kokonaispisteet)):
        pisteraja = 14
        if kokonaispisteet[pistemaara] > pisteraja and koepisteet[pistemaara] >= 10: #<-------- viimeisin muutos "and koepisteet jne"
            koe_lapi.append(kokonaispisteet[pistemaara])

    hyv_prosentti = (len(koe_lapi) / len(koepisteet))*100
    return hyv_prosentti, kokonaispisteet

def arvosanajakauma(kokonaispisteet, koepisteet: list): #kokonaispisteet = [23, 15, 15, 5]
    arvosanat = []
    i = 0
    for pistemaara in kokonaispisteet:
        if pistemaara > 27 and koepisteet[i] >= 10:
            arvosanat.append(5)
            
        elif pistemaara > 23 and koepisteet[i] >= 10:
            arvosanat.append(4)
            
        elif pistemaara > 20 and koepisteet[i] >= 10:
            arvosanat.append(3)
            
        elif pistemaara > 17 and koepisteet[i] >= 10:
            arvosanat.append(2)
            
        elif pistemaara > 14 and koepisteet[i] >= 10:
            arvosanat.append(1)
        else:
            arvosanat.append(0)
        i+=1
    arvosanalista = sorted(arvosanat)
    arvosanalista = arvosanalista[::-1]
    mahdolliset_arvosanat = [5, 4, 3, 2, 1, 0]
    
    for n in mahdolliset_arvosanat:
        if n in arvosanalista:
            kerroin = arvosanalista.count(n)
            print(f"  {n}: {'*'*kerroin}")
        else:
            print(f"  {n}:")
def main():
    data = kysely()
    koepisteet, harjoitusten_lkmr = listan_jakaminen(data)

    har_pisteytys = harjoituspisteet(harjoitusten_lkmr)
    keskiarvo = karvo(koepisteet, har_pisteytys)

    hyv_prosentti, kokonaispisteet = hyv_prosentti_ja_pisteiden_summa(koepisteet, har_pisteytys)
    print(f"Hyväksymisprosentti: {hyv_prosentti:.1f}")

    print("Arvosanajakauma: ")
    arvosanat = arvosanajakauma(kokonaispisteet, koepisteet)
main()

#if __name__ == "__main__":