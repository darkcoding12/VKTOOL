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
\033[01m
█             █
██           ██
█▒█         █▒█
█▄▄█▄▄▄▄▄▄▄█▄▄█
█▒▒▒▒▒▒▒▒▒▒▒▒▒█                                     
█▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  
█▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
█▒\033[34m█\033[0m\033[01m▒▒▒\033[34m█\033[0m\033[01m▒▒\033[34m█\033[0m\033[01m▒▒\033[34m█\033[0m\033[01m▒█▒▒▄▄▄▄▄▒▒▄▄▄▄▒▒▒▒▄▄▄▄▒▒▒█▒▒▒▒▒█ 
█▒\033[34m█\033[0m\033[01m▒▒▒\033[34m█\033[0m\033[01m▒▒\033[34m█\033[0m\033[01m▒\033[34m█\033[0m\033[01m▒▒█▒▒▒▒█▒▒▒█▒▒▒▒█▒▒█▒▒▒▒█▒▒█▒▒▒▒▒█  
█▒\033[34m█\033[0m\033[01m▒▒▒\033[34m█\033[0m\033[01m▒▒\033[34m██\033[0m\033[01m▒▒▒█▒▒▒▒█▒▒▒█▒▒▒▒█▒▒█▒▒▒▒█▒▒█▒▒▒▒▒█ 
█▒▒\033[34m█\033[0m\033[01m▒\033[34m█\033[0m\033[01m▒▒▒\033[34m█\033[0m\033[01m▒\033[34m█\033[0m\033[01m▒▒█▒▒▒▒█▒▒▒█▒▒▒▒█▒▒█▒▒▒▒█▒▒█▒▒▒▒▒█
█▒▒▒\033[34m█\033[0m\033[01m▒▒▒▒\033[34m█\033[0m\033[01m▒\033[34m█\033[0m\033[01m▒▒█▒▒▒▒█▒▒▒▒▀▀▀▀▒▒▒▒▀▀▀▀▒▒▒▀▀▀▀▀▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
 ▀███████████▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  
                                  
\033[0m
"""
menu = """
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█|\033[32m\033[01m1\033[0m| \033[01m\033[31mИстория VKTOOL\033[0m                       █
█|\033[32m\033[01m2\033[0m| \033[01m\033[31mРассылка сообщений\033[0m                   █
█|\033[32m\033[01m3\033[0m| \033[01m\033[31mБан страницы\033[0m                         █
█|\033[32m\033[01m4\033[0m| \033[01m\033[31mЗаполнить стену\033[0m                      █
█|\033[32m\033[01m5\033[0m| \033[01m\033[31mОчистить стену\033[0m                       █
█|\033[32m\033[01m6\033[0m| \033[01m\033[31mПроверить токен на валидность\033[0m        █
█|\033[32m\033[01m7\033[0m| \033[01m\033[31mСоздать Беседу\033[0m                       █
█|\033[32m\033[01m0\033[0m| \033[01m\033[31mEXIT\033[0m                                 █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
"""
#создать беседу тест
def chat()
    tok = input("[ACCESS-TOKEN] ► ") 
    token = vk_api.VkApi(token = tok) 
    vk = token.get_api()
    a = vk.friends.get()
    id = vk.friends.get()['items']
    list = id
    while(id):
        for ids in id:
            print('Беседа создана!')
            vk.messages.createChat(user_ids=list, title=namechat)
            posts = vk.friends.get()['items']
            time.sleep(80)
    
#создать посты
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
        main()
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
                vk.wall.post(message='121212121')
                print('Запрос отправленн. Ожидайте бана!')
                time.sleep(3)
            except Exception as er:
                print('Аккаунт в бане!')
                main()
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
            ange = randint(1000000, 9999999)
            vk.messages.send(user_id=ange, message=mes, random_id=get_random_id())
            time.sleep(3)
            print("Успешно отправленно!")
        except Exception as e:
            print('Стоят настройки приватности!')
    main()
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
    if num_menu == "6":
        chat()
    if num_menu == "0":
        os.system(e) 
    else:
        main()
main()
