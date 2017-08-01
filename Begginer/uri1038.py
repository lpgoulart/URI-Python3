line = input().split(" ")
var1, var2 = line

price = [ 0, 4.0, 4.5, 5.0, 2.0, 1.5 ]

out =  ( ( price[int(var1)] )* int(var2) ) 

print  ("Total: R$ %.2f"  %out)
