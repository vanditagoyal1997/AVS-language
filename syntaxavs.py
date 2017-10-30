def StartEnd(line):
	if 'START' not in line[0] or 'END' not in line[count_lines-1]:
		return False
	else:
		return True

def isComment(s):
	if s[0]=="*":
		if s[len(s)-1]=="*":
			return True
		else:
			return False
	else:
		return True
def checkVar(s):
		if s in keyword:
			return False
		elif s[0].isalpha()==False:
			if s[0]!="_" :
				return False
		else:
			for i in s:
				if i in ['#','@','!','/','$','>','<']:
					return False 
			return True
def isDefinition(s):
	if '=' in s:
		g=s.split('=')
		d=checkVar(g[0])
		return d
	else:
		return True
def isFunc(s):
	if "def_func" in s:
		if s.count('<')==1 and s.count('>')==1:
			lfunc=s.split(" ")
			lidfunc=lfunc[1].split("<")
			sidfunc=lidfunc[0]
			if sidfunc.isalpha():
				if sidfunc.isupper()==False:
					return False
			else:
				if sidfunc[0].isalpha():
					for i in sidfunc:
						if i.isalpha():
							if i.isupper()==False:
								return False
						else:
							if i not in ['#','@','!','/','$']:
								return False
				else:
					return False
			spara=lidfunc[1]
			if ">" in spara:
				spara=spara.replace(">","")
				spara=spara.remove("")
			lpara=spara.split(",")
			if len(lpara)!=0:
				for i in range(len(lpara)):
					d=checkvar(lpara[i])
					if d==False:
						return False
				if i==(len(lpara)-1):
					functionlist.append(sidfunc)
					return True
			else:
				functionlist.append(sidfunc)
				return True
			
		else:
			return False
	else:
		return True

			
def isDisplay(s):
	if s not in functionlist:
		if s[0]=='D' :
			if s[1]=='I':
			 	if s[2]=='S':
					if s[3]!='P':
						if s[4]=='L':
							if s[5]=='A': 
								if s[6]=='Y':  
									if s[7]==':':
										if s[8]=='['and s[9]=='[':
											if s[len(s)-2]==']' and s[len(s)-1]==']':
												return True
		else:
			return False
	else: 
		return True
				
			

def isRead(s):
	lexp=s.split("=")
	if checkVar(lexp[0]):
		if lexp[1][0]=='R':
			if lexp[1][1]=='E':
				if lexp[1][2]=='A':
					if lexp[1][3]=='D':
						if lexp[1][4]==':':
							if lexp[1][5]=='['and lexp[1][6]=='[':
								if lexp[1][len(lexp[1])-2]==']' and lexp[1][len(lexp[1])-1]==']':
									return True
	else:
		return False
	
	

def incomingprec(s):
	if s=='+' or s=='-':
		return 3
	elif s=='*' or s=='/':
		return 5
	elif s=='^':
		return 8
	elif s=='<=' or s=='>=' or s=='>' or s=='<':
		return 1
def instackprec(s):
	if s=='+' or s=='-':
		return 4
	elif s=='*' or s=='/':
		return 6
	elif s=='^':
		return 7
	elif s=='<=' or s=='>=' or s=='>' or s=='<':
		return 2
	
				
def exprchecker(s):
    stack1=[]
    stack2=[]
    
    i=0
    while(i<len(s)):
        if s[i] in operation:
            while len(stack2)!=0 and incomingprec(s[i])>instackprec(stack2[-1]):
                stack2.pop()
                if len(stack1)>=2:
                    stack1.pop()
                else:
                    return False
            i=i+1   
            stack2.append(s[i])
        else:
            num=""
            while i<len(s) and s[i] not in operation :
                num=num+s[i]
                i=i+1;
            stack1.append(num)
           
    while len(stack2)!=0 and len(stack1)!=0:
        stack2.pop()
        stack1.pop()
    if len(stack1)!=1 or len(stack2)!=0:
        return False

def isLoop(s):
		if "REPEAT_TILL" in s:
				lexp=s.split("<")
				lexp[1]=lexp[1].replace(">","")
				if "" in lexp:
                                        lexp=lexp.remove("")
				if len(lexp)>1:
					d=exprchecker(lexp[1])
					if d:
						return True
					else:
						return False
				else:
					return False
		else:
			return True	
def isCondition(s):
		if "EITHER" in s or "OR" in s:
				lexp=s.split("<")
				lexp[1]=lexp[1].replace(">","")
				if "" in lexp:
                                        lexp=lexp.remove("")
				if len(lexp)>1:
					d=exprchecker(lexp[1])
					if d:
						return True
					else:
						return False
				else:
					return False
		else:
			return True			

keyword=["EITHER","DISPLAY","READ","OR","REPEAT_TILL"]
operation=["+","/","-","*",">=","<=","<",">","^"]
functionlist=[]
filename=input("enter file name:")
f1= open(filename,'r')
l=f1.readlines()

#to check START and END
start=True
comment=True
definition=True
userfunc=True
disp=True
start=StartEnd(l)
if not start:
	print ("Invalid Code: Check START and END" )

i=1
for i in range(1,len(l):
	l[i]=l[i].strip()
	definition=isDefinition(l[i])
	comment1=isComment(l[i])
	userfunc=isFunc(l[i])
	display=isDisplay(l[i])
	read=isRead(l[i])
	loop=isLoop(l[i])
	condition=isCondition(l[i])
	#to check syntax of COMMENT
	
	if not comment:
		print ("Invalid Code: Check comment syntax in line:",i )


	#to check syntax of DEFINITION
	
	if not definition:
		print ("Invalid Code: Check definition syntax in line:",i )


	#to check syntax of USER DEFINED FUNCTION
	
	if not userfunc:
		print ("Invalid Code: Check function syntax in line:",i )


	#to check syntax of DISPLAY FUNCTION


	if not userfunc:
		print ("Invalid Code: Check display function syntax in line:",i )
	
	#to check syntax of READ FUNCTION
	
	if not read:
		print ("Invalid Code: Check read syntax in line:",i )
	
	#to check syntax of LOOP FUNCTION
	
	if not loop:
		print ("Invalid Code: Check loop syntax in line:",i )
	
	#to check syntax of CONDITION FUNCTION
	
	if not condition:
		print ("Invalid Code: Check condition syntax in line:",i )




