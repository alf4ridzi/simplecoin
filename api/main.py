# SimpleCoin Project Kelompok 5
# Code by Muhammad Alfaridzi
# API for simplecoin

from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import sys
import encrypt
import os
import parser_config
import time
import random

DATABASE_INFORMATION = parser_config.get_database_information()
WALLET_ADMIN = parser_config.get_admin_network_address()
FEE = parser_config.get_network_fee()

app = Flask(__name__)

app.config['MYSQL_HOST'] = DATABASE_INFORMATION[0]
app.config['MYSQL_USER'] = DATABASE_INFORMATION[1]
app.config['MYSQL_PASSWORD'] = DATABASE_INFORMATION[2]
app.config['MYSQL_DB'] = DATABASE_INFORMATION[3]

mysql = MySQL(app)

def communicate_with_database(query: str):
    cur = mysql.connection.cursor()
    cur.execute(query)

    if query.startswith("SELECT"):
        valid = cur.fetchone()
        cur.close()

        return valid
    
    elif query.startswith("UPDATE") or query.startswith('INSERT'):
        mysql.connection.commit()
        cur.close()

# delete nonce
def clear_nonce(username: str):
    update_nonce = communicate_with_database(f"UPDATE account SET nonce = '0' WHERE username = '{username}'")

# check nonce is match
def is_nonce_match(nonce: str, username: str):
    if communicate_with_database(f"SELECT nonce FROM account WHERE username = '{username}'")[0] == nonce:
        return True
    return False

# add nonce to public records
def add_nonce(transaction_id, nonce):
    update_nonce = communicate_with_database(f"INSERT INTO nonce (transaction_id, nonce) VALUES ('{transaction_id}', '{nonce}')")

# check nonce in database
def is_nonce_on_database(nonce) -> bool:
    if communicate_with_database(f"SELECT nonce FROM nonce WHERE nonce = '{nonce}'"):
        return True
    return False

# create nonce
def create_nonce(username: str) -> str:
    # get unix time
    unixtime = int(time.time())
    add = str(unixtime) + username

    nonce = ''.join(random.choice(add) for _ in range(6))

    # update nonce in account
    update_nonce = communicate_with_database(f"UPDATE account SET nonce = '{nonce}' WHERE username = '{username}'")

    return nonce

# create unique transaction_id
def create_transaction_id(user1: str, user2: str = "") -> str:
    # we get unixtime first
    unixtime = str(time.time())
    # create a random string (4 length)
    random_str = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for _ in range(4))
    # gabung username pengirim & penerima
    unique_str = user1 + user2
    # finally. we hash it using sha256
    return encrypt.hash_sha256(unixtime + random_str + unique_str)

def return_msg(success: bool = True, message: str = "Unknown Error") -> dict:
    json_data = {
        'success': success,
        'message': message
    }

    return json_data

def check_account_on_database(username: str, password: str):
    return communicate_with_database(f"SELECT * FROM account WHERE username = '{username}' AND password = '{password}'")

@app.route('/create_nonce', methods=['POST'])
def creating_nonce():
    if not request.method == 'POST':
        return return_msg(
            success=False,
            message="Method accepts POST only"
        )
    
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return return_msg(
            success=False,
            message="Payload Error."
        )
    
    password = encrypt.hash_password_md5(password)
    if check_account_on_database(username, password):
        nonce = create_nonce(username)
        return return_msg(
            success=True,
            message=nonce
        )
    
    else:
        return return_msg(
            success=False,
            message="Username or password is incorrect."
        )
    

# add transaction to pending
# def pending_transaction(transaction_id: str, method: str, from_wallet: str, to_wallet: str, note: str, status = "PENDING", amount: float = 0.0):
#     # update public records
#     update_public_records = communicate_with_database(f"INSERT INTO public_records (transaction_id, method, from_wallet, to_wallet, note, amount, fee, status) VALUES ('{transaction_id}', '{method}', '{from_wallet}', '{to_wallet}', '{note}', '{amount}', '{status}')")

