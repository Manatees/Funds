from datetime import date
        
class buy_record(object):
    """docstring for buy_record"""
    def __init__(self, s_date, amount, T, hold_share):
        super(buy_record, self).__init__()
        self.date = date(*map(int, s_date.split('-')))
        self.amount = float(amount)
        self.T = float(T)
        self.hold_share = float(hold_share)
        
    def __str__(self):
        return '{} {:.2f} {:.4f} {:.2f}'.format(self.date.isoformat(), self.amount, self.T, self.hold_share)

    def hold_days(self):
        dt = date.today() - self.date
        return dt.days

def main():
    line = '2020-03-23  100.00  0.8126  122.94'
    param = filter(None, line.split(' '))
    rec1 = buy_record(*param)
    print(rec1)
    print(rec1.hold_days())

if __name__ == '__main__':
    main()



