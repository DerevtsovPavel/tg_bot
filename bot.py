import random
import json as js
import pandas as pd
from numpy import transpose
import os.path

class simp_bot:
    dela = {
        1: "Хорошо",
        2: "Не очень"
    }
    hello = {
        1: "Привет",
        2: "Здравствуйте",
        3: "С возвращением"
    }
    joke = {
        1: 'Электрик Жора получил разряд не став спортсменом.',
        2: "ХаХА"
    }
    def say_hi(self):
        c = random.randint(1,3)
        return self.hello[c]

    def say_bi(self):
        return "До свидания"

    def say_joke(self):

        c = random.randint(1,2)
        return self.joke[c]

    def generate_array(self,n:int, a:int ,b:int):
        m=[]
        for i in range (n):
            c = random.randint(a,b)
            m.append(c)
        return m

    def read_txt(self,fn:str):
        '''
        считывает массив строк из текстового файла fn
        :param fn:имя текстового файла
        :return:массив строк
        '''
        st = []
        if os.path.exists(fn):

            with open(fn, 'r') as f:
                st = f.readlines()  # считываем все строки в файле

            for i in range (len(st)):
                st[i]=st[i][:len(st[i])-1]#убираем символ конца строки
        else: st = "Файла не существует"
        return st

    def read_json(self,fn:str):
        '''
        читает json файл и возврощает массив строк
        :param fn: имя файла
        :return: массив строк
        '''
        st = []
        if os.path.exists(fn):
            with open(fn, 'r') as f_j:
                st = js.load(f_j)  # возвращаем массив из json файла

            for i in range (len(st)):
                st[i]=st[i][:len(st[i])-1]#убираем символ конца строки
        else: st = "Файла не существует"
        return st

    def read_excel(self,fn:str):
        '''
        читает exel файл и возвращает матрицу значений
        :param fn:имя файла
        :return:матрица с содержимым excel таблицы
        '''
        tr_st=[]
        if os.path.exists(fn):
            data = pd.read_excel(fn, index_col=None, header=None)  # читаем в датафрейм лист эксель
            st = []
            for i in range(len(data.keys())):
                a = []
                for j in range(len(data[i])):
                    a.append(data[i][j])
                st.append(a)

            tr_st = transpose(st)#транспонируем матрицу
        else:
            tr_st = "Файла не существует"
        return tr_st

    def read_csv(self, fn:str):

        data = []
        if os.path.exists(fn):
            list = pd.read_csv(fn, delimiter=";", index_col=None)  # читаем в датафрейм лист эксель
            l_l = []
            l_l.append(list)

            for i in range (len(l_l)):
                a = []
                for j in range (len(l_l[i])):
                    a.append(l_l[i])
                data.append(a)


        else: data = "Файла не существует"
        return data

    def say_dela(self):

        c = random.randint(1,2)
        return self.dela[c]

    def say_about(self):
        a=[]
        a.append("1. Отвечаю на привет, пока, как дела")
        a.append("2. Вывожу содержимое txt, xlsx, csv, json файлов")
        a.append("3. Рассказываю анекдот")
        a.append("4. Генерирую n целых чисел от а до b")
        a.append("5. Вывожу температуру в Чите с сайта Яндекс Погода")
        return a
