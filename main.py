# IT-Grundlagen-Quiz
# Projekttag Git und GitHub
#
# Wichtige Regel:
# Jede Person bearbeitet nur ihren eigenen Arbeitsbereich.
# Aendern Sie nicht das Hauptprogramm und nicht die Arbeitsbereiche anderer Personen.
#
# Starten:
# python main.py
# oder:
# python3 main.py


def frage_stellen(frage):
    """Stellt eine einzelne Frage und gibt 1 Punkt bei richtiger Antwort zurueck."""
    frage_text = frage[0]
    antwort_a = frage[1]
    antwort_b = frage[2]
    antwort_c = frage[3]
    richtige_antwort = frage[4]

    print()
    print(frage_text)
    print("a) " + antwort_a)
    print("b) " + antwort_b)
    print("c) " + antwort_c)

    eingabe = input("Ihre Antwort: ").lower().strip()

    if eingabe == richtige_antwort:
        print("Richtig!")
        return 1
    else:
        print("Leider falsch. Richtig waere: " + richtige_antwort)
        return 0


def quiz_starten(thema, fragen):
    """Startet ein Quiz zu einem Thema."""
    print()
    print("=" * 40)
    print("Quiz: " + thema)
    print("=" * 40)

    punkte = 0

    for frage in fragen:
        punkte = punkte + frage_stellen(frage)

    print()
    print("Sie haben " + str(punkte) + " von " + str(len(fragen)) + " Punkten erreicht.")


# ============================================================
# ARBEITSBEREICH PERSON 1: NETZWERK
# Bearbeiten Sie nur diesen Bereich.
# Ergaenzen Sie mindestens drei eigene Fragen.
# ============================================================

def fragen_netzwerk():
    fragen = [
        [
            "Welche Aufgabe hat eine IP-Adresse?",
            "Sie identifiziert ein Geraet in einem Netzwerk.",
            "Sie verschluesselt automatisch alle Dateien.",
            "Sie ersetzt das Betriebssystem.",
            "a"
        ],
        # Fuegen Sie unter dieser Zeile Ihre eigenen Fragen ein.
        [
            "In welchem Layer des OSI-Modells arbeiten Switche in der Regel?",
            "Application Layer",
            "Data Link Layer",
            "Network Layer",
            "b"
        ],

        [
            "Welcher Befehl muss in der CLI eingegeben werden, um in den global configuration mode zu kommen?",
            "enable",
            "interface <...>",
            "configure terminal",
            "c"
        ],

        [
            "Welche Beschreibung trifft am ehesten auf TCP zu?",
            "Anwendungsprotokoll zum Versenden vom E-Mails.",
            "Transportprotokoll mit Verbindungsaufbau fuer zuverlaessige und geordnete Dateiuebertragung.",
            "Schnelles, verbindungsloses Transportprotokoll ohne Sicherung der Zustellung.",
            "b"
        ],

        [
            "Was ist ein Vorteil von VLSM beim Subnetting?",
            "Es muss nur eine Subnetzmaske ausgewaehlt werden.",
            "Alle IP-Adressen werden automatisch zugewiesen.",
            "IP-Adressen werden effektiv vergeben.",
            "c"
        ],
    ]

    return fragen


# ============================================================
# ARBEITSBEREICH PERSON 2: HARDWARE
# Bearbeiten Sie nur diesen Bereich.
# Ergaenzen Sie mindestens drei eigene Fragen.
# ============================================================

def fragen_hardware():
    fragen = [
        [
            "Wofuer ist der Arbeitsspeicher hauptsaechlich zustaendig?",
            "Fuer die dauerhafte Speicherung von Daten.",
            "Fuer das kurzfristige Speichern aktuell benoetigter Daten.",
            "Fuer die Verbindung zum Internet.",
            "b"
        ],
        # Fuegen Sie unter dieser Zeile Ihre eigenen Fragen ein.
        [
            "Wofür wird eine SSD hauptsächlich verwendet??",
            "Zum schnellen Speichern und Abrufen von Daten.",
            "Zum Kühlen des Prozessors.",
            "Zum Verbinden des Computers mit dem Internet.",
            "a"
        ],
        [
            "Was ist die Aufgabe eines Prozessors (CPU) in einem Computer?",
            "Er verarbeitet Befehle und führt Berechnungen aus.",
            "Er speichert dauerhaft alle Dateien des Computers.",
            "Er verbessert die Lautstärke der Lautsprecher.",
            "a"
        ],
        [
            "Wofuer steht DDR4?",
            "Double Data Rate 4.",
            "Digital Data Register 4.",
            "Dynamic Drive RAM 4.",
            "a"
        ],
    ]

    return fragen


# ============================================================
# ARBEITSBEREICH PERSON 3: BETRIEBSSYSTEME
# Bearbeiten Sie nur diesen Bereich.
# Ergaenzen Sie mindestens drei eigene Fragen.
# ============================================================

