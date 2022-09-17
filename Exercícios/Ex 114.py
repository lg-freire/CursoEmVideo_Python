import requests

try:
    sitedata=requests.get("http://pudim.com.br/", timeout=6)
    print('\033[32mThis site was reachable.\033[m')
except (requests.ConnectionError, requests.Timeout):
    print('\033[31mThis site was unreachable.\033[m')
