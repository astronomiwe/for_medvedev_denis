import yaml

current_price = int()

with open("config.yaml", 'r') as file:
    try:
        config_dict = yaml.safe_load(file)
        print(config_dict)
    except yaml.YAMLError as exc:
        print(exc)

gap = float(config_dict['robot']['gap'])
gap_ignore = float(config_dict['robot']['gap_ignore'])
sell_price = int()
buy_price = int()


def getPrice():
    return current_price


def createSellOrder():
    ask_price = current_price + gap
    return ask_price


def createBuyOrder():
    bid_price = current_price - gap / 2
    return bid_price


def cancelSell():
    pass


def cancelBuy():
    pass


bot_is_working = True
is_buying = True

while bot_is_working:

    if is_buying:
        createBuyOrder()
        current_price = getPrice()
        if current_price <= buy_price:
            is_buying = False
        elif current_price > buy_price + gap + gap_ignore:
            cancelBuy()

    else:
        createSellOrder()
        current_price = getPrice()
        if current_price >= sell_price:
            is_buying = True
        elif getPrice() < sell_price - gap - gap_ignore:
            cancelSell()
