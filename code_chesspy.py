import random as rd; from operator import xor; from time import sleep


#creacion de la clase chess util para todos las operaciones que se llevaran a cabo
class chess:
    def __init__(self, type, piece, position, index):
        #definicion de propiedades para los objetos de la clase chess
        self.type = type
        self.piece = piece
        self.index = index
        self.position = position
        self.value = 0


    #definicion de variables utiles para almacenamiento de objetos de la clase chess y operaciones con la tabla de ajerdrez
    global Listvar, dict_board, dict_objs
    Listvar= [i+f"{j}" for i in ["A","B","C","D","E","F","G","H"] for j in range(8)]; Listvar.sort(key=lambda var: var[1])
    dict_board= {i: None for i in Listvar}; dict_objs= {}


    #definicion de turno del jugador
    def turn(self, x):
        return "black" if x % 2 != 0 else "white"

    #definicion del fin del juego
    def game_over(self):
        kings= []
        for obj in dict_objs.keys():
            if dict_objs[obj].piece == "king":
                kings.append(obj)
        if len(kings) != 2:
            winner = "black" if dict_objs[kings[0]].type == "black" else "white"
            print(f"Game over! {winner} wins.")
            return True
        return False


    #definicion de promocion de peones en la ultima fila
    def pawn_promotion(self, turn, varvalue):
        #definicion variables repuesta
        bp= rd.choice(["yes","no"]); cp= rd.choice(["queen", "rook", "bishop", "knight"])
        new_piece= ""; fp= rd.choice(["yes","no"]); ep= rd.choice(["queen", "rook", "bishop", "knight"])
        
        #verificar peones para promocion
        for ip in (Listvar[0:8] + Listvar[56:64]):
            zp = 0
            if dict_board[ip] != None:
                if dict_objs[dict_board[ip]].piece == "pawn" and  dict_objs[dict_board[ip]].piece == "white"\
                    and dict_objs[dict_board[ip]].value == 1 and ip in Listvar[56:64]: print(ip, dict_objs[dict_board[ip]]); zp= 1
                elif dict_objs[dict_board[ip]].piece == "pawn" and  dict_objs[dict_board[ip]].piece == "black"\
                    and dict_objs[dict_board[ip]].value == 1 and ip in Listvar[0:8]: print(ip, dict_objs[dict_board[ip]]); zp= 1

            #verificar variables respuesta
            if zp == 1:
                if turn == "white" and bp == "yes": 
                    print("pawn promotion available, do you want do it? (yes/no, please write like this \"yes queen\"): ", end="")
                    sleep(0.35); print(f"yes {cp}")
                elif turn == "white" and bp == "no": 
                    print("pawn promotion available, do you want do it? (yes/no, please write like this \"yes queen\"): ", end="")
                    sleep(0.35); print("no"); zp = 0

                if turn == "black" and varvalue != 1:
                    new_piece= input("pawn promotion available, do you want do it? (yes/no, please write like this \"yes queen\"): ")

                    if new_piece.split()[0] == "yes" and new_piece.split()[1] in ["queen", "rook", "bishop", "knight"]: None
                    elif new_piece.split()[0] == "no": zp = 0
                    else: print("Invalid choice. Please choose again.")
                
                elif turn == "black" and varvalue == 1 and fp == "yes":
                    print("pawn promotion available, do you want do it? (yes/no, please write like this \"yes queen\"): ", end="")
                    sleep(0.35); print(f"yes {cp}")
                elif turn == "black" and varvalue == 1 and fp == "no": 
                    print("pawn promotion available, do you want do it? (yes/no, please write like this \"yes queen\"): ", end="")
                    sleep(0.35); print("no"); zp = 0

                #promocion de peones al tipo de ficha deseado
                if zp == 1 and xor(new_piece.split()[0] == "yes", bp == "yes"):
                    if cp == "queen" and dict_objs[dict_board[ip]].type == "white":
                        dict_objs[dict_objs[dict_board[ip]].index] = ("white", "queen", ip, "♕1"); dict_board[ip] = "♕1"; return True
                    elif new_piece.split()[1] == "queen" and dict_objs[dict_board[ip]].type == "black" and varvalue != 1:
                        dict_objs[dict_objs[dict_board[ip]].index] = ("black", "queen", ip, "♛1"); dict_board[ip] = "♛1"; return True
                    elif ep == "queen" and dict_objs[dict_board[ip]].type == "black" and varvalue == 1:
                        dict_objs[dict_objs[dict_board[ip]].index] = ("black", "queen", ip, "♛1"); dict_board[ip] = "♛1"; return True
                    
                    if cp == "rook" and dict_objs[dict_board[ip]].type == "white":
                        dict_objs[dict_objs[dict_board[ip]].index] = ("white", "rook", ip, "♖"); dict_board[ip] = "♖"; return True
                    elif new_piece.split()[1] == "rook" and dict_objs[dict_board[ip]].type == "black" and varvalue != 1:
                        dict_objs[dict_objs[dict_board[ip]].index] = ("black", "rook", ip, "♜"); dict_board[ip] = "♜"; return True
                    elif ep == "rook" and dict_objs[dict_board[ip]].type == "black" and varvalue == 1:
                        dict_objs[dict_objs[dict_board[ip]].index] = ("black", "rook", ip, "♜"); dict_board[ip] = "♜"; return True
                    
                    if cp == "bishop" and dict_objs[dict_board[ip]].type == "white":
                        dict_objs[dict_objs[dict_board[ip]].index] = ("white", "bishop", ip, "♗"); dict_board[ip] = "♗"; return True
                    elif new_piece.split()[1] == "bishop" and dict_objs[dict_board[ip]].type == "black" and varvalue != 1:
                        dict_objs[dict_objs[dict_board[ip]].index] = ("black", "bishop", ip, "♝"); dict_board[ip] = "♝"; return True
                    elif ep == "bishop" and dict_objs[dict_board[ip]].type == "black" and varvalue == 1:
                        dict_objs[dict_objs[dict_board[ip]].index] = ("black", "bishop", ip, "♝"); dict_board[ip] = "♝"; return True
                    
                    if cp == "knight" and dict_objs[dict_board[ip]].type == "white":
                        dict_objs[dict_objs[dict_board[ip]].index] = ("white", "knight", ip, "♘"); dict_board[ip] = "♘"; return True
                    elif new_piece.split()[1] == "knight" and dict_objs[dict_board[ip]].type == "black" and varvalue != 1:
                        dict_objs[dict_objs[dict_board[ip]].index] = ("black", "knight", ip, "♞"); dict_board[ip] = "♞"; return True
                    elif ep == "knight" and dict_objs[dict_board[ip]].type == "black" and varvalue == 1:
                        dict_objs[dict_objs[dict_board[ip]].index] = ("black", "knight", ip, "♞"); dict_board[ip] = "♞"; return True
                    

                    print(f"Pawn promoted to {new_piece} at {ip}")

        return False


    #definicion del torniquete para el rey
    def castling(self, turn, varvalue):
        #definicion variables respuesta y operacion
        qc = 0; bc= rd.choice(["yes","no"]); fc= rd.choice(["yes","no"]) 
        Listtiles= [("A0", "E0"), ("H0", "E0"), ("A7", "E7"), ("H7", "E7")]
        #verificar la posibilidad de torniquete
        for ic, yc in Listtiles:
            zc = 0; kc = 0
            if dict_board[ic] != None and dict_board[yc] != None: zc = 1

            if zc == 1:
                piece_king = dict_objs[dict_board[ic]]; piece_rook = dict_objs[dict_board[yc]]
                if piece_king.piece == "king" and piece_rook.piece == "rook":
                    for ic, yc in [(1, 4), (5, 7), (56, 59), (61, 63)]:
                        for x in [None if dict_board[Listvar[x]] == None else 0 for x in range(ic, yc)]:
                            if x == None: kc += 1 
                            else: kc += 0

            #verificar variables respuesta
            if zc == 1 and piece_rook.value == 0 and piece_king.value == 0 and qc == 0 and kc == 2 or kc == 3:
                if turn == "white" and bc == "yes": 
                    print(f"Castling available for player {turn}, {piece_king.index} and {piece_rook.index} do you want do it? (yes/no): ", end="")
                    sleep(0.35); print("yes"); zc = 2; qc = 1
                elif turn == "white" and bc == "no":
                    print(f"Castling available for player {turn}, {piece_king.index} and {piece_rook.index} do you want do it? (yes/no): ", end="")
                    sleep(0.35); print("no"); qc = 1
                elif turn == "black" and varvalue != 1:
                    answer= input(f"Castling available for player {turn}, {piece_king.index} and {piece_rook.index} do you want do it? (yes/no): ", end="")

                    if answer == "yes": zc = 2; qc = 1
                    elif answer == "no": qc = 1
                    else: print("Invalid choice. Please choose again.")
                elif turn == "black" and varvalue == 1 and fc == "yes":
                    print(f"Castling available for player {turn}, {piece_king.index} and {piece_rook.index} do you want do it? (yes/no): ", end="")
                    sleep(0.35); print(f"yes"); zc = 2; qc = 1
                elif turn == "black" and varvalue == 1 and fc == "no": 
                    print(f"Castling available for player {turn}, {piece_king.index} and {piece_rook.index} do you want do it? (yes/no): ", end="")
                    sleep(0.35); print("no"); qc = 1 
                        
                #realizar accion de torniquete
                if zc == 2 and qc == 1 and kc == 2 or kc == 3:
                    if dict_board[Listvar(Listvar.index(piece_king.position)+2)] == None \
                        and dict_board[Listvar(Listvar.index(piece_rook.position)-3)] == None:
                        dict_board[piece_king.position] = None
                        piece_king.position = Listvar[Listvar.index(piece_king.position)+2]
                        dict_board[piece_king.position] = piece_king.index
                        dict_board[piece_rook.position] = None
                        piece_rook.position = Listvar[Listvar.index(piece_rook.position)-3]
                        dict_board[piece_rook.position] = piece_rook.index
                        piece_king.value += 1; piece_rook.value += 1
                        print(f"Castling performed: {piece_king.index} to {piece_king.position}, {piece_rook.index} to {piece_rook.position}")
                        return True
                                
                    elif dict_board[Listvar(Listvar.index(piece_king.position)-2)] == None \
                        and dict_board[Listvar(Listvar.index(piece_rook.position)+2)] == None:
                        dict_board[piece_king.position] = None
                        piece_king.position = Listvar[Listvar.index(piece_king.position)+2]
                        dict_board[piece_king.position] = piece_king.index
                        dict_board[piece_rook.position] = None
                        piece_rook.position = Listvar[Listvar.index(piece_rook.position)-3]
                        dict_board[piece_rook.position] = piece_rook.index
                        piece_king.value += 1; piece_rook.value += 1
                        print(f"Castling performed: {piece_king.index} to {piece_king.position}, {piece_rook.index} to {piece_rook.position}")
                        return True
                        
        return False

    #iniciar primeras posiciones en el tablero
    def initial_position(self):
        for type in ["white","black"]:
            for piece in ["pawn", "knight", "rook", "bishop", "queen", "king"]:
                y = 0; position = None; index = None
                for position in Listvar:
                    if piece == "pawn" and position in Listvar[8:16]+Listvar[48:56]:
                        if type == "black" and position in Listvar[48:56]: 
                            index = ["♙"+str(x) for x in range(1, 9)] 
                            dict_objs[index[y]] = chess(type, piece, position, index[y])
                            dict_board[position] = index[y]; y += 1
                        elif type == "white" and position in Listvar[8:16]:
                            index = ["♟"+str(x) for x in range(1, 9)]
                            dict_objs[index[y]] = chess(type, piece, position, index[y])
                            dict_board[position] = index[y]; y += 1
                        if y == 8: y = 0

                    if piece == "knight" and position in ["B0", "G0", "B7", "G7"]:
                        if type == "black" and position in ["B7", "G7"]: 
                            index = ["♘1", "♘2"]
                            dict_objs[index[y]] = chess(type, piece, position, index[y])
                            dict_board[position] = index[y]; y += 1
                        elif type == "white" and position in ["B0", "G0"]:
                            index = ["♞1", "♞2"]
                            dict_objs[index[y]] = chess(type, piece, position, index[y])
                            dict_board[position] = index[y]; y += 1
                        if y == 2: y = 0

                    if piece == "rook" and position in ["A0", "H0", "A7" , "H7"]: 
                        if type == "black" and position in ["A7", "H7"]: 
                            index = ["♖1", "♖2"]
                            dict_objs[index[y]] = chess(type, piece, position, index[y])
                            dict_board[position] = index[y]; y += 1
                        elif type == "white" and position in ["A0", "H0"]:
                            index = ["♜1", "♜2"]
                            dict_objs[index[y]] = chess(type, piece, position, index[y])
                            dict_board[position] = index[y]; y += 1
                        if y == 2: y = 0

                    if piece == "bishop" and position in ["C0", "F0", "C7", "F7"]:
                        if type == "black" and position in ["C7", "F7"]:
                            index = ["♗1", "♗2"]
                            dict_objs[index[y]] = chess(type, piece, position, index[y])
                            dict_board[position] = index[y]; y += 1 
                        elif type == "white" and position in ["C0", "F0"]: 
                            index = ["♝1", "♝2"]
                            dict_objs[index[y]] = chess(type, piece, position, index[y])
                            dict_board[position] = index[y]; y += 1
                        if y == 2: y = 0

                    if piece == "queen" and position in ["D0", "E7"]:
                        if type == "black"  and position in ["E7"]:
                            index = "♕ "
                            dict_objs[index] = chess(type, piece, position, index)
                            dict_board[position] = index
                        elif type == "white" and position in ["D0"]: 
                            index = "♛ "
                            dict_objs[index] = chess(type, piece, position, index)
                            dict_board[position] = index

                    if piece == "king" and position in ["E0", "D7"]:
                        if type == "black" and position in ["D7"]: 
                            index = "♔ "
                            dict_objs[index] = chess(type, piece, position, index)
                            dict_board[position] = index
                        elif type == "white" and position in ["E0"]: 
                            index = "♚ "
                            dict_objs[index] = chess(type, piece, position, index)
                            dict_board[position] = index


    #definicion de movimientos de las piezas
    def move(self, index_piece=None, new_position=None, turn=None, varvalue=0):
        #definicion variables para identificacion de movimientos del jugador humano
        List_piece = ["p"+str(i) for i in range(1, 9)] + [f"{y}"+str(i) for y in ["h", "r", "b"] for i in range(1, 3)] + ["q", "k"] + ["h", "r", "b", "q1"]
        List_index = ["♙"+str(x) for x in range(1, 9)] + ["♘1", "♘2", "♖1", "♖2", "♗1", "♗2", "♕ ", "♔ "] + ["♘", "♖", "♗", "♕1"]
        dict_piece = {k: v for k, v in zip(List_piece, List_index)}

        #creacion inteligencia artificial :d (no lo es...)
        while True:
            if turn == "white":
                new_position = rd.choice(Listvar)
                index_piece = rd.choice([k for k, v in dict_objs.items() if v.type == "white"])
            elif turn == "black" and varvalue == 1:
                new_position = rd.choice(Listvar)
                index_piece = rd.choice([k for k, v in dict_objs.items() if v.type == "black"])
            #verificar movimientos del usuario
            elif turn == "black" and varvalue != 1:
                answer = input("select a piece and a position to move (please write like this \"p1 a1\"): ")
                while True:
                    try: 
                        index_piece, new_position = answer.split()
                        index_piece = index_piece.lower(); new_position = new_position.upper()
                        if index_piece not in dict_piece.keys() or new_position not in Listvar:
                            answer = input("Invalid input format. Please use the format \"p1 a1\": ")
                        else: index_piece = dict_piece[index_piece]; break
                    except Exception: 
                        answer = input("Invalid input format. Please use the format \"p1 a1\": ")

            #definicion variables para operacion de los movimientos
            y = 1 if dict_objs[index_piece].type == "white" else -1; c = 0; q = 0
            i = abs(int(new_position[1])-int(dict_objs[index_piece].position[1]))
            position = Listvar.index(dict_objs[index_piece].position)
            path_clear = True

            #verificar movimiento del peon
            if dict_objs[index_piece].piece == "pawn":
                if dict_board[new_position] == None and (new_position == Listvar[position+8*y] if 64 > position+8*y else False) \
                    and (int(new_position[1]) == int(dict_objs[index_piece].position[1])+y):
                    
                    dict_board[dict_objs[index_piece].position] = None
                    dict_objs[index_piece].position = new_position
                    dict_board[dict_objs[index_piece].position] = dict_objs[index_piece].index
                    return f"plays {index_piece} in {new_position}"

                elif dict_board[new_position] == None and (new_position == Listvar[position+16*y] if 64 > position+16*y else False) \
                    and (int(new_position[1]) == int(dict_objs[index_piece].position[1])+2*y) and dict_objs[index_piece].value == 0:
                    path_clear = True
                    for k in range(position+y*8, Listvar.index(new_position)+y, 8*y):
                        if dict_board[Listvar[k]] != None:
                            path_clear = False; break
                    if path_clear:
                        dict_objs[index_piece].value += 1
                        dict_board[dict_objs[index_piece].position] = None
                        dict_objs[index_piece].position = new_position
                        dict_board[dict_objs[index_piece].position] = dict_objs[index_piece].index
                        return f"plays {index_piece} in {new_position}"
                    else:
                        if turn == "black" and varvalue != 1: print("Invalid move")
                        else: None
                else:
                    if turn == "black" and varvalue != 1: print("Invalid move")
                    else: None

                if (dict_objs[index_piece].type != dict_objs[dict_board[new_position]].type if dict_board[new_position] != None else False) and xor(
                    (new_position == Listvar[position+7*y] if 64 > position+7*y else False) and (int(new_position[1]) == int(dict_objs[index_piece].position[1])+1*y) ,\
                    (new_position == Listvar[position+9*y] if 64 > position+9*y else False) and (int(new_position[1]) == int(dict_objs[index_piece].position[1])+1*y)
                ):
                    if (dict_objs[index_piece].type != dict_objs[dict_board[new_position]].type if dict_board[new_position] != None else False):
                        dict_board[dict_objs[index_piece].position] = None
                        del dict_objs[dict_board[new_position]]; dict_objs[index_piece].position = new_position
                        dict_board[dict_objs[index_piece].position] = dict_objs[index_piece].index
                        return f"plays {index_piece} in {new_position}"
                    
                    else:
                        if turn == "black" and varvalue != 1: print("Invalid move")
                        else: None


            #verificar movimiento del caballo
            if dict_objs[index_piece].piece == "knight":
                if xor(xor(
                    (new_position == Listvar[position+6*y] if 64 > position+6*y else False) and int(new_position[1]) == int(dict_objs[index_piece].position[1])+1*y ,\
                    (new_position == Listvar[position+10*y] if 64 > position+10*y else False) and int(new_position[1]) == int(dict_objs[index_piece].position[1])+1*y
                    ), xor(
                    (new_position == Listvar[position+15*y] if 64 > position+15*y else False) and int(new_position[1]) == int(dict_objs[index_piece].position[1])+2*y ,\
                    (new_position == Listvar[position+17*y] if 64 > position+17*y else False) and int(new_position[1]) == int(dict_objs[index_piece].position[1])+2*y
                    )):
                    if (dict_objs[index_piece].type != dict_objs[dict_board[new_position]].type if dict_board[new_position] != None else False): 
                        dict_board[dict_objs[index_piece].position] = None
                        del dict_objs[dict_board[new_position]]
                        dict_objs[index_piece].position = new_position
                        dict_board[dict_objs[index_piece].position] = dict_objs[index_piece].index
                        return f"plays {index_piece} in {new_position}"
                    elif (dict_board[new_position] == None):
                        dict_board[dict_objs[index_piece].position] = None
                        dict_objs[index_piece].position = new_position
                        dict_board[dict_objs[index_piece].position] = dict_objs[index_piece].index
                        return f"plays {index_piece} in {new_position}"
                    else:
                        if turn == "black" and varvalue != 1: print("Invalid move")
                        else: None
                        
                else:
                    if turn == "black" and varvalue != 1: print("Invalid move")
                    else: None


            #verificar movimiento de la torre
            if dict_objs[index_piece].piece == "rook":
                if xor(
                    (new_position == Listvar[position+8*i*y] if 64 > position+8*i*y else False) and position < Listvar.index(new_position) ,\
                    (new_position == Listvar[position+8*i*y] if 64 > position+8*i*y else False) and position > Listvar.index(new_position)
                    ):
                    if (dict_objs[index_piece].type != dict_objs[dict_board[new_position]].type if dict_board[new_position] != None else False):
                        for k in (range(position+y, Listvar.index(new_position)+y, 8*y)):
                            if dict_board[Listvar[k]] != None:
                                path_clear = False; break
                        if path_clear:
                            dict_board[dict_objs[index_piece].position] = None
                            del dict_objs[dict_board[new_position]]
                            dict_objs[index_piece].position = new_position
                            dict_board[dict_objs[index_piece].position] = dict_objs[index_piece].index
                            return f"plays {index_piece} in {new_position}"
                        
                        else:
                            if turn == "black" and varvalue != 1: print("Invalid move")
                            else: None
                            
                    elif dict_board[new_position] == None:
                        for k in (range(position+y*8, Listvar.index(new_position)+y, 8*y)):
                            if dict_board[Listvar[k]] != None:
                                path_clear = False; break
                        if path_clear:
                            dict_board[dict_objs[index_piece].position] = None
                            dict_objs[index_piece].position = new_position
                            dict_board[dict_objs[index_piece].position] = dict_objs[index_piece].index
                            return f"plays {index_piece} in {new_position}"
                    
                    else:
                        if turn == "black" and varvalue != 1: print("Invalid move")
                        else: None
                        

                if(new_position == Listvar[(Listvar.index(new_position)-position)+position] if 64 > (Listvar.index(new_position)-position)+position else False) \
                    and (int(Listvar[position][1])-int(new_position[1]) == 0):
                    if (dict_objs[index_piece].type != dict_objs[dict_board[new_position]].type if dict_board[new_position] != None else False):
                        c = (1 if Listvar.index(new_position) > position else -1)
                        for k in (range(position+c, Listvar.index(new_position)+c, c)):
                            if dict_board[Listvar[k]] != None:
                                path_clear = False; break
                        if path_clear:
                            dict_board[dict_objs[index_piece].position] = None
                            del dict_objs[dict_board[new_position]]
                            dict_objs[index_piece].position = new_position
                            dict_board[dict_objs[index_piece].position] = dict_objs[index_piece].index
                            return f"plays {index_piece} in {new_position}"
                            
                        else:
                            if turn == "black" and varvalue != 1: print("Invalid move")
                            else: None

                    elif dict_board[new_position] == None:
                        c = (1 if Listvar.index(new_position) > position else -1)
                        for k in (range(position+c, Listvar.index(new_position)+c, c)):
                            if dict_board[Listvar[k]] != None:
                                path_clear = False; break
                        if path_clear:
                            dict_board[dict_objs[index_piece].position] = None
                            dict_objs[index_piece].position = new_position
                            dict_board[dict_objs[index_piece].position] = dict_objs[index_piece].index
                            return f"plays {index_piece} in {new_position}"
                    
                    else:
                        if turn == "black" and varvalue != 1: print("Invalid move")
                        else: None


            #verificar movimiento del alfil
            if dict_objs[index_piece].piece == "bishop":
                if new_position == Listvar[position+9*i*y] if 64 > position+9*i*y else False:
                    if xor(new_position == Listvar[position+9*i*y] if 64 > position+9*i*y else False and position < position+9*i*y ,\
                        new_position == Listvar[position+9*i*y] if 64 > position+9*i*y else False and position > position+9*i*y):
                        for k in range(position+y*9, Listvar.index(new_position)+y, 9*y):
                            if dict_board[Listvar[k]] != None:
                                path_clear = False; break
                        if path_clear:
                                dict_board[dict_objs[index_piece].position] = None
                                del dict_objs[dict_board[new_position]]
                                dict_objs[index_piece].position = new_position
                                dict_board[dict_objs[index_piece].position] = dict_objs[index_piece].index
                                return f"plays {index_piece} in {new_position}"
                        else:
                            if turn == "black" and varvalue != 1: print("Invalid move")
                            else: None  
                
                    elif dict_board[new_position] == None:
                        for k in range(position+y*9, Listvar.index(new_position)+y, 9*y):
                            if dict_board[Listvar[k]] != None:
                                path_clear = False; break
                        if path_clear:
                            dict_board[dict_objs[index_piece].position] = None
                            dict_objs[index_piece].position = new_position
                            dict_board[dict_objs[index_piece].position] = dict_objs[index_piece].index
                            return f"plays {index_piece} in {new_position}"
                    
                    else:
                        if turn == "black" and varvalue != 1: print("Invalid move")
                        else: None


                if xor((new_position == Listvar[position+7*i*y] if 64 > position+7*i*y else False) and (position < position+7*i*y) ,\
                        (new_position == Listvar[position+7*i*y] if 64 > position+7*i*y else False) and (position > position+7*i*y)):
                    if (dict_objs[index_piece].type != dict_objs[dict_board[new_position]].type if dict_board[new_position] != None else False):
                        for k in list(range(position+y*7, Listvar.index(new_position)+y, 7*y)):
                            if dict_board[Listvar[k]] != None:
                                path_clear = False; break
                        if path_clear:
                            dict_board[dict_objs[index_piece].position] = None
                            del dict_objs[dict_board[new_position]]
                            dict_objs[index_piece].position = new_position
                            dict_board[dict_objs[index_piece].position] = dict_objs[index_piece].index
                            return f"plays {index_piece} in {new_position}"
                        else:
                            if turn == "black" and varvalue != 1: print("Invalid move")
                            else: None  
                
                    elif dict_board[new_position] == None:
                        for k in range(position+y*7, Listvar.index(new_position)+y, 7*y):
                            if dict_board[Listvar[k]] != None:
                                path_clear = False; break
                        if path_clear:
                            dict_board[dict_objs[index_piece].position] = None
                            dict_objs[index_piece].position = new_position
                            dict_board[dict_objs[index_piece].position] = dict_objs[index_piece].index
                            return f"plays {index_piece} in {new_position}"
                    
                    else:
                        if turn == "black" and varvalue != 1: print("Invalid move")
                        else: None


            #verificar movimiento de la reina
            if dict_objs[index_piece].piece == "queen":
                if xor(
                    (new_position == Listvar[position+8*i*y] if 64 > position+8*i*y else False) and position < Listvar.index(new_position) ,\
                    (new_position == Listvar[position+8*i*y] if 64 > position+8*i*y else False) and position > Listvar.index(new_position)
                    ):
                    if (dict_objs[index_piece].type != dict_objs[dict_board[new_position]].type if dict_board[new_position] != None else False):
                        for k in list(range(position+y*8, Listvar.index(new_position)+y, 8*y)):
                            if dict_board[Listvar[k]] != None:
                                path_clear = False; break
                        if path_clear:
                            dict_board[dict_objs[index_piece].position] = None
                            del dict_objs[dict_board[new_position]]
                            dict_objs[index_piece].position = new_position
                            dict_board[dict_objs[index_piece].position] = dict_objs[index_piece].index
                            return f"plays {index_piece} in {new_position}"
                        
                        else:
                            if turn == "black" and varvalue != 1: print("Invalid move")
                            else: None
                            
                    elif dict_board[new_position] == None:
                        for k in list(range(position+y*8, Listvar.index(new_position)+y, 8*y)):
                            if dict_board[Listvar[k]] != None:
                                path_clear = False; break
                        if path_clear:
                            dict_board[dict_objs[index_piece].position] = None
                            dict_objs[index_piece].position = new_position
                            dict_board[dict_objs[index_piece].position] = dict_objs[index_piece].index
                            return f"plays {index_piece} in {new_position}"
                    
                    else:
                        if turn == "black" and varvalue != 1: print("Invalid move")
                        else: None
                        

                if (new_position == Listvar[(Listvar.index(new_position)-position)+position] if 64 > (Listvar.index(new_position)-position)+position else False) \
                    and int(Listvar[position][1])-int(new_position[1]) == 0:
                    if (dict_objs[index_piece].type != dict_objs[dict_board[new_position]].type if dict_board[new_position] != None else False):
                        c = (1 if Listvar.index(new_position) > position else -1)
                        for k in list(range(position+c, Listvar.index(new_position)+c, c)):
                            if dict_board[Listvar[k]] != None:
                                path_clear = False; break
                        if path_clear:
                            dict_board[dict_objs[index_piece].position] = None
                            del dict_objs[dict_board[new_position]]
                            dict_objs[index_piece].position = new_position
                            dict_board[dict_objs[index_piece].position] = dict_objs[index_piece].index
                            return f"plays {index_piece} in {new_position}"
                            
                        else:
                            if turn == "black" and varvalue != 1: print("Invalid move")
                            else: None

                    elif dict_board[new_position] == None:
                        c = (1 if Listvar.index(new_position) > position else -1)
                        for k in list(range(position+c, Listvar.index(new_position)+c, c)):
                            if dict_board[Listvar[k]] != None:
                                path_clear = False; break
                        if path_clear:
                            dict_board[dict_objs[index_piece].position] = None
                            dict_objs[index_piece].position = new_position
                            dict_board[dict_objs[index_piece].position] = dict_objs[index_piece].index
                            return f"plays {index_piece} in {new_position}"
                    
                    else:
                        if turn == "black" and varvalue != 1: print("Invalid move")
                        else: None

                        
                if xor(new_position == Listvar[position+9*i*y] if 64 > position+9*i*y else False and position < position+9*i*y ,\
                        new_position == Listvar[position+9*i*y] if 64 > position+9*i*y else False and position > position+9*i*y):
                    if (dict_objs[index_piece].type != dict_objs[dict_board[new_position]].type if dict_board[new_position] != None else False): 
                        for k in list(range(position+y*9, Listvar.index(new_position)+y, 9*y)):
                            if dict_board[Listvar[k]] != None:
                                path_clear = False; break
                        if path_clear:
                                dict_board[dict_objs[index_piece].position] = None
                                del dict_objs[dict_board[new_position]]
                                dict_objs[index_piece].position = new_position
                                dict_board[dict_objs[index_piece].position] = dict_objs[index_piece].index
                                return f"plays {index_piece} in {new_position}"
                        else:
                            if turn == "black" and varvalue != 1: print("Invalid move")
                            else: None  
                
                    elif dict_board[new_position] == None:
                        for k in list(range(position+y*9, Listvar.index(new_position)+y, 9*y)):
                            if dict_board[Listvar[k]] != None:
                                path_clear = False; break
                        if path_clear:
                            dict_board[dict_objs[index_piece].position] = None
                            dict_objs[index_piece].position = new_position
                            dict_board[dict_objs[index_piece].position] = dict_objs[index_piece].index
                            return f"plays {index_piece} in {new_position}"
                    
                    else:
                        if turn == "black" and varvalue != 1: print("Invalid move")
                        else: None
                    

                if xor((new_position == Listvar[position+7*i*y] if 64 > position+7*i*y else False) and (position < position+7*i*y) ,\
                        (new_position == Listvar[position+7*i*y] if 64 > position+7*i*y else False) and (position > position+7*i*y)):
                    if (dict_objs[index_piece].type != dict_objs[dict_board[new_position]].type if dict_board[new_position] != None else False):
                        for k in list(range(position+y*7, Listvar.index(new_position)+y, 7*y)):
                            if dict_board[Listvar[k]] != None:
                                path_clear = False; break
                        if path_clear:
                            dict_board[dict_objs[index_piece].position] = None
                            del dict_objs[dict_board[new_position]]
                            dict_objs[index_piece].position = new_position
                            dict_board[dict_objs[index_piece].position] = dict_objs[index_piece].index
                            return f"plays {index_piece} in {new_position}"
                        else:
                            if turn == "black" and varvalue != 1: print("Invalid move")
                            else: None  
                
                    elif dict_board[new_position] == None:
                        for k in list(range(position+y*7, Listvar.index(new_position)+y, 7*y)):
                            if dict_board[Listvar[k]] != None:
                                path_clear = False; break
                        if path_clear:
                            dict_board[dict_objs[index_piece].position] = None
                            dict_objs[index_piece].position = new_position
                            dict_board[dict_objs[index_piece].position] = dict_objs[index_piece].index
                            return f"plays {index_piece} in {new_position}"
                    
                    else:
                        if turn == "black" and varvalue != 1: print("Invalid move")
                        else: None
                      

            #verificar movimiento del rey
            if dict_objs[index_piece].piece == "king":
                if xor(
                    (new_position == Listvar[position+1*y] if 64 > position+1*y else False) and int(new_position[1]) == int(dict_objs[index_piece].position[1]) ,\
                    (new_position == Listvar[position+8*y] if 64 > position+8*y else False) and int(new_position[1]) == int(dict_objs[index_piece].position[1])+1*y
                    ) or xor(
                    (new_position == Listvar[position+9*y] if 64 > position+9*y else False) and int(new_position[1]) == int(dict_objs[index_piece].position[1])+1*y ,\
                    (new_position == Listvar[position+7*y] if 64 > position+7*y else False) and int(new_position[1]) == int(dict_objs[index_piece].position[1])+1*y
                    ):
                    if (dict_objs[index_piece].type != dict_objs[dict_board[new_position]].type if dict_board[new_position] != None else False): 
                        dict_objs[index_piece].value += 1
                        dict_board[dict_objs[index_piece].position] = None
                        del dict_objs[dict_board[new_position]]
                        dict_objs[index_piece].position = new_position
                        dict_board[dict_objs[index_piece].position] = dict_objs[index_piece].index
                        return f"plays {index_piece} in {new_position}"
                    elif (dict_board[new_position] == None):
                        dict_objs[index_piece].value += 1
                        dict_board[dict_objs[index_piece].position] = None
                        dict_objs[index_piece].position = new_position
                        dict_board[dict_objs[index_piece].position] = dict_objs[index_piece].index
                    
                        return f"plays {index_piece} in {new_position}"
                    else:
                        if turn == "black" and varvalue != 1: print("Invalid move")
                        else: None


    #definicion de la impresion del tablero
    def __str__(self):

        x= 0; y= 8
        board=" │ A  │ B  │ C  │ D  │ E  │ F  │ G  │ H  │"
        for i in range(8):
            board += "\n-"
            for q in range(8):
                board += "+----"
            board += "+\n "
            for q in range(8):
                board += "│    "
            board += f"│\n{i}"
            for q in Listvar[x:y]:
                if dict_board[q] == None: board += "│    "
                else: board += f"│ {dict_board[q]} "
            board += "│\n "
            for q in range(8):
                board += "│    "
            board += "│"

            x += 8; y += 8
        board += "\n-"
        for q in range(8):
            board += "+----"
        board += "+\n "

        return board


#inicion del juego
chess.initial_position(self=chess)
print("""
      Welcome to the Chess Game! 
    Below, you can choose between playing or watching a simulation of a game. 
    Note: to play, you need to use the following notation to make your moves; 
    p1 a1, where p represents a piece and 1 represents the identification of 
    the piece, and a1 represents a square. In addition, the piece and the square
    you want to play must be separated by a space. Below are the identifications
    of the pieces: p (pawn), h (knight), r (rook), b (bishop), q (queen), k (king).
      
    With nothing more to add, enjoy!
      """)

print(chess.__str__(self=chess))

#definicion de pregunta al usuario entre ver simulacion o jugar
varvalue = input("Do you want to play or to see a simulation (1= yes/ 0= no): ")
varvalue = int(varvalue); qstion = 1

while qstion == 1:
    for turn in range(1, 999):
        #impresion movimientos del player
        print(f"Turn {turn}, player {chess.turn(self=chess, x=turn)} to play.")
        sleep(0.35)
        #posibilidad de torniquete o promocion de peon, y movimieto de las piezas
        if not (chess.castling(self=chess, turn=chess.turn(self=chess, x=turn), varvalue=varvalue) \
            and chess.pawn_promotion(self=chess, turn=chess.turn(self=chess, x=turn), varvalue=varvalue)):
            x = chess.move(self=chess, turn=chess.turn(self=chess, x=turn), varvalue=varvalue)
            print(x)
            print(chess.__str__(self=chess))
        #verificar fin del juego
        if not chess.game_over(self=chess):
            None
        else:
            #verificar nuevo juego
            qstion = input("do you want to play again? (1= yes/ 0= no):")
            qstion = int(qstion)
            if qstion == 1:
                qstion = 1; break
            elif qstion == 0: qstion = 0; break