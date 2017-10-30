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
def isFunc(s):
	lfunc=s.split(" ")
	if lfunc[0]=='func':
		if s.count('<')==1 and s.count('>')==1:
			lidfunc=lfunc[1].split("<")
			sidfunc=lidfunc[0]
			if sidfunc[0] not in keyword:
				if sidfunc[0].isalpha():
					for i in sidfunc:
						if i.isalpha():
							if i.isupper()==False:
								return False
						else:
							if i not in ['#','@','!','/','$']:
								return False
					symboltab["funcid"].append(sidfunc)
					return True
				else:
					return False
			else:
				return False
keyword=["EITHER","DISPLAY","READ","OR","REPEAT_TILL","func"]
operation=["+","/","-","*",">=","<=","<",">","^"]
functionlist=[]
filename=input("enter file name:")
f1= open(filename,'r')
l=f1.readlines()

#to check START and END

word_list=""

symboltab={"start":["START"],
"end":["END"],\
"comment":[],\
"funcid":[],\
"newline":["\n"],\
"tab":["\t"],\
"op":["+","-","*","/","^","<",">","%"],\
"assop":["="],\
"space":[" "],\
"invcom":["'",'"'],\
"lpar":["(",")"],\
"fpar":["[","]"],\
"loop":["REPEAT_TILL"],\
"conditional":["EITHER","OR"],\
"ip":["READ"],\
"output":["DISPLAY"],\
"var":[]}	

i=0
for i in range(0,len(l)):
	if l[i].strip()=="START":
		word_list+="#start"
	elif l[i].strip()=="END":
		word_list+=" #end"
	else:
		if "func" in l[i]:
			d=isFunc(l[i])
			if d:
				word_list+=" #func #funcid"
		
		else:
			j=0
			while (j<len(l[i])):
				if l[i][j]=="=":
					word_list+=" #assop"
					j=j+1
				elif l[i][j] in operation:
					word_list+=" #op"
					j=j+1
				
				elif l[i][j]=='R':
					if l[i][j+1]=='E':
						if l[i][j+2]=='A':
							if l[i][j+3]=='D':
								word_list+=" #ip"
								j=j+4
				elif l[i][j]=='D':
					if l[i][j+1]=='I':
						if l[i][j+2]=='S':
							if l[i][j+3]=='P':
								if l[i][j+4]=='L':
									if l[i][j+5]=='A':
										if l[i][j+6]=='Y':
											word_list+=" #output"
											j=j+7
				elif l[i][j]=='E':
					if l[i][j+1]=='I':
						if l[i][j+2]=='T':
							if l[i][j+3]=='H':
								if l[i][j+4]=='E':
									if l[i][j+5]=='R':
										word_list+=" #conditional"
										j=j+6
				elif l[i][j]=='R':
					if l[i][j+1]=='E':
						if l[i][j+2]=='P':
							if l[i][j+3]=='E':
								if l[i][j+4]=='A':
									if l[i][j+5]=='T':
										if l[i][j+6]=='_':
											if l[i][j+7]=='T':
												if l[i][j+8]=='I':
													if l[i][j+9]=='L':
														if l[i][j+10]=='L':
															word_list+=" #loop"
															j=j+11
				elif l[i][j]=='O':
					if l[i][j+1]=='R':
						word_list+=" #conditional"
						j=j+2
						
				elif l[i][j].isalpha():
					d=checkVar(l[i][j])
					if d:
						symboltab["var"].append(l[i][j])
						word_list+=" #var"
					j=j+1
				elif l[i][j].isdigit():
					word_list+=" #digit"
					j=j+1
				
				elif l[i][j]=="[" or l[i][j]=="]":
					word_list+=" #fpar"
					j=j+1
				elif l[i][j]==",":
					word_list+=" #comma"
					j=j+1
				elif l[i][j]=="\n":
					word_list+=" #newline"
					j=j+1
				elif l[i][j]=="\t":
					word_list+=" #tab"
					j=j+1
				else:
					break
	
						


print(word_list)

for k, v in symboltab.items():
    print(k, v)
            
               
