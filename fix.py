new = ""
with open("./sc.txt", "r") as f:
   for l in f.readlines():
      new += l[:-1] + " ";

with open("./sc2.txt", "w") as f:
   f.write(new);