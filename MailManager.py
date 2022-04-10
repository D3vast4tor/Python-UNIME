import colorama,time,string,ast
class Mail():
    _db = dict()
    _User = dict()
    _logged = False
    _usercount = 0
    def create_account(self,mail,password):
        username = mail.lstrip(mail,'@')
        '''
        NON FUNZIONA LSTRIP(), LA FUNZIONE NON HA QUESTO METODO
        DA TROVARE UN MODO PER DIVIDERE LA MAIL, LO CERCO QUANDO HO TESTA
        '''
        self._User['username'] = username
        self._User['mail'] = mail
        self._User['password'] = password
        if self._User['username'] == 'admin':
            self._User['account'] = 'admin'
            self._usercount += 1
        else:
            self._User['account'] = 'user'
        self._usercount += 1
    
    def get_mail(self):
        mail = input("Inserire l'username: ")
        if len(mail) != 0:
            return mail
        else:
            print(colorama.Fore.RED + "Nessun username inserito. Riprovare.\n")
            self.get_mail()
    
    def get_password(self):
        password = input("Inserisci la password: ")
        conf_password = input("Conferma la password: ")
        if password == conf_password:
            print(colorama.Fore.GREEN + "Le password coincidono.")
            return password
        else:
            print(colorama.Fore.RED + "Le password non coincidono. Riprova.")
            self.get_password()
    
    def update_db(self,user):
        for i in range(1,self._usercount):    
            if i == self._usercount:
                self._db[i] = user
        self._User = dict()
    def save_db(self):
        if self._User['account'] == 'admin':
            with open("Database.txt","w") as out_file:
                for i in range(1,self._usercount):
                    user = ast.literal_eval(self._db[i])
                    print( "User n°%d: %s\nMail: %s\nPassword: %s" %
                          (i,user['username'],user['mail'],user['password']),
                        file = out_file
                        )
            print(colorama.Fore.CYAN + "Salvando il database su disco...")
            time.sleep(2)
            print(colorama.Fore.GREEN + "Database salvato con successo.")
        else:
            print(colorama.Fore.RED + "Il tuo account non è autorizzato ad eseguire questa operazione.")
            
    def login(self,mail,password):
        for i in range(1,self._usercount):
            self._User = ast.literal_eval(self._db[1])
            if self._User['mail'] == mail and self._User['password'] == password:
                self._logged = True 
                break
        if self._logged== False:
            print(colorama.Fore.RED + "Nessun utente trovato con le credenziali inserite")        
        if self._logged == True:
            print(colorama.Fore.GREEN + "Benvenuto %s. " % (self._User['username']))
               
    def logout(self):
        self._User = dict()
        self._logged = False
        
        
def main():
    choise = ''
    while choise != 'q':        
        print(colorama.Fore.GREEN + "\nc)Crea account\nl)Login\ns)Salva database\t|SOLO PER ADMINISTRATORI|\nL)Logout")
        choise = input("Inserire la scelta:")
        if choise == 'c':
            Mail.create_account(Mail,Mail.get_mail,Mail.get_password)
            Mail.update_db(Mail,Mail._User)
        elif choise == 'l':
            mail = input("Inserire il proprio indirizzo di posta elettronica: ")
            password = input("Inserire la password:  ")
            Mail.login(Mail,mail,password)
        elif choise == 's':
            Mail.save_db(Mail)
        elif choise == 'L':
            Mail.logout(Mail)

if __name__ == '__main__':
    main()