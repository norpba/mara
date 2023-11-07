
# tentti Heikki Niinimäki 7.11.2023

# tentti alkaa

from random import randint

def tulostukset():
    print()
    print("#"*15)
    print()

def koe():

    print()
    print("#"*13)
    print("Tentti alkaa!")
    print("#"*13)
    print()

    # tiedosto1 <- toimii

    lause = input("Anna lause: ")
    with open("testi1.txt", "w") as tiedosto:
        tiedosto.write(lause)



    tulostukset()
    # tiedosto2 <- toimii

    lause = input("Anna lause: ")
    with open("testi2.txt", "a") as tiedosto:
        tiedosto.write(lause)



    tulostukset()
    # poikkeukset <- toimii

    luvut = []
    while True:
        try:
            lisays = input("Anna kokonaisluku, (0 lopettaa): ")
            luku = int(lisays)
            if lisays == "0":
                print(luvut)
                break
            luvut.append(luku)
        except ValueError:
            print(f"{lisays} ei ollut kokonailuku...")
            continue



    tulostukset()
    # viittaukset <- toimii

    def poista_suurin(luvut: list):
        luvut = luvut.remove(max(luvut))

    luvut = [2, 4, 6, 1, 3, 5]
    poista_suurin(luvut)
    print(luvut)



    tulostukset()
    # sanakirja <- toimii

    leffa_ja_paaosa = {}

    while True:
        leffa = input("Anna elokuvan nimi (tyhjä lopettaa): ")
        if leffa == "":
            nayttelija_valinta = input("Anna näyttelijän nimi, jonka elokuvat tulostetaan: ")
            for n in leffa_ja_paaosa:
                if leffa_ja_paaosa[n] == nayttelija_valinta:
                    print(n)
            break
        paaosa = input("Anna päänäyttelijän nimi: ")
        leffa_ja_paaosa[leffa] = paaosa



    tulostukset()
    # random1 <- toimii

    print("Heitetään kolikkoa viidesti:")
    for i in range(5):
        kolikonpuoli = randint(0, 1)
        if kolikonpuoli == 0:
            print("Klaava!")
        else:
            print("Kruuna!")



    tulostukset()
    # random2 <- toimii

    luvut = []
    while True:
        try:
            alku = int(input("Anna alku: "))
            loppu = int(input("Anna loppu: "))
            maara = int(input("Anna määrä: "))

            for i in range(maara):
                valinta = randint(alku, loppu)
                if valinta not in luvut:
                    luvut.append(valinta)
                else:
                    while valinta in luvut:
                        valinta = randint(alku, loppu)
                    luvut.append(valinta)
            print(luvut)
            break
        except ValueError:
            print("Syötteissä oli virheitä")
            jatkoa = input("(j)atkentaanko vai (l)opetetaanko?")
            if jatkoa == "j":
                continue
            else:
                break
    print()
    print("#"*14)
    print("Tentti loppuu!")
    print("#"*14)
    print()

if __name__ == "__main__":
    koe()

# tentti loppuu
