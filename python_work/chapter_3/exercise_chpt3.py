#3.1. Имена: сохраните имена нескольких своих друзей в списке с именем names. 
# Выведите имя каждого друга, обратившись к каждому элементу списка (по одному за раз).
friends=['Саша', 'Наташа', 'Кирилл', 'Вероника', 'Андрей']
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[-1])

#____________________________________________________________
#3.2. Сообщения: начните со списка, использованного в упражнении 3.1, но вместо вывода имени каждого человека выведите сообщение. 
# Основной текст всех сообщений должен быть одинаковым, но каждое сообщение должно включать имя адресата.
message=f"{friends[0]} не курит кальян, {friends[1]} не может идти в сауну, {friends[2]} не играет в настолки, {friends[3]} не хочет на лыжи, {friends[-1]} хороший человек"
print(message)

#____________________________________________________________
#3.3. Собственный список: выберите свой любимый вид транспорта (например, мотоциклы или машины) и создайте список с примерами. 
# Используйте свой список для вывода утверждений об элементах типа: «Я хотел бы купить мотоцикл Honda».
bicycles = ['trek', 'cannondale', 'redline', 'specialized', 'Cube', 'Merida']
message2=f"Я бы хотел купить велосипед {bicycles[-2]}"
print(message2)

#____________________________________________________________
#3.4. Список гостей: если бы вы могли пригласить кого угодно (из живых или умерших) на обед, то кого бы вы пригласили? 
# Создайте список, включающий минимум трех людей, которых вам хотелось бы пригласить на обед. 
# Затем используйте этот список для вывода пригласительного сообщения каждому участнику.
guests=['Петя', 'Вася', 'Коля']
invitation1=f"{guests[0]} пошли жрац."
invitation2=f"{guests[1]} пошли жрац."
invitation3=f"{guests[2]} пошли жрац."
print(invitation1)
print(invitation2)
print(invitation3)

#____________________________________________________________
#3.5. Изменение списка гостей: вы только что узнали, что один из гостей прийти не сможет, поэтому вам придется разослать новые приглашения. 
# Отсутствующего гостя нужно заменить кем-то другим.
# Начните с программы из упражнения 3.4. Добавьте в конец программы команду print для вывода имени гостя, который прийти не сможет.
# Измените список и замените имя гостя, который прийти не сможет, именем нового приглашенного.
# Выведите новый набор сообщений с приглашениями — по одному для каждого участника, входящего в список.
invitation_fail=f"{guests[0]} не пойдет жрац."
print(invitation_fail)

del guests[0]
print(guests)

guests.append('Степа')
print(guests)

invitation1=f"{guests[0]} пошли жрац."
invitation2=f"{guests[1]} пошли жрац."
invitation3=f"{guests[2]} пошли жрац."
print(invitation1)
print(invitation2)
print(invitation3)

#____________________________________________________________
#3.6. Больше гостей: вы решили купить обеденный стол большего размера. Дополнительные места позволяют пригласить на обед еще трех гостей.
# Начните с программы из упражнения 3.4 или 3.5. Добавьте в конец программы коман­ду print, которая выводит сообщение о расширении списка гостей.
# Добавьте вызов insert() для добавления одного гостя в начало списка.
# Добавьте вызов insert() для добавления одного гостя в середину списка.
# Добавьте вызов append() для добавления одного гостя в конец списка.
# Выведите новый набор сообщений с приглашениями — по одному для каждого участника, входящего в список.

expansion='К нам придут еще гости'
print(expansion)

guests.insert(0, 'Боря')
guests.insert(2, 'Ваня')
guests.append('Юра')

print(guests)

invitation1_2=f"{guests[0]} пошли жрац."
invitation2_2=f"{guests[1]} пошли жрац."
invitation3_2=f"{guests[2]} пошли жрац."
invitation4_2=f"{guests[3]} пошли жрац."
invitation5_2=f"{guests[4]} пошли жрац."
invitation6_2=f"{guests[5]} пошли жрац."
print(invitation1_2)
print(invitation2_2)
print(invitation3_2)
print(invitation4_2)
print(invitation5_2)
print(invitation6_2)

#____________________________________________________________
#3.7. Сокращение списка гостей: только что выяснилось, что новый обеденный стол привезти вовремя не успеют и места хватит только для двух гостей.
# Начните с программы из упражнения 3.6. Добавьте команду для вывода сообщения о том, что на обед приглашаются всего два гостя.
# Используйте метод pop() для последовательного удаления гостей из списка до тех пор, пока в списке не останутся только два человека. 
# Каждый раз, когда из списка удаляется очередное имя, выведите для этого человека сообщение о том, что вы сожалеете об отмене приглашения.
# Выведите сообщение для каждого из двух человек, остающихся в списке. Сообщение должно подтверждать, что более раннее приглашение остается в силе.
# Используйте команду del для удаления двух последних имен, чтобы список остался пустым. 
# Выведите список, чтобы убедиться в том, что в конце работы программы список действительно не содержит ни одного элемента.

print('Впрочем...')

cancel = guests.pop()
print(guests)
print(f"{cancel} не пойдет")

cancel = guests.pop()
print(guests)
print(f"{cancel} не пойдет")

cancel = guests.pop()
print(guests)
print(f"{cancel} не пойдет")

cancel = guests.pop()
print(guests)
print(f"{cancel} не пойдет")

del guests[0]
print(guests)
del guests[0]
print(guests)

#____________________________________________________________
#3.8. Повидать мир: вспомните хотя бы пять стран, в которых вам хотелось бы побывать.
# Чехия, Япония, Норвегия, Швейцария, Канада
# -Сохраните названия стран в списке. Проследите за тем, чтобы список не хранился в алфавитном порядке.
countries=['Чехия', 'Япония', 'Норвегия', 'Швейцария', 'Канада']
# -Выведите список в исходном порядке. Не беспокойтесь об оформлении, просто выведите его как обычный список Python.
print(countries)
# -Используйте функцию sorted() для вывода списка в алфавитном порядке без изменения списка.
print(sorted(countries))
# -Снова выведите список, чтобы показать, что он по-прежнему хранится в исходном порядке.
print(countries)
# -Используйте функцию sorted() для вывода списка в обратном алфавитном порядке без изменения порядка исходного списка.
print(sorted(countries, reverse=True))
# -Снова выведите список, чтобы показать, что исходный порядок не изменился.
print(countries)
# -Измените порядок элементов вызовом reverse(). Выведите список, чтобы показать, что элементы следуют в другом порядке.
countries.reverse()
print(countries)
# -Измените порядок элементов повторным вызовом reverse(). Выведите список, чтобы показать, что список вернулся к исходному порядку.
countries.reverse()
print(countries)
# -Отсортируйте список в алфавитном порядке вызовом sort(). Выведите список, чтобы показать, что элементы следуют в другом порядке.
countries.sort()
print(countries)
# -Вызовите sort() для перестановки элементов списка в обратном алфавитном порядке. Выведите список, чтобы показать, что порядок элементов изменился.
countries.sort(reverse=True)
print(countries)

#____________________________________________________________
#3.9. Количество гостей: в одной из программ из упражнений с 3.4 по 3.7 используйте len() 
# для вывода сообщения с количеством людей, приглашенных на обед.
print(len(guests))
print(len(bicycles))