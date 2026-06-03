import random

# 🌸 Little Companion Bot

name = input("🌸 Hello! What's your name?\n> ").strip().title()

print(f"\nBot: Nice to meet you, {name} 🌷")
print(f"Bot: Welcome, {name}! I'm your Little Companion.\n")

message_count = 0
mood_count = 0
last_mood = None


def menu():
    print("\n🌱 What would you like to do today?")
    print("1. Have a chat 💬")
    print("2. Mood Check-In 😊")
    print("3. Motivation ⭐")
    print("4. Study Tip 📚")
    print("5. Fun Fact 🌍")
    print("6. My Stats 📊")
    print("7. Exit 👋")


menu()

while True:
    choice = input(f"\n{name}: ").lower().strip()
    message_count += 1

    # CHAT
    if choice in ["1", "chat"]:

        print(f"\nBot: How has your day been so far, {name}? 😊")
        day = input("> ").lower()

        if any(word in day for word in ["good", "great", "nice", "amazing"]):
            print("Bot: That's wonderful to hear! 🌸")
            print("Bot: Tell me one good thing that happened today.")
            input("> ")
            print("Bot: Aww, that sounds lovely! ✨")

        elif any(word in day for word in ["bad", "sad", "terrible", "stress"]):
            print("Bot: 🌿 I'm sorry it's been tough.")
            print("Bot: Remember, one difficult day doesn't define your journey.")

        else:
            print("Bot: 💙 Thanks for sharing that with me.")

        menu()

    # MOOD CHECK-IN
    elif choice in ["2", "mood"]:

        mood = input(
            "\nBot: How are you feeling today?\n"
            "(happy / sad / tired / stressed / excited)\n> "
        ).lower()

        mood_count += 1
        last_mood = mood

        if mood == "happy":
            print("Bot: ☀️ Keep spreading that positive energy!")

        elif mood == "sad":
            print("Bot: 🌷 Be gentle with yourself today.")

        elif mood == "tired":
            print("Bot: 🌙 Don't forget to rest and recharge.")

        elif mood == "stressed":
            print("Bot: 🌿 One small step at a time.")

        elif mood == "excited":
            print("Bot: 🎉 I love that energy!")

        else:
            print("Bot: 💙 Thank you for sharing.")

        talk = input("\nBot: Would you like to talk a little more about it? (yes/no)\n> ").lower()

        if talk == "yes":
            print("Bot: Sometimes writing down your thoughts helps clear your mind ✨")

        menu()

    # MOTIVATION
    elif choice in ["3", "motivation", "motivate"]:

        quotes = [
            "⭐ Small progress is still progress.",
            "⭐ Consistency beats perfection.",
            "⭐ Keep going — you're doing better than you think.",
            "⭐ Start where you are. Use what you have.",
            "⭐ Every expert was once a beginner."
        ]

        while True:
            print("\nBot:", random.choice(quotes))

            more = input(
                "\nBot: Would you like another motivational quote? (yes/no)\n> "
            ).lower()

            if more != "yes":
                break

        print(f"\nBot: Alright {name} 🌸")
        menu()

    # STUDY TIP
    elif choice in ["4", "study", "study tip"]:

        tips = [
            "📚 Use active recall instead of rereading notes.",
            "📚 Study for 25 minutes, then take a 5-minute break.",
            "📚 Teach a topic to yourself out loud.",
            "📚 Remove distractions before starting.",
            "📚 Focus on understanding before memorizing."
        ]

        while True:
            print("\nBot:", random.choice(tips))

            more = input(
                "\nBot: Would you like another study tip? (yes/no)\n> "
            ).lower()

            if more != "yes":
                break

        print(f"\nBot: You've got this, {name}! 📖")
        menu()

    # FUN FACT
    elif choice in ["5", "fact", "fun fact"]:

        facts = [
            "🐙 Octopuses have three hearts.",
            "🍯 Honey never spoils.",
            "🦒 A giraffe's tongue can be about 50 cm long.",
            "🌍 Earth is the only known planet with life.",
            "🧠 Your brain uses about 20% of your body's energy."
        ]

        while True:
            print("\nBot:", random.choice(facts))

            more = input(
                "\nBot: Would you like another fun fact? (yes/no)\n> "
            ).lower()

            if more != "yes":
                break

        print(f"\nBot: Hope you learned something new today, {name}! 🌍")
        menu()

    # STATS
    elif choice in ["6", "stats"]:

        print("\n📊 Session Stats")
        print(f"Messages exchanged: {message_count}")
        print(f"Mood check-ins: {mood_count}")

        if last_mood:
            print(f"Most recent mood: {last_mood}")
        else:
            print("Most recent mood: None")

        menu()

    # EXIT
    elif choice in ["7", "exit", "bye", "quit"]:

        print(f"\nBot: It was nice talking to you, {name}! 🌸")
        print("Bot: Take care and have a lovely day 👋")
        break

    # INVALID INPUT
    else:
        print("\nBot: 🤔 I didn't quite understand that.")
        print("Bot: Please choose a number from 1 to 7.")
        menu()
