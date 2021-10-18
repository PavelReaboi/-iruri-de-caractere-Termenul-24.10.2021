x1='ABCDEFGH Z'
x2=""
for i in range(len(x1)):
	if x1[i]=='Z':
		x2+='A'
	if x1[i]!='Z' and x1[i]!=' ':
	   x2+=chr(ord(x1[i])+1)
	if x1[i]==' ':
		x2+='-'

print(x2)
