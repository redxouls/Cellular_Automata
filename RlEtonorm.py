k = input()
f = open(k,"r").read()
print(f)
output = input("Ouput file name :") + ".txt"

with open(output,"w") as text_file:
    temp =""
    for i in range(len(f)):
        try:
            int(f[i])
            temp += f[i]
        except ValueError:
            print("GG",temp)
            if temp =="":
                temp="1"
            if f[i] == "b":
                print("b")
                temp = int(temp)
                a = "O"*temp
                print(a)
                text_file.write(a)
            elif f[i]== "o":
                temp = int(temp)
                a = "."*temp
                text_file.write(a)
            elif f[i] =="$":
                text_file.write("\n")
            elif f[i] =="\n":
                continue
            temp = ''
            