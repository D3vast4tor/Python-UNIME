import colorama,time
class Hanged_man():
    _found = False
    def controllo_lettera(self,lettera,parola):
        if lettera in parola:
            print(colorama.Fore.GREEN + "la lettera %c e presente nella parola" % lettera)
            stampa = self.stampa_parola(parola,lettera,stampa)
            self._found = True
        else:
            print(colorama.Fore.RED + "scarsoo, la lettera %c non e presente nella parola" % lettera)
            trovato = 0
        return trovato

    def stampa_parola(self,parola,lettera,stampa):
        for i in range(len(parola)):
            if parola[i] == lettera and i == 0:
                stampa += lettera
            elif i != 0 and parola[i] == lettera:
                index = i
            else:
                stampa += '_'
        print(stampa)
        return stampa
    
        
        
def main():
    tentativi = 0
    lettere_indovinate = 0
    parola = ''
    choise = ''
    while choise != 'n':
        parola = input("inserire la parola: ")
        while tentativi < 5 and lettere_indovinate < len(parola):
            lettera = input("inserire la lettera: ")
            if Hanged_man.controllo_lettera(Hanged_man,lettera,parola) == True:
                lettere_indovinate += 1
                Hanged_man._found = False
            else:
                tentativi += 1
        if lettere_indovinate == len(parola):
            print("Bravissimo, hai indovinato la parola che era: ",parola)
        else:
            print("Sei troppo scarso, te l'avevo detto. La parola era: ",parola)
        choise = input("Continuare?(s/n): ")
    print(colorama.Fore.GREEN + "Va bene, ritorna a giocare quando vuoi.")
        
if __name__ == '__main__':
    main()
