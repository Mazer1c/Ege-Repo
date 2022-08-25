print ("x y z w f")
for x in range (2):
    for y in range (2):
        for z in range (2):
            for w in range (2):
                f=((x<=y)==(y<=z)) and (y or w)
                    #Переписывай пример из условия в программу,используя знаки ниже.
                    # * - "и" (and)
                    # + - "или" (or)
                    # ≡ - "безусловно равно" (==)
                    # -> - cледование (<=)
                if f==1: #Если функция в условии ложна.
                    print(x,y,z,w)