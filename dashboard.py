# SimpleCoin Project Kelompok 5
# Code by Muhammad Alfaridzi
# Dashboard simplecoin.
# I love you Nakano Nino.

import sys
import urllib3
import lib.create_qrcode as qrcode
import os
from lib import request_api, parser_config
from typing import Literal
from PyQt6.QtWidgets import (QMainWindow, QApplication, QListWidgetItem, QMessageBox, QInputDialog, QLineEdit, QTableWidgetItem, QTableWidget, QComboBox, QVBoxLayout,
                             QFrame, QLabel, QWidget, QHBoxLayout)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QGuiApplication, QColor
from PyQt6 import QtGui
from dashboard_ui import Ui_MainWindow
from datetime import datetime

timeout = urllib3.Timeout(total=3)
http = urllib3.PoolManager(timeout=timeout)

# get node
NODE = parser_config.get_node()

# Define a custom MainWindow class
class MainWindow(QMainWindow):
    def __init__(self, username: str = None):
        super().__init__()
        
        self.username = username        
        # Initialize the UI from the generated 'main_ui' class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # set fix width & height
        self.setFixedSize(980, 700)
        self.ui.welcomeusername.setText(f"Welcome, {self.username}")
        # Set window properties
        self.setWindowIcon(QIcon("./img/simplecoin.png"))
        self.setWindowTitle("SimpleCoin: Dashboard")

        # Initialize UI elements
        self.title_label = self.ui.title_label
        self.title_label.setText("SimpleCoin")

        self.title_icon = self.ui.title_icon
        self.title_icon.setText("")
        self.title_icon.setPixmap(QPixmap("./img/simplecoin_ico.png"))
        self.title_icon.setScaledContents(True)

        self.side_menu = self.ui.listWidget
        self.side_menu.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.side_menu_icon_only = self.ui.listWidget_icon_only
        self.side_menu_icon_only.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.side_menu_icon_only.hide()

        self.menu_btn = self.ui.menu_btn
        self.menu_btn.setText("")
        self.menu_btn.setIcon(QIcon("./icon/close.svg"))
        self.menu_btn.setIconSize(QSize(30, 30))
        self.menu_btn.setCheckable(True)
        self.menu_btn.setChecked(False)

        
        self.main_content = self.ui.stackedWidget

        # set stylesheet dari style.qss
        self.setStyleSheet(open('style.qss', 'r').read())
        frame_layout = QVBoxLayout(self.ui.frame_wallet)
        # indonesia wallet
        self.wallet_for_deposit = ["Dana", "Gopay", "OVO", "Bank BCA", "Bank Mandiri", "Jenius"]
        # dropdown menu for wallet on deposit
        self.combobox = QComboBox(self)
        self.combobox.setFixedSize(420, 50)
        for wallet in self.wallet_for_deposit:
            self.combobox.addItem(wallet)
        
        frame_layout.addWidget(self.combobox)
        self._set_information()
        # get informasi account
        # self._get_account_information()
        # # get wallet number
        
        # # set balance
        # self._set_balance_text(
        
        
        # change widget index
        self.ui.sendmoney_button.clicked.connect(lambda: self.switch_to_index(1))
        self.ui.buy_sell_button.clicked.connect(lambda: self.switch_to_index(2))
        self.ui.deposit_button.clicked.connect(lambda:  self.switch_to_index(6))
        # refresh button
        self.ui.refresh_button.clicked.connect(self._set_information)
        #self.ui.amount_input.setInputMask(str(self.balance_account))
        # membuat qrcode
        qrcode.create_qrcode(self.wallet_number)
        self.ui.sendmoney_button_2.clicked.connect(self._filter_send_money)
        self.ui.spend_input.textChanged.connect(lambda: self.change_text_buy('buy'))
        self.ui.spend_sell_input.textChanged.connect(lambda: self.change_text_buy('sell'))
        # buy button
        self.ui.buy_button.clicked.connect(lambda: self._buy_sell_simplecoin(method='BUY'))
        self.ui.sell_simplecoin_button.clicked.connect(lambda: self._buy_sell_simplecoin(method='SELL'))
        self.ui.search_button.clicked.connect(lambda: self._update_public_records(wallet_address=self.ui.wallet_address_history.text()))
        self.ui.deposit_button_.clicked.connect(self._deposit)
        # menampilkan qr code
        if os.path.exists('user_img/qrcode_wallet.png'):
            self.ui.qrcode_label.clear()
            label_width = 281
            label_height = 241
            image_path = "user_img/qrcode_wallet.png"

            image = QtGui.QImage(image_path)
            image_width = image.width()
            image_height = image.height()

            scale_factor = min(label_width / image_width, label_height / image_height)
            
            scaled_width = int(image_width * scale_factor)
            scaled_height = int(image_height * scale_factor)

            
            self.ui.qrcode_label.setStyleSheet(f'''
                image: url("{image_path}");
                width: {scaled_width}px;
                height: {scaled_height}px;
            ''')
        self.ui.copy_button.clicked.connect(self.address_copy_to_clipboard)
            # self.ui.qrcode_label.setStyleSheet('''
            #     background-image: url("user_img/qrcode_wallet.png");
            #     background-repeat: no-repeat;
            #     background-position: center;
            # ''')
            # self.ui.qrcode_label.setFixedSize(281, 161)
            # self.ui.qrcode_label.setScaledContents(True)
            # aspectRatio = 350 / 350
            # fixedWidth = 240  # Set your desired width
            # fixedHeight = int(fixedWidth / aspectRatio)  # Convert the height to an integer
            # self.ui.qrcode_label.setFixedSize(fixedWidth, fixedHeight)
            # self.ui.qrcode_label.setScaledContents(True)

        # Define a list of menu items with names and icons
        self.menu_list = [
            {
                "name": "Dashboard",
                "icon": "./icon/dashboard.svg",
                "widget": self.ui.dashboard
            },
            {
                "name": "Send/Recieve Coins",
                "icon": "./icon/trade.svg",
                "widget": self.ui.send_rec
            },
            {
                "name": "Buy/Sell Coins",
                "icon": "./icon/products.svg",
                "widget": self.ui.buy_sell
            },
            {
                "name": "Public Records",
                "icon": "./icon/public_records.svg",
                "widget": self.ui.public_records
            },
            {
                "name": "Transaction History",
                "icon": "./icon/transaction_history.svg",
                "widget": self.ui.transaction_history
            },
            {
                "name": "About",
                "icon": "./icon/settings.svg",
                "widget": self.ui.about
            },
            {
                "name": "Deposit",
                "icon": "./icon/deposit.svg",
                "widget": self.ui.deposit
            },
        ]

        # Initialize the UI elements and slots
        self.init_list_widget()
        self.init_single_slot()

    def _get_nonce(self, username, password) -> str:
        try:
            nonce = request_api.get_nonce(username, password)
            return nonce['message']
        except:
            return False
        
    # deposit
    def _deposit(self):
        amount_text = self.ui.amount_deposit.text()
        wallet_selected = str(self.combobox.currentText())
        if not amount_text:
            self.show_dialog(type='critical', title="Amount error.", message="Please enter amount correctly.")
            return
        password = self.show_dialog('input')
        if password:
            amount = float(amount_text)
            nonce = self._get_nonce(self.username, password)
            if not nonce:
                self.show_dialog(type='critical', title="Failed input password", message="Failed to get nonce")
                return
            deposit = request_api.deposit(self.username, password, amount, wallet_selected, nonce)
            if deposit:
                self.show_dialog('information', title="Deposit success", message=f"Deposit {amount}$ Success to your account.")
                self._set_information()
            else:
                self.show_dialog('critical', title="Deposit failed", message=f"Deposit Failed! Please try again.")
    
    # update public records
    def _update_public_records(self, wallet_address: str = None):
        table = self.ui.table_publicrecords
        self.ui.public_records_label.setText("Public Records of SimpleCoin")
        self.ui.public_records_balance.clear()
        self.ui.wallet_address_history.clear()
        table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        public_records_req = request_api.get_public_records(wallet_address)
        if public_records_req['success']:
            if wallet_address:
                public_records = public_records_req['information']['public_records']
                self.ui.public_records_label.setText(f"Public Records \t: {wallet_address}")
                self.ui.public_records_balance.setText(f"Balance\t\t: {public_records_req['information']['balance']}\nFiat Balance\t: {public_records_req['information']['fiat_balance']}")
            else:
                public_records = public_records_req['public_records']
            table.setRowCount(len(public_records))
            for number, data in enumerate(public_records):
                table.setItem(number, 0, QTableWidgetItem(data['date']))
                table.setItem(number, 1, QTableWidgetItem(data['transaction_id']))
                table.setItem(number, 2, QTableWidgetItem(str(data['amount'])))
                table.setItem(number, 3, QTableWidgetItem(data['method']))
                table.setItem(number, 4, QTableWidgetItem(str(data['from_wallet'])))
                table.setItem(number, 5, QTableWidgetItem(data['to_wallet']))
                table.setItem(number, 6, QTableWidgetItem(str(data['fee'])))
                table.setItem(number, 7, QTableWidgetItem(data['note']))

            table.resizeColumnsToContents()
        else:
            table.clearContents()
            self.ui.public_records_label.setText("No transaction or wallet address found.")
            
        # rowPosition = table.rowCount()
        # table.insertRow(rowPosition)
        # table.setItem(rowPosition, 0, QTableWidgetItem("halo"))
        # table.setItem(rowPosition, 1, QTableWidgetItem("halo"))
        # table.setItem(rowPosition, 2, QTableWidgetItem("halo"))

    def _format_date(self, date: str) -> str:
        date_format = "%a, %d %b %Y %H:%M:%S GMT"
        # format date into like this "26 Apr 2024 08:49:24"
        # Convert string to datetime object
        date_obj = datetime.strptime(date, date_format)
        output_format = "%d %b %Y %H:%M:%S"
        output_date_string = date_obj.strftime(output_format)

        return output_date_string

    # update transaction_history
    def _update_transaction_history(self):
        item = self.ui.list_widget_transaction_history_self
        recent_transaction_history = self.ui.recent_transaction
        item.clear()
        recent_transaction_history.clear()
        recent_transaction_history.addItem("Date\t\t\tInformation")

        trx_history = request_api.get_public_records(self.wallet_number)
        if trx_history['success']:
            previous_date = None
            for data in trx_history['information']['public_records']:
                date = self._format_date(data['date'])
                amount = data['amount']
                method = data['method']
                from_wallet = data['from_wallet']
                to_wallet = data['to_wallet']
                note = data['note']

                amount_text = ""
                text_color = QColor("black")

                if method == "SELL":
                    amount_text = f"SELL -{amount}$SPC => +{amount}$"
                    text_color = QColor("red")
                elif method == "BUY":
                    amount_text = f"BUY +{amount}$SPC => -{amount}$"
                    text_color = QColor("green")
                elif method == "TRANSFER" and from_wallet == self.wallet_number:
                    amount_text = f"-{amount}$SPC Transfer to {to_wallet}"
                    text_color = QColor("red")
                elif method == "TRANSFER" and from_wallet != self.wallet_number:
                    amount_text = f"+{amount}$SPC Receive From {from_wallet}"
                    text_color = QColor("green")
                elif "Deposit" in str(method):
                    amount_text = f"+{amount}$SPC {method} From Wallet {to_wallet}"
                    text_color = QColor("green")
                else:
                    amount_text = f"{amount}$SPC"

                if note:
                    note = "| Note : " + note

                # Add a line separator with date if the date changes
                current_date = date.split()
                current_date = current_date[0]+'/'+current_date[1]+'/'+current_date[2]
                if current_date != previous_date:
                    if previous_date is not None:
                        # Create a QWidget to hold the date label and line
                        separator_widget = QWidget()
                        layout = QHBoxLayout()

                        date_label = QLabel(current_date)
                        line = QFrame()
                        line.setFrameShape(QFrame.Shape.HLine)
                        line.setFrameShadow(QFrame.Shadow.Sunken)
                        line.setStyleSheet("background-color: #A9A9A9; max-height: 1px;")

                        layout.addWidget(date_label)
                        layout.addWidget(line)
                        layout.setStretch(1, 1)  # Make the line stretch

                        separator_widget.setLayout(layout)
                        separator_item = QListWidgetItem()
                        separator_item.setSizeHint(separator_widget.sizeHint())
                        item.addItem(separator_item)
                        item.setItemWidget(separator_item, separator_widget)

                    previous_date = current_date

                transaction_item = QListWidgetItem(f"{date} | {amount_text} {note}")
                transaction_item.setForeground(text_color)
                item.addItem(transaction_item)

                recent_transaction_history.addItem(f"{date}\t\t{amount_text}")
                recent_transaction_history.item(recent_transaction_history.count() - 1).setForeground(text_color)
                
    # buy simplecoin
    def _buy_sell_simplecoin(self, method: Literal['BUY', 'SELL'] = 'BUY'):
        if method == 'BUY':
            amount = self.ui.spend_input.text()
        elif method == 'SELL':
            amount = self.ui.spend_sell_input.text()
        if not amount:
            self.show_dialog('critical', title="Input error!.", message="Please enter the balance correctly!")
            return
        amount = float(amount)
        password = self.show_dialog(type='input')
        if password:
            nonce = self._get_nonce(self.username, password)
            if not nonce:
                self.show_dialog(type='critical', title="Failed input password", message="Failed to get nonce")
                return
            buy_sell = request_api.buy_sell(self.username, password, amount, method=method, nonce=nonce)
            if buy_sell['success']:
                if method == 'BUY':
                    message_text = f"Success buying {amount}$SPC Worth Of SimpleCoin.\n\nMore Details : {NODE}/{buy_sell['information']['transaction_id']}"
                elif method == 'SELL':
                    message_text = f"Success selling {amount}$SPC Worth of {amount} $DOLLAR.\n\nMore Details : {NODE}/{buy_sell['information']['transaction_id']}"
                self.show_dialog(type='information', title='Success buy SimpleCoin', message=message_text)
            else:
                self.show_dialog(type='critical', title="Transaction Failed.", message=f"Failed {'buy' if method == 'BUY' else 'sell'} simplecoin\n{buy_sell['message']}")
        else:
            self.show_dialog(type='critical', title="Failed input password", message="Failed to input password")

        self._set_information()
        # clear
        self.ui.spend_sell_input.clear()
        self.ui.recieve_label_sell.clear()
        self.ui.spend_input.clear()
        self.ui.recieve_label.setText("0")

    
    # change text for buy/sell
    def change_text_buy(self, method: Literal['buy', 'sell']):
        try:
            if method == "buy":
                self.balance = self.fiat_balance
                self.amount_text_spend = self.ui.spend_input.text()
                alert = self.ui.max_amount_alert_buy
                text_warning = f"Maksimal SimpleCoin Yang Bisa Di Beli : {self.fiat_balance} $SPC"
                rec_label = self.ui.recieve_label
            elif method == "sell":
                self.balance = self.simplecoin_balance
                self.amount_text_spend = self.ui.spend_sell_input.text()
                alert = self.ui.max_amount_alert_sell
                text_warning = f"Maksimal SimpleCoin Yang Bisa Di Jual : {self.simplecoin_balance} $SPC"
                rec_label = self.ui.recieve_label_sell
            if float(self.amount_text_spend) > self.balance:
                alert.setText(text_warning)
                rec_label.setText(f"{self.balance}")
            else:
                alert.clear()
                rec_label.setText(self.amount_text_spend)
        except:
            self.ui.recieve_label.clear()
            return

    # show pesan dialog 
    def show_dialog(self, type: Literal['critical', 'information', 'warning', 'input'] = "critical", title: str = "Default title", message: str = "Unknown", button: QMessageBox.StandardButton = QMessageBox.StandardButton.Ok):
        msg_box = QMessageBox(parent=self)
        if type == "critical":
            msg_box.setIcon(QMessageBox.Icon.Critical)
        elif type == "warning":
            msg_box.setIcon(QMessageBox.Icon.Warning)
        elif type == "information":
            msg_box.setIcon(QMessageBox.Icon.Information)
        # input dialog
        elif type == "input":
            dialog = QInputDialog(self)
            dialog.setWindowTitle('Password required')
            dialog.setLabelText('Password required to continue the transaction.\nEnter your password :')
            dialog.setInputMode(QInputDialog.InputMode.TextInput)
            dialog.setTextEchoMode(QLineEdit.EchoMode.Password)
            if dialog.exec() == QInputDialog.DialogCode.Accepted:
                return dialog.textValue()
            return None

        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(button)
        # Set the window flag to make the message box stay on top
        msg_box.setWindowFlags(msg_box.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
        
        # Show the message box and return the result
        return msg_box.exec()

        
        
    def _set_information(self):
        # refresh or set information to account
        self._get_account_information()
        self.wallet_number = self._get_wallet_number()
        self._set_balance_text()
        self._set_network_fee()
        self._update_public_records()
        self.ui.spend_input.setMaxLength(len(str(self.simplecoin_balance)))
        self._update_transaction_history()
        
    def _get_account_information(self):
        self.account_information = request_api.get_username_information(self.username)

    def _set_network_fee(self):
        self.NETWORK_FEE = request_api.get_network_fee()
        self.ui.network_fee.setText(f'{self.NETWORK_FEE} $SPC')

    def _set_balance_text(self):
        # get balance
        self.balance_account = self._get_balance()
        self.simplecoin_balance = float(self.balance_account[0])
        self.fiat_balance = float(self.balance_account[1])
        # set amount dari wallet
        self.ui.balance.setText(str(self.simplecoin_balance) + " $SPC")
        self.ui.fiat_balance.setText(str(self.fiat_balance) + " $")
        # set estimated wallet ke dollar
        self.ui.estimated.setText("≈ $" + str(self.simplecoin_balance))
        self.ui.wallet_number.setText(self.wallet_number)
        self.ui.your_balance_buy.setText(f"Your Balance : {self.fiat_balance} $")
        self.ui.your_balance_sell.setText(f"Your Balance : {self.simplecoin_balance} $SPC")

    def _filter_send_money(self):
        getWalletTujuan = self.ui.wallet_input.text()
        getAmount = self.ui.amount_input.text()
        getNote = self.ui.note_input.text()

        if not getWalletTujuan:
            self.show_dialog("critical", "Wallet address empty", message="Destination wallet cannot be empty")
            return
        if not getAmount:
            self.show_dialog("critical", "Amount cannot empty", message="Please fill in the amount you want to send")
            return
        if not getNote:
            getNote = ''
        
        if getWalletTujuan == self.wallet_number:
            self.show_dialog("critical", "Address Error", message="Can't send money to your own wallet address.")
            return
        
        try:
            mountFloat = float(getAmount)
        except:
            self.show_dialog("critical", "Amount error", message="Please input the amount correctly")
            self.ui.amount_input.clear()
            return

        add_network_fee = mountFloat + self.NETWORK_FEE
        if add_network_fee > self.simplecoin_balance:
            self.show_dialog("critical", "Amount error", message="Amount not enough to make transaction")
            self.ui.amount_input.clear()
            return
        
        password = self.show_dialog(type='input')
        if password:
            self._send_money(password, getWalletTujuan, add_network_fee, note=getNote)
        else:
            self.show_dialog("warning", title="Input password error", message="Input password error!")

    def _send_money(self, password: str, wallet_tujuan: str, amount: float, note: str = ""):
        nonce = self._get_nonce(self.username, password)
        if not nonce:
            self.show_dialog(type='critical', title="Failed input password", message="Failed to get nonce")
            return
        data = {
            "username": self.username,
            "password": password,
            "from_wallet": self.wallet_number,
            "to_wallet": wallet_tujuan,
            "note": note,
            "amount": amount,
            "nonce": nonce
        }

        send_money = request_api.send_money(data)
        if send_money:
            if 'information' in send_money:
                self.show_dialog("information", title="Transfer success!", message=f"Transfer {amount}$SPC to {wallet_tujuan} Success!.\n\nMore Details : {NODE}/transaction_information/"+send_money['information']['transaction_id'])
                self._set_information()
                # clear
                self.ui.wallet_input.clear()
                self.ui.amount_input.clear()
                self.ui.note_input.clear()
            else:
                self.show_dialog('critical', title='Transaction Failed', message=send_money)
        else:
            self.show_dialog('critical', title='Transaction Failed', message=f'Transfer money to {wallet_tujuan} Failed!. Please check the wallet number again.')
        
    def address_copy_to_clipboard(self):
        try:
            clipboard = QGuiApplication.clipboard()
            clipboard.setText(self.wallet_number)
            self.show_dialog('information', title='Success', message='Success copy to clipboard', button=QMessageBox.StandardButton.Ok)
        except:
            self.show_dialog('critical', title='Error', message='Error copy to clipboard', button=QMessageBox.StandardButton.Ok)
            
    def _get_wallet_number(self) -> str:
        return self.account_information['wallet_number']

    def _get_balance(self) -> tuple:
        balance = float(self.account_information['balance'])
        fiat_balance = float(self.account_information['fiat_balance'])

        return balance, fiat_balance

    def init_single_slot(self):
    # Connect signals and slots for menu button and side menu
        self.menu_btn.toggled['bool'].connect(self.side_menu.setHidden)
        self.menu_btn.toggled['bool'].connect(self.title_label.setHidden)
        self.menu_btn.toggled['bool'].connect(self.side_menu_icon_only.setVisible)
        self.menu_btn.toggled['bool'].connect(self.title_icon.setHidden)
        self.menu_btn.toggled.connect(self.button_icon_change)

        # Connect signals and slots for switching between menu items
        self.side_menu.currentRowChanged['int'].connect(self.switch_to_index)
        self.side_menu_icon_only.currentRowChanged['int'].connect(self.switch_to_index)

        # Connect signals and slots for menu item clicks
        self.side_menu.itemClicked.connect(self.on_menu_item_clicked)

    def switch_to_index(self, index):
        self.main_content.setCurrentIndex(index)

    def on_menu_item_clicked(self, item):
        index = self.side_menu.indexFromItem(item).row()
        if index != -1 and index < len(self.menu_list):
            self.main_content.setCurrentWidget(self.menu_list[index]["widget"])
            self.side_menu.setCurrentRow(index)
            self.side_menu_icon_only.setCurrentRow(index)

    def init_list_widget(self):
        # Initialize the side menu and side menu with icons only
        self.side_menu_icon_only.clear()
        self.side_menu.clear()

        for menu in self.menu_list:
            # Set items for the side menu with icons only
            item = QListWidgetItem()
            item.setIcon(QIcon(menu.get("icon")))
            item.setSizeHint(QSize(50, 50))
            self.side_menu_icon_only.addItem(item)
            self.side_menu_icon_only.setCurrentRow(0)

            # Set items for the side menu with icons and text
            item_new = QListWidgetItem()
            item_new.setIcon(QIcon(menu.get("icon")))
            item_new.setText(menu.get("name"))
            self.side_menu.addItem(item_new)
            self.side_menu.setCurrentRow(0)

    def button_icon_change(self, status):
        # Change the menu button icon based on its status
        if status:
            self.menu_btn.setIcon(QIcon("./icon/open.svg"))
        else:
            self.menu_btn.setIcon(QIcon("./icon/close.svg"))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Load style file
    # with open("style.qss") as f:
    #     style_str = f.read()

    #app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
