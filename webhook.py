def send_teams_message(webhook_url, message):
    headers = {'Content-Type': 'application/json'}
    data = {"text": message}
    response = requests.post(webhook_url, json=data, headers=headers)
if response.status_code == 200:
    print("Zpráva úspěšně odeslána na Teams!")
else:
    print("Nastala chyba při odesílání na Teams:", response.status_code)

teams_webhook_url = "https://prod-14.westeurope.logic.azure.com:443/workflows/6266bba73746407e95b3464bd32529b5/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=4PAYC1dGp-BJ-4evdosRWdSPdqKYmSZv1mOVGGAKWgM"
teams_message = "Toto je zpráva odeslaná přes webhook!"
send_teams_message(teams_webhook_url, teams_message)
