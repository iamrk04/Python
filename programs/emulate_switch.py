if __name__ == "__main__":
    mapping = {
        1: lambda: print("You selected 1, great"),
        2: lambda: print("You selected 2, wow"),
        3: lambda: print("You selected 3, cool")
    }

    print("Choose 1, 2 or 3")
    i = int(input())

    # if i == 1:
    #     print("You selected 1, great")
    # elif i == 2:
    #     print("You selected 2, wow")
    # elif i == 3:
    #     print("You selected 3, cool")
    # else:
    #     print("You have selected the wrong option")

    try:
        statement = mapping[i]
    except KeyError:
        print("You have selected the wrong option")
    else:
        statement()
