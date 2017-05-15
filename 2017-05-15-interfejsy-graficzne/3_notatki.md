Notatki z zajęć 3
=================

Punkt organizacyjny
-------------------
1. Co z salą?
2. Czy forma prezentacji notatek jest w porządku?
3. Praktyki!

Przygotowanie do zajęć
----------------------
1. Instalacja pipa: `sudo apt-get install python-pip`
2. Upgrade taurusa: `sudo pip install -U taurus`

Prezentacja biblioteki Taurus
-----------------------------
1. Biblioteka graficzna do wizualizacji różnych elementów systemu Tango:
    1. API dla programistów
    2. Proste narzędzia dla użytkowników
2. Jest rozszerzeniem biblioteki PyQt4 - bindingu Qt do Pythona.
3. Adaptacja do innych systemów jest rozwijana.
4. Dokumentacja dostępna tu: http://www.taurus-scada.org/

Narzędzia biblioteki Taurus
---------------------------
1. TaurusForm.
    1. Własnoręcznie zdefiniowany zestaw atrybutów -> TaurusModelChooser
    2. Automatyczne włączenie edycji.
    3. Ustawianie limitów dla atrybutów urządzeń (przez Jive).
    4. Ustawienie wyliczania parametrów -> `eval://`
    5. Zapisywanie konfiguracji.
    
2. TaurusDevicePanel:
    1. Uruchamianie z nazwą urządzenia.
    2. Który panel z poprzednich zajęć Wam to przypomina?
    
3. TaurusTrend:
    1. Opcje uruchomieniowe.
    2. Wybór atrybutów.
    3. Opcje wykresu.
    4. Tryb inspekcji danych.
    5. Przybliżanie i resetowanie widoku.
    6. Okres wymuszonego odczytu.
    7. Zmiana tytułów wykresów w legendzie.
    8. Zapisywanie danych.
4. TaurusGUI:
    1. Połączenie wszystkich mniejszych klocków.
    2. Nowe GUI: `taurusgui --new`
    3. Perspektywy i ich blokowanie.
    4. Nowe panele.
    5. Zewnętrzne aplikacje.
    6. Różnica między stałymi a tymczasowymi panelami.
    7. Zachowywanie stanu okna przy wyłączeniu.
        
Ćwiczenie: skonfigurować TaurusGUI z następującymi elementami
-------------------------------------------------------------
1. 1 Taurus Form (pozycje wszystkich motorów i ich sumę).
2. 1 TaurusDevicePanel (z Waszym TangoTestem z poprzednich zajęć).
3. 1 TaurusTrend (to samo, co na TaurusFormie).

Dodatek: TaurusDesigner
-----------------------
1. Pozycjonowanie paneli do wykorzystania w aplikacji pisanej samemu.
2. Wczytywanie plików UI - przykład.

```python
import sys
from PyQt4 import QtGui, uic

class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('mywindow.ui', self)
        self.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
```
    
JDraw
-----
1. Narzędzie do rysowania prostych paneli synoptycznych dla Tango.
2. Połączenie z Tango: przeciąganie z listy po lewej.
3. Zapisywanie z rozszerzeniem .jdw
4. Wykorzystanie w praktyce: zaznaczanie kształtów na schematach.
    
Zadanie domowe
--------------
1. Przygotować TaurusGUI z panelami synoptycznymi linii UARPES i PEEM/XAS z SOLARIS na
podstawie załączonych schematów.
2. Uzupełnienie paneli urządzeniami dowolne (przynajmniej 5 urządzeń na schemacie).
3. TaurusForm i TaurusTrend takie, jak na zajęciach (prezentujące pozycje wszystkich motorów
i ich sumę).
4. Dołączyć:
    1. Logo AGH.
    2. Uruchamianie zewnętrznych aplikacje: Jive i Astor.
5. Rozwiązania w formie pliku config.py (takiego, jak w przykładzie example01 dostępnego
w `/usr/local/lib/python2.7/dist-packages/taurus/qt/qtgui/taurusgui/conf/tgconf_example01` - opis tu:
http://www.taurus-scada.org/en/latest/users/ui/taurusgui.html#examples-of-taurusgui-based-applications )
