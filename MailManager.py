from os import confstr_names
import colorama,time,string,ast
class Mail():
    _db = dict()
    _User = dict()
    _logged = False
    _usercount = 0
    def create_account(self,mail = str(),password = str()):
        self._User['username'] = mail.lstrip('@')
        self._User['mail'] = mail
        self._User['password'] = password
        if self._User['username'] == 'admin':
            self._User['account'] = 'admin'
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
    
    def update_db(self,user = dict()):
        for i in range(1,self._usercount):    
            self._db[user] = i
            
    def save_db(self,database):
        if ast.literal_eval(self._db['account']) == 'admin':
            with open("Database.txt","w") as out_file:
                for i in range(1,self._usercount):
                    print("User count: %d\nUser n°%d: %s\nMail: %s\nPassword: %s" % 
                        (self._usercount,self._usercount,ast.literal_eval(self._db['username']),
                        ast.literal_eval(self._db['mail']),ast.literal_eval(self._db['password'])) )
            print(colorama.Fore.CYAN + "Salvando il database su disco...")
            time.sleep(2)
            print(colorama.Fore.GREEN + "Database salvato con successo.")
        else:
            print(colorama.Fore.RED + "Il tuo account non è autorizzato ad eseguire questa operazione.")
            
    def login(self,mail,password):
        if ast.literal_eval(self._db['mail']) == mail and ast.literal_eval(self._db['password']) == password:
            self._logged = True
            for data in ast.literal_eval(self._db):
                self._User[data]
        '''
        DA COMPLETARE IL LOGIN, STO SBAGLIANDO QUALCOSA, LO SO MA NON RIESCO A CAPIRE COSA.
        '''