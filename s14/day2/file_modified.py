__author__ = "Steven Lee"

f = open("yesterday2", "r", encoding="utf-8")
f_new = open("yesterday2.bak", "w", encoding="utf-8")

for line in f:
    if "肆意的快乐" in line:
        line = line.replace("肆意的快乐等我去享受", "肆意的快乐等着stevenlee去享受")
    f_new.write(line)

f.close()
f_new.close()
