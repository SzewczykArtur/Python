from read_database import Data, AddNewItem
from send_email import SendMail
from price_check import GetPrice
import time


def create_msg():
    """
    This function open database. Read everything what is in tabel which  name is 'data'.
    Next check price for everyone item, and creates a new message. If something is wrong, skips this information.
    """
    items_data: list[str] = Data('database.sql').item_data()
    shops_data = Data('database.sql').shop_data()
    msg = ''
    item_list = []
    for item in items_data:
        shop_name = item[0]
        item_name = item[1]
        item_url = item[2]
        item_old_price = item[3]
        shop_details = shops_data[shop_name]
        tag = shop_details['tag']
        tag_name = shop_details['tag_name']

        try:
            new_price = GetPrice(url=item_url, tag=tag, tag_name=tag_name).get_price()
            if new_price[1] == 200:
                msg += f'New price {item_name} is: {new_price[0]} zl | Old price was: {str(item_old_price)} zl' \
                       f'|{shop_name} | {item_url} \n'
            else:
                msg += 'Something is wrong :( \n'
        except:
            continue

        item = [shop_name, item_name, new_price[0], item_old_price, item_url]
        item_list.append(item)

    return msg, item_list


def main(msg):
    """ Send mail """
    SendMail('art.szewczyk98@gmail.com', msg=msg[0]).send_mail()


if __name__ == '__main__':

    main(create_msg())

