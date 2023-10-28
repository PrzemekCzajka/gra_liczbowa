import re, random

print("WITAJ W GRZE 'SEKRETNA LICZBA'")
print("SPRÓBUJ ODGADNĄĆ LICZBĘ WYLOSOWANĄ PRZEZ KOMPUTER")

def main():
    # Zapytaj o poziom trudności
    poziom_trudnosci = input("WYBIERZ POZIOM TRUDNOŚCI: ŁATWY, ŚREDNI, TRUDNY: ")

    # Wybierz odpowiedni zakres liczb i liczbę prób
    if poziom_trudnosci == "łatwy":
        zakres_liczb = range(1, 11)
        liczba_prob = 2
    elif poziom_trudnosci == "średni":
        zakres_liczb = range(1, 101)
        liczba_prob = 5
    else:
        zakres_liczb = range(1, 1001)
        liczba_prob = 10

    # Wylosuj liczbę
    liczba = random.choice(zakres_liczb)

    # Uruchom grę
    for i in range(1, liczba_prob + 1):
        # Pobierz od gracza liczbę
        gracz = input("Zgadnij liczbę od 1 do {}: ".format(max(zakres_liczb)))

        # Sprawdź, czy gracz podał liczbę
        poprawna_liczba = re.match(r"\d+", gracz)
        if poprawna_liczba is None:
            print("To nie jest liczba. Spróbuj ponownie.")
            continue
        gracz = int(gracz)

        # Sprawdź, czy gracz zgadł
        if gracz == liczba:
            print("Brawo, zgadłeś!")
            break
        else:
            if gracz > liczba:
                print("Liczba jest za duża.")
            else:
                print("Liczba jest za mała.")

    # Jeśli gracz nie zgadł po maksymalnej liczbie prób, to przegrywa
    if i == liczba_prob:
        print("Niestety, przegrałeś.")

if __name__ == "__main__":
    main()