import requests


def send_post(url, message):
    payload = {'text': message}
    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print("Failed to send message")

def main():    
    url = "http://127.0.0.1:5000/receive"

    message = input("Enter message: ")

    send_post(url, message)

if __name__ == "__main__":
    main()
