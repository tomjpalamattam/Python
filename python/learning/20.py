class Bank:
    def __init__(self, hours, days):     # parent class , this will take hours and days. also a bank1 variable is declared in this class
        self.hours = hours
        self.days = days

    def tothours(self):
        total_hours = self.hours * self.days
        return total_hours

    def clerk(self, mwc):   # here the parameter is minimum wage of clerk
        th = self.tothours()
        tot_sal = th * mwc
        print('Total Salary for Clerk:' + str(tot_sal))
        return tot_sal

    def manager(self, mwm):   # here the parameter is minimum wage of manager
        th = self.tothours()
        tot_sal = th * mwm
        print('Total Salary for Manager' + str(tot_sal))
        return tot_sal


class Private(Bank): # inherited class from bank
    def tax_manager(self,minwagm2):
        print('This is a private bank, so taxes are higher')
        salary=int(self.manager(minwagm2))
        taxes=salary*0.3
        print(f'tax:{taxes}')

    def tax_clerk(self,minwagc2):
        print('This is a private bank, so taxes are higher')
        salary=int(self.clerk(minwagc2))
        taxes=salary*0.1
        print(f'tax:{taxes}')


class Public(Bank):  # inherited class from bank
    def tax_manager(self,minwagm2):
        print('This is a public bank, so taxes are lower')
        salary=int(self.manager(minwagm2))
        taxes=salary*0.2
        print(f'tax:{taxes}')

    def tax_clerk(self,minwagc2):
        print('This is a public bank, so taxes are lower')
        salary=int(self.clerk(minwagc2))
        taxes=salary*0.05
        print(f'tax:{taxes}')


h = int(input('Giver hours'))
d = int(input('Give days'))
southindian = Private(h, d)
rbi = Public(h, d)
bank1= Bank(h, d)
x = int(bank1.tothours())
print(f"hours total: {x}")
option = input('''
1: clerk
2.manager
To quit type quit''')

while (True):
    if int(option) == 1:
        minwagc = int(input('Give minimum wage for clerks:'))
        print('For Private Bank')
        southindian.clerk(minwagc)
        southindian.tax_clerk(minwagc)
        print('For Public Bank')
        rbi.clerk(minwagc)
        rbi.tax_clerk(minwagc)
        break

    if int(option) == 2:
        minwagm = int(input('Give minimum wage for Managers:'))
        print('For Private Bank')
        southindian.manager(minwagm)
        southindian.tax_manager(minwagm)
        print('For Public Bank')
        rbi.manager(minwagm)
        rbi.tax_manager(minwagm)
        break

    if option.lower() == 'quit':
        break
