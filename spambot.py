# -*- coding: utf-8 -*-
from time import sleep
import vk_api
from vk_api.longpoll import VkLongPoll,VkEventType
from cfg_file import LOGIN, PASS, ID

id = ID
text = 'It is time to do something new'
f = False
def await_user():
    login, password = LOGIN, PASS
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        try:
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text == '1':
                print('id{}: "{}"'.format(event.user_id, event.text), end=' ')

                text = 'We a begining!'

                attachments = []

                vk.messages.send(
                    user_id=event.user_id,
                    attachment=','.join(attachments),
                    message=text
                )
                print('ok')
                return True
            elif event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text == '0':
                print('id{}: "{}"'.format(event.user_id, event.text), end=' ')
                return False
        except Exception as exc:
            print('Ошибка', exc)
def main(f):
    a = []

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

            sleep(10)

if __name__ == '__main__':
    f = await_user()
    main(f)
    

