START
a=2
REPEAT_TILL(a==1)[[
a=a-1
]]
EITHER(a==1)[[
b=0
]]
OR[[
b='hi'
]]
func HI(b)[[
s=1
]]
DISPLAY[['Good Job']]
v=READ[['%d']]
END
