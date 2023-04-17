import PySimpleGUI as sg
from email_send import EmailSend
from mysql_database import MysqlDatabase

class LaundryGui:
    def __init__(self) -> None:
        self.layot_main_window = [ [sg.Text("enter your email")],
                                   [sg.Input(key= '-email-')],
                                   [sg.Text("enter your password")],
                                   [sg.Input(key= '-password-')],
                                   [sg.Button("sign in"), sg.Button("sign up"), sg.Button("forgot password")] ]
        
        self.window = sg.Window("welcome", self.layot_main_window)

    def run(self):
        while(True):
            self.event, self.value = self.window.read()
            if self.event == sg.WIN_CLOSED:
                break
            if self.event == "sign in":
                self.sign_in
            elif self.event == "sign up":
                pass
            elif self.event == "forgot password":
                self.forget_password(self.value['-email-'])
        self.window.close()

    def sign_in(self, email, password):
        pass

    def sign_up(self):
        pass

    def forget_password(self, email):
        print(email)
        if email:
            if MysqlDatabase.check_client_existence(email):
                EmailSend.password_recovery(email)
                sg.popup('The password has been sent to your email address')
            else:
                sg.popup("The email address is not yet registered. Please select the 'sign up' option to register")
        else:
            sg.popup('Please enter an email address')
        





guy = LaundryGui()
guy.run()
