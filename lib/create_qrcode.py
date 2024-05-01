# simplecoin project
# create qr code for wallet address

import qrcode
import os

def create_qrcode(wallet_address: str):
    # text with wallet_address information
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qrcode_text = f"SPC:{wallet_address}"

    qr.add_data(qrcode_text)

    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    file_path_save = os.getcwd().replace('lib', 'user_img')
    if os.path.exists('user_img/qrcode_wallet.png'):
        os.remove('user_img/qrcode_wallet.png')
    if os.name == 'nt':
        img.save(file_path_save + '\\' + 'user_img\\qrcode_wallet.png')
    else:
        img.save(file_path_save + "/" + 'user_img/qrcode_wallet.png')



