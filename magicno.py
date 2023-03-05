secretno =  777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

x = int(input())

while x != secretno:
    print ("Ha ha! You're stuck in my loop!")
    x = int(input())

    if x == secretno:
        print ("Well done, muggle! You are free now.")