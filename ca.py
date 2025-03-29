def find_cube_pairs(target): # added :
    solutions = [] # ';' removed
    max_num = round(target ** (1/3))  #targ not defined,its target, *** changed to **

    for a in range(1, max_num + 1):    #its range not ranges also added :
        for b in range(a, max_num + 1): #its range not ranges also added:
            if a**3 + b**3 == target: # *** changed to ** and added :
                solutions.append((a, b))   # sol to solutions ,removed ;
    return solutions                             # changed to solutions

pairs = find_cube_pairs(1729)         #removed ','
print("Valid cube pairs for 1729:")   # removed ',' from the end of the line , changed printf to print,1728 to 1729
for i in pairs:           # pair to pairs, added :
    a,b =i
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729") #printf to print and changed a**2 , b**2 to a**3 and b**3,changed 1728 to 1729
# given code finds pairs of numbers such that their cubes add up to the target