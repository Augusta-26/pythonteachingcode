def cheese_order(order_amount,min=1,max=100,price=7):
        amount = float(order_amount)
        if amount > max:
            print(amount,'is more than currently available stock')
        elif amount < min:
            print(amount,'is below minimum order amount')
        else:
            total = amount * price
            print(amount,'costs $' + str(total))
        
user_input = input('how many cheese order you want?: ')
cheese_order(user_input)
            