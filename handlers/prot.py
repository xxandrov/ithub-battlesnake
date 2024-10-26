def prot_backwards(my_headx: int, my_heady: int, my_neckx: int, my_necky: int, sides: dict):
    if my_neckx < my_headx:  # Neck is left of head, don't move left
        sides["left"] = False

    elif my_neckx > my_headx:  # Neck is right of head, don't move right
        sides["right"] = False

    elif my_necky < my_heady:  # Neck is below head, don't move down
        sides["down"] = False

    elif my_necky > my_heady:  # Neck is above head, don't move up
        sides["up"] = False

def prot_border(my_headx: int, my_heady: int, width: int, height: int, sides: dict):
    if my_headx >= width:
        sides["right"] = False
    if my_headx <= 0:
        sides["left"] = False
    if my_heady >= height:
        sides["up"] = False
    if my_heady <= 0:
        sides["down"] = False

def prot_snakes_body(my_headx: int, my_heady: int, yourself: list, sides: dict):
    i_for_while = 0
    while i_for_while <= len(yourself) - 1:
        
        if i_for_while <= 3: 
            i_for_while += 1
            continue
        else:
            tf_for_x = my_headx - yourself[i_for_while]["x"]
            tf_for_y = my_heady - yourself[i_for_while]["y"]

            if  tf_for_x == -1:
                sides["right"] = False
                i_for_while += 1

            if tf_for_x == 1:
                sides["left"] = False
                i_for_while += 1

            if tf_for_y == -1:
                sides["up"] = False
                i_for_while += 1

            if tf_for_y == 1:
                sides["down"] = False
                i_for_while += 1

def prot_another_snakes_body(my_headx: int, my_heady: int, anothersnake: list, sides: dict, your_lenth: int, anothersnake_lenth: int):
    i_for_while = 0
    while i_for_while <= len(anothersnake) - 1:
        another_headx = anothersnake[0]["x"]
        another_heady = anothersnake[0]["y"]
        headsx = my_headx - another_headx
        hedsy = my_heady - another_heady
        tf_for_x = my_headx - anothersnake[i_for_while]["x"]
        tf_for_y = my_heady - anothersnake[i_for_while]["y"]

        if headsx == 1 and hedsy == 1 and your_lenth <= anothersnake_lenth:
            sides["down"] = False
        if headsx == 1 and hedsy == -1 and your_lenth <= anothersnake_lenth:
            sides["up"] = False
        if headsx == -1 and hedsy == 1 and your_lenth <= anothersnake_lenth:
            sides["down"] = False
        if headsx == -1 and hedsy == -1 and your_lenth <= anothersnake_lenth:
            sides["up"] = False

        if headsx == 1 and hedsy == 0 and your_lenth <= anothersnake_lenth:
            sides["right"] = False
        if headsx == 0 and hedsy == -1 and your_lenth <= anothersnake_lenth:
            sides["up"] = False
        if headsx == -1 and hedsy == 0 and your_lenth <= anothersnake_lenth:
            sides["left"] = False
        if headsx == 0 and hedsy == 1 and your_lenth <= anothersnake_lenth:
            sides["down"] = False


        if  tf_for_x == -1:
            sides["right"] = False
            i_for_while += 1

        if tf_for_x == 1:
            sides["left"] = False
            i_for_while += 1

        if tf_for_y == -1:
            sides["up"] = False
            i_for_while += 1

        if tf_for_y == 1:
            sides["down"] = False
            i_for_while += 1