<div align="center">
  <img src="https://raw.githubusercontent.com/alf4ridzi/simplecoin/main/img/simplecoin-banner.png">
</div>

# SimpleCoin
SimpleCoin is a software wallet that works to send money from one person to another

## What Technology Does SimpleCoin Use?
- Python
- MySQL & PhpMyAdmin For Database
- Python-Flask For API
- Qt Designer For Design
- PyQt6 For Login & GUI

## What Features on SimpleCoin ?
- Login Page
- Register Page
- Dashboard
- Send / Receieve coin
- Buy / Sell coin
- Public records
- Transaction history
- Deposit
- Refresh
- QrCode Wallet
- etc ...
## How To Run SimpleCoin ?
- Download XAMPP <a href='https://www.apachefriends.org/download.html'>Download Here</a><br>
- Download Python <a href='https://www.python.org'>Download Here</a><br>

1. Run XAMPP Apache & MySQL
2. Import file named 'simplecoin_db.sql' to your PhpMyAdmin
3. Install Module Python
```
pip install PyQt6 PySide6 Flask qrcode
```
4. Configure config.ini on API folder & edit what you need.
```
[DATABASE]
HOST = localhost
USER = root
PASSWORD = your_password
DATABASE = simplecoin

[NETWORK]
NETWORK_FEE = 0.01

[ADMINISTRATOR]
WALLET_NUMBER = 0xnZfn2LseArFTErhL1gwPCPtMCJ4
```
5. Run main.py on API to run server
```
python main.py
```
6. Run login.py
```
python login.py
```

## Gallery
## Login
![](https://raw.githubusercontent.com/alf4ridzi/simplecoin/main/img/gallery/login.png)
## Register
![](https://raw.githubusercontent.com/alf4ridzi/simplecoin/main/img/gallery/register.png)
## Dashboard
![](https://raw.githubusercontent.com/alf4ridzi/simplecoin/main/img/gallery/dashboard.png)
## Send Rec
![](https://raw.githubusercontent.com/alf4ridzi/simplecoin/main/img/gallery/sendrec.png)
## Buy Sell
![](https://raw.githubusercontent.com/alf4ridzi/simplecoin/main/img/gallery/buysell.png)
## Public Records
![](https://raw.githubusercontent.com/alf4ridzi/simplecoin/main/img/gallery/publicrecords.png)
## Transaction History
![](https://raw.githubusercontent.com/alf4ridzi/simplecoin/main/img/gallery/transactionhistory.png)
## Deposit
![](https://raw.githubusercontent.com/alf4ridzi/simplecoin/main/img/gallery/deposit.png)
## About & Team
![](https://raw.githubusercontent.com/alf4ridzi/simplecoin/main/img/gallery/about.png)

