f = open('expdata.txt','r')
#input file is the coded locations as string, 12321123...
#on a new line for each subject
s = 1
for line in f.readlines():
    t = list(line) #convert to list
    t.pop() #delete end character
    t = t[1:] #ignore first location (placement of mouse)
    entries = len(t)
    v = 0 #counter for number of unique triads
    for i in range(len(t)-2):
        if t[i] != t[i+1] and t[i] != t[i+2] and t[i+1] != t[i+2]:
            v += 1
    altper = (v / (len(t)-2))*100
    print("Subject", s, "| unique triads:", v,  \
        "| arm entries:", entries, "| alteration percentage:", altper) 
    s += 1
