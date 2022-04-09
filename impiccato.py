import colorama,time,pprint
'''
class Hanged_man():
    to_guess_word = ''
    _guessed_word = dict()
    _parola_trovata = ''
    _tentativi = 0
    lettere_indovinate = 0
    def __init__(self,parola):
        for i in range(len(parola)):
            Hanged_man._guessed_word[i] = '_'     
    def controllo_lettera(self,lettera,parola):
        for i in range(len(self.to_guess_word)):
            if lettera in parola:
                self._guessed_word[i] = lettera
                return True 
    
    def update_guess(self):
        while self._tentativi < 4 and self.lettere_indovinate < len(self.to_guess_word):
            lettera = input("inserire la lettera: ")
            self._parola_trovata = ''
            if Hanged_man.controllo_lettera(Hanged_man,lettera,self.to_guess_word) == True:
                for i in range(len(self.to_guess_word)):
                    self._parola_trovata += self._guessed_word[i]
                print( "\nLa parola da indovinare è: %s" % (self._guessed_word[i]) )
                self.lettere_indovinate += 1
                Hanged_man._found = False
            else:
                self._tentativi += 1
        
    
def main():
    choise = ''
    while choise != 'n':
        Hanged_man.to_guess_word = input("inserire la parola: ")
        Hanged_man.__init__(Hanged_man,Hanged_man.to_guess_word)
        Hanged_man.update_guess(Hanged_man)
        if Hanged_man.lettere_indovinate == len(Hanged_man.to_guess_word):
            print("Bravissimo, hai indovinato la parola che era: ",Hanged_man.to_guess_word)
        else:
            print("Sei troppo scarso, te l'avevo detto. La parola era: ",Hanged_man.to_guess_word)
        choise = input("Continuare?(s/n): ")
    print(colorama.Fore.GREEN + "Va bene, ritorna a giocare quando vuoi.")
        
if __name__ == '__main__':
    main()
'''  



    
def controllo_lettera(lettera,parola,stampa):
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
    parola_incompleta = ''
    for i in range(len(parola)):
        if parola[i] == lettera:
            stampa[i] = lettera
            '''
            Che succede se mettiamo caso la parola da indovinare è "prova" e metto prima la o invece della p
            che si trova a indice 2?
            la variabile stampa ancora è una stringa vuota e anche mettendo caso che non fosse vuota le stringhe non 
            supportano l'assegnazione per indicizzazione
            '''
    parola_incompleta = str(stampa)
    print(parola_incompleta)
    return stampa
    
        
def main():
    parola = input("inserire la parola: ")
    tentativi = 0
    lettere_indovinate = 0
    stampa = ['_']*len(parola)
    while tentativi < 5 and lettere_indovinate < len(parola):
        lettera = input("inserire la lettera: ")
        trovato = controllo_lettera(lettera,parola,stampa)
        if trovato:
            lettere_indovinate += 1
            #stampa_parola(parola,lettera,stampa)
        else:
            tentativi += 1
    if lettere_indovinate == len(parola):
        print("Bravissimo, hai indovinato la parola che era ",parola)
    else:
        print("Sei troppo scarso, te l'avevo detto. La parola era ",parola)

if __name__ == '__main__':
    main()
