import sys,ast

test={}
passData={}
test[1]=1
test[2]=2
passData[0]=test
print test
#{1:1,2:2}
test1=ast.literal_eval(str(passData[0]))
print test1
