def checkVar(s):
		if s in keyword:
			return False
		elif s[0].isalpha():
			if s[0].islower()==False:
				return False
		elif s[0].isalpha()==False:
			if s[0]!="_" :
				return False
		else:
			for i in s:
				if i in ['#','@','!','/','$','>','<']:
					return False 
		return True
filename=input("enter file name:")
f1= open(filename,'r')
l=f1.readlines()
keyword=["EITHER","DISPLAY","READ","OR","REPEAT_TILL","func"]
vartype={"int":[],"float":[],"string":[]}
k=0
for i in l:
	k=k+1
	v1=""
	v2=""
	if "=" in i:
		i=i.strip()
		s=i.split("=")
		if "+" in s[1] or "-" in s[1] or "/" in s[1] or "*" in s[1]:
			d=checkVar(s[0])
			if d:
				if "+" in s[1]:
					f=s[1].split("+")
				elif "-" in s[1]:
					f=s[1].split("-")
				elif "*" in s[1]:
					f=s[1].split("*")
				elif "/" in s[1]:
					f=s[1].split("/")
				for i in vartype.keys():
					for j in vartype[i]:
						if j==f[0]:
							v1=i
							break
				for i in vartype.keys():
					for j in vartype[i]:
						if j==f[1]:
							v2=i
							break
				if not v1:
					if "'" in f[0]:
						v1="string"
					elif "." in f[0]:
						v1="float"
					elif f[0].isdigit():
						v1="int"
					else:
						print("variable not defined at line:",k)
						break
				if not v2:
					if "'" in f[1]:
						v2="string"
					elif "." in f[1]:
						v2="float"
					elif f[1].isdigit():
						v2="int"
					else:
						print("variable not defined at line:",k)
						break
				if v1==v2:
					vartype[v1].append(s[0])
				elif v1=="float" and v2=="int":
					vartype[v1].append(s[0])
				elif v1=="int" and v2=="float":
					print("correct syntax")
					vartype[v2].append(s[0])
				else:
					print("variable type mismatch at line:",k)
					break
			else:
				print("variable not defined properly at line:",k)
				break
			
				
				
				
			
			
		else:
			if "READ" not in s[1]:
				d=checkVar(s[0])
				if d:
					for i in vartype.keys():
						for j in vartype[i]:
							if j==s[0]:
								vartype[i].remove(s[0])
					if "'" in s[1]:
						vartype["string"].append(s[0])
					elif "." in s[1]:
						vartype["float"].append(s[0])
					elif s[1].isdigit():
						vartype["int"].append(s[0])
					else:
						break
				else:
					print("variable not defined properly at line:",k)
					break
if k==len(l):
	print("correct syntax")	
		

