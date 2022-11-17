# Outputs a string n amount
# of times to a txt-file


out_text = "Output test"
out_file = "file.txt"

with open(out_file, "w") as f:
    n = input("Amount of times?")
    for i in range(int(n)):
        f.write(str(out_text))
