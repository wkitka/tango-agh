Notatki z zajęć 4
=================

Punkt organizacyjny
-------------------
1. Sala zostaje do końca kursu.

Obiektowość
-----------
1. Czym jest programowanie obiektowe?
2. Co może być obiektem?
3. Realizacja obiektowości w Tango.

Przypomnienie architektury:
---------------------------
1. Urządzenie a serwer urządzeń.
2. Elementy:
    1. Atrybuty (ang. attributes)
        1. Typy danych
        2. Wymiary
    2. Komendy (ang. commands)
    3. Właściwości (ang. properties)

Generator kodu POGO
-------------------
1. Informacje ogólne.
2. Opis struktury urządzenia.
3. Możliwość generacji kodu w różnych językach.

Przykładowy serwer
------------------
1. Opis logiki - symulacja odpowiedzi skokowej obiektu pierwszego rzędu.
2. Gdzie co się wstawia?
3. Pola chronione.
4. Uruchomienie serwera:
```console
python FirstOrderStepResponse.py test
```

Ćwiczenie: własny serwer urządzeń
---------------------------------
1. Serwer ma symulować odpowiedź impulsową obiektu 2 rzędu.
2. Należy dodać atrybuty odpowiadające pozostałym stałym.
3. Pokazać 3 typy odpowiedzi takiego obiektu:
    1. Oscylacje nietłumione.
    2. Oscylacje tłumione.
    3. Odpowiedź aperiodyczna.
    
Zadanie domowe:
---------------
1. Napisać serwer, który wylicza kąt z wartości atrybutu `double_scalar` urządzenia typu TangoTest
(np. `sys/tg_test/1`).
2. Nazwa urządzenia, którego atrybut odczytujemy powinna być we właściwości urządzenia.
2. Wskazówki:
    1. Amplituda zmian tego atrybutu to 360.
    2. Do obliczania arcus sinus można użyć funkcji `numpy.arcsin`.
    3. Odczyt atrybutu realizujemy przy pomocy klasy `PyTango.AttributeProxy`, np.:
```python
import PyTango
attr_proxy = PyTango.AttributeProxy('sys/tg_test/1/double_scalar')
value = attr_proxy.read().value  # metoda read() zwraca obiekt DeviceAttribute
```