# deposit
@app.route('/deposit', methods=['POST'])
def deposit():
    if request.method != 'POST':
        return return_msg(
            success=False,
            message='Method accepts POST only'
        )
    
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    amount = data.get('amount')
    wallet = data.get('wallet')
    nonce = data.get('nonce')

    if not username and not password and not amount and not wallet and not nonce:
        return return_msg(
            success=False,
            message="Payload Error."
        )
    
    
    # check username & password
    password = encrypt.hash_password_md5(password)
    if check_account_on_database(username, password):
        if not is_nonce_match(nonce, username):
            clear_nonce(username)
            return return_msg(
                success=False,
                message="Nonce not match"
            )
        
        if is_nonce_on_database(nonce):
            clear_nonce(username)
            return return_msg(
                success=False,
                message="Nonce already used"
            )
    
        transaction_id = create_transaction_id(username)
        amount = float(amount)
        # get wallet address
        wallet_address = communicate_with_database(f"SELECT wallet_number FROM account WHERE username = '{username}' AND password = '{password}'")[0]
        # get current fiat balance
        fiat_balance = communicate_with_database(f"SELECT fiat_balance FROM account WHERE username = '{username}' AND password = '{password}'")[0]        
        # edit fiat balance
        add_fiat_balance = communicate_with_database(f"UPDATE account SET fiat_balance = '{fiat_balance + amount}' WHERE username = '{username}' AND password = '{password}'")
        # update public_records
        update_public_records = communicate_with_database(f"INSERT INTO public_records (transaction_id, method, to_wallet, amount) VALUES ('{transaction_id}', 'Deposit {wallet}', '{wallet_address}', '{amount}')")
        add_nonce(transaction_id, nonce)
        clear_nonce(username)
        return jsonify({
            "success": True,
            "information": {
                "transaction_id":transaction_id,
                "method": f"Deposit {wallet}",
                "to_wallet": wallet_address,
                "amount": amount
            }
        })
    else:
        return return_msg(
            success=False,
            message="Username/Password incorrect."
        )

# showing transaction history with wallet address
@app.route('/public_records/<wallet_address>', methods=['GET'])
def public_records_wallet_address(wallet_address):
    if request.method != 'GET':
        return return_msg(
            success=False,
            message='Method accepts GET only'
        )
    get_information_account = communicate_with_database(f"SELECT wallet_number, balance, fiat_balance FROM account WHERE wallet_number = '{wallet_address}'")
    # get all transaction wallet_address
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM public_records WHERE to_wallet = '{wallet_address}' OR from_wallet = '{wallet_address}'")
    data_public_records = cur.fetchall()
    
    if not data_public_records:
        return return_msg(
            success=False,
            message="Wallet address not found."
        )
    cur.execute("SHOW COLUMNS FROM public_records")
    columns = [column[0] for column in cur.fetchall()]
    cur.close()

    # Converting data into a list of dictionaries
    records_list = []
    for row in data_public_records:
        record_dict = {}
        for i in range(len(columns)):
            record_dict[columns[i]] = row[i]
        records_list.append(record_dict)

    return jsonify({
        "success": True,
        "information": {
            "wallet_address": get_information_account[0],
            "balance": get_information_account[1],
            "fiat_balance": get_information_account[2],
            "public_records": records_list
        }
    })

# showing all transaction / public records.
@app.route('/public_records', methods=['GET'])
def public_records():
    if request.method != 'GET':
        return return_msg(
            success=False,
            message='Method accepts GET only'
        )
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM public_records")
    data_public_records = cur.fetchall()
    #cur.close()

    # Extracting column names
    #cur = mysql.connection.cursor()
    cur.execute("SHOW COLUMNS FROM public_records")
    columns = [column[0] for column in cur.fetchall()]
    cur.close()

    # Converting data into a list of dictionaries
    records_list = []
    for row in data_public_records:
        record_dict = {}
        for i in range(len(columns)):
            record_dict[columns[i]] = row[i]
        records_list.append(record_dict)

    if records_list:
        return jsonify({
            "success": True,
            "public_records": records_list
        })
    else:
        return return_msg(
            success=False,
            message="No transaction made."
        )
