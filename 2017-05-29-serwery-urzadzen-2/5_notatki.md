Notatki z zajęć 5
=================

Schematy komunikacyjne:
-------------------------
1. Polling:
    1. komendy,
    2. atrybuty,
2. Zdarzenia:
    1. change_event:
        1. rel_change,
        2. abs_change,
    2. periodic_event:
        1. event_period,
    3. archive_event:
        1. archive_rel_change,
        2. archive_abs_change,
        3. archive_period,

System logowania w Tango:
-------------------------
1. Poziomy logów:
    1. OFF - brak logów,
    2. FATAL - błąd krytyczny, proces zostanie przerwany,
    3. ERROR - nieznany błąd, proces przetrwał,
    4. WARN - reprodukowalny błąd,
    5. INFO - wykonanie ważnego zadania,
    6. DEBUG - szczegóły dotyczące funkcjonowania urządzenia,
    7. Kolejność:
        1. DEBUG < INFO < WARN < ERROR < FATAL < OFF
2. Zapis logów:
    1. Podanie informacji w odpowiednim miejscu:
        ```python
        self.debug_stream("-errorIndex: {}".format(errorIndex))
        ```
3. Odczyt logów:
    1. Aplikacja LogViewer.
    
Ćwiczenie:
----------