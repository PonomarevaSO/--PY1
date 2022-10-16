money_capital: float = 10000
salary: float = 5000
spend: float = 6000
increase = 0.05

month: int = 0  # количество месяцев, которое можно прожить

while money_capital > spend:
    spend += increase*spend
    money_capital += salary - spend
    month+=1
print(month)



