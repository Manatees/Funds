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

# 2020-03-23  100.00  0.8126  122.94  
# 2020-03-20  100.00  0.8375  119.28  
# 2020-03-19  100.00  0.8110  123.18  
# 2020-03-18  1000.00 0.8394  1190.14 
# 2020-03-17  1000.00 0.8623  1158.53 
# 2020-03-16  1000.00 0.8808  1134.20 
# 2020-02-28  1000.00 0.9085  1099.62 
# 2020-02-18  1000.00 0.9283  1076.16 
# 2020-02-17  1000.00 0.9331  1070.63 
# 2020-02-14  1000.00 0.9257  1079.18 
# 2020-02-13  1000.00 0.9280  1076.51 
# 2020-02-12  1000.00 0.9350  1068.45 
# 2020-02-11  1000.00 0.9324  1071.43 
# 2020-02-10  1000.00 0.9112  1096.36 
# 2020-02-06  1000.00 0.9014  1108.28 
# 2020-02-05  1000.00 0.8926  1119.20 
# 2020-02-04  1000.00 0.8809  1134.07 
# 2019-08-09  100.00  0.8983  111.21  
# 2019-08-07  100.00  0.8969  111.38  
# 2019-08-02  100.00  0.9117  109.58  
# 2019-08-01  100.00  0.9180  108.82  
# 2019-07-17  100.00  0.9607  103.99

buy_rate
0 <= price < 50W    0.10%
50W <= price <100W  0.05%
100W<=              1000

sale_rate
0 <= days < 7       1.50%
7 <= days < 360     0.50%
365<= days < 730    0.25%
730<= days          0.00%