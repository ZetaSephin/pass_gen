# Cryptographically generated random password

import random
import string

# Start Passgen

print("Please input a max-character limit for required password")
size = input()
try:
    val = int(size)
except ValueError:
    print("That's not an int!")

else:
    print("Input accepted, Now generating password...")

# Generate the Password
def pass_gen():

    uletters = string.ascii_uppercase
    lletters = string.ascii_lowercase
    digits = string.digits
    punctuation = string.punctuation
    chars = (uletters, lletters, digits, punctuation)
    p = ''

    for i in range(int(size)//4):

        p += ''.join(random.SystemRandom().choices(uletters, k=1))
        p += ''.join(random.SystemRandom().choices(lletters, k=1))
        p += ''.join(random.SystemRandom().choices(digits, k=1))
        p += ''.join(random.SystemRandom().choices(punctuation, k=1))
    print("Your randomly generated password is: " + p)

#Run the function
pass_gen()