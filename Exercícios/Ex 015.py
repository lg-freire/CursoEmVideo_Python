days = int(input('Days rented: '))
travel = float(input('Distance traveled (in km): '))
dayprice = int(days*60)
travelprice = float(travel*0.15)
price = dayprice+travelprice
print('You owe US${:.2f} for {} days rented and {:.1f}km traveled.'.format(price, days, travel))
print(type(price))