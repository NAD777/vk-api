# -*- coding: utf-8 -*-

import requests

import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from cfg_file import LOGIN, PASS, ID

def main():
    session = requests.Session()

    # Авторизация пользователя:
    login, password = LOGIN, PASS
    vk_session = vk_api.VkApi(login, password)
    
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()

    upload = VkUpload(vk_session)  # Для загрузки изображений
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        try:
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                print('id{}: "{}"'.format(event.user_id, event.text), end=' ')

                text = 'Привет, стрелок! ' + event.text[::-1] + ' Пленных не брать!'

                attachments = []

                # if image_url:
                #     image = session.get(image_url, stream=True)
                #     photo = upload.photo_messages(photos=image.raw)[0]

                #     attachments.append(
                #         'photo{}_{}'.format(photo['owner_id'], photo['id'])
                #     )

                vk.messages.send(
                    user_id=event.user_id,
                    attachment=','.join(attachments),
                    message=text
                )
                print('ok')
        except Exception as exc:
            print('Ошибка', exc)


if __name__ == '__main__':
    main()
