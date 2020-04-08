from rates import redemption_rate

class Fund(object):
    """docstring for Fund"""

    def __init__(self, code, name):
        super(Fund, self).__init__()
        self.code = code
        self.name = name                
    
    def fund_purchase_rate(self):
        pass    

    
    def fund_redemption_rate(self, hold_days):
        rates = redemption_rate.rates[self.code]
        return rates.get_rate_value(hold_days)


if __name__ == '__main__':
    print('main')

    afund = Fund('161725', '白酒')    
    rate = afund.fund_redemption_rate(hold_days=7)
    print('fund name: {}, hold 7 days\'s rate: {}'.format(afund.name, rate))
