#!/usr/bin/env python3
import copy
import random
from random import shuffle

import base as Base
import draw as Drawer

class Player(Base.BasePlayer):
    def __init__(self, board, name, color):
        Base.BasePlayer.__init__(self, board, name, color)
        self.algorithmName = "UGANDAv0.5"
    def get_suitable_neighbor(self, row, col):  # returns first empty space which can be played
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if (i == j or i == -j or not self.inside(row + 1 * i, col + 1 * j)):
                    continue
                # cat=self.get_forced_color(row+1*i,col+1*j,self.board)

                if (self.board[row + 1 * i][col + 1 * j] == "none"):
                    return 1 * i, 1 * j
        return 0, 0
    def get_color(self, row, col, pos, deska):  # returns color of connection
        return deska[row][col][pos]
    def get_positions(self, row, col, radek, sloupec, first):  # returns all required values
        if (sloupec == 0):
            color = self.get_color(row, col, 2 + radek, self.board)
        else:
            color = self.get_color(row, col, 1 + sloupec, self.board)
        if (radek == 1):
            neigh = 1
        elif (radek == -1):
            neigh = 3
        elif (sloupec == 1):
            neigh = 0
        elif (sloupec == -1):
            neigh = 2
        if first is True:
            return [row + radek, col + sloupec, color, neigh]
        else:
            return neigh, self.my2other[neigh]
    def get_playable_position(self):  # najde prvni moznou hratelnou pozici = najde jiz polozeny dilek a hleda, jestli ma okolo sebe None
        positions=[]
        if not any("none" in tile for tile in self.board):  # pokud se na desce uz nevyskytuje volne misto
            return []
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] != "none":
                    radek, sloupec = self.get_suitable_neighbor(row, col)
                    if (radek == sloupec == 0):
                        continue
                    else:
                        ###print(radek,sloupec,row,col)
                        positions.append(self.get_positions(row, col, radek, sloupec, True))
        return positions
    def is_suitable(self, row, col, piece):  # checks if the picked tile is really suitable for playing
        all_four = 0
        for radek in [-1, 0, 1]:
            for sloupec in [-1, 0, 1]:
                if radek == sloupec or radek == -sloupec:
                    continue
                if not self.inside(row + 1 * radek, col + 1 * sloupec) or self.board[row + 1 * radek][
                    col + 1 * sloupec] == "none":
                    all_four += 1
                    continue
                neigh, own = self.get_positions(row, col, radek, sloupec, False)
                if piece[own] == self.board[row + 1 * radek][col + 1 * sloupec][neigh]:
                    all_four += 1
                else:
                    return False
        return True if all_four == 4 else False
    def get_piece(self, color, neigh, row, col):  # returns array of all playable pieces with this type of enter position of color
        pieces = []
        for dilek in self.tiles:
            if dilek[neigh] == color:
                pieces.append(dilek)
        random.shuffle(pieces)
        return pieces
    def check_col(self, tile):
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if (i == j or i == -j or not self.inside(row + 1 * i, col + 1 * j) or tile[row + 1 * i][
                    col + 1 * j] == "none"):
                    continue
                if (i == 1):
                    neigh = 1
                elif (i == -1):
                    neigh = 3
                elif (j == 1):
                    neigh = 0
                elif (j == -1):
                    neigh = 2
    def get_forced_color(self, row, col, deska,radek,sloupec,barvy):
        # jsem ted na prazdnem poli, ktere kontroluju
        ##print("kontroluju:", deska[row + 1 * radek][col + 1 * sloupec])
        if (sloupec == 0):
            color = self.get_color(row + 1 * radek, col + 1 * sloupec, 2 - radek, deska)
        else:
            color = self.get_color(row + 1 * radek, col + 1 * sloupec, 1 - sloupec, deska)
            ##print(color)
        if (radek == 1):  # muj prazdny musi navazovat na 2
            neigh = 1
        elif (radek == -1):  # muj prazdny musi navazovat na 0
            neigh = 3
        elif (sloupec == 1):  # muj prazdny musi navazovat na 1
            neigh = 0
        elif (sloupec == -1):  # muj prazdny musi navazovat na 3
            neigh = 2
        barvy[self.my2other[neigh]] = color  # ukladam, na jake pozici moji prazdne kostky musi byt barva na navazovani
        ##print("navrhuju jako forced:", barvy,"na pozici:",row + 1 * radek, col + 1 * sloupec)
        return barvy
    def get_forced_moves(self, deska,forced_moves):
        while True:
            # Procházej hrací plochu a hledej prázdná místa, do kterých vedou dvě cesty stejné barvy z okolních dílků
            for row in range(len(deska)):
                for col in range(len(deska[0])):
                    if deska[row][col] == "none":
                        barvy = ["n","n","n","n"]
                        ##print("#####kontroluju okoli",row,col)
                        for radek in [-1, 0, 1]:
                            for sloupec in [-1, 0, 1]:
                                if radek == sloupec or radek == -sloupec or not self.inside(row + 1 * radek, col + 1 * sloupec):
                                    continue
                                if deska[row + 1 * radek][col + 1 * sloupec] != "none":
                                    barvy=self.get_forced_color(row, col, deska,radek,sloupec,barvy)
                                #print("tah:",barvy,"na coord",row + 1 * radek,col + 1 * sloupec)
                        tah = "".join(str(x) for x in barvy)
                        pocetL=tah.count('l')
                        pocetD=tah.count('d')
                        if pocetL>2 or pocetD>2:
                            #print("tady")
                            return None
                        if pocetL == 2:
                            tah = tah.replace('n', 'd')
                        elif pocetD == 2:
                            tah = tah.replace('n', 'l')
                        if tah in self.tiles:  # pokud vedou dve stejne barvy do meho prazdneho, umistit konkretni dilek
                            #print("nutny tah", tah)
                            deska[row][col] = tah
                            forced_moves.append([row, col, tah])
                            #print("validni forced:", forced_moves)
                            self.get_forced_moves(deska, forced_moves)
            break
        # Zkontroluj, zda nevzniklo prázdné místo, do kterého vedou více než 2 cesty stejné barvy
        for row in range(len(deska)):
            for col in range(len(deska[0])):
                if deska[row][col] == "none":
                    barvy = ["n","n","n","n"]
                    for radek in [-1, 0, 1]:
                        for sloupec in [-1, 0, 1]:
                            if radek == sloupec or radek == -sloupec or not self.inside(row + 1 * radek, col + 1 * sloupec):
                                continue
                            barvy=self.get_forced_color(row, col, deska,radek,sloupec,barvy)
                            # Pokud vedou více než 2 cesty stejné barvy, tah není platný a hra končí
                            if barvy.count('l')>2 or barvy.count('d')>2:
                                #print("Invalid move - more than 2 paths with the same color lead to this location.")
                                return None
         ##print("pryc forced:",forced_moves)
        return forced_moves
    def forced_moves(self,piece,playable_piece):
        tah=[]
        deska=copy.deepcopy(self.board)
        deska[playable_piece[0]][playable_piece[1]]=piece
        forced_moves = self.get_forced_moves(deska,[])
        if forced_moves is None:  # musim zmenit pocatecni dilek
            return None
        elif len(forced_moves)==0: #nejsou zadne vynucene tahy
            return []
        else:
            ##print("XXXXXXXXXXXXXXXXXXXXXXXX pridavam")
            return forced_moves
    def move(self):
        tah = []
        ###TODO if there is no suitable tile, picks another playable position out of the array with suffled playable positions
        playable_pieces2 = self.get_playable_position()  # Picks one of eligible spaces to play
        random.shuffle(playable_pieces2)
        if len(playable_pieces2)== 0:  # If there are no empty spaces, return without placing a piece
            ##print("playable")
            return []
        j=0
        while j<len(playable_pieces2):
            pos = 0
            playable_piece = playable_pieces2[j]
            #print(playable_pieces2,"XXXXXXXXXX",playable_piece)
            pieces = self.get_piece(playable_piece[2], playable_piece[3], playable_piece[0], playable_piece[1])
            while pos < 3:  # if the first picked tile is not suitable, picks next one. If none of them is suitable, returns []
                if self.is_suitable(playable_piece[0], playable_piece[1], pieces[pos]):
                    tah.append([playable_piece[0], playable_piece[1], pieces[pos]])
                    ##print("navrhuju:", tah)
                    forced=self.forced_moves(pieces[pos],playable_piece)
                    if forced is None:
                        tah.pop()
                        pos+=1
                    elif len(forced)==0:
                        j = len(playable_pieces2)
                        break
                    else:
                        for i in range(len(forced)):
                            tah.append(forced[i])
                        j=len(playable_pieces2)
                        break
                else:
                    pos += 1
                ##print("pos:",pos)
            else:
                ##print(playable_pieces2)
                j+=1
                if j==len(playable_pieces2):
                    ##print(tah)
                    return []
        ##print("hraje:", tah)
        new_tah = []
        for elem in tah:
            if not elem in new_tah:
                new_tah.append(elem)
        return new_tah

