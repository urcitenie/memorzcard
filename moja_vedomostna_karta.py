from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
import random
from random import randint


questions = [
    {
        "question": "Kto bol prvy programator?", 
        "options": ["Ada Lovelace", "Charles Babbage", "Bill Gates", "Mark Zuckerberg"], 
        "correct_answer": "Ada Lovelace"
    },

    {"question": "Kto je autorkou knihy Pýcha a predsudok?", "options": ["Jane Austen", "Charlotte Brontë", "Emily Dickinson", "Louisa May Alcott"], "correct_answer": "Jane Austen"},
    {"question": "Ktorý z týchto mesiacov má len 30 dní?", "options": ["Február", "Marec", "Jún", "December"], "correct_answer": "Február"},
    {"question": "Koľko hviezd je na Európskej únii vlajke?", "options": ["12", "10", "15", "7"], "correct_answer": "12"},
    {"question": "Kto je autorom diela Don Quijote?", "options": ["Miguel de Cervantes", "Leo Tolstoy", "Franz Kafka", "Fyodor Dostoevsky"], "correct_answer": "Miguel de Cervantes"},
    {"question": "Ktorá planéta je najbližšie k Slnku?", "options": ["Merkúr", "Venuša", "Mars", "Jupiter"], "correct_answer": "Merkúr"},
    {"question": "Ktoré zvieratá spolu tvoria zimný spánok?", "options": ["Medvede", "Sova aživé", "Veverice", "Všetky vyššie uvedené"], "correct_answer": "Všetky vyššie uvedené"},
    {"question": "Ktorý druh kôry sa vytvára na plesňových záhradách?", "options": ["Pach pary", "Vosk", "Zelená", "Rúžové"], "correct_answer": "Zelená"},
    {"question": "Ktorý z nasledujúcich orgánov nie je súčasťou tráviaceho systému?", "options": ["Pľúca", "Žalúdok", "Pečeň", "Žalúdočná sliznica"], "correct_answer": "Pľúca"}
]

points = 0
zoznam_uz_opytanych = []
def generovanie_otazky():
    global text_otazka, options_list, spravna_odpoved, zoznam_uz_opytanych
    
    # Select a random question index that has not been asked before
    while True:
        cislo_otazky = randint(0, len(questions) - 1)
        if cislo_otazky not in zoznam_uz_opytanych:
            zoznam_uz_opytanych.append(cislo_otazky)
            break

    # Get the question and its details
    aktualna_otazka = questions[cislo_otazky]
    text_otazka = aktualna_otazka["question"]
    options_list = aktualna_otazka["options"]
    random.shuffle(options_list)
    spravna_odpoved = aktualna_otazka["correct_answer"]


def ask():
    global options_list
    otazka.setText(text_otazka) #vypises otazku
    rb1.setText(options_list[0]) 
    rb2.setText(options_list[1])
    rb3.setText(options_list[2])
    rb4.setText(options_list[3])

    text_spravnosti.setText(spravna_odpoved) #ulozi sa sem spravna odpoved, ktoru nasledne vypiseme

    #zobrazenie okna s otazkou a skrytie okna s vyhodnotenim
    moznosti_group.show()
    vyhodnotenie_group.hide()

def check_answer(): #kontrola, ci si zaklikol spravnu odpoved
    global points
    if rb1.isChecked():
        if rb1.text() == spravna_odpoved: #text radioveho tlacidla sa ma rovnat so spravnou odpovedou
            show_correct("Správne")
            points += 1
        else:
            show_correct("Nesprávne")
    elif rb2.isChecked():
        if rb2.text() == spravna_odpoved:
            show_correct("Správne")
            points += 1
        else:
            show_correct("Nesprávne")
    elif rb3.isChecked():
        if rb3.text() == spravna_odpoved:
            show_correct("Správne")
            points += 1
        else:
            show_correct("Nesprávne")
    elif rb4.isChecked():
        if rb4.text() == spravna_odpoved:
            show_correct("Správne")
            points += 1
        else:
            show_correct("Nesprávne")

def show_correct(text): # zobrazi sa po stlaceni tlacidla vyhodnotit
    text_spravnosti.setText(text)
    moznosti_group.hide()
    vyhodnotenie_group.show()
    vyhodnot_button.setText("Ďalšia otázka")

def show_result():
    moznosti_group.hide()
    vyhodnotenie_group.show()
    check_answer() # zavolam funkciu aby mi zobrazila, ci som odpovedal spravne
    vyhodnot_button.setText("Ďalšia otázka")

