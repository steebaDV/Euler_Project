money = [1, 2, 5]
bill = 10
bill_now = 0
variations = 1
money_now = {1: 0, 2: 0, 5: 2}
point = len(money)-1
while money_now[1]!= 10:
    point_now = point
    bill_now = 0
    if money_now[money[point]] != 0:
        money_now[money[point]] -= 1
        bill_now += money[point]
        point_now -= 1
        while True:
            money_now[money[point_now]] += bill_now // money[point_now]
            bill_now = bill_now % money[point_now]
            if bill_now == 0:
                break
            else:
                point_now -= 1

    elif point != 0 and money_now[money[point]] == 0:
        point -= 1
        money_now[money[point]] //= bill
    else:
        variations += 1
        break
    variations += 1
    print(money_now)
print(variations)
