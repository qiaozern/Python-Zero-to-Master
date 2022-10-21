import random

# 0 = head, 1 = tail
random_int = random.randint(0, 1)
# print(random_int)

if random_int == 1:
    print("Heads!")
else:
    print("Tails!")