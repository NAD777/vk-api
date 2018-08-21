a = []
with open('login.txt') as f:
    for line in f:
        a = list(map(str,line.split(';')))
        print(a)
