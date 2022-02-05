year_salary = int(input('Введите заработную плату в месяц: ')) * 12 
credit = int(input('Введите, какой процент(%) уходит на ипотеку: '))
money_spent = int(input('Введите, какой процент(%) уходит на жизнь: '))
print('На ипотеку было потрачено: ' , int(year_salary * credit / 100))
print('Было накоплено: ', int(year_salary - (year_salary * ((credit + money_spent) / 100))))