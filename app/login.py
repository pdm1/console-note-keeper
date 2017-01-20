class Login:
    """This is for basic concept... for the love of god,
    
    do not use this in a real application
    """
    def __init__(self):
        self.accounts = {}
        
    def create_account(self, user_name, user_pw, user_pw_repeat):
        if self._password_check(user_pw, user_pw_repeat): #Check if PW is valid
            if user_name not in self.accounts:
                self.accounts[user_name] = user_pw
                return True
        return False
                
    def sign_in(self, user_name, user_pw):
        for key in self.accounts:
            if self.accounts[user_name] == user_pw:
                return True
        print("No match")
        return False
    
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
        
            
'''
me = Login()

me.create_account("Bobby", "kitty12^", "kitty12^")
me.sign_in("Bobby", "kitty12^")
me.sign_in("Bobby", "adsf^")
print me.accounts
'''

        