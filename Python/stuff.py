input = open("/home/harryl/Downloads/wordlist", "r").readlines()
output = open("/home/harryl/Downloads/wrdlst", "a+")

for i in input:
    for l in input:
        for m in input:
            i = i.replace("\n", "")
            l = l.replace("\n", "")
            m = m.replace("\n", "")
            txt = i + l + m
            output.write(txt + "\n")
            txt = ""