def fragen_betriebssysteme():
    fragen = [
        [
            "Welche Aufgabe hat ein Betriebssystem?",
            "Es verwaltet Hardware und stellt grundlegende Funktionen bereit.",
            "Es ersetzt alle Anwendungsprogramme.",
            "Es verhindert grundsaetzlich jede Netzwerkverbindung.",
            "a"
        ],
        [
            "Was versteht man unter 'Paging' (Seitenwechsel) im Betriebssystem?",
            "Eine Methode zur Speicherverwaltung, bei der Hauptspeicher in feste Bloecke aufgeteilt wird.",
            "Das automatische Sortieren von Dateien auf der Festplatte.",
            "Ein Protokoll zur schnelleren Ubertragung von Webseiten im Browser.",
            "a"
        ],
        [
            "Welche Rolle hat der Kernel (Kern) eines Betriebssystems?",
            "Er stellt die grafische Benutzeroberflache (GUI) bereit.",
            "Er ist die zentrale Komponente, die den direkten Zugriff auf die Hardware steuert.",
            "Er dient als Firewall fuer ein- und ausgehenden Datenverkehr.",
            "b"
        ],
        [
            "Was ist der Hauptunterschied zwischen einem Prozess und einem Thread?",
            "Ein Prozess hat einen eigenen Speicherbereich, waehrend Threads desselben Prozesses sich den Speicher teilen.",
            "Ein Thread ist sicherer als ein Prozess und kann nicht abstuerzen.",
            "Prozesse werden nur auf der CPU ausgefuehrt, Threads auf der Festplatte.",
            "a"
        ]
    ]

    return fragen


# ============================================================
# ARBEITSBEREICH PERSON 4: IT-SICHERHEIT
# Bearbeiten Sie nur diesen Bereich.
# Ergaenzen Sie mindestens drei eigene Fragen.
# ============================================================

def fragen_sicherheit():
    fragen = [
        [
            "Was ist ein eher sicheres Passwort?",
            "12345678",
            "Der eigene Vorname",
            "Eine lange Kombination aus verschiedenen Zeichen",
            "c"
        ],
        [
            "Was sollte man tun, wenn man eine verdächtige E-Mail mit einem Link erhält?",
            "Den Link sofort öffnen",
            "Die E-Mail löschen oder den Absender prüfen",
            "Das Passwort in der E-Mail eingeben",
            "b"
        ],
        [
            "Was bedeutet die Abkürzung VPN?",
            "Virtual Private Network",
            "Very Personal Number",
            "Virus Protection Network",
            "a"
        ],
        [
            "Warum sollte man Software regelmäßig aktualisieren?",
            "Damit der Computer langsamer wird",
            "Um Sicherheitslücken zu schließen",
            "Damit mehr Werbung erscheint",
            "b"
        ],
    ]

    return fragen


# ============================================================
# ARBEITSBEREICH PERSON 5: GIT UND GITHUB
# Bearbeiten Sie nur diesen Bereich.
# Ergaenzen Sie mindestens drei eigene Fragen.
# ============================================================

def fragen_git():
    fragen = [
        [
            "Wofuer wird ein Commit verwendet?",
            "Um einen gespeicherten Stand der Aenderungen festzuhalten.",
            "Um Python automatisch zu installieren.",
            "Um den Computer neu zu starten.",
            "a"
        ],
        # Fuegen Sie unter dieser Zeile Ihre eigenen Fragen ein.
        [
            "Welcher Befehl laedt ein Repository von einem Remote-Server herunter?",
            "git push",
            "git clone",
            "git commit",
            "b"
        ],
        [
            "Wofuer wird git push verwendet?",
            "Um Aenderungen in das lokale Repository zu laden.",
            "Um ein neues Repository zu erstellen.",
            "Um lokale Commits auf ein Remote-Repository hochzuladen.",
            "c"
        ],
        [
            "Was ist ein Repository (Repo)?",
            "Ein Speicherort fuer Projektdateien und Versionshistorie.",
            "Ein Texteditor fuer Programmierer.",
            "Eine Programmiersprache.",
            "a"
        ],
    ]

    return fragen


# ============================================================
# HAUPTPROGRAMM
# Diesen Bereich bitte nicht veraendern.
# ============================================================

def alle_fragen_sammeln():
    alle_fragen = []
    alle_fragen.extend(fragen_netzwerk())
    alle_fragen.extend(fragen_hardware())
    alle_fragen.extend(fragen_betriebssysteme())
    alle_fragen.extend(fragen_sicherheit())
    alle_fragen.extend(fragen_git())
    return alle_fragen


def main():
    while True:
        print()
        print("IT-Grundlagen-Quiz")
        print("==================")
        print("1 - Netzwerk")
        print("2 - Hardware")
        print("3 - Betriebssysteme")
        print("4 - IT-Sicherheit")
        print("5 - Git und GitHub")
        print("6 - Alle Themen")
        print("0 - Beenden")

        auswahl = input("Ihre Auswahl: ").strip()

        if auswahl == "1":
            quiz_starten("Netzwerk", fragen_netzwerk())
        elif auswahl == "2":
            quiz_starten("Hardware", fragen_hardware())
        elif auswahl == "3":
            quiz_starten("Betriebssysteme", fragen_betriebssysteme())
        elif auswahl == "4":
            quiz_starten("IT-Sicherheit", fragen_sicherheit())
        elif auswahl == "5":
            quiz_starten("Git und GitHub", fragen_git())
        elif auswahl == "6":
            quiz_starten("Alle Themen", alle_fragen_sammeln())
        elif auswahl == "0":
            print("Programm beendet.")
            break
        else:
            print("Ungueltige Eingabe. Bitte erneut versuchen.")


if __name__ == "__main__":
    main()