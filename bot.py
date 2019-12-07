import requests
import misc

from valute_bot import Parsing
# import json
import time
import valute_bot

token = misc.token
URL = 'https://api.telegram.org/bot' + token + '/'

global last_update_id
last_update_id = 0


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()
    last_object = data['result'][-1]
    current_update_id = last_object['update_id']

    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id

        chat_id = last_object['message']['chat']['id']
        message_text = last_object['message']['text']

        message = {'chat_id': chat_id,
                   'text': message_text}
        return message
    return None


def send_message(chat_id, text='Wait a second, please...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def main():
    obj = Parsing()
    obj.get_table()
    # print(obj.total_inf(obj.data))
    # d = get_updates()

    # with open('updates.json', 'w') as file:
    #     json.dump(d, file, indent=2, ensure_ascii=False)
    while True:
        answer = get_message()
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']
            if text == '/start':
                for obbs in obj.data.get('bank'):
                    sobsheniye = f"У банка {obj.data.get('bank')[obbs]}, \n" \
                                 f"по адрессу {obj.data.get('location')[obj.data.get('bank')[obbs]]['Adress']}, \n" \
                                 f"номер телефона:{obj.data.get('location')[obj.data.get('bank')[obbs]]['Phone']}, \n" \
                                 f"покупная цена $ {obj.data.get('buy_price')[obj.data.get('bank')[obbs]]} KGS,\n" \
                                 f"цена продажи $ {obj.data.get('sell_price')[obj.data.get('bank')[obbs]]} KGS"
                    send_message(chat_id, sobsheniye)
        else:
            continue

            sleep(3)

if __name__ == '__main__':
    main()
