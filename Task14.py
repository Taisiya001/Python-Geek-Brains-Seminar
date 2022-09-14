N = float(input('Введите число: '))
С = str(N)
def get_count(N):
    C = str(N)
    if '.' in C:
        return abs(C.find('.') - len(C)) - 1
    else:
        return 0
get_count(N)
    