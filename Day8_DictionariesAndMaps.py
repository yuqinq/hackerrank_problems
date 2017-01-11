n = int(input())
phonebook = []
for i in range(n):
    phonebook.append(input().split())
dic = {phonebook[i][0]: phonebook[i][1] for i in range(n)}
while True:
    try:
        name = input()
        if name in dic:
            print ("%s=%s"%(name,dic[name]))
        else:
            print ("Not found")
    except:
        break   
