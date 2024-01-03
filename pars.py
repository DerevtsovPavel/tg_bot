import bs4
import requests

def get_dat():
    '''
    вытаскиваем температуру в Чите с Яндекс Погоды
    :return:возвращаем температуру
    '''
    url = "https://yandex.ru/pogoda/?from=tableau_yabro"#адресс страницы
    responce = requests.get(url)
    soup = bs4.BeautifulSoup(responce.text, "lxml")#код страницы в формате lxml
    fin = soup.find('span',"temp__value temp__value_with-unit")#ищем объект span  с именем temp__value temp__value_with-unit
    return fin.text#вытаскиваем текст из объекта
