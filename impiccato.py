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
            if parola[i] == lettera:
                stampa = stampa + lettera
            else:
                stampa = stampa + '_'
        print(stampa)
        return stampa
    
        
        
def main():
    parola = input("inserire la parola: ")
    tentativi = 0
    lettere_indovinate = 0
    choise = ''
    while choise != 'n':
        while tentativi < 5 and lettere_indovinate < len(parola):
            lettera = input("inserire la lettera: ")
            Hanged_man._found = Hanged_man.controllo_lettera(lettera,parola)
            if Hanged_man._found == True:
                lettere_indovinate += 1
            else:
                tentativi += 1
        if lettere_indovinate == len(parola):
            print("Bravissimo, hai indovinato la parola che era ",parola)
        else:
            print("Sei troppo scarso, te l'avevo detto. La parola era ",parola)
        choise = input("Continuare?(s/n): ")
        if choise == 'n':
            print(colorama.Fore.GREEN + "Va bene, ritorna a giocare quando vuoi.")
            quit(0)
        
if __name__ == '__main__':
    main()