import random

def unknown_string(): # restituisce una di queste risposte in caso il bot non abbia una risposta alla domanda presentata
    random_list = [
        "Sembra che tu abbia scritto qualcosa che non comprendo.",
        "Mi dispiace, non ho capito cosa mi hai chiesto.",
        "Potresti gentilmente ripetere la tua richiesta?",
        "Qualcosa è andato storto, prova a chiedere qualcos altro.",
        "Non so ancora rispondere a questa domanda, prova con qualcos altro.",
        "Potresti provare a riscrivere la tua domanda?",
        "Per favore, riprova a esporre la tua richiesta."
    ]
    risposta_random = random.randrange(len(random_list))
    return random_list[risposta_random]