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
funcname={}
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
			
	elif "func" in i:
		i=i.strip()
		s=i.split(" ")
		c=s[1]
		c=c.strip(")[[")
		w=c.split("(")
		v=w[1].split(",")
		o=len(v)
		lfuncvar=[o]
		for p in v:
			for i in vartype.keys():
				for j in vartype[i]:
					if j==p:
						v1=i
						lfuncvar.append(v1)
						break 
			if not v1:
				print("variable used is not defined")
				exit()
		if w[0].isalpha():
				if w[0].isupper()==False:
					print("function name is not correctly defined at line:",k)
					break
				else:
					funcname[w[0]]=lfuncvar
		else:
			if w[0][0].isalpha():
				for i in sidfunc:
					if i.isalpha():
						if i.isupper()==False:
							print("function name is not correctly defined at line:",k)
							break
						else:
							funcname[w[0]]=lfuncvar
					else:
						if i not in ['#','@','!','/','$']:
							print("function name is not correctly defined at line:",k)
							break
						else:
							funcname[w[0]]=lfuncvar
			else:
				print("function name is not correctly defined at line:",k)
				break
		print(funcname)
	else:
		if "EITHER" not in i and "DISPLAY" not in i and "READ" not in i and "OR" not in i and "REPEAT_TILL" not in i and "START" not in i and "END" not in i and "]]" not in i:
			i=i.strip()
			c=i
			c=c.strip(")")
			w=c.split("(")
			if w[0] in funcname:
				v=w[1].split(",")
				o=len(v)
				lfuncvar=[o]
				for p in v:
					for i in vartype.keys():
						for j in vartype[i]:
							if j==p:
								v1=i
								lfuncvar.append(v1)
								break 
					if not v1:
						print("variable used is not defined at line:",k)
						exit()
				print (lfuncvar)
				if lfuncvar!=funcname[w[0]]:
					print("function not called properly at line:",k)
					break
			else:
				print("function not defined at line:",k)
				break
				
if k==len(l):
	print("correct syntax")
	print(vartype)
	print(funcname)	
						
