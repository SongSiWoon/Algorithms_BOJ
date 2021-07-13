str = ["c=","c-","dz=","d-","lj","nj","s=","z="]
s = input()
for i in str:
    s=s.replace(i,"a")
print(len(s))
