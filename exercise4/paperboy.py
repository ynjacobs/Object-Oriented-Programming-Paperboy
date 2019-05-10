class Paperboy:
#Paper boy has a name, experience = number of papers delivered, earnings = amount of money earned

# Every day, each paperboy is given a house number to start at and a house number to finish at. 
# They get paid $0.25 for every paper they deliver and $0.50 for every paper over their quota.
#  If at the end of the day they haven't met their quota, they lose $2.

# The minimum number of papers to deliver is 50.
# The quota is calculated as half of your experience added to the minimum.
# So the first time a paperboy makes a delivery, the quota is 50. 
# The next time, the quote is 50 plus half the number of papers that the paperboy has delivered in the past.
# In this way the quota should increase after every delivery the paperboy makes.
   
    def __init__(self, name, experience=0):
        self.name = name
        self.experience = experience
        self.earnings = 0
        self.minimum = 50


    def __str__(self):
        return


    def quota(self):
        a_quota = (self.experience / 2) + self.minimum
        return a_quota

    def deliver(self, start_address, end_address):
        today_earning = 0
        num_deliveries = (end_address + 1) - start_address
        for current_address in range(num_deliveries):
            if current_address < self.quota():
                today_earning += 0.25
            #     print('after .25', self.earnings, current_address)
            else:
                today_earning  +=0.5
        # print('earn before checking quot', self.earnings)
        if num_deliveries < self.quota():
            today_earning -=2
            # print('self.earnings -=2', self.earnings)
        self.experience += num_deliveries
        self.earnings += today_earning
        return float(today_earning)




    def report(self):
        return "I'm {} and I've delivered {} papers and I've earned {} so far, now my quota is {}".format(self.name, self.experience, self.earnings, self.quota())

tommy = Paperboy("Tommy")

print(tommy.quota()) #  50
print(tommy.deliver(101, 160)) # 17.5
print(tommy.earnings) # 17.5
print(tommy.report()) # "I'm Tommy, I've delivered 60 papers and I've earned $17.5 so far!"

print(tommy.quota()) # 80
print(tommy.deliver(1, 75)) # 16.75
print(tommy.earnings) # 34.25
print(tommy.report()) # "I'm Tommy, I've been delivered 135 papers and I've earned $34.25 so far!"


# yael = Paperboy('yael')
# print(yael.quota()) 
# yael.deliver(1, 10)
# print(yael.earnings) 
# print(yael.report())


# yael.deliver(1, 10)
# print(yael.earnings) 
# print(yael.report())
