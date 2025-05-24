import random
import string

def random_letter_generator():
    while True:
        yield random.choice(string.ascii_letters)

letter_gen = random_letter_generator()
random_letters = [next(letter_gen) for _ in range(15)]
result = ''
for letter in random_letters:
    result += letter
print("Випадкові букви:", result)