# Kompresja RLE - Flamaster (SPOJ FLAMASTE)

## Opis
Projekt jest implementacją w Pythonie rozwiązującą problem [SPOJ FLAMASTE](https://pl.spoj.com/problems/FLAMASTE/).
Program wykorzystuje algorytm **Run-Length Encoding (RLE)** do skracania napisów poprzez zliczanie następujących po sobie identycznych znaków.

## Jak działa algorytm?
Program iteruje po podanym ciągu znaków i zlicza powtórzenia:
1.  Porównuje bieżący znak z poprzednim.
2.  Jeśli są takie same, zwiększa licznik.
3.  Jeśli są różne, dopisuje znak i wartość licznika do wyniku, a następnie resetuje licznik.

### Przykładowa kompresja:
* Wejście: `AAABBBBCC`
* Wyjście: `A3B4C2`

## Uruchomienie
Wymagany jest Python 3.

```bash
python main.py
