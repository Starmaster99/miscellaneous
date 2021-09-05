# радио для самых маленьких
# как узнать chat_id: https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id

import requests

token = ''              # токен вашего бота
list_of_groups = ['']   # список чатов, в которые бы вы хотели отправлять {message}
message = 'Как дела?'   # ваше сообщение. мгновенно отсылается в выбранные чаты при запуске


def send_msg(list_of_groups, message):
    for id_list in list_of_groups:
        url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id_list}&text={message}&parse_mode=HTML'
        resp = requests.get(url)
        print(resp.text)


send_msg(list_of_groups, message)
