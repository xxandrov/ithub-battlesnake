import random
from functools import lru_cache 
from prot import *





# See https://docs.battlesnake.com/api/example-move for available data
def handle_move(game_state: dict) -> dict:
    is_move_safe = {"up": True, "down": True, "left": True, "right": True}

    # prevent from moving backwards
    my_head = game_state["you"]["body"][0]  # Coords of your head
    my_neck = game_state["you"]["body"][1]  # Coords of your "neck"
    h = game_state["board"]["height"] - 1 # y
    w = game_state["board"]["width"] - 1 # x
    
    #не врезаемся в себя
    prot_backwards(my_head["x"], my_head["y"], my_neck["x"], my_neck["y"], is_move_safe)
    
    #не врезаемсся в стены and углы
    prot_border(my_head["x"], my_head["y"], w, h, is_move_safe)

    #не врезаемся в себя 2
    prot_snakes_body(my_head["x"], my_head["y"], game_state["you"]["body"], is_move_safe)

    #не врезаемся в другую змею
    prot_another_snakes_body(my_head["x"], my_head["y"], game_state["board"]["snakes"][0], is_move_safe, game_state["you"]["length"],
                             game_state["board"]["snakes"][0]["length"])

    
    
    # TODO: Step 1 - Prevent your Battlesnake from moving out of bounds+
    # board_width = game_state['board']['width']
    # board_height = game_state['board']['height']

    # TODO: Step 2 - Prevent your snake from colliding with itself+
    # my_body = game_state['you']['body']

    # TODO: Step 3 - Prevent your snake from colliding with other snakes
    # opponents = game_state['board']['snakes']

    # Are there any safe moves left?
    safe_moves = []
    for move, is_safe in is_move_safe.items():
        if is_safe:
            safe_moves.append(move)

    # Move down if there is no better solution...
    if len(safe_moves) == 0:
        return {"move": "down"}

    # Choose a random move from the safe ones
    next_move = random.choice(safe_moves)

    # TODO: Step 4 - Move towards food instead of random, to regain health
    # food = game_state['board']['food']
    print(safe_moves)
    print(f"MOVE {game_state.get('turn', '')}: {next_move}")
    return {"move": next_move}


