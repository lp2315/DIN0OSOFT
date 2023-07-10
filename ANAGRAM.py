# Anagram checker

def anagram():
    w = str(input("Anagram?\n")).lower()

    lw = list(w)
    rw = list(reversed(w))

    if lw == rw:
        print("Yes\n")
    else:
        print("No\n")


while True:
    anagram()
