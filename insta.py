import time
import sys

def print_colored(text, color):
    colors = {
        'blue': '\033[94m',
        'green': '\033[92m',
        'reset': '\033[0m'
    }
    print(f"{colors[color]}{text}{colors['reset']}")

def fake_instagram_hack():
    username = input("Enter Instagram username: ")
    print_colored("Connecting to Instagram API...", 'blue')
    time.sleep(2)  # Simulate loading time
    print_colored("Connected Successfully", 'green')
    print_colored("Buy Me Coffee", 'green')
    print("\n7012407319\nOpay\nAbubakar Bello Bawa\n")
    
    confirmation = input("Type Y if you have sent the money: ")
    if confirmation.lower() == 'y':
        print_colored("IDiot na me u wan do scam for abeg send money jo nothing is free in this life wallahi nothing is free 🤣", 'green')

fake_instagram_hack()
