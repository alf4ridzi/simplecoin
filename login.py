# SimpleCoin Project Kelompok 5
# Code by Muhammad Alfaridzi
# login.py for login

import sys
from lib import request_api
from lib.parser_config import get_node
from typing import Literal
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox

# edit with your own server.
NODE = get_node()

class Login(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui", self)
        self.setFixedSize(690, 520)
        self.registerButton.clicked.connect(self.signup)
        self.loginButton.clicked.connect(self.login)
        self.register_window = None
        self.attempts = 0
        self.username = None
        self.password = None

    def show_dialog(self, type: Literal['cricital', 'information', 'warning'] = "cricital", title: str = "Default title", message: str = "Unknown", button: QMessageBox.StandardButton = QMessageBox.StandardButton.Ok):
        if type == "cricital":
            show = QMessageBox.critical(
                self,
                title,
                message,
                button
            )

            return show
        
        elif type == "warning":
            show = QMessageBox.warning(
                self,
                title,
                message,
                button
            )

            return show
        
        elif type == "information":
            show = QMessageBox.information(
                self,
                title,
                message,
                button
            )

            return show

    def login(self):
        
        self.username = self.usernameInput.toPlainText()
        self.password = self.passwordInput.text()
        if not self.username or not self.password:
            self.show_dialog(type="cricital", title="Not Valid", message="Username Or Password Cannot Empty", button=QMessageBox.StandardButton.Ok)
        else:
            max_att = 3
            if self.attempts < max_att:
                if self.send_login_request(self.username, self.password):
                    self.switch_to_dashboard(self.username)
                self.attempts += 1
            else:
                show = self.show_dialog(type='cricital', title="Cricital", message="Max login attempts reached", button=QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Close)

                if show == QMessageBox.StandardButton.Close:
                    self.close()
        


    def send_login_request(self, username: str, password: str):
        send_login = request_api.check_valid_account(username, password)
        if type(send_login) != bool:
            show = self.show_dialog(type='cricital', title="Failed Login", message=send_login)
            return False
        if send_login:
            return True
        show = self.show_dialog(type='cricital', title="Cricital", message="Username/Password incorrect", button=QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Close)
        return False

    def check_server(self):
        # try:
        #     resp = http.request("GET", NODE).status
        #     if resp == 200:
        #         return True
        #     show = self.show_dialog(type='cricital', title="Server ERROR!!", message="Cannot connect to server")
        # except Exception as e:
        #     print(e)
        #     show = self.show_dialog(type='cricital', title="Server ERROR!!", message="Cannot connect to server")
        #     return False
        if request_api.check_server():
            return True
        else:
            show = self.show_dialog(type='cricital', title="Server ERROR!!", message="Cannot connect to server")

    def signup(self):
        self.close()
        if not self.register_window or not self.register_window.isVisible():
            self.register_window = Register()
            self.register_window.show()
        else:
            self.register_window.activateWindow()
    
    # berganti ke dashboard
    def switch_to_dashboard(self, username):
        
        try:
            from dashboard import MainWindow
            self.dashboard = MainWindow(username=username)
            self.dashboard.show()

            self.hide()
        except Exception as e: 
            print(e)

class Register(Login):

    def __init__(self):
        super().__init__()
        
        uic.loadUi("register.ui", self)
        self.setFixedSize(690, 520)
        self.login_window = None
        self.backtologinbutton.clicked.connect(self.loginpage)
        self.registerButton.clicked.connect(self.registerProccess)
        
    def registerProccess(self):
        username = self.usernameInput.toPlainText()
        password = self.passwordInput1.text()
        password_verif = self.passwordInput2.text()

        if username and password and password_verif:
            if self.check_username(username):
                if password == password_verif:
                    if len(password) < 8:
                        show = self.show_dialog(type='cricital', title='Input Error', message='Minimum password is 8 character')
                    else:
                        if self.create_user(username, password):
                            show = self.show_dialog(type='information', title='Success', message='Success create account. back to login page ?', button=QMessageBox.StandardButton.Ok|QMessageBox.StandardButton.Close)
                            if show == QMessageBox.StandardButton.Ok:
                                self.loginpage()
                        else:
                            show = self.show_dialog(type='cricital', title='Error', message='Failed create account')
                else:
                    show = self.show_dialog(type='cricital', title='Error', message='Password dont match')
            else:
                show = self.show_dialog(type='cricital', title='Error', message='Username already exist')
                self.usernameInput.clear()
        else:
            show = self.show_dialog(type='cricital', title='Error', message='Username or password cannot empty')
    def check_username(self, username):
        check_username = request_api.check_username(username)
        if type(check_username) != bool:
            self.show_dialog(type='cricital', title='Error', message=check_username)
            return False
        if check_username:
            return True
        return False

    def create_user(self, username, password):
        create_user = request_api.create_user(username, password)
        if type(create_user) != bool:
            self.show_dialog(type='cricital', title='Error', message=create_user)
            return False
        if create_user:
            return True
        return False
        
        
    

    def loginpage(self):
        self.close()
        if not self.login_window or not self.login_window.isVisible():
            self.login_window = Login()
            self.login_window.show()
        else:
            self.login_window.activateWindow()
        

    
if __name__ == '__main__':
    # check server first..
    app = QtWidgets.QApplication(sys.argv)
    window = Login()
    if not window.check_server():
        sys.exit(0)
    window.show()
    app.exec()
