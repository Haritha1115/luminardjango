txt = "ABCDABCDABCD"
dict = {}
for letter in txt:  # using this we can split ...without using split()
    print(letter)
for letter in txt:
    if letter not in dict:
        dict[letter] = 1
    else:
        print("\n",letter," is the first recursive letter")
        break