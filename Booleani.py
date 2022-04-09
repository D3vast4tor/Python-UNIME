#Ti spiego perchè in python è meglio usare i valori booleani per un controllo vero o falso
# piuttosto che valori come 0 o 1 come nel c
def main():
    found = False
    trovato = 0
    print(type(found))
    print(type(trovato))
    trovato = 1
    if trovato:
        print("L'ho trovato.")
    elif not trovato:
        print("Non l'ho trovato.")
    else:
        print("Non si può usare questa dicitura per flessibilità di scrittura.")
    for i in range(1,4):
        if (i % 2) == 0:
            found = True
        else:
            found = False
        if found:
            print("L'ho trovato.")
        elif not found:
            print("Non l'ho trovato.")
        else:
            print("Tanto per farti vedere che qui manco ci arriva.")
main()