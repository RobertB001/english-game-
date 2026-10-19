import random
import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
from googletrans import Translator

words_by_level = {
    "łatwy": ["kot", "pies", "jabłko", "mleko", "słońce"],
    "średni": ["banan", "szkoła", "przyjaciel", "okno", "żółty"],
    "trudny": ["technologia", "uniwersytet", "informacja", "wymowa", "wyobraźnia"]
}

punkty_za_poziom = {"łatwy": 1, "średni": 2, "trudny": 3}

tlumacz = Translator()


def nagraj(czas=3, plik="nagranie.wav"):
    fs = 44100
    print("Mów teraz...")
    audio = sd.rec(int(czas * fs), samplerate=fs, channels=1, dtype="int16")
    sd.wait()
    write(plik, fs, audio)
    print("Nagrywanie zakończone.")
    return plik


def rozpoznaj(plik):
    r = sr.Recognizer()
    with sr.AudioFile(plik) as zrodlo:
        dzwiek = r.record(zrodlo)
    try:
        tekst = r.recognize_google(dzwiek, language="en-US")
        return tekst.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        print("Brak połączenia z internetem.")
        return ""


def wybierz_poziom():
    poziomy = {"1": "łatwy", "2": "średni", "3": "trudny"}
    print("Wybierz poziom trudności:")
    print("1 - łatwy  (1 pkt za słowo)")
    print("2 - średni (2 pkt za słowo)")
    print("3 - trudny (3 pkt za słowo)")
    while True:
        wybor = input("Twój wybór (1/2/3): ").strip()
        if wybor in poziomy:
            return poziomy[wybor]
        print("Nie ma takiego poziomu, wpisz 1, 2 albo 3.")


def przetlumacz(slowo):
    try:
        wynik = tlumacz.translate(slowo, src="pl", dest="en")
        return wynik.text.lower()
    except Exception:
        print("Tłumacz nie działa, sprawdź internet.")
        return ""


def graj():
    poziom = wybierz_poziom()
    slowa = words_by_level[poziom].copy()
    punkty = 0
    zycia = 3
    dobre = 0

    while zycia > 0 and len(slowa) > 0:
        slowo = random.choice(slowa)
        slowa.remove(slowo)
        tlumaczenie = przetlumacz(slowo)
        if tlumaczenie == "":
            continue

        print()
        print("-" * 35)
        print("Punkty:", punkty, "| Życia:", "<3 " * zycia)
        print("Słowo po polsku:", slowo)
        input("Naciśnij Enter i powiedz to po angielsku...")

        powiedziane = rozpoznaj(nagraj())

        if powiedziane == "":
            print("Nic nie usłyszałem.")
        else:
            print("Powiedziałeś:", powiedziane)

        if powiedziane == tlumaczenie or tlumaczenie in powiedziane.split():
            zdobyte = punkty_za_poziom[poziom]
            punkty += zdobyte
            dobre += 1
            print("Dobrze! +" + str(zdobyte) + " pkt")
        else:
            zycia -= 1
            print("Źle! Poprawnie:", tlumaczenie)
            print("Tracisz życie, zostało:", zycia)

    print()
    print("=" * 35)
    if zycia == 0:
        print("KONIEC GRY - straciłeś wszystkie życia.")
    else:
        print("WYGRAŁEŚ - przeszedłeś wszystkie słowa!")
    print("Dobre odpowiedzi:", dobre)
    print("Wynik końcowy:", punkty, "pkt")
    print("=" * 35)


graj()
