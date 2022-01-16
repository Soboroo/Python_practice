import re
for i in range(int(input())):print(sum(map(lambda x:len(x)*(len(x)+1)//2,re.findall("O+",input()))))