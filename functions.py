import re
def create_k_a_b(s:str):
    '''
    вытаскиваем из строки кол-во генерируемых чисел и их диапазон
    :param s: исходная строка
    :return: кортеж из кол-ва, нижней и верхней границы
    '''
    m = re.search(r"\d+", s)  # n
    k = int(s[m.start():m.end()])

    cur_s = s[m.end():len(s)]


    m = re.search(r"-?\d+", cur_s)#a
    a = int(cur_s[m.start():m.end()])

    cur_s = cur_s[m.start() + 1:len(cur_s)]


    m = re.search(r"-?\d+", cur_s)#b
    b = int(cur_s[m.start():m.end()])

    return k,a,b


def type_file(s:str):
    '''
    возвращает тип файла из имени файла
    :param s:имя файла
    :return:тип файла
    '''
    m = re.search(r"[.]\w+",s)#ищем .type
    tp = s[m.start()+1:len(s)]
    return tp

def create_str_from_arr(a:list):
    s=""
    for i in range (len(a)):
        s = s + str(a[i]) + " "

    return s