def login():
    print("login")
def signin():
    print("signin")
def driverPanel():
    print("driver panel")

def setting():
    print("you has etnered setings")

def welcomeMessage(welcomeMessageData):
    print(f"{" Kerbwise ":─^40} \n")
    for index, part in enumerate(welcomeMessageData):
        output = f"{index+1}: {part["name"]: ^{12}}"
        print(f"{output: ^40}")       
    print("")

def callMenuFunction(welcomeMessageData, menuOption):
    welcomeMessageData[menuOption]["function"]()

def handleWelcomeInput():
    while True:
        try:
            userInput = int(input("> "))
            if userInput-1 in range(0, len(welcomeMessageData)):
                callMenuFunction(welcomeMessageData, userInput-1)
            else: 
                raise IndexError("Please enter a number between 1 to 3")
            break
        except ValueError, IndexError:
            print("\033[A\033[2K\033[A\033[2K", end="", flush=True)
            print(f"\x1b[31mPlease only enter a number from 1 to {len(welcomeMessageData)}.\x1b[0m")


welcomeMessageData = [
                  {"name": "Login", "function": login},
                  {"name": "signin", "function": signin},
                  {"name": "Settings", "function": setting},
                  {"name": "Driver Panel", "function": driverPanel}
                ]




def main():
    welcomeMessage(welcomeMessageData)
    handleWelcomeInput()

if __name__ == "__main__":
    try:
        main()
        pass
    except KeyboardInterrupt:
        print("Bye :(")




