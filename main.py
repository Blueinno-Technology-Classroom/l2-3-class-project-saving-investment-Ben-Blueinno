##################################################
'''
Q1: 
'''

# TODO: Write your code here

current_balance = 1000
interest_rate = 0.065
new_deposit = 100

for i in range(1, 26):
    interest = current_balance * interest_rate
    new_balance = current_balance + interest
    print(f'{i:02d}: current balance: {current_balance:.2f}, interest: {
          interest:.2f}, deposit: {new_deposit}, new balance: {new_balance:.2f}')
    current_balance = new_balance + new_deposit
