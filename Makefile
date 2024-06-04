make:
	pyuic6 -x main.ui -o dashboard_ui.py
	pyuic6 -x transaction_detail_popup.ui -o lib/trx_popup.py
exe:
	pyinstaller --onefile login.py
