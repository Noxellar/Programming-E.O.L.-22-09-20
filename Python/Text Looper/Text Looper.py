word = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K"]

file = open("out.txt", "a+")

for a in word:
    for b in word:
        for c in word:
            for d in word:
                for e in word:
                    for f in word:
                        for g in word:
                            for h in word:
                                for i in word:
                                    for j in word:
                                        list = a + b + c + d + e + f + g + h + i + j

                                        file.write(list + "\n")
