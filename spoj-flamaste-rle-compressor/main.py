def main():
    napis = "AAABBBBCC"
    wynik = kompresuj(napis)
    print(wynik)

def kompresuj(napis):
    pusta = ""
    licznik = 1

    for i in range(1, len(napis)):
        if napis[i] == napis[i - 1]:
            licznik += 1
        else:
            pusta += napis[i - 1] + str(licznik)
            licznik = 1
    
    pusta += napis[-1] + str(licznik)
    return pusta

main()
