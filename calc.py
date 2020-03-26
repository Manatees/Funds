def middleValue(buy_price, rate, T, amount, price):
    net_price = buy_price / (1 + rate)
    fee_value = buy_price - net_price
    buy_amount = net_price / T

    return ((price + buy_price) / (amount + buy_amount), buy_amount, fee_value)


if __name__ == '__main__':
    calculated_val = middleValue(buy_price=1000, rate=0.01, T=0.7977, amount=19456.30, price=17300)
    print(calculated_val)