# buy / sell
@app.route('/buy_sell', methods=['POST', 'GET'])
def buy_sell():
    if not request.method == 'POST':
        return jsonify({'success': False, 'message': 'method accept POST only'}), 403
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    amount = data.get('amount')
    method = data.get('method')
    nonce = data.get('nonce')
    if not username and not password and not amount and not method:
        return return_msg(success=False, message="Payload Error.")
    
    password = encrypt.hash_password_md5(password)
    if check_account_on_database(username, password):
        if not is_nonce_match(nonce, username):
            clear_nonce(username)
            return return_msg(
                success=False,
                message="Nonce is not valid."
            )
        
        if is_nonce_on_database(nonce):
            clear_nonce(username)
            return return_msg(
                success=False,
                message="Nonce already used"
            )
        
        generate_transaction_id = create_transaction_id(username)
        # get simplecoin & fiat balance
        
        balance = communicate_with_database(f"SELECT balance, fiat_balance FROM account WHERE username = '{username}' and password = '{password}'")
        simplecoin_balance = balance[0]
        fiat_balance = balance[1]
        # get wallet address 
        wallet_address = communicate_with_database(f"SELECT wallet_number FROM account WHERE username = '{username}'")[0]

        try:
            if method == 'buy':
                if amount > fiat_balance:
                    return return_msg(success=False, message="Fiat balance not enough to make transaction")
                # update simplecoin & fiat balance
                update_simplecoin_fiat_balance = communicate_with_database(f"UPDATE account SET balance = {simplecoin_balance + amount}, fiat_balance = {fiat_balance - amount} WHERE username = '{username}' AND password = '{password}'")
                # update public records 
                update_public_records = communicate_with_database(f"INSERT INTO public_records (transaction_id, method, to_wallet, amount) VALUES ('{generate_transaction_id}', 'BUY', '{wallet_address}', {amount})")

            elif method == 'sell':
                if simplecoin_balance < amount:
                    return return_msg(success=False, message="SimpleCoin not enough to make transaction")
                update_simplecoin_fiat_balance = communicate_with_database(f"UPDATE account SET balance = {simplecoin_balance - amount}, fiat_balance = {fiat_balance + amount} WHERE username = '{username}' AND password = '{password}'")
                # update public records 
                update_public_records = communicate_with_database(f"INSERT INTO public_records (transaction_id, method, to_wallet, amount) VALUES ('{generate_transaction_id}', 'SELL', '{wallet_address}', {amount})")
            add_nonce(generate_transaction_id, nonce)
            clear_nonce(username)
            return jsonify({"success": True,
                            "information": {
                                "transaction_id": generate_transaction_id,
                                "wallet": wallet_address,
                                "amount": amount,
                                "method": method
                            }}
            )

        except:
            return return_msg(
                success=False,
                message="Unknown Error"
            )
    
    else:
        return return_msg(
            success=False,
            message="Username/Password Incorrect"
        )
    
# get transaction information
@app.route('/transaction_information/<transaction_id>', methods=['GET'])
def transaction_information(transaction_id):
    if not request.method == 'GET':
        return jsonify({'success': False, 'message': 'method accept GET only'}), 403
    check_transaction = communicate_with_database(f"SELECT * FROM public_records WHERE transaction_id = '{transaction_id}'")
    if not check_transaction:
        return return_msg(success=False, message='Transaction not found')
    get_information_transaction = communicate_with_database(f"SELECT transaction_id, method, from_wallet, to_wallet, note, amount, fee, date FROM public_records WHERE transaction_id = '{transaction_id}'")
    return jsonify({
        'success': True,
        'information': {
            'transaction_id': get_information_transaction[0],
            'method': get_information_transaction[1],
            'from_wallet': get_information_transaction[2],
            'to_wallet': get_information_transaction[3],
            'note': get_information_transaction[4],
            'amount': get_information_transaction[5],
            'fee': get_information_transaction[6],
            'date': get_information_transaction[7]
        }
    })
            

@app.route('/send_money', methods=['POST', 'GET'])
def send_money():
    if not request.method == 'POST':
        return jsonify({'success': False, 'message': 'method accept POST only'}), 403
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    from_wallet = data.get('from_wallet')
    to_wallet = data.get('to_wallet')
    amount = float(data.get('amount'))
    fee = FEE
    note = data.get('note')
    amount = amount - fee
    nonce = data.get('nonce')
    if not username and not password and not to_wallet and not from_wallet:
        return return_msg(success=False, message='Payload not valid.')
    
    password = encrypt.hash_password_md5(password)
    # check if username & password is match
    if communicate_with_database(f"SELECT * FROM account WHERE username = '{username}' AND password = '{password}'"):
        if not is_nonce_match(nonce, username):
            clear_nonce(username)
            return return_msg(
                success=False,
                message="Nonce is not valid."
            )
        
        if is_nonce_on_database(nonce):
            clear_nonce(username)
            return return_msg(
                success=False,
                message="Nonce already used"
            )
        
        generate_transaction_id = create_transaction_id(username, user2=to_wallet)
        # mendapatkan balance pengirim & penerima terlebih dahulu
        sender_balance = communicate_with_database(f"SELECT balance FROM account WHERE wallet_number = '{from_wallet}'")[0]
        if sender_balance < amount + FEE:
            return return_msg(success=False, message="Sender balance not enough to make transaction.")
        recipient_balance = communicate_with_database(f"SELECT balance FROM account WHERE wallet_number = '{to_wallet}'")
        if not recipient_balance:
            return return_msg(
                success=False,
                message="Wallet address not found."
            )
        recipient_balance = recipient_balance[0]
        admin_network_balance = communicate_with_database(f"SELECT balance FROM account WHERE wallet_number = '{WALLET_ADMIN}'")[0]
        # update balance pengirim & penerima 
        update_balance_sender = communicate_with_database(f"UPDATE account SET balance = {sender_balance - amount} WHERE wallet_number = '{from_wallet}'")
        update_balance_recipient = communicate_with_database(f"UPDATE account SET balance = {recipient_balance + amount} WHERE wallet_number = '{to_wallet}'")
        # transfer fee to wallet_admin
        update_balance_recipient = communicate_with_database(f"UPDATE account SET balance = {admin_network_balance + fee} WHERE wallet_number = '{WALLET_ADMIN}'")
        # update public records
        update_public_records = communicate_with_database(f"INSERT INTO public_records (transaction_id, method, from_wallet, to_wallet, note, amount, fee) VALUES ('{generate_transaction_id}', 'TRANSFER', '{from_wallet}', '{to_wallet}', '{note}', {amount}, {fee})")
        add_nonce(generate_transaction_id, nonce)
        clear_nonce(username)
        return jsonify({
            'success': True,
            'message': {
                'information': {
                    'transaction_id': generate_transaction_id,
                    'method': 'transfer',
                    'from_wallet': from_wallet,
                    'to_wallet': to_wallet,
                    'amount': amount,
                    'fee': fee,
                    'note': note
                }
            }
        })
    
    else:
        return return_msg(success=False, message='Username & Password not valid.')
    #return communicate_with_database(f"SELECT nonce FROM account WHERE username = 'alfaridzi'")[0]


    

