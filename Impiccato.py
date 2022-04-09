def controllo_lettera(lettera,parola):
    trovato = 1
    if lettera in parola:
        print("la lettera %c e presente nella parola" % lettera)
        stampa = stampa_parola(parola,lettera,stampa)
        trovato = 1
    else:
        print("scarsoo, la lettera %c non e presente nella parola" % lettera)
        trovato = 0
    return trovato

def stampa_parola(parola,lettera,stampa):
    for i in range(len(parola)):
        if parola[i] == lettera:
            stampa = stampa + lettera
        else:
            stampa = stampa + '_'
    print(stampa)
    return stampa
    
        
        

parola = input("inserire la parola: ")
tentativi = 0
lettere_indovinate = 0
while tentativi < 5 and lettere_indovinate < len(parola):
    lettera = input("inserire la lettera: ")
    trovato = controllo_lettera(lettera,parola)
    if trovato:
        lettere_indovinate += 1
    else:
        tentativi += 1
if lettere_indovinate == len(parola):
    print("Bravissimo, hai indovinato la parola che era ",parola)
else:
    print("Sei troppo scarso, te l'avevo detto. La parola era ",parola)

