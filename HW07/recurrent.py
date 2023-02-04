# easy variant of the task No.7
# GNU General Public License v3.0
def recu(size, x):
    if (size == 0):
        known[0] = -1
        return -1
    elif (size == 1):
        known[1] = x
        return x
    elif (size == 2):
        known[2] = (-(x + 1) / 3)
        return (-((x + 1) / 3))
    if (size in known):
        return known[size]
    value = (size / x) * recu(size - 1, x) + ((-1) ** size) * ((size + 1) / (size - 1)) * recu(size - 2, x) + ((size - 1) / (2 * x)) * recu(size - 3, x)
    known[size] = value
    return value
if __name__ == "__main__":
    size = int(input())
    x = float(input())
    known = {}  # dictionary data type, stores any calculated value to itself to improve speed
    #sum=-1
    sum=recu(size, x)
    print(sum)
