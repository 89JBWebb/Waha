imp = input("> ")
while imp != "quit":
    print(imp)

    si = imp.split()
    x = imp.find(" ")
    y = imp.rfind(" ")
    print(imp[:x])
    print(imp[y+1:])

    if si[0].upper() == "CREATE":
        si[0] 
        print("create!")

    imp = input("> ")

#commands
#   create a unit
#       outfit the unit
#   have a unit attack another

