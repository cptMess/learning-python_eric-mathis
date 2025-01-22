#____________________________________________________________
#2.3. Личное сообщение: сохраните имя пользователя в переменной и выведите сообщение, предназначенное для конкретного человека. 
# Сообщение должно быть простым — например, «Hello Eric, would you like to learn some Python today?”.

name = "Eric"
print(f"Hello {name}, would you like to learn some Python today?")

#____________________________________________________________
#2.4. Регистр символов в именах: сохраните имя пользователя в переменной и выведите его в нижнем регистре, 
# в верхнем регистре и с капитализацией начальных букв каждого слова.

name_2 = "Andrew Martynov"
print(name_2.lower())
print(name_2.upper())
print(name_2.title())

#____________________________________________________________
#2.5. Знаменитая цитата: найдите известное высказывание, которое вам понравилось. 
# Выведите текст цитаты с именем автора. Результат должен выглядеть примерно так (включая кавычки): 
# Albert Einstein once said, "A person who never made a mistake never tried anything new."

autor = "albert einstein"
print(f'{autor.title()} once said, "A person who never made a mistake never tried anything new."')

#____________________________________________________________
#2.6. Знаменитая цитата 2: повторите упражнение 2.5, но на этот раз сохраните имя автора цитаты в переменной famous_person. 
#Затем составьте сообщение и сохраните его в новой переменной с именем message. Выведите свое сообщение.

famous_person = "albert einstein"
message = f'{famous_person.title()} once said, "A person who never made a mistake never tried anything new."'
print(message)  

#____________________________________________________________
#2.7. Удаление пропусков: сохраните имя пользователя в переменной. Добавьте в начале и в конце имени несколько пропусков. 
# Проследите за тем, чтобы каждая служебная последовательность , "\t" и "\n", встречалась по крайней мере один раз. 
# Выведите имя, чтобы были видны пропуски в начале и конце строки. 
# Затем выведите его снова с использованием каждой из функций удаления пропусков: lstrip(), rstrip() и strip().

username = " Andrew Martynov "
print("\t  Andrew Martynov ")
print("Andrew \nMartynov ")
print(username.lstrip())
print(username.rstrip())
print(username.strip())