if __name__ == "__main__":
    #boardRows = 12
    #boardCols = boardRows
    #board = [["none"] * boardCols for _ in range(boardRows)]
    #board[boardRows // 2][boardCols // 2] = ["lldd", "dlld", "ddll", "lddl", "dldl", "ldld"][random.randint(0, 5)]
    board = [['none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none'],
                  ['none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none'],
                  ['none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none'],
                  ['none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none'],
                  ['none', 'none', 'lldd', 'ddll', 'lldd', 'dlld', 'lddl', 'dlld', 'lddl', 'dlld', 'none'],
                  ['ddll', 'lddl', 'ddll', 'lldd', 'ddll', 'lddl', 'dlld', 'lddl', 'dlld', 'ldld', 'ldld'],
                  ['lldd', 'dlld', 'lldd', 'ddll', 'lldd', 'dlld', 'lddl', 'dlld', 'none', 'none', 'lddl'],
                  ['none', 'none', 'none', 'lldd', 'ddll', 'lddl', 'none', 'none', 'none', 'none', 'dlld'],
                  ['none', 'none', 'none', 'none', 'lldd', 'dldl', 'none', 'none', 'none', 'none', 'ldld'],
                  ['none', 'none', 'none', 'none', 'lddl', 'dlld', 'lldd', 'dldl', 'ddll', 'ldld', 'ldld'],
                  ['none', 'none', 'none', 'none', 'none', 'ddll', 'lddl', 'dlld', 'lldd', 'ddll', 'ldld']]
    d = Drawer.Drawer()
    p1 = Player(board, "player1", 'l');
    p2 = Player(board, "player2", 'd');
    idx = 0
    while (True):
        rmove = p1.move()  # call player for his move
        for move in rmove:
            row, col, tile = move
            p1.board[row][col] = tile
            p2.board[row][col] = tile
        d.draw(p1.board, "moves/move-{:04d}.png".format(idx))  # make png with resulting board
        idx += 1
        if len(rmove) == 0:
            #print("End of game")
            break
        p1, p2 = p2, p1  # switch players
