print ('Welcome to my Bus......')
dest=input('''
select the destination by entering
    1 for Delhi
    2 for Mumbai
    3 for Channai
    4 for Hyderabad
:-''')
adult_seats=int(input('Number of adults:-'))
child_seats=int(input('Number of childs:-'))
Category=input('enter\n 1 for Ac \n 2 for non-Ac\n:-')
distance={'1':2000,'2':800,'3':350,'4':500}
if Category=='1':
    adult_price=10
    child_price=5
elif Category=='2':
    adult_price=5
    child_price=3
total_price=distance[dest]*(adult_price*adult_seats+child_price*child_seats)
print('The total amount is:-',total_price,'rupees')
confirm=input('press yes to conforim')
if confirm == 'yes':
    print('your transaction is successfull')
    print('Thankyou.....\n visit again.....\n Happy journey.....')
else:
    print('your trnsaction canceled')
    print('Thankyou.....\nvisit again.....')
