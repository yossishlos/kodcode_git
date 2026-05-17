import random
cheked_letters = []
number_of_attempts = 10
words_list = [
"Sky",
"Cloud",
"Key",
"Jump",
"Fast",
"Blue",
"Book",
"Tree",
"Wind",
"Gold"
]
word = random.choice(words_list).lower()
status_word = len(word) * "#"
# print(word)

while True:
    print(f"        {status_word}")

    print(f"words you cheked: {cheked_letters}")

    print(f"attemps left: {number_of_attempts}")

    if status_word == word:
        print("good")
        break

    user_input = input("pleasa enter a cher: ")
    
    if number_of_attempts == 0:
        print("The attempts are over.")
        break

    if user_input in word:
        for i, cher in enumerate(word):
            if cher == user_input:
                tmp = list(status_word)

                tmp[i] = user_input

                status_word = "".join(tmp)

    else:        
        cheked_letters.append(user_input)
        
        number_of_attempts -= 1
                
