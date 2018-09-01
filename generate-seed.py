import random
import string

print(''.join(random.choices(string.ascii_uppercase + "9", k=81)))
