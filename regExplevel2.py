0|1|2|3|4|5|6|7|8|9 # both same
[0123456789]# both same
[0-9] # this same
\d #first char only
[]
() 
{n} #eg \d{8} ==\d\d\d\d\d\d\d\d , eg={4}
[A-Za-z0-9]
{0,}==*
{1,}==+
{0,1}==?
\d==[0-9]
\w==[A-Za-z0-9]
\S==[^]


import re
p="080-41400404"  #gives all char except new line #like read first line
#o=re.compile("cat",re.I)
#n="rat"
data= """Our old number was 080-65655005
New Number is080-41400404"""
#p= "cat"
var=re.search(p,data,re.I|re.DOTALL) #count gives no.of ax subsiute req
print(var)
#if var:
 	#print("Pattern Found",var.start(),var.end(),var.span(),var.group())
#else:
 	#print("Pattern Not Found")
