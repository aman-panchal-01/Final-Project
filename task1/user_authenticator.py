
import json        
class USER_MANAGER:
    def __init__(self):
        try:
            self.user_datafile ="user_data.json"
            self.users = self.load_user()
            
        except FileNotFoundError:
            self.users= {}
        
    def load_user(self):
        
        with open('user_data.json','r') as f:
             temp_data =json.load(f)
             return temp_data
    
    def save_user(self):
        
        with open(self.user_datafile,'w') as f:
            json.dump(self.users , f,indent=4)
    
    def signup(self,email,password,firstname,lastname,age):
        
        while True:
            try:
                
                 if email in self.users:
                    raise ValueError('the user is already exist please try another email')
                 self.users[email] = {
                    "password": password,
                    "first_name": firstname,
                    "last_name": lastname,
                    "age": age
                }
                
                 self.save_user()
                 return 'Sign up Succesnfully'    
            except ValueError as e:
                
                print(str(e))
                email = input("Enter a new email: ")
            
    
    def signin(self, email, password):
        while True:
            try:
                if email not in self.users:
                    raise ValueError('The email does not exist.')
                
                if self.users[email]['password'] != password:
                    raise ValueError('Incorrect password.')
                
                return  " Sign-In successful !!"
            except ValueError as e:
                print(str(e))
                email = input("Enter your email again: ")
                password = input("Enter your password again: ")
            
        
        
        
        
class MENU:
    def __init__(self):
        
        self.user_manager = USER_MANAGER()
        self.menubar()
        
    def menubar(self):
        
        while True:
            print('\nWelcome to login page of spotify!!')
            print('''
        Press 1 for SIGN-up
        Press 2 for SIGN-in
        Press 3 for EXIT   
                ''')
            choice =input('Enter your choice here :- ')
            if choice == '1':
                self.menu_signup()
            elif choice == '2':
                self.menu_signin()
            else:
                print("You have exited the program")
                break
            
    def menu_signup(self):
            print('Welcome to SIGN_UP page \n Please fill the detail below correclty')
            email = input('Enter your email: ')
            while True:
                password = input('Enter a password : ')
                if password.isalnum() and len(password) >= 8:
                    break
                else:
                    print("Passwrod must be of 8 letter and alphanumeric")
            fname = input('Enter your first name: ')
            lname = input('Enter your last name: ')
            age = int(input('enter your age: '))
            print(self.user_manager.signup(email,password,fname,lname,age))
            
    def menu_signin(self):
            print('Welcome to SIGN_IN page \n Please enter your email and password')
            email = input('Enter your E-mail : ')
            password = input('Enter your Password: ')
            print(self.user_manager.signin(email,password))
        
if __name__ == '__main__':        
    menu = MENU()





