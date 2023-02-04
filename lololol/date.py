# difficult variant of the task No.3
# GNU General Public License v3.0
days_ordinal = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth',
                'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth',
                'eighteenth',
                'nineteenth', 'twentieth', '', '', '', '', '', '', '', '', '', 'thirtieth']
units = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
         'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
months_text = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
               'November', 'December']
tens = ['teen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety',
        'hundred', 'thousand']
months_num = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def error():  # prints ERROR & terminates the program
    print("ERROR")
    quit()
    return None
def num_check(input):  # checks the correctness of the entered numeric input
    dot = 0
    for i in range(len(input)):  # checks the number of '.'
        if (input[i] == '.'):
            dot += 1
    if (dot != 2):  # if the number of dots does not match, evaluate it as an error
        error()
    return None
def printing_txt_nums(sum_day, sum_month, sum_year):  # vypisuje textove datum
    if sum_year == 0:
        error()
    ten_day = sum_day // 10
    day = sum_day - ten_day * 10
    if (ten_day != 0 and ten_day * 10 + day > 20 and ten_day * 10 + day != 30):  # prints days with a dash
        print("the", tens[ten_day - 1] + "-" + days_ordinal[day - 1], end="")  # prints 20th & 30th
    elif (ten_day != 0):  # prints the days without a dash, and if they are not the 20th and 30th
        print("the", days_ordinal[ten_day * 10 + day - 1], end="")
    else:
        print("the", days_ordinal[day - 1], end="")
    print(" of", months_text[sum_month - 1], "", end="")  # prints out the month
    thousand = sum_year // 1000
    sum_year -= thousand * 1000
    if (thousand > 0 and thousand < 20):
        print(units[thousand - 1] + "thousand", end="")  # prints out thousands [1;19] of the year
    elif (thousand > 0):
        print(str(tens[thousand // 10 - 1]) + str(units[thousand % 10 - 1]) + "thousand", end="")  # prints tens of thousands [20;99] of the year
    hundred = sum_year // 100
    sum_year -= hundred * 100
    if (hundred > 0):
        print(units[hundred - 1] + "hundred", end="")  # prints out hundreds for the year
    ten_year = sum_year // 10
    if (0 < ten_year < 2):  # vypisuje jednotkodesitky u roku, pokud je rok mezi [..11 a ..19]
        print(units[sum_year - 1], end="")
    else:
        ten_year = sum_year // 10
        sum_year -= ten_year * 10
        if (ten_year > 0):
            print(tens[ten_year - 1], end="")  # vypisuje desitky u roku
        if (sum_year > 0):
            print(units[sum_year - 1], end="")  # vypisuje jednotky u roku
    return None
def num_input(input):  # prevadi vstupni hodnotu na cislo
    num_check(input)  # vyhodnocuje, jestli je vstup korektni
    sum = 0
    dot = 0
    for i in range(len(input) + 1):
        if i == len(input):  # pri poslednim cyklu ulozi ciselnou hodnotu roku
            year = sum
            if year > 99999 or year < 0:
                error()
            printing_txt_nums(day, month, year)  # posila ulozene ciselne hodnoty do funkce na vypisovani
        elif i < len(input):
            if (input[i] == '.'):  # po prvni tecce ulozi ciselnou hodnotu dne
                if (dot == 0):
                    day = sum
                elif (dot == 1):  # po druhe tecce ulozi ciselnou hodnotu mesice
                    month = sum
                    if (month > 12):  # kontroluje, ze zadany mesic neni vetsi jak 12
                        error()
                    if (not (months_num[month - 1] >= day)):  # kontroluje, ze spravny pocet dni pro dany mesic
                        error()
                    dot += 1
                dot += 1
                sum = 0
            else:
                if (dot < 2 and input[i + 1] != '.'):  # pricita hodnotu krat deset pro mesic
                    sum += int(input[i]) * 10
                elif (dot < 2):  # pricte hodnotu pro danou promennou
                    sum += int(input[i])
                if (dot >= 2):  # scita hodnotu pro rok
                    sum += int(input[i]) * (10 ** (len(input) - i - 1))
    return None
def number_finding(input):  # vypise ciselnou hodnotu daneho dne
    string = ''
    day = ''
    day1 = ''
    dash = -1
    day_count = 0
    for i in range(4):  # ulozi 4 znaky do promenne, na dane pozici se ocekava 'the '
        string += input[i]
        pos = i
    if (string != 'the '):  # hlida, ze input ma na spravnem miste 'of '
        error()
    for j in range(pos + 1, 20):  # hleda, jestli se nekde v cisle dne vyskytuje pomlcka
        if (input[j] == '-'):
            dash = j
            break
        elif (input[j] == ' '):  # pokud narazi na konec cisla a nenalezne pomlcku, ukonci cyklus
            break
    if (dash != -1):  # ve dni se objevuje pomlcka
        for k in range(pos + 1, dash):  # uklada pismeno po pismeni prvni cast cisla pred pomlckou
            day += input[k]
        if (day == 'twenty'):  # pta se, jestli je dany string 20
            day_count = 20
        elif (day == 'thirty'):  # nebo 30
            day_count = 30
        else:  # pokud ani jedno, vypise ERROR, protoze nic jineho nemuze byt
            error()
        for l in range(dash + 1, 20):
            if (input[l] == ' '):  # pokud narazi na mezeru za cislem, ukonci cyklus a ulozi si pozici
                end_of_num = l + pos
                break
            else:
                day1 += input[l]  # spojuje znaky pismeno po pismeni dokud nenarazi na mezeru
        for n in range(len(days_ordinal)):  # hleda jestli se ulozeny string shoduje s nekterym z nazvu v poli
            if (day1 == days_ordinal[n]):  # pokud ano, ulozi si jeho ciselnou hodnotu
                day_count += n + 1
                break
            if (n == 19):
                day_count = -1
    else:  # cislo dne je bez pomlcky
        for i in range(pos + 1, 20):
            if (input[i] == ' '):
                end_of_num = i + pos  # pokud narazi na mezeru za cislem, ukonci cyklus a ulozi si pozici
                break
            else:
                day += input[i]  # spojuje znaky pismeno po pismeni dokud nenarazi na mezeru
        for j in range(len(days_ordinal)):
            if (day == 'thirtieth'):  # hleda jestli je ulozeny string 30
                day_count = 30
                break
            elif (day == days_ordinal[j]):  # hleda jestli se ulozeny string shoduje s nekterym z nazvu v poli
                day_count = j + 1  # pokud ano, ulozi si jeho ciselnou hodnotu
                break
            else:
                day_count = -1
    if (day_count == -1):
        error()
    return end_of_num, day_count
def month_finding(input, end_of_day):  # vypise ciselnou hodnotu daneho mesice
    string = ''
    month = ''
    for i in range(end_of_day - 2, end_of_day + 1):  # ulozi 3 znaky do promenne, na dane pozici se ocekava 'of '
        string += input[i]
    if (string == 'of '):  # hlida, ze input ma na spravnem miste 'of '
        begg_month = i + 1  # ulozi si pozici zacatku slova se jmenem mesice
    else:
        error()  # pokud 'of ' neni na spravnem miste/je v jinem tvaru, vypise ERROR
    for i in range(begg_month, begg_month + 15):  # postupne uklada jednotlive pismena mesice do stringu
        if (input[i] != ' '):  # dokud nenarazi na mezeru, uklada pismena
            month += input[i]
        else:  # jakmile narazi na mezeru za mesicem, ukonci if
            end_of_month = i  # ulozi si, na jake pozici byla mezera za mesicem
            break
    for i in range(0, 12):  # porovna ulozeny string s korektne napsanymi nazvy mesicu
        if (month == months_text[i]):  # pokud se shoduje, vypise ciselnou hodnotu daneho mesice
            month_count = i
            break
        else:
            month_count = -1
    if (month_count == -1):  # pokud se string neshoduje s zadnym mesicem, vypise ERROR
        error()
    return end_of_month, month_count  # vrati pozici mezery za mesicem
def cipher_finding(input, posD):
    num = ''
    for i in range(posD + 1, len(input)):
        num += input[i]
        # print(","+str(cislo)+",")
        for j in range(len(units)):
            if (num == units[j]):  # hleda, jestli se string shoduje s nejakym z ulozench v poli
                numC = j + 1  # int hodnota cisla
                return numC, (posD + len(units[j]))  # jedna se o ciselnou hodnotu psaneho inputu a zaroven u pozici-1 kde skoncilo cislo
    else:
        return -1, -1
def tens_finding(input, posC):
    ten = ''
    for i in range(posC + 1, len(input)):
        ten += input[i]
        for j in range(len(tens)):
            if (ten == tens[j]):
                if (j > 9 and j < 11):
                    tenC = 1000
                elif (j == 11):
                    tenC = 10
                else:
                    tenC = (j + 1) * 10
                return tenC, (posC + len(tens[j]))
    else:
        return -1, -1
def year_finding(input, end_of_month):
    sum = 0
    tenC, posD = tens_finding(input, end_of_month)  # hledam nejdriv desitku, na vstupu muze bych rok napr "89"
    if (posD == -1):
        numC, posC = cipher_finding(input, end_of_month)
        if posC == len(input) - 1:
            return numC
        tenC, posD = tens_finding(input, posC)  # tisic
        sum = tenC * numC
        last = posD
        if last < len(input) - 1:
            tenC, posD = tens_finding(input, posD)
            if (posD == -1):
                numC, posC = cipher_finding(input, last)
                if posC == len(input) - 1:
                    return sum + numC
                tenC, posD = tens_finding(input, posC)  # sto
                sum += tenC * numC
                last = posD
                if last < len(input) - 1:
                    tenC, posD = tens_finding(input, posD)
                    if (posD == -1):
                        numC, posC = cipher_finding(input, last)
                        if posC == len(input) - 1:
                            return sum + numC
                        tenC, posD = tens_finding(input, posC)  # desitky
                        sum += tenC + numC
                        last = posD
                        if last < len(input) - 1:
                            numC, posC = cipher_finding(input, last)
                            if posC == len(input) - 1:
                                return sum + numC
                            else:
                                error()
                        elif (last == len(input) - 1):
                            return sum
                    elif (posD == len(input) - 1):
                        sum += tenC
                    elif (posD < len(input) - 1):
                        numC, posC = cipher_finding(input, posD)
                        if (posC == len(input) - 1):
                            sum += tenC + numC
                        else:
                            error()
            elif (posD == len(input) - 1):
                sum += tenC
            elif (posD < len(input) - 1):
                numC, posC = cipher_finding(input, posD)  # vrati ciselnou hodnotu
                if (posC == len(input) - 1):
                    sum += tenC + numC
                else:
                    error()
    elif (posD == len(input) - 1):
        sum = tenC
    elif (posD < len(input) - 1):
        numC, posC = cipher_finding(input, posD)  # vrati ciselnou hodnotu
        if (posC == len(input) - 1):
            sum = tenC + numC
        else:
            error()
    return sum
def txt_input(input):  # ridici funkce, ktera v chronologickem poradi pousti jednotlive funkce
    end_of_day, day_count = number_finding(input)
    end_of_month, month_count = month_finding(input, end_of_day)
    year_count = year_finding(input, end_of_month)
    if (day_count <= months_num[month_count]):
        print(str(day_count) + "." + str(month_count + 1) + "." + str(year_count))
    else:
        error()
    return None
if __name__ == "__main__":
    input = input()
    if (ord(input[0]) >= 48 and ord(input[0]) <= 57):  # pozna, jestli se jedna o ciselny nebo pisemny input
        num_input(input)
    elif (input[0] == 't'):  # pisemny input musi vzdy zacinat s t, takze tim zaroven ochranim zavadny input
        txt_input(input)
    else:  # pokud se nejedna o ciselny nebo korektni pisemny input, vypise ERROR
        error()
"""""        
Nektere komentare jsou v cestine, nektere v anglictine, to same plati pro promenne. 
Byl jsem uz moc liny to prepisovat + mi dochazel cas, ale na pozadani muzu doplnit :).
"""""
