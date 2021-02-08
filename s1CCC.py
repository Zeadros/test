#solving problem 1 of the senior canadian computing competition for no reason
n = int(input("Amount of obsevations : "))
t, s, o = [], [], []
for i in range(1, n+1):
    v = input("observation "+ str(i) + " time & space : ")
    t.append(int(v.split(" ")[0]))
    s.append(int(v.split(" ")[1]))
for i in range(n):
    for z in range(n):
        if(i == z):
            continue
        o.append(float(abs(s[i] - s[z]) / abs(t[i] - t[z])))
o.sort()
print("max speed = " + str(o[len(o)-1]))