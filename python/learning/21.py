class Bank:
    def __init__(self, hours, days):
        self.hours=hours
        self.days=days


    def tothours(self):
        total_hours=self.hours*self.days
        return total_hours


    def clerk(self, th):
        tot_sal=th*7
        print('Total Salary for Clerk:' + str(tot_sal))

h=int(input('Giver hours'))
d=int(input('Give days'))
southindian=Bank(h,d)
x=int(southindian.tothours())
print(f"hours total: {x}")
southindian.clerk(x)
