import random
import string


list = random.sample(range(10000), 10)


password = random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + str(random.choice(list)) + random.choice(string.punctuation)


print(password)