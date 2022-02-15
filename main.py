from freekassa import Merchant


def test():
    merchant = Merchant(shop_id=123456789,
                        secret1="secret1",
                        secret2="secret2",
                        api_key="api_key")
    # return merchant.get_payment_form_url(amount=123, order_id="dasd", us_={'token':'dasd',"test":"test"})
    return merchant.get_balance()


if __name__ == '__main__':
    print(test())
