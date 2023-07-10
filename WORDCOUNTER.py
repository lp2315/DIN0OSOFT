import os

# Parameters

mapp = "D:/bib/"
max_count = 1000
min_count = 20


# Word counter

def word_count(text):
    count = dict()                                  # word + count as dictionary

    words = text.split()

    for line in words:
        line = line.strip()                         # formatting
        line = line.lower()
        words = line.split(" ")

        for word in words:                          # iterate over each word
            if word in count:                       # check if word is already in dict
                count[word] = count[word] + 1
            else:
                count[word] = 1

    return count


# Text-file reader

for textfile in os.listdir(mapp):

    print("\n")

    if textfile.endswith(".txt") and textfile != "test.txt":

        print("Words that appear " + str(min_count) + "-" + str(max_count) + " times in <" + textfile + ">:\n")

        with open((mapp + textfile), "r", encoding = "utf-8") as f:

            textmass = word_count(f.read())

            t_sorted = sorted(textmass.items(), key = lambda x: x[1], reverse = True)

            for i in t_sorted:

                if max_count > i[1] > min_count:
                    print(i[0], i[1])

    else:

        pass


