i = open("E:\Files\leetcode_sol\lib\python\data.txt", "r", encoding="utf-8")
o = open("E:\Files\leetcode_sol\lib\python\data2.txt", "w", encoding="utf-8")
l = set()
for j in i:
    l.add(j.split("Мне нравится\\")[1].split("(")[0].split(".")[0])

for i in l:
    o.write(i)
    o.write("\n")
