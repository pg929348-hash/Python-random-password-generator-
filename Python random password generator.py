import random
import string
print("== password generator==")
length=int( input(" enter the length of password:-"))
all_character= string.ascii_letters + string.digits + string.punctuation
password=''.join ( random.choices(all_character,k= length))
print(f" your password of{length} is :-{password}")
