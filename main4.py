import time
import requests

def ping_site():
    url = "https://cowldl.onrender.com"
    while True:
        try:
            response = requests.get(url)
            print(f"Pinged {url} - Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to ping the site: {e}")
        # Wait for 5 minutes before the next ping
        time.sleep(300)

if __name__ == "__main__":
    ping_site()
