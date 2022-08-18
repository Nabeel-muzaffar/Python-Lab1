
def makeIcecream(flavour , sauce ):
    combination = 0
    print(f"{flavour} ice cream sundae with {sauce} sauce ")
    return  combination + 1 
    





flavors = ["vanilla", "chocolate", "strawberry", "pistacchio"]
sauces = ["caramel", "butterscotch", "chocolate"]
totalCombination = 0

for fl in flavors:
    # print(fl)
    for sc in sauces:
        # print(sc)
        com = makeIcecream(fl , sc )
        totalCombination += com
    


print(f"Total combination : {totalCombination}")