@app.route('/get_network_fee', methods=['GET'])
def check_network_fee():
    NETWORK_FEE = parser_config.get_network_fee()
    return jsonify(
        {'success': True, 'network_fee': NETWORK_FEE}
    )

# check account
@app.route('/check_account', methods=['POST', 'GET'])
def check_account():
    if not request.method == 'POST':
        return jsonify({'success': False, 'message': 'method accept POST only'}), 403
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'success': False, 'message': 'Username or password are required'}), 400
    password_hashed = encrypt.hash_password_md5(password)
    cur = mysql.connection.cursor()
    query = "SELECT * FROM account WHERE username = %s AND password = %s"
    cur.execute(query, (username, password_hashed))

    valid = cur.fetchone()
    cur.close()
    if valid:
        return jsonify({'success': True, 'message': 'username or password are correct'}), 200
    return jsonify({'success': False, 'message': 'username or password are incorrect'}), 201

# get information account
@app.route('/get_information', methods=['GET'])
def get_information_account():
    if not request.method == 'GET':
        return jsonify(return_msg(success=False, message="Only support GET requests"))
    # get data post
    username = request.args.get('username')
    if not username:
        return jsonify(return_msg(success=False, message="Parameter username is missing"))
    cur = mysql.connection.cursor()
    query = "SELECT wallet_number, balance, fiat_balance FROM account WHERE username = %s;"
    cur.execute(query, (username, ))
    information = cur.fetchone()
    if information:
        return jsonify({'success': True, 'information': {'wallet_number': information[0], 'balance': information[1], 'fiat_balance': information[2]}})
    else:
        return jsonify({
            'success': False,
            'information': None
        })
    
@app.route('/create_account', methods=['POST', 'GET'])
def create_account():
    if not request.method == 'POST':
        return jsonify({'success': False, 'message': 'method accept POST only'}), 403
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'success': False, 'message': 'Username or password are required'}), 400
    cur = mysql.connection.cursor()
    query = "SELECT * FROM account WHERE username = %s"
    cur.execute(query, (username, ))
    valid = cur.fetchone()
    #cur.close()
    if valid:
        return jsonify({'success': True, 'message': 'username already exist'}), 400
    # creating account
    wallet_number = encrypt.create_wallet_number(username)
    password_enc = encrypt.hash_password_md5(password)
    create_account_query = "INSERT INTO account (wallet_number, username, password, balance, nonce) VALUES (%s, %s, %s, 0, 0)"
    cur.execute(create_account_query, (wallet_number, username, password_enc))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'success'}), 200

# check username exist or not
@app.route('/check_username', methods=['GET'])
def check_username():
    username = request.args.get('username')
    if not username:
        return jsonify({'success': True, 'message':"missing parameters"}), 400
    # if not username:
    #     return jsonify({"error":"missing parameters"}), 400
    cur = mysql.connection.cursor()
    query = "SELECT * FROM account WHERE username = %s"
    cur.execute(query, (username, ))
    valid = cur.fetchone()
    cur.close()
    if valid:
        return jsonify({'success': True, 'message': 'username exist'}), 200
    return jsonify({'success': False, 'message':'username doesnt exist'}), 200
    

@app.route('/')
def home():
    return "API for SimpleCoin Project"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port='5000')
