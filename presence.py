import argparse
import requests
import html2text

url = "http://intranet.supinternet.fr/?action=login"

# requests.get(url, auth=HTTPBasicAuth('login', 'pwd'))
parser = argparse.ArgumentParser()
parser.add_argument(
    "presence",
)
args = parser.parse_args()

# va fermer le fichier
with open('sup.txt') as f:
    auth = tuple(f.read().split(':'))
session = requests.session()

r = session.post("http://intranet.supinternet.fr/?action=login", data={'login': auth[0], 'pwd': auth[1], 'do': 'Connexion'})
# print(r.status_code, r.reason, r.text)
r = session.post("http://intranet.supinternet.fr/?action=presence", data={'token': args.presence, 'valider': 'Valider'})
# print(r.text)
html = r.text
htmltext = html2text.html2text(html)
print(htmltext)