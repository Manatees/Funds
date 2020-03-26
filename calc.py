def purchase(price, rate, T):
    """
    买规则
    净申购金额 = 申购金额 / ( 1 + 申购费率)
    申购费用 = 申购金额 - 净申购金额
    申购份额 = 净申购金额 / T日净值

    Args:
        price: 申购金额
        rate:  申购费率 
        T:     T日净值 

    Returns:
        (申购份额, 申购费用)
        
    """
    net_price = price / (1 + rate)
    buy_fee = price - net_price
    buy_amount = net_price / T
    return (buy_amount, buy_fee)

def redemption(amount, rate, T):
    """
    卖规则
    赎回总额 = 赎回数量 * T日净值
    赎回费用 = 赎回总额 * 赎回费率
    赎回金额 = 赎回总额 - 赎回费用
    
    Args:
        amount: 赎回数量
        rate:   赎回费率
        T:      T日净值
    
    Returns:
        （赎回金额，赎回费用）
    """
    sale_amount_price = amount * T
    sale_fee = sale_amount_price * rate
    sale_price = sale_amount_price - sale_fee
    return (sale_price, sale_fee)


def middleValue(buy_price, rate, T, amount, price):
    # net_price = buy_price / (1 + rate)
    # fee_value = buy_price - net_price
    # buy_amount = net_price / T
    fee_value, buy_amount = purchase(buy_price, rate, T)    

    return ((price + buy_price) / (amount + buy_amount), buy_amount, fee_value)



if __name__ == '__main__':
    calculated_val = middleValue(buy_price=1000, rate=0.01, T=0.7977, amount=19456.30, price=17300)
    print(calculated_val)
