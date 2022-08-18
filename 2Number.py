print ("x y z w")
for x in range (0,2):
    for y in range (0,2):
        for z in range (0,2):
            for w in range (0,2):
                if not ((z and y) or ((x<=z)==(y<=w))):
                    #Cверху пример "(((z and y) or ((x<=z)==(y<=w)))"
                    #Переписывай пример из условия в программу,используя знаки ниже.
                    # * - "и" (and)
                    # + - "или" (or)
                    # ≡ - "безусловно равно" (==)
                    # -> - cледование (<=) ????
                    print(x,y,z,w)