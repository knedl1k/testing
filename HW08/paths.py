import sys
def loadBoard(filename):
    # načtení souboru a vytvoření 2D matice
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            matrix.append(line.strip().split(' '))
    return matrix
def inside_check(matrix, row, col):
    return (row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0]))
def vlevo(barva, piece, row, col):
    if (piece[row][col][2] == barva):
        return True
    return False
def nahoru(barva, piece, row, col):
    if (piece[row][col][3] == barva):
        return True
    return False
def vpravo(barva, piece, row, col):
    if (piece[row][col][0] == barva):
        return True
    return False
def dolu(barva, piece, row, col):
    if (piece[row][col][1] == barva):
        return True
    return False
def korektni_konec(piece, row, col, barva,zacatek):
    if(piece[row][col][2] == barva and col == len(piece[row])-1 and zacatek==0):
        return 1
    if(piece[row][col][3]==barva and row==len(piece)-1 and zacatek==1):
        return 1
    return 0
def najdi_smer(piece, row, col, barva, smer):
    for i in range(4):
        if (i == smer):
            continue
        if (piece[row][col][i] == barva):
            return i

def nasleduj_caru(piece, row, col, smer, barva, pocet_dilku,zacatek):  # poslu sem uz souradnice 2. dilku, do ktereho cesta urcite pokracuje
    # smer je hodnota vstupu dalsiho dilku
    max_delka = -1
    #posledni=None
    kompletni = True
    smer = najdi_smer(piece, row, col, barva, smer)  # smer kudy pryc
    while (kompletni == True):
        stara_col=col
        stara_row=row
        #if posledni==piece[row][col]:
        #    return -1
        #print("smer1",smer)
        #print(piece[row][col], row, col, smer)
        #print("dilky:", pocet_dilku)
        #print("smer",smer)
        if(row==len(piece)-1 or col==len(piece[row])-1):
            konec=korektni_konec(piece, row, col, barva,zacatek)
            if konec==1:
                pocet_dilku+=1
                break
        if (smer == 0 and inside_check(piece, row, col - 1)):
            kompletni = vlevo(barva, piece, row, col - 1)
            if (kompletni == True):
                pocet_dilku += 1
                col = col - 1
                smer = najdi_smer(piece, row, col, barva, 2) #smer kudy pryc
            else:
                pocet_dilku = -1
        elif (smer == 1 and inside_check(piece, row - 1, col)):
            # cesta pokracuje nahoru
            kompletni = nahoru(barva, piece, row - 1, col)
            if (kompletni == True):  # cesta korektne navazuje
                pocet_dilku += 1
                row = row - 1
                smer = najdi_smer(piece, row, col, barva, 3)
            else:
                pocet_dilku = -1
        elif (smer == 2 and inside_check(piece, row, col + 1)):
            # cesta pokracuje vpravo
            kompletni = vpravo(barva, piece, row, col + 1)
            if (kompletni == True):  # cesta korektne navazuje
                pocet_dilku += 1
                col = col + 1
                smer = najdi_smer(piece, row, col, barva, 0) #smer kudy pryc
            else:
                pocet_dilku = -1
        elif (smer == 3 and inside_check(piece, row + 1, col)):
            # cesta pokracuje dolu
            kompletni = dolu(barva, piece, row + 1, col)
            if (kompletni == True):  # cesta korektne navazuje
                pocet_dilku += 1
                row = row + 1
                smer = najdi_smer(piece, row, col, barva, 1) #smer kudy pryc
            else:
                pocet_dilku = -1
        else:
            pocet_dilku = -1
        if(stara_col==col and stara_row==row):
            pocet_dilku=-1
            break
    #print("dilky:", pocet_dilku, max_delka)
    max_delka = max(max_delka, pocet_dilku)
    return max_delka

def ridici(piece, barva, zacatek):  # najde korektne otocenou pocatecni kostku a spusti chuzi po care
    celkovy_pocet = -1
    #print("----------zac:",zacatek)
    if(zacatek==0):
        for row in range(len(piece)):
            pocet_dilku = -1
            if (piece[row][0][0] == barva):
                # nasel spravny zacatek
                #print("nasel jsem!", row)
                pocet_dilku = 0
                for i in range(1, 4):
                    if (piece[row][0][i] == barva):  # hleda druhy vyskyt hledane barvy v dilku, abych vedel, jakym smerem smeruje
                        smer = i
                        break
                if (smer == 1 and inside_check(piece, row - 1, 0)):
                    # cesta pokracuje nahoru
                    kompletni = nahoru(barva, piece, row - 1, 0)
                    if (kompletni == True):  # cesta korektne navazuje
                        pocet_dilku += 1
                        pocet_dilku = nasleduj_caru(piece, row - 1, 0, 3, barva, pocet_dilku,zacatek)
                    else:
                        pocet_dilku = -1
                elif (smer == 2):
                    # cesta pokracuje vpravo
                    kompletni = vpravo(barva, piece, row, 1)
                    if (kompletni == True):  # cesta korektne navazuje
                        pocet_dilku += 1
                        pocet_dilku = nasleduj_caru(piece, row, 1, 0, barva, pocet_dilku,zacatek)
                    else:
                        pocet_dilku = -1
                elif (smer == 3 and inside_check(piece, row + 1, 0)):
                    # cesta pokracuje dolu
                    kompletni = dolu(barva, piece, row + 1, 0)
                    if (kompletni == True):  # cesta korektne navazuje
                        pocet_dilku += 1
                        pocet_dilku = nasleduj_caru(piece, row + 1, 0, 1, barva, pocet_dilku,zacatek)
                    else:
                        pocet_dilku = -1
                else:
                    pocet_dilku = -1
            else:
                pocet_dilku = -1
            celkovy_pocet = max(celkovy_pocet, pocet_dilku)
    else:
        for col in range(len(piece[0])):
            pocet_dilku = -1
            if (piece[0][col][1] == barva):
                # nasel spravny zacatek
                #print("nasel jsem!", col)
                pocet_dilku = 0
                for i in range(0, 4):
                    if (piece[0][col][i] == barva):  # hleda druhy vyskyt hledane barvy v dilku, abych vedel, jakym smerem smeruje
                        if(i==1):
                            continue
                        smer = i
                        break
                if (smer == 0 and inside_check(piece, 0, col - 1)):
                    # cesta pokracuje nahoru
                    kompletni = vlevo(barva, piece, 0, col-1)
                    if (kompletni == True):  # cesta korektne navazuje
                        pocet_dilku += 1
                        pocet_dilku = nasleduj_caru(piece, 0, col-1, 2, barva, pocet_dilku,zacatek)
                    else:
                        pocet_dilku = -1
                elif (smer == 2 and inside_check(piece,0,col+1)):
                    # cesta pokracuje vpravo
                    kompletni = vpravo(barva, piece, 0, col+1)
                    if (kompletni == True):  # cesta korektne navazuje
                        pocet_dilku += 1
                        pocet_dilku = nasleduj_caru(piece, 0, col+1, 0, barva, pocet_dilku,zacatek)
                    else:
                        pocet_dilku = -1
                elif (smer == 3 and inside_check(piece, 1, col)):
                    # cesta pokracuje dolu
                    kompletni = dolu(barva, piece, 1, col)
                    if (kompletni == True):  # cesta korektne navazuje
                        pocet_dilku += 1
                        pocet_dilku = nasleduj_caru(piece, 1, col, 1, barva, pocet_dilku,zacatek)
                    else:
                        pocet_dilku = -1
                else:
                    pocet_dilku = -1
            else:
                pocet_dilku = -1
            celkovy_pocet = max(celkovy_pocet, pocet_dilku)
    return celkovy_pocet
if __name__ == "__main__":
    filename=sys.argv[1] #při nahrání do BRUTE odkomentovat
    #filename = "paths.txt"
    board = loadBoard(filename)
    delky=[]
    barvy=['l','d']
    for i in range(2): #vsechny kombinace check
        for barva in barvy: #obe barevne kombinace pro danou hraci desku (l a d)
            delky.append(ridici(board,barva,i))
    for i in range(len(delky)):
        print(delky[i],end=" ")