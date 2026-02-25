import re

"""
name = input("name please")

s1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', name)
s2 = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s1)

print(s2.lower())
"""

word = input("Enter word : ")

for char in word:
    if char.isupper():
        print("_", char.lower(), sep="", end="")
    else:
        print(char, end="")
print("")