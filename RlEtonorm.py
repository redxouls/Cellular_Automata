k = input() + ".txt"
f = open(k,"r").read()
output = input("Ouput file name :") + ".txt"
ma = 0
with open(output,"w") as text_file:
    temp =""
    count = 0
    for i in range(len(f)):
        try:
            int(f[i])
            temp += f[i]
        except ValueError:
            #if temp != '':
                #print(temp)
            if temp =="":
                temp="1"
            if f[i] == "b":
                temp = int(temp)
                a = "."*temp
                text_file.write(a)
                if temp > ma :
                    ma = temp
            elif f[i]== "o":
                temp = int(temp)
                a = "O"*temp
                text_file.write(a)
                if temp > ma :
                    ma = temp
            elif f[i] =="$":
                count += 1
                #print("newline")
                text_file.write("\n")
            elif f[i] =="\n":
                temp = ''
                continue
            if temp == 1123:
                tempp = ''
                for k in range(-10,10):
                    tempp += f[i+k]
                
                print(tempp)
            temp = ''
print(count,ma)