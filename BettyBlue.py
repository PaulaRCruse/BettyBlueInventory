stock = {'cups': 5, 'plates': 6, 'bowls':10, 'hearts': 8}

pottery = input('What pottery was purchased? ') 
customer = input('Who purchased the pottery? ' )

if pottery in stock:
    stock[pottery] -= 1
    print('{} purchased {}'.format(customer, pottery))
else:
    print('{} are out of stock'.format(pottery))
    

