Notatki z zajęć 6
=================

Punkt organizacyjny
-------------------
1. Co z kolejnymi zajęciami?

Systemy [SCADA](https://en.wikipedia.org/wiki/SCADA)
-------------
1. Supervisory, Control and Data Acquisition - rozwinięcie skrótu i podsumowanie zadań systemu.
2. Ogólnie: Zarządzanie procesami technologicznymi / eksperymentami naukowymi.
3. Przydatne w rozproszonych systemach sterowania. 
4. [Mnogość rozwiązań](http://automatykaonline.pl/Artykuly/Komputery-i-HMI/Wybor-systemu-SCADA-czym-sie-kierowac). Przykłady:
    1. Zenon
    2. InTouch

[Sardana](http://sardana-controls.org/en/latest/) - główne cechy
----------------------------------------------------------------
1. Zarządzanie eksperymentami na liniach badawczych.
2. Prowadzenie pomiarów i zapis danych z nich pochodzących.
3. Prosty i zunifikowany dostęp do ruchu komponentami linii.
4. W całości napisana w Pythonie 2.7.
5. Szeroko używana w środowisku synchrotronów europejskich.

Architektura Sardany
--------------------

![sardana-architecture](http://sardana-controls.org/en/latest/_images/sardana_sketch.png)

1. Interfejsy użytkownika:
    1. GUI oparte na Taurusie: gotowe i w kawałkach.
    2. Interfejs linii poleceń `spock`.
2. Dwie części serwera urządzeń Sardana:
    1. Serwer makr (`MacroServer`) - przechowuje i wykonuje procedury od użytkowników.
    2. Pula urządzeń (`Pool`) - zarządza urządzeniami i wykonuje na nich bezpośrednie operacje.
        1. Kontrolery do różnych typów urządzeń i kanałów pomiarowych (w tym czysto programowych).
        2. Pośrednicznie między warstwą Sardany a Tango.
        3. Synchronizacja operacji.
        4. Grupowanie urządzeń.
3. Powiązania z systemem sterowania Tango.

Ćwiczenie - uruchomienie makr
-----------------------------
1. Uruchomić polecenie `spock` w konsoli.
2. Znaleźć w [dokumentacji](http://sardana-controls.org/en/latest/users/standard_macro_catalog.html) makra do:
    1. Wypisania wszystkich motorów.
    2. Wypisania wszystkich kontrolerów.
    3. Poruszenia motorem  `mot01` do pozycji 100.
    
Skan
----
1. Zbieranie danych w trakcie ruchu elementów zmotoryzowanych.
2. Jakie dane zbierane są w czasie skanów?
3. Typy skanów:
    1. Relatywne / absolutne.
    2. Jedno- / wielowymiarowe.
    
Ćwiczenie - skany
-----------------
1. Uruchomić `spock` w konsoli.
2. Wpisać: `senv ScanDir /home/tango-cs/Documents/`, aby ustawić miejsce zapisywania danych ze skanów.
3. Wpisać: `senv ScanFile test_scan.dat`, aby ustawić plik do zapisywania danych.
4. Uruchomić polecenie `dscan?`, a następnie uruchomić skan.
5. Uruchomić polecenie `expconf`.

Zadanie domowe
--------------
1. Napisać makro, które:
    1. Ustawi `ScanDir` i `ScanFile`.
    2. Ustawi grupę pomiarową (`ActiveMntGrp`) na `mntgrp01`.
    3. Uruchomi `dscan` motorem `mot01` (dobrać samemu parametry skanu).
2. Samouczek pisania makr jest dostępny [tu](http://sardana-controls.org/en/latest/devel/howto_macros/macros_general.html).
3. Dołączenie makr do `MacroServer` polega na ustawieniu właściwości `MacroPath` urządzenia `MacroServer`
na katalog zawierający plik z makrem. Następnie należy zrestartować `MacroServer` przez aplikację Astor.