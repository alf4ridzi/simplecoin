from configparser import ConfigParser

def read_config():
    config = ConfigParser()
    config.read('config.ini')
    return config

def get_database_information() -> tuple:
    config = read_config()
    HOST = config['DATABASE']['HOST']
    USER = config['DATABASE']['USER']
    PASSWORD = config['DATABASE']['PASSWORD']
    DATABASE = config['DATABASE']['DATABASE']

    return (HOST,
            USER,
            PASSWORD,
            DATABASE)

def get_network_fee() -> float:
    config = read_config()
    return float(config['NETWORK']['NETWORK_FEE'])

def get_admin_network_address() -> str:
    config = read_config()
    return config['ADMINISTRATOR']['WALLET_NUMBER']