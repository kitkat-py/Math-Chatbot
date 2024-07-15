from json import load
from re import split # RegEx (Regular Expressions)
import risposte_random

def load_json(file): # prende le risposte dal file json
    with open(file) as risposta_bot:
        return load(risposta_bot)

def select_arg(chapter): # seleziona argomento
    global risposte_dati
    chapter_index = int(chapter) - 1 # poiché gli index partono da zero, bisogna sottrarre un'unità all'input
    chapters_list = ["01.json", "02.json"] # lista dei file di dati
    risposte_dati = load_json(chapters_list[chapter_index])

def ottieni_risposta(input_str):
    split_mssg = split(r'\s+|[,;?!.-]\s*', input_str.lower()) # split della stringa di messaggio (posta in minuscolo) in parole con cu in lavorare
    score_list = [] # per trovare la risposta più appropriata, tiene il messaggio

    for risposta in risposte_dati:
        risposta_score = 0
        score_richiesto = 0 # per determinare quante delle parole richieste sono nell'oggetto json
        parole_richieste = risposta["parole_richieste"] # permette di prendere le parole che sono necessarie dal file json

        if parole_richieste: # controlla se ci sono delle parole richieste
            for parola in split_mssg: # serve controllare ogni parola
                if parola in parole_richieste:
                    score_richiesto += 1 # per fare in modo che lo score delle parole richieste sia effettivamente uguale al numero delle parole richieste

        if score_richiesto == len(parole_richieste): # controlla che il numero di parole richieste sia uguale allo score
            for parola in split_mssg: # controlla ogni parola dell'input
                if parola in risposta["user_input"]: # se la parola è nella risposta, aggiunge allo score
                    risposta_score += 1
        elif score_richiesto >= 1: # per fare in modo che non debba essere un match perfetto
            for parola in split_mssg:
                if parola in risposta["user_input"]:
                    risposta_score += 1
                if parola in risposta["parole_richieste"]: # per dare più importanza alle parole richieste
                    risposta_score += 2

        score_list.append(risposta_score) # crea una lista in cui pone tutti gli score delle diverse risposte, in base a quanto sono accurate

    miglior_risposta = max(score_list) # trova la risposta migliore
    risposta_index = score_list.index(miglior_risposta)

    if input_str == "" or input_str == "." or input_str == ",": # se l'input è vuoto
        return("Scrivi qualcosa in modo che io possa aiutarti.")

    if miglior_risposta != 0: # restituisce una risposta
        return risposte_dati[risposta_index]["risposta_bot"]
    
    return risposte_random.unknown_string() # se non c'è una risposta adeguata, restituisce una risposta tra quelle di errore

while True: # loop per creare la chat
    print("Bot: Scegli il capitolo su cui vuoi approfondire tra i seguenti e digita il numero corrispondente per selezionarlo: 1. Insiemi, numeri e operazioni. 2. Monomi e polinomi.")
    user_input = input("Tu: ") # seleziona l'argomento
    if user_input.isnumeric() and 1 <= int(user_input) <= 2: # controlla che l'input sia un numero e che comprenda solo i numeri dei capitoli
        select_arg(user_input) # richiama la funzione che seleziona il file di dati richiesto
        print("Bot: Il tuo argomento è stato selezionato con successo! Ricorda che puoi cambiare argomento in ogni momento digitando 'Cambia argomento'.")
        while True:
            user_input = input("Tu: ") # input utente
            if user_input == "Cambia argomento" or user_input == "cambia argomento":
                break
            else:
                print("Bot: ", ottieni_risposta(user_input)) # risposta in base all'input dell'utente
    else:
        print("Bot: Per favore, inserisci un numero corrispondente all'argomento di cui vuoi trattare.")