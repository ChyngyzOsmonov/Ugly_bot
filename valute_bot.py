import requests
from bs4 import BeautifulSoup

# url = 'https://valuta.kg/'
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# html = get_html(url)
#
#
# def total_inf(data):
#     return data
#
#
# data = {}
#
# def get_table(html):
#     soup = BeautifulSoup(html, 'lxml')
#
#     ads = soup.find('div', class_='rate-list active').find('tbody').find_all('tr')
#     for ad in ads:
#         try:
#             title = ad.find('td').find('div', class_='td-member__info').find('h4').find('a').text.strip()
#             data['title'] = title
#             # print(title)
#         except:
#             title = ''
#         try:
#             adress = ad.find('td').find('div', class_='td-member__info').find('p').text.split()[1:7]
#             mergelist = (''.join(map(str, adress[0:2])))
#             mergelist1 = (''.join(map(str, adress[2:7])))
#             # print(mergelist,mergelist1)
#         except:
#             mergelist1 = ''
#         try:
#             buy = ad.find('td', class_='td-rate td-rate--even').find('div', class_='td-rate__wrp').text.strip()
#             data['buy'] = buy
#
#             # print(buy)
#         except:
#             buy = ''
#         try:
#             sell = ad.find('td', class_='td-rate td-rate--even -last-in-group').find('div', class_='td-rate__wrp').text.strip()
#             data['sell'] = sell
#
#             # print(sell)
#         except:
#             sell = ''
#
#         try:
#             # data = {'title': title,
#             #         'mergelist1': mergelist1,
#             #         'buy': buy,
#             #         'sell': sell}
#             pass
#
#
#         except:
#             print("pusto")
#
# get_table(html)
# print(total_inf(data))







class Parsing:

    url = 'https://valuta.kg/'
    data = {}

    def get_html(self, url):
        r = requests.get(url)
        return r.text

    def main(self):
        return self.get_html(Parsing.url)


    def total_inf(self, data):
        return data



    def get_table(self):
        soup = BeautifulSoup(self.main(), 'lxml')
        bank = {}
        location = {}
        buy_price = {}
        sell_price = {}
        ads = soup.find('div', class_='rate-list active').find('tbody').find_all('tr')
        for num, ad in enumerate(ads):
            try:
                title = ad.find('td').find('div', class_='td-member__info').find('h4').find('a').text.strip()
                bank.update({num:title})
                # print(title)
            except:
                title = ''

            try:
                adress = ad.find('td').find('div', class_='td-member__info').find('p').text.split()[1:7]
                mergelist = (''.join(map(str, adress[0:2])))
                mergelist1 = (''.join(map(str, adress[2:7])))
                location.update({bank[num]:{'Phone': mergelist, 'Adress': mergelist1}})
            except:
                mergelist1 = ''

            try:
                buy = ad.find('td', class_='td-rate td-rate--even').find('div', class_='td-rate__wrp').text.strip()
                buy_price.update({bank[num]:buy})
            except:
                buy = ''

            try:
                sell = ad.find('td', class_='td-rate td-rate--even -last-in-group').find('div', class_='td-rate__wrp').text.strip()
                sell_price.update({bank[num]:sell})
            except:
                sell = ''

            Parsing.data['bank'] = bank
            Parsing.data['location'] = location
            Parsing.data['buy_price'] = buy_price
            Parsing.data['sell_price'] = sell_price
            # try:
            #     # data = {'title': title,
            #     #         'mergelist1': mergelist1,
            #     #         'buy': buy,
            #     #         'sell': sell}
            #     pass
            #
            #
            # except:
            #     print("pusto")
    #
    # get_table(html)
    # print(total_inf())

# obj = Parsing()
# obj.get_table()
# print(obj.total_inf(obj.data))