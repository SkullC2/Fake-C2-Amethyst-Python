import colorama
import time
import fade
import os
from colorama import Fore

colorama.init()

def attackpanel(method, target, port, duration):
    bannerattack = """
╔═╗╔╦╗╔═╗╔╦╗╦ ╦╦ ╦╔═╗╔╦╗
╠═╣║║║║╣  ║ ╠═╣╚╦╝╚═╗ ║ 
╩ ╩╩ ╩╚═╝ ╩ ╩ ╩ ╩ ╚═╝ ╩ 
"""
    print(Fore.MAGENTA + bannerattack)
    print(Fore.BLUE + "Attack ID: 1")
    print(Fore.BLUE + "Method: " + Fore.YELLOW + method)
    print(Fore.BLUE + "Target: " + Fore.YELLOW + target)
    print(Fore.BLUE + "Port: " + Fore.YELLOW + port)
    print(Fore.BLUE + "Time: " + Fore.YELLOW + duration)
    print(Fore.YELLOW + 'Enter "cls" to clear the terminal or "exit" to exit the attack panel.')

    while True:
        command = input(Fore.CYAN + "Amethyst" + Fore.WHITE + "@" + Fore.CYAN + "C2> " + Fore.RESET)
        if command.lower() == "cls":
            os.system('cls' if os.name == 'nt' else 'clear')
        elif command.lower() == "exit":
            break

def login() -> bool:
    print("Login to the CNC System. Please input your login credentials")
    username = input("User> ")
    password = input("Password> ")
    if username == "admin" and password == "password123":
        print(Fore.GREEN + "Welcome (admin) to the Amethyst C2. Please wait...")
        time.sleep(2)
        panel()
        return True
    else:
        print("Invalid credentials. Try again.")
        return False

def panel():
    banner = """
      .o.       ooo        ooooo oooooooooooo ooooooooooooo ooooo   ooooo oooooo   oooo  .oooooo..o ooooooooooooo 
     .888.      `88.       .888' `888'     `8 8'   888   `8 `888'   `888'  `888.   .8'  d8P'    `Y8 8'   888   `8 
    .8"888.      888b     d'888   888              888       888     888    `888. .8'   Y88bo.           888      
   .8' `888.     8 Y88. .P  888   888oooo8         888       888ooooo888     `888.8'     `"Y8888o.       888      
  .88ooo8888.    8  `888'   888   888    "         888       888     888      `888'          `"Y88b      888      
 .8'     `888.   8    Y     888   888       o      888       888     888       888      oo     .d8P      888      
o88o     o8888o o8o        o888o o888ooooood8     o888o     o888o   o888o     o888o     8""88888P'      o888o     
"""
    print(Fore.MAGENTA + banner)
    print(Fore.MAGENTA + "Welcome. You have been connected to the Amethyst C2. Enter 'help' for a list of commands.")

    while True:
        command = input(Fore.CYAN + "Amethyst" + Fore.WHITE + "@" + Fore.CYAN + "C2> " + Fore.RESET)

        if command.lower() == "help":
            print(Fore.YELLOW + "Available commands below:")
            print(Fore.YELLOW + "help - Show this help page")
            print(Fore.YELLOW + "methods - Shows the available attack methods")
            print(Fore.YELLOW + "plan - Shows the information about your plan")
            print(Fore.YELLOW + "exit - Exits the C2 panel")

        elif command.lower() == "methods":
            attackbanner = """
╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗
║║║║╣  ║ ╠═╣║ ║ ║║╚═╗
╩ ╩╚═╝ ╩ ╩ ╩╚═╝═╩╝╚═╝
"""
            print(Fore.MAGENTA + attackbanner)
            print(Fore.YELLOW + "Available attack methods:")
            print(Fore.GREEN + "Layer 4 Method Vectors:")
            print(Fore.YELLOW + "udp - UDP FLOOD")
            print(Fore.YELLOW + "tcp - TCP FLOOD")
            print(Fore.YELLOW + "icmp - ICMP FLOOD")
            print(Fore.YELLOW + "syn - SYN FLOOD")
            print(Fore.YELLOW + "ack - ACK FLOOD")
            print(Fore.YELLOW + "ovh - OVH FLOOD")
            print(Fore.GREEN + "Layer 7 Method Vectors:")
            print(Fore.YELLOW + "http - HTTP FLOOD")
            print(Fore.YELLOW + "https - HTTPS FLOOD")
            print(Fore.YELLOW + "tls - TLS FLOOD")
            print(Fore.MAGENTA + "Attack Syntax: <method> <target> <port> <time>")

        elif any(command.startswith(method) for method in ["udp", "tcp", "icmp", "syn", "ack", "ovh", "http", "https", "tls"]):
            args = command.split()
            if len(args) == 4:
                method, target, port, duration = args
                attackpanel(method, target, port, duration)
            else:
                print(Fore.RED + "Invalid attack syntax. Use: <method> <target> <port> <time>")

        elif command.lower() == "exit":
            print("Exiting... bye!")
            break

        else:
            print(Fore.RED + f"Unknown command: {command}")

if __name__ == "__main__":
    while not login():
        pass
