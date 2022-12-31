'''
A common thing people do is borrow money. When people repay money, they pay interest
which is paid back annually and added to the original amount the person borrowed.
You are going to create a loan calculator that shows how much money you owe for a loan 
of $1,000 with a 5% APR (APR is fancy for Annual Percentage Rate) over 10 years.
This means each year the amount of money you owe will increase 5%.
Figure out how much you owe altogether for 10 years?
'''

loan = 1000
apr = 0.05
for i in range(10):
  loan+=(loan*apr)
  print("Year", i+1, "is", round(loan,2))
