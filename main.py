import re
import bot as bt
import functions as fc
from numpy import set_printoptions
import telebot
import pars as pr

set_printoptions(precision=2)
token = "мой токен"
b = telebot.TeleBot(token)
Flag = True
bo = bt.simp_bot()#объект моего бота

@b.message_handler(content_types=['text']) #ловим текстовые сообщения от пользователя
def mess (message):
        s = message.text #берём текст сообщения
        s = s.lower()
        match_hi = re.fullmatch(r"\w*\s*п\w*в\w*т\s*\w*", s)  # бот привет бот
        match_bi = re.fullmatch(r"\w*\s*д\w*\s*с\w*н\w*я\s*\w*|п\w*ка", s)  # бот досвидания бот
        match_jk = re.fullmatch(r"р\w*ж\w*\s*а\w*т", s)  # расскажи анекдот
        match_dela = re.fullmatch(r"как\s*д\w*ла[?]?", s)  # как дела
        match_good = re.fullmatch(r"х\w*шо|от\w*но", s)  # хорошо или отлично
        match_bad = re.fullmatch(r"не\s*х\w*шо|не\s*от\w*но|пл\w*хо", s)
        match_gen = re.fullmatch(r"\w+\s*\d+\s+\w*\s+\w*\s*-?\d+\s+\w*\s+-?\d+", s)  # сгенерируй n чисел от а до б
        match_file = re.fullmatch(r"вы\w*и\s*\w*\s*\w*\s*\w*[.]\w+", s)  # выведи содержимое файла а.type
        match_weather = re.fullmatch(r"\w*\s*т\w*м\w*ра\s*\w*\s*\w*",s)#температура

        if match_hi:#если здороваются
            ans = bo.say_hi()
            b.send_message(message.from_user.id,ans)

        elif match_bi:#если прощаются
            ans = bo.say_bi()
            b.send_message(message.from_user.id, ans)


        elif match_jk:#просят анекдот
           ans = bo.say_joke()
           b.send_message(message.from_user.id, ans)

        elif match_gen:#генерируем n чисел от a до b
            cor = fc.create_k_a_b(s)#вытаскиваем необходимые числа

            n = cor[0]#кол-во генерируемых чисел
            min = cor[1]
            max = cor[2]

            c = bo.generate_array(n, min, max)#генерируем массив чисел
            b.send_message(message.from_user.id,"Ваши числа")
            ans = fc.create_str_from_arr(c)#делаем строку
            b.send_message(message.from_user.id,ans)#отправляем строку


        elif match_dela:#отвечаем на как дела
            ans = bo.say_dela()
            b.send_message(message.from_user.id, ans)
            b.send_message(message.from_user.id,"А у вас?")

        elif match_good:#реагируем на хорошо
            b.send_message(message.from_user.id,"Рад за вас")

        elif match_bad:#реагируем на плохо
            b.send_message(message.from_user.id, "Всё наладится")


        elif match_file:#выводим содержимое файла
            m = re.search(r"\w+[.]\w+", s)#ищем имя файла с его типом
            fn = s[m.start():m.end()]#имя файла
            t_f = fc.type_file(fn)#тип файла

            if t_f == 'txt':
                st = bo.read_txt(fn)
                ans = fc.create_str_from_arr(st)
                b.send_message(message.from_user.id, ans)

            elif t_f == 'json':
                st = bo.read_json(fn)
                ans = fc.create_str_from_arr(st)
                b.send_message(message.from_user.id, ans)

            elif t_f == 'xlsx':
                st = bo.read_excel(fn)
                ans = fc.create_str_from_arr(st)
                b.send_message(message.from_user.id, ans)


            elif t_f == 'csv':
                st = bo.read_csv(fn)
                b.send_message(message.from_user.id, st)

            else:#если не поддерживаемый тип
                b.send_message(message.from_user.id, "Тип файла не поддерживается")

        elif match_weather:#если спрашивают температуру
            t = pr.get_dat() + " градусов"
            b.send_message(message.from_user.id, t)

        elif s == "\start" or s=="\help":
            b.send_message(message.from_user.id, "Привет, вот мои команды")
            ans = bo.say_about()
            for i in range (len(ans)):
                b.send_message(message.from_user.id, ans[i])

        else:#отвечаем на непредусмотренные команды
            b.send_message(message.from_user.id, "Не знаю")



b.polling(none_stop=True, interval=0)
