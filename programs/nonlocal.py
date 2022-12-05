def enclosing():
    mssg = "enclosing"

    def local():
        nonlocal mssg
        mssg = "local"
        print(mssg)
    
    return local

e1 = enclosing()
e1()

e2 = enclosing()
e2()