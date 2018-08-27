# -*- coding: utf-8 -*-
from time import sleep
import vk_api
from vk_api.longpoll import VkLongPoll,VkEventType
from cfg_file import LOGIN, PASS, ID

id = ID
text = 'Пора заняться чем-то новым'

def main():
    a = []
    while True:
        with open('123.txt') as f:
            for line in f:

                a = list(map(str, line.split(';')))
                print(a)

                # Авторизация пользователя:
                login, password = a[0], a[1]
                vk_session = vk_api.VkApi(login, password)
                try:
                    vk_session.auth(token_only=True)
                except vk_api.AuthError as error_msg:
                    print(error_msg)
                    continue # or just return

                vk = vk_session.get_api()

                longpoll = VkLongPoll(vk_session)

                attachments = []

                vk.messages.send(user_id=id,attachment=','.join(attachments),message=text)
                vk.messages.deleteConversation(peer_id = id) #очистка переписки по id
                for event in longpoll.listen():
                    try:
                        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                            print('id{}: "{}"'.format(event.user_id, event.text), end=' ')
                            print('ok')
                    except Exception as exc:
                        print('Ошибка', exc)
                sleep(2)

if __name__ == '__main__':

    main()
    

