import time

def speed_typing_test():
    text = "The sun is shining and the sky is blue."
    print("Welcome to the Speed Typing Test!")
    print("Type the following text as fast as you can:")
    print(text)
    input("Press Enter to start...")

    start_time = time.time()

    user_input = input("Type the text and press Enter: ")

    end_time = time.time()
    elapsed_time = end_time - start_time

    correct_chars = 0
    for i in range(min(len(text), len(user_input))):
        if text[i] == user_input[i]:
            correct_chars += 1

    accuracy = (correct_chars / len(text)) * 100
    words_per_minute = (len(text) / 5) / (elapsed_time / 60)

    print("\nTime taken: {:.2f} seconds".format(elapsed_time))
    print("Accuracy: {:.2f}%".format(accuracy))
    print("Words per minute: {:.2f}".format(words_per_minute))

if __name__ == "__main__":
    speed_typing_test()