def show_question():
    # Resetuje radiove tlacidla aby nezostala zobrazena tvoja stara odpoved, dobre ked pridame viacero otazok
    otazka.setText(text_otazka)
    rb1.setText(options_list[0])
    rb2.setText(options_list[1])
    rb3.setText(options_list[2])
    rb4.setText(options_list[3])
    rb1.setChecked(False)
    rb2.setChecked(False)
    rb3.setChecked(False)
    rb4.setChecked(False)
    vyhodnot_button.setText("Vyhodnoť")
    moznosti_group.show()
    vyhodnotenie_group.hide()

def start_test(): #spusta sa po stlaceni tlacidla, v pripade, ze je text vyhodnot spusti vam okno s vysledkom, ak je iny text respektive "dalsia otazka", zobrazi vam opat otazku
    global points
    if vyhodnot_button.text() == "Vyhodnoť":
        show_result()
    else:
        generovanie_otazky()
        show_question()
        if len(zoznam_uz_opytanych) == len(questions):
            QMessageBox.information(my_win, 'Quiz hotovy', f'Zodpovedal si na vsetky otazky\nPocet tvojich bodov je {points}')
            
app = QApplication([]) # konstruktor na vytvorenie aplikacie

my_win = QWidget() # vytvoris si samotne okno
my_win.setWindowTitle('Vedomostne karty')
my_win.resize(600, 500)

generovanie_otazky()

#OKNO OTAZKA

otazka = QLabel(text_otazka)
vyhodnot_button = QPushButton("Vyhodnoť")
moznosti = QGroupBox("Možnosti odpovedí")

#priradis jednotlive texty odpovedi k radiovym tlacitkam
rb1 = QRadioButton(options_list[0])
rb2 = QRadioButton(options_list[1])
rb3 = QRadioButton(options_list[2])
rb4 = QRadioButton(options_list[3])

#vertikalna vodiaca ciara pre moznost a, b
rb12_lay = QVBoxLayout()
rb12_lay.addWidget(rb1)
rb12_lay.addWidget(rb2)

#vertikalna vodiaca ciara pre moznost c, d
rb34_lay = QVBoxLayout()
rb34_lay.addWidget(rb3)
rb34_lay.addWidget(rb4)

#horizontalna vodiaca ciara okolo ktorej zarovnas predchadzajuce dve vertikalne ciary
moznosti_h_ciara = QHBoxLayout()
moznosti_h_ciara.addLayout(rb12_lay)
moznosti_h_ciara.addLayout(rb34_lay)
moznosti_h_ciara.setSpacing(50) #aby na sebe neboli natlacene

moznosti.setLayout(moznosti_h_ciara) #nastavis rozlozenie group-boxu pomocou hlavnej horizontalnej vodiacej ciary

#vertikalna vodiaca ciara pomoocu ktorej zoradim cele okno
moznosti_v_hlavna = QVBoxLayout()
moznosti_v_hlavna.addWidget(otazka, alignment = Qt.AlignLeft)
moznosti_v_hlavna.addWidget(moznosti, alignment = Qt.AlignCenter)
moznosti_v_hlavna.addWidget(vyhodnot_button, alignment = Qt.AlignCenter)

moznosti_group = QGroupBox()
moznosti_group.setLayout(moznosti_v_hlavna)

#OKNO REAKCIA
text_najtazia = QLabel("Najtazsia otazka na svete!")
dalej_otazka_button = QPushButton("Dalsia otazka")
hodnotenie = QGroupBox("Vyhodnoť")
vyhodnotenie_group = QGroupBox() #nizsie pouzijeme, ako cele okno reakcie

spravna_odpoved_vypis = QLabel("Spravna odpoved: ")
text_spravnosti = QLabel(spravna_odpoved)

spravnost_v = QVBoxLayout()
spravnost_v.addWidget(spravna_odpoved_vypis, alignment = Qt.AlignLeft)
spravnost_v.addWidget(text_spravnosti, alignment = Qt.AlignCenter)

hodnotenie.setLayout(spravnost_v)

vysledky_v_ciara = QVBoxLayout()
vysledky_v_ciara.addWidget(text_najtazia, alignment = Qt.AlignCenter)
vysledky_v_ciara.addWidget(hodnotenie, alignment=Qt.AlignCenter)
vysledky_v_ciara.addWidget(dalej_otazka_button, alignment=Qt.AlignCenter)

vyhodnotenie_group.setLayout(vysledky_v_ciara)
############

stacked_layout = QStackedLayout()
stacked_layout.addWidget(moznosti_group)
stacked_layout.addWidget(vyhodnotenie_group)

main_layout = QVBoxLayout()
main_layout.addLayout(stacked_layout)

my_win.setLayout(main_layout)

moznosti_group.hide()
vyhodnotenie_group.show()

vyhodnot_button.clicked.connect(start_test)
dalej_otazka_button.clicked.connect(start_test)

generovanie_otazky()
ask()

my_win.show()
app.exec_()