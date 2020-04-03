class Fund(object):
    """docstring for Fund"""
    def __init__(self, code, name):
        super(Fund, self).__init__()
        self.arg = code
        self.name = name
    
    def purchase_rate(self):
        pass

    def redemption_rate(self):
        pass


class Rate(object):
    """docstring for Rate"""
    def __init__(self, arg):
        super(Rate, self).__init__()        
        self._parse(arg)

    def _parse(self, line):
        items = line.split('|')
        self.code = items[0]
        self.during = self._during(items[1])        
        self._during_limit(items[2])

    def _during(self, str_during):        
        items = str_during.split(',')
        return [tuple(map(float, d.split(':'))) for d in items]

    def _during_limit(self, str_limit):
        ret = list(map(float, str_limit.split(':')))
        self.limit = ret[0]
        self.limit_value = ret[1]
        return self.limit, self.limit_value

    def get_rate_value(self, opt):
        ret = None
        for x in self.during:
            if opt < x[0]:
                ret = x[1]
                break
        if ret == None:
            ret = self.limit_value
        return ret
            
        
if __name__ == '__main__':
    r = Rate('161725|7:0.015,360:0.0005,730:0.0025|730:0')
    print(r.code, r.limit_value)
    print('during', r.during)
    print(r.get_rate_value(730))
    
# buy_rate
# 0 <= price < 50W    0.10%
# 50W <= price <100W  0.05%
# 100W<=              1000

# sale_rate
# 161725|7:0.015,360:0.0005,730:0.0025|730:0
# 0 <= days < 7       1.50%
# 7 <= days < 360     0.50%
# 365<= days < 730    0.25%
# 730<= days          0.00%