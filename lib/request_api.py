# simplecoin project
# API for request to NODE/API

import urllib3
import json
from typing import Literal
from lib.parser_config import get_node

NODE = get_node()

timeout = urllib3.Timeout(total=5)
http = urllib3.PoolManager(timeout=timeout)

def deposit(username: str, password: str, amount: float, wallet):
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "username": username,
        "password": password,
        "amount": amount,
        "wallet": wallet
    }

    data = json.dumps(data).encode('utf-8')
    try:
        resp = http.request("POST", NODE+"/deposit", headers=headers, body=data).json()
        return resp
    except:
        return {
            'success': False,
            'message': 'Failed deposit.'
        }

def get_public_records(wallet_address: str = None):
    if wallet_address:
        api = NODE+f'/public_records/{wallet_address}'
    else:
        api = NODE+'/public_records'

    try:
        resp = http.request("GET", api).json()
        return resp
    except:
        return {
            'success': False,
            'message': 'Failed to get public records.'
        }

def buy_sell(username, password, amount: float, method: Literal['BUY', 'SELL'] = "BUY") -> json:
    method = method.lower()
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "username": username,
        "password": password,
        "method": method,
        "amount": amount
    }

    data = json.dumps(data).encode('utf-8')
    try:
        resp = http.request("POST", NODE+'/buy_sell', headers=headers, body=data).json()
        return resp
    except Exception as e:
        return {
            "success": False,
            "message": e
        }

def send_money(data):
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps(data)
    try:
        resp = http.request("POST", NODE+'/send_money', body=data, headers=headers).json()
        return resp['message']
    except:
        return False

def check_valid_account(username: str, password: str):
    headers = {
        "Content-Type": "application/json"
    }

    data = json.dumps({
        "username": username,
        "password": password
    }).encode('utf-8')

    try:
        check = http.request("POST", NODE+"/check_account", headers=headers, body=data)
        if check.status != 200:
            return False
        return True
    except Exception as e: 
        return e

def get_username_information(username: str) -> dict:
    try:
        req = http.request("GET", NODE+'/get_information?username={}'.format(username)).json()
        if req['success']:
            return req['information']
        else:
            return {"success": False}
    except:
        return {"success": False}

def check_username(username: str) -> bool:
    try:
        resp = http.request("GET", NODE+"/check_username?username={}".format(username)).json()
        if not resp['success'] and resp['message'] == "username doesnt exist":
            return True
        return False
    except Exception as e:
        return e

def create_user(username: str, password: str):
    headers = {
        "Content-Type": "application/json"
    }

    data = json.dumps({
        "username": username,
        "password": password
    }).encode('utf-8')
    try:
        resp = http.request("POST", NODE+"/create_account", body=data, headers=headers)
        if resp.status == 200:
            return True
        return False
    except Exception as e:
        return e

def get_network_fee() -> float:
    try:
        resp = http.request("GET", NODE+'/get_network_fee').json()
        return resp['network_fee']
    except:
        return 0.0
    
def check_server() -> bool:
    try:
        resp = http.request("GET", NODE).status
        return resp == 200
    except:
        return False
