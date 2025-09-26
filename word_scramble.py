import random
import time

words = {
    "easy": ["cat", "dog", "book", "sun", "pen"],
    "medium": ["python", "banana", "laptop", "jumble", "window"],
    "hard": ["developer", "algorithm", "scramble", "operation", "cryptography"]
}

def scramble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

def guess_word(original_word, scrambled):
    attempts = 3
    print(f"\nScrambled word: {scrambled}")
    want_hint = input("Do you want a hint? (yes/no): ").strip().lower()
    if want_hint == "yes":
        time.sleep(2) 
        print("Hint: The word starts with", original_word[0])

    while attempts > 0:
        guess = input("Your guess (type 'exit' to quit): ").strip().lower()

        if guess == "exit":
            print(f"The correct word was: {original_word}")
            return "exit", 0

        if guess == original_word:
            print("✅ Correct!\n")
            return "correct", 1
        else:
            attempts -= 1
            print(f"❌ Wrong! Attempts left: {attempts}")

    print(f"😢 The correct word was: {original_word}")
    return "wrong", 0

def play_game():
    print("\n🎮 Welcome to the Word Scramble Game!")
    score = 0

    while True:
        difficulty = input("Choose difficulty (easy / medium / hard): ").strip().lower()
        if difficulty not in words:
            print("Invalid difficulty. Please choose again.")
            continue

        original_word = random.choice(words[difficulty])
        scrambled = scramble_word(original_word)
        while scrambled == original_word:
            scrambled = scramble_word(original_word)

        result, point = guess_word(original_word, scrambled)
        score += point

        if result == "exit":
            break

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break

    print(f"\n🎉 Thanks for playing! Your final score: {score}")

# Start the game
play_game()
