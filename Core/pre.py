import os
import random
import time
from rgbprint import gradient_print
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Function to simulate delay (for animation-like effects)
def delay_print(message, delay=0.01):  # Reduced delay to speed up animation
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Dark-themed colors for a hacker-like interface
green = "\033[1;32;40m"
yellow = "\033[1;33;40m"
red = "\033[1;31;40m"
blue = "\033[1;34;40m"
purple = "\033[1;35;40m"
white = "\033[1;37;40m"
bold_white = "\033[1;37m"

# Set Version
Version = "2.2"

# Banner (in ASCII art with dark theme)
banner = f"""
██████╗ ██╗      █████╗  ██████╗██╗  ██╗    ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝    ██╔══██╗██║  ██║██║██╔════╝██║  ██║
██████╔╝██║     ███████║██║     █████╔╝     ██████╔╝███████║██║███████╗███████║
██╔══██╗██║     ██╔══██║██║     ██╔═██╗     ██╔═══╝ ██╔══██║██║╚════██║██╔══██║
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗    ██║     ██║  ██║██║███████║██║  ██║
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝ \n
			</> Author: Fahim Muntasir | BLACK HAT BD

	===========================================================
			Telegram: @fahimciphers
	===========================================================
"""

# Check Internet Connection
def connected(host='http://duckduckgo.com'):
    try:
        urlopen(host)
        return True
    except:
        return False

# Function to animate text
def banner_animation():
    delay_print(banner, 0.01)  # Faster animation (1 second total)

# Create the menu with smooth animation
def menu():
    clear_screen()  # Clear screen before displaying menu
    banner_animation()  # Banner with typing animation

    # Animated "stay updated" message
    delay_print(red + "More Versions Will Come Soon. Stay Updated, Follow My Github\n", 0.01)
    
    print(white + "Options:")

    # Displaying the menu options
    menu_items = [
        ("Instagram", 1), ("Paypal", 12), ("Facebook", 2), ("Discord", 13), ("Gmail", 3), ("Spotify", 14),
        ("Gmail (simple)", 4), ("Blockchain", 15), ("Twitter", 5), ("RiotGames", 16), ("Snapchat", 6),
        ("Rockstar", 17), ("Snapchat (simple)", 7), ("AskFM", 18), ("Steam", 8), ("000Webhost", 19),
        ("Dropbox", 9), ("Linkedin", 10), ("Gamehag", 21), ("Playstation", 11), ("Mega", 22)
    ]
    
    for name, index in menu_items:
        print(green + f"[{white}{index}{green}] {white}{name}")

    print(green + "-----------------------------------------------------------------------")
    print(green + f"[{white}00{green}] {red}EXIT")

# Welcome Function to clear screen and show banner
def Welcome():
    clear_screen()
    delay_print(f"{blue}Initializing system...\n", 0.01)
    time.sleep(0.5)  # Simulate a short wait for system readiness

# Main Execution
if __name__ == "__main__":
    Welcome()
    menu()
