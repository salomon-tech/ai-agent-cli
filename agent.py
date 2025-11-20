from random import choice, random
import random
import datetime

ai_answers = {
    "salut": [
        "Salut ! Comment tu vas ?",
        "Bonjour ! Je suis là pour toi 😄",
        "Yo ! Besoin d'aide ?"
    ],
    "comment tu vas": [
        "Je vais super bien, merci ! Et toi ?",
        "Toujours opérationnel ✊",
        "Prêt à coder avec toi."
    ],
    "heure": [
        "Il est " + datetime.datetime.now().strftime("%H h : %M min")
    ],
    "motivation": [
        "Continue frère, tu vas devenir chaud 🔥",
        "Le code c'est comme la muscu : persévère.",
        "Tu vas réussir, ne lâche JAMAIS 💪"
    ],
    "bye": [
        "À plus ! Continue à t'entraîner 💚",
        "On se voit bientôt 👋",
        "Bye frère, force à toi ✊"
    ]
}

def get_message(message):
    massage = ai_answers.keys()

    for key in message:
        if key in massage:
            return random.choice(ai_answers[key])
    return "word not found, u can try a gain ❗"

def chat():
    print(random.choice(ai_answers["salut"]))
    print("if u need help, type 'help🆘' ")

    while True:
        user_input = input("you: ").lower()
        if user_input == "help":
            print("if u want to exit type 'exit' ")
            continue
        if user_input == 'exit':
            print(random.choice(ai_answers["bye"]))
            break
        Response = get_message(user_input.split())
        print("AI agent: " + Response)

if __name__ == "__main__":
    chat()
