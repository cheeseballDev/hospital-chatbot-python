import os

greetings = {
    "hello": "Hi, how may I help you today?",
    "hi": "Hello, how may I help you today?",
    "greetings": "Salutations! How may I help you today?"
}
diagnosis = {
    "sick": "Shall we schedule you for an appointment?",
    "ill": "Shall we schedule you for an appointment?",
    "help": "What do you need help with?"
}
doctor =  {
    "appointment": "What time is your appointment?",
    "doctor": "I'll try to notify the next available doctor for you."
}

def main() -> None:
    os.system('cls||clear')
    print("Welcome to Cheese's Hospital, I am Mika. How may I help you today?")
    while True:
        user_response = check_response_valid()
        print(response_output(user_response))


def response_output(user_response) -> str:
    response = []
    for word in user_response:
        if word in greetings:
            response.append(response_greetings(word))
        elif word in diagnosis:
            response.append(response_diagnosis(word))
        elif word in doctor:
            response.append(response_doctor(word))
    if response:
        return " ".join(response)
    return "I'm sorry, I didn't understand what you said. Can you repeat it for me?"


def response_greetings(user_response) -> str:
    return str(greetings[user_response])

def response_diagnosis(user_response) -> str:
    return str(diagnosis[user_response])

def response_doctor(user_response) -> str:
    return str(doctor[user_response])


## check if user response is valid or not
def check_response_valid() -> str:
    while True:
        try:
            user_response = input().lower().strip().translate(str.maketrans('','',"!?.,'123456789")).split()
            return user_response
        except:
            print("I'm sorry, I didn't quite understand what you said.")
            continue
    

if __name__ == "__main__":
    main()
