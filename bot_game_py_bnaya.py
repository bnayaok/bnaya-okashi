

import random
import time


user=input("please enter your name:")
print("welcome to the game")
bot_name= "bob"
print("my name is", bot_name)

#תמונה לבוט 
def print_bot(message):
    print(f"🤖{bot_name}: {message}")

#הדפסת הודעה עם אפקט של הקלדה איטית
def print_bot(message):
    print(f"🤖 {bot_name}: ", end="", flush=True)
    
    for char in message:
        print(char, end="", flush=True)
        time.sleep(0.05) 
    
    print()

print_bot("I can play games with you, and tell jokes,and interact with you in a fun way")
print_bot("if you want to know what I can do, just type 'HELP' and I'll show you!") 

#HELP definition
def show_help():
    print_bot("Here are some things you can say:")
    print_bot("HELLO - I'll greet you!")
    print_bot("JOKE - I'll tell you a joke!")
    print_bot("GAME - We can play a game together!")
    print_bot("EXIT - I'll say goodbye and end the conversation!")


#jokes definitions
def tell_joke():
    jokes = [
        "why did the chicken cross the road? to get to the other side!",
        "why was the math book sad? because it had too many problems!",
        "why did the tomato turn red? because it saw the salad dressing!"
    ]
    print_bot(random.choice(jokes))
#greetings definitions
def greeting():
    greetings = ["hello", "hi!", "hey there!", "welcome!"]
    print_bot(random.choice(greetings))

#goodbye definitions
def goodbye():
    goodbye_messages = ["goodbye!", "see you later!", "take care!", "have a nice day!", "bye!"]
    print_bot(random.choice(goodbye_messages))

#guessing game definition
def guessing_game():
            print_bot("lets play the guessing game! if you want to stop playing, just type '900' ")
            number = random.randint(1, 100)
            attempts = 0
            while True: 
                guess= int(input("enter a number between 1 and 100: "))
                attempts += 1
                if guess == number:
                    print_bot(f"congatulations! {user} you guessed the number in {attempts} attempts!")
                
                elif guess < number:
                    print_bot("too low! try again.")
                elif guess == 900:
                    print_bot("okay, maybe next time!")
                    break
                else:
                    print_bot("too high! try again.")

#game rock paper scissors definition
def rock_paper_scissors():
    print_bot("lets play rock paper scissors! if you want to stop playing, just type 'stop' ")
    optipons= ["rock","paper","scissors"]
    while True:
            user_choice = input("enter rock, paper, or scissors: ").lower()
            if user_choice == "stop":
                    print_bot("okay, maybe next time!")
                    break
            if user_choice not in optipons:
                    print_bot("invalid choice! try again.")
                    continue
            bot_choice = random.choice(optipons)
            print_bot(f"I choose {bot_choice}!")
            if user_choice == bot_choice:
                    print_bot("it's a tie! try again.")
            elif (user_choice == "rock" and bot_choice == "scissors") or (user_choice == "paper" and bot_choice == "rock") or (user_choice == "scissors" and bot_choice == "paper"):
                    print_bot(f"congratulations! {user} you win!")
            else:
                    print_bot("sorry, I win! try again.")



#analyze mood function
def analyze_mood(message):
    message = message.lower()
    
    # רשימת מילים שמחות
    happy_words = ["happy", "great", "awesome", "good", "amazing", "fantastic", "love"]
    
    # רשימת מילים עצובות
    sad_words = ["sad", "bad", "terrible", "awful", "hate", "angry", "upset"]
    
    # בדיקה למילים שמחות
    for word in happy_words:
        if word in message:
            return "happy"
    
    # בדיקה למילים עצובות
    for word in sad_words:
        if word in message:
            return "sad"
    
    return "neutral"




# =============================================================================
# MAIN FUNCTION
# =============================================================================

def get_response(message, user_name):
    message_lower = message.lower()
    
    # Greeting
    if any(word in message_lower for word in ["hello", "hi", "hey"]):
        greetings = ["Hello", "Hi", "Hey there"]
        return f"{random.choice(greetings)}, {user_name}!"
    
    # How are you
    elif "how are you" in message_lower:
        return "I'm doing great! How are you?"
    
    # Bot name
    elif "your name" in message_lower or "who are you" in message_lower:
        return "I'm Bob a chatbot 🤖"
    
    # Joke
    elif "joke" in message_lower or "funny" in message_lower:
        return tell_joke()
    
    # Game
    elif "game" in message_lower or "play" in message_lower:
        return "game_menu"
    
    # Help
    elif "help" in message_lower or "commands" in message_lower:
        show_help()
        return "What else can I help with?"
    
    # Math
    elif any(op in message_lower for op in ["+", "-", "*", "/"]):
        try:
            result = eval(message)
            return f"The answer is: {result}"
        except:
            return "Sorry, I couldn't calculate that."
    
    # תוספות
    
    # Favorite color
    elif "color" in message_lower:
        return "I like blue! What's your favorite color?"
    
    # Music
    elif "music" in message_lower:
        return "I love music! What do you like to listen to?"
    
    # Sports
    elif "sport" in message_lower:
        return "I enjoy football and basketball! What about you?"
    
    # School
    elif "school" in message_lower:
        return "School can be fun sometimes 😄 What's your favorite subject?"
    
    # Food
    elif "food" in message_lower:
        return "I wish I could eat pizza 🍕 What's your favorite food?"
    
    # Mood detection
    mood = analyze_mood(message)
    
    if mood == "happy":
        return "That's awesome to hear! 😄"
    elif mood == "sad":
        return "I'm sorry to hear that... I'm here if you want to talk 💙"
    
    # Default responses
    default_responses = [
        "That's interesting!",
        "Tell me more!",
        "I see...",
        "Cool!",
        f"Thanks for sharing, {user_name}!"
    ]
    
    return random.choice(default_responses)




#לולאה ראשית

while True:
    user_input = input("Say something (HELLO / JOKE / GAME / EXIT / HELP): ")
# greeting
    if user_input.upper() == "HELLO":
        greeting()
#joke
    elif user_input.upper() == "JOKE":
        tell_joke()
#help
    elif user_input.upper() == "HELP":
        show_help()
  #games  
    elif user_input.upper() == "GAME":
        print_bot("lets play a game!")
        print_bot("choose a game: 1. Guessing Game 2. Rock Paper Scissors")
        choice = input("Enter the number of the game you want to play: ")   
        #guessing game
        if choice == "1":
            guessing_game()
        #rock paper scissors
        if choice == "2":
            rock_paper_scissors()         

    elif user_input.upper() == "EXIT":
        goodbye()
        break
    else:
        response = get_response(user_input, user)
    
        if response == "game_menu":
            print_bot("lets play a game!")
            print_bot("choose a game: 1. Guessing Game 2. Rock Paper Scissors")
            choice = input("Enter the number of the game you want to play: ")
        
            if choice == "1":
                guessing_game()
            elif choice == "2":
                rock_paper_scissors()
    
        else:
            print_bot(response)  










