def cheese_order(order_amount, max=100, min=1, price=7):
    order_amount = float(order_amount)
    if order_amount > max:
        print(order_amount,'is more than currently available stock')
    elif order_amount < min:
        print(order_amount,'is below minimum order amount')
    else:
        total = price * order_amount
        print(order_amount,'costs $',total)

user_choice = input('Quang Huynh, how many cheese orders do you want? (number only)')
cheese_order(user_choice)