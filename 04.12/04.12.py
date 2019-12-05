#00-09 #10
#11-19 #9
#22-29 #8

#000-099 #10+9+8...
#111-199 #9+8+7...
#222-299 #8+7+6...

#For the duplicates

#00-09 #1
#11-19 #1
# etc


#000-099 # 19 (10 + 10 - 1)
#-> 000-009 # 10
#0000-0999
#->0000-0099 #100
#->0000-0009 #10


#111-199


#Input range is 272091 to 815432

def sum_of_descending_to_one(n):
    return (n/2) * (n+1)

#So after seeing the input range I gave up on a mathematical solution and instead bruteforced it...
