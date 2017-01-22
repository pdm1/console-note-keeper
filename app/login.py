class Login:
    """This is for basic concept... for the love of god,
    
    do not use this in a real application
    """
    def __init__(self):
        self.accounts = {None: "blank"}
     
    def create_account(self, user_name, user_pw, user_pw_repeat):
        if self._password_check(user_pw, user_pw_repeat): #Check if PW is valid
            self._load_account()
            if user_name in self.accounts:
                print("User already exists")
            elif user_name not in self.accounts:
                self.accounts[user_name] = user_pw
                self._save_account(user_name, user_pw)
                return True
        return False
    
    def sign_in(self, user_name, user_pw):
        self._load_account()
        for key in self.accounts:
            try:
                if self.accounts[user_name] == user_pw:
                    return True
            except KeyError:
                return False
        return False
        
    def _save_account(self, user_name, user_pw):
        txt_file = open("credentials.txt", "a")
        txt_file.write("%s,%s\n" % (user_name, user_pw))
        txt_file.close()
        
    def _load_account(self):
        with open('credentials.txt') as f:
            content = f.readlines()
        for lines in content:
            lines = lines.strip("\n")
            lines = lines.split(",") 
            self.accounts[lines[0]] = lines[1]
        return 
    
    def _password_check(self, user_pw, user_pw_repeat):
        if user_pw != user_pw_repeat:
            print("Passwords do not match, retry")
            return False
        if len(user_pw) < 7:
            print("Password is too short. Required, at least 7 characters with one being a symbol")
            return False
        symbols = ['!','@','#','$','%','^','&','*','(',')']
        if not any(x in user_pw for x in symbols):
            print("Password must contain at least one symbol (Number shift chars)")
            return False
        if user_pw == user_pw_repeat:
            return True
        
            

        