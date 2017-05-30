Notatki z zajęć 5
=================

Konwencja nazewnictwa
---------------------
1. CamelCase dla nazw klas, atrybutów, komend i właściwości.
2. snake_case dla nazw metod, pól pomocniczych i modułów. 

Jakość wartości atrybutów
-------------------------
1. Co zrobić, gdy wiemy, że wartość atrybutu jest niepoprawna?
2. Jakości:
    * ATTR_VALID
    * ATTR_INVALID
    * ATTR_ALARM
    * ATTR_CHANGING
    * ATTR_WARNING
3. Możliwość określania w kodzie:
```python
from time import time
from PyTango import AttrQuality

def read_MyAttr(self):
    value = 0.0
    attr_quality = AttrQuality.ATTR_WARNING
    return value, time(), attr_quality
```

Schematy komunikacyjne
----------------------
1. Odpytywanie (polling) - aktywność ze strony użytkownika
    1. Wątki odpytywania.
    1. Możemy odpytywać:
        1. komendy,
        2. atrybuty.
2. Zdarzenia - aktywność ze strony serwera:
    1. Schemat komunikacji PUB-SUB.
    2. Typy zdarzeń:
        1. zmiana (change_event),
        2. okresowy (periodic_event),
        3. archiwizacji (archive_event).
    3. Konfiguracja zdarzeń.
    4. Możliwość własnoręcznego wysyłania z kodu:
        ```python
        from time import time
        from PyTango import AttrQuality
        
        def read_MyAttr(self):
            value = 0.0
            attr_quality = AttrQuality.ATTR_WARNING
            self.push_change_event("MyAttr", value, time(), attr_quality)
            self.push_archive_event("MyAttr", value, time(), attr_quality)
            return value, time(), attr_quality
        ```
    5.  Prosta subskrypcja po stronie klienta:
        ```python
        import PyTango
        
        device = PyTango.DeviceProxy('some/device/1')
        event_id = device.subscribe_event('SomeAttribute', PyTango.EventType.CHANGE_EVENT, PyTango.utils.EventCallBack())
        ```

System logowania w Tango
------------------------
1. Poziomy logów:
    1. OFF - brak logów,
    2. FATAL - błąd krytyczny, proces zostanie przerwany,
    3. ERROR - nieznany błąd, proces przetrwał,
    4. WARN - reprodukowalny błąd,
    5. INFO - wykonanie ważnego zadania,
    6. DEBUG - szczegóły dotyczące funkcjonowania urządzenia.
    7. Kolejność:
        1. DEBUG < INFO < WARN < ERROR < FATAL < OFF
2. Zapis logów:
    1. Podanie informacji w odpowiednim miejscu.
    2. Metody `*nazwa_poziomu*_stream`:
```python
from PyTango.server import Device, DeviceMeta

class MyDevice(Device):
   __metaclass__ = DeviceMeta
   def init_device(self):
       self.debug_stream("Some debug information")
```
3. Odczyt logów:
    1. Aplikacja LogViewer.
    2. Logowanie do pliku.
    3. Logowanie do konsoli.
    4. Zaawansowane - logowanie do urządzenia.
    
Ćwiczenie
---------
1. Napisać serwer urządzeń, który wylicza maksimum z atrybutu `double_image_ro` urządzenia typu TangoTest (np. `sys/tg_test/1`). Dopisać fragment kodu odpowiadający za wysyłanie zdarzeń.
2. Nazwa urządzenia, którego atrybut odczytujemy powinna być we właściwości urządzenia.
3. Uzależnić stan urządzenia od wartości powyższego atrybutu, np. 
	1. `DevState.OFF` dla wartości mniejszych od 20,
	2. `DevState.WARNING` dla wartości pomiędzy 20, a 30,
	3. `DevState.ON` dla wartości większych od 30.
4. Dodać atrybut, który odczytuje wartości atrybutu `double_scalar` urządzenia typu TangoTest. Ustawić mu polling na 100 ms oraz zapisywać jego aktualną wartość do debug_stream.
5. Dodać komendę, która będzie zmieniać jakość powyższego atrybutu pomiędzy wszystkimi dostępnymi. Należy również tą komendę odpytywać co 1,25 s. 
