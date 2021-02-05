import matplotlib.pyplot as plt

# Get Data
x = []
y = []
f = open("./out/206full.csv","r")
l = f.readline()
while l != "":
    d = l.split(",")
    x.append(float(d[0]))
    y.append(float(d[1]))
    l = f.readline()
f.close()
plt.plot(x, y)
plt.show()
