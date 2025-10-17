import sys

number = 5
divisor = 1

if divisor>0 and number>divisor:
    res = number/divisor
    sys.stdout.write( "\nResultado: "+str(res) )
else:
    sys.stdout.write( "\nDivisão não permitida." )


#Meu nome 

v = "aeiouy" 
c= "bcdfghjklmnpqrstvwx"
e = "\x20\x0A"
#sys.stdout.write(c[11]+v[5]+e[0]+c[1]+v[3]+c[2]+v[1])
sys.stdout.write(v[5]+v[0]+c[14]+c[9]+v[2]+c[10])

