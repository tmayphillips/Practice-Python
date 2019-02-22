size = int(input("What size boad would you like: "))

def create_board(size,width, height,symbol_across,symbol_down):
    space = " "
    i = 1
    print(f"{space + (symbol_across * width)}" * size)
    while i <= size:
        h = 1
        while h <= height:
            print(f"{symbol_down}" + f"{space * width}{symbol_down}" * (size))
            h += 1
        print(f"{space}{(symbol_across * width)}" * size)
        if i == size + 1:
            print(f"{space}{(symbol_across * width)}" * size)
            i += 1
        i += 1

create_board(size, 6, 3, "-", "|")