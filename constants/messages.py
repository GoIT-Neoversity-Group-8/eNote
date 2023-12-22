# -- Custom error messages
error_messages = {
    "invalid_command": "Ти шо сі вводиш? Ану напиши по-людськи і заюзай 'help'!",
    "no_command": "Введи команду бо я тебе не андестенд.",
    "no_name": "Назви сі мене або що?!",
    "name_not_found": "Не знаю такого імені!", #TODO ім'я не знайдено (видалення, редагування тощо)
    "no_name_and_phone": "Мені потрібен твій одяг, черевики і мотоцикл… ой не то. Дай мені ім’я та телефон :)",
    "no_name_and_phones": "Мені цього замало. Кому, Що і на Що я маю змінити?",
    "no_name_and_email": "Мені потрібен твій одяг, черевики і мотоцикл… ой не то. Дай мені ім’я та email :)",
    #TODO у існуючого контакта вже є телефон, який намагаємось додати
    "phone_exist": "Та вже записаний у нього цей номер",
    #TODO у контакта не знайдено заданий телефон (напр. видалення)
    "phone_not_exist": "Немає такого номера",
    "no_name_and_phones": "Назви мене, додай телефон для оновлення та новий телефон. Негайно!",
    "no_contact": "Краще цілься! Такого контакту немає.",
    "no_contacts": "У ваших контактиках ще немає контактів.",
    "exist_contact": "Нічосі не вийде! Контакт вже існує.",
    "no_name_and_birthday": "Напиши мені ім'я та день народження. Але все це може бути використано проти тебе в суді.",
    "no_name_and_note_data": "Ану сі дай мені ім'я, тег для нотаток і повідомлення.",
    "no_note_tag": "А додай но мені ще тег для нотаток.",
    "no_days": "А додай но мені ще коректну кількість днів"
}

# -- Validation error messages
validation_messages = {
    "invalid_phone": "Ганьба! Телефон введено неправильно.",
    "invalid_date": "Ганьба! Дата введена неправильно. Формат дати - ДД.ММ.РРРР",
    "invalid_email": "Ганьба! Емейл введено неправильно.",
}

raccoon = "\n    /\\_/\\ \n   ( o.o )\n    > ^ <\n"

# -- User helpers for commands
command_messages = {
    "welcome": raccoon + "Hello Everybody, це eNote!",
    "commands":  "\nНаявні команди:",
    "enter_command": "Введіть но команду: ",
    "hello": raccoon + "Hello Everybody,\nчим допомогти?",
    "contact_added": "Перемога! Контакт додано",
    # TODO повідомлення після успішного оновлення даних контакту
    "contact_updated": "Вітаннячко! Контакт {name} оновлено.",
    "contact_deleted": "Вибачай, {name}, буду тебе пам'ятати.",
    "phone_added": "Перемога! Телефон додано",
    "phone_updated": "Перемога! Телефон змінено",
    "phone_deleted": "У {name} видалено телефон {phone}", # TODO успішно виделно телефон з контакта
    #TODO у існуючого контакта немає телефонів
    "no_phones": "Цей вуйко ще не має телефону",
    "email_added": "Перемога! Емейл додано",
    "birthday_added": "Перемога! День народження додано",    
    "note_added": "Перемога! Нотатку додано",
    "note_updated": "Перемога! Нотатку оновлено", # TODO перевріити переклад 
    "note_deleted": "Нотатку видалено", # TODO перевріити переклад 
    "no_notes_by_tag": "Нічого не знайдено за тегом {tag}", # TODO перевріити переклад 
    "no_notes_by_string": "Я не знайшов нічого схожого на '{search_term}'", # TODO перевріити переклад 
    "enter_phone": "Введіть телефон: ",
    "enter_email": "Введіть емейл: ",
    "enter_address": "Введіть адресу: ",
    "enter_birthday": "Введіть день народження: ",
    "enter_note": "Введіть повідомлення нотатки: ",
    "enter_tag": "Введіть тег нотатки: ",
    "email_added": "Перемога! Емейл додано",
    "email_updated": "Перемога! Емейл оновлено",
    "email_deleted": "Всьо, чисто :)",
    "address_added": "Перемога! Адресу додано. Тре заскочити в АТБ - і в гості :)",
    "address_deleted": "Всьо, чисто :)",
    "prompt_edit_contact": "Агов! Контакт {name} вже існує. Будемо його редагувати?: ",
    "prompt_add_contact": "Та ну немає такого контакту з іменем {name}. Будемо додавати?: [y, n]",
    #TODO show_phones - "Phones number for {name}:\n {txt_phones}" 
    "show_phones": "Осьо телефони {name}",
    "show_birthday": "Ця чарівна людина була народжена {birthday}",
    "no_birthday": "Нажаль, ми не знаємо, коли народилася ця чарівна людина (",
    "no_birthdays": "Йой, жодного дня народження серед контактів не знайдено.", # TODO перевріити переклад 
    "no_birthdays_in_days": "Я не знайшов кого Вам привітати у наступні {days} днів (", # TODO перевріити переклад 
    "good_bye": "\nОбійняв-припідняв і до нової здибанки! І не забувайте донатити на фонд “Повернись живим” щоб єнотів більше не викрадали ;)\n" + raccoon,
    "cycle_hint_contact": "'n' - наступний, 'e' - вийти геть з контакту",
    "cycle_hint_note": "'n' - наступний, 'e' - вийти геть з нотатки"
}

# -- Help table column headers
help_table_messages = {
    "command_col": "Команда",
    "example_col": "Приклад з аргументами",
    "description_col": "Опис", 
}

# -- Help table command descriptions
command_descriptions = {
    "help": "Показує список доступних команд і трохи більше.",
    "hello": "Шле вітаннячко і тисне лапу.",
    "exit": "Бажає всього найліпшого і виходить з програми.",
    "show_all": "Показує всі контакти, викладені за іменами",
    "add_contact": "Долучає ім'я новенького контакту",
    "find": "Вишукує контакти по всім полям.", # TODO перевріити переклад 
    "add_phone": "Долучає новенький телефон (10-знаків) для контакту\nпо імені",
    "edit_phone": "Змінює існуючий номер на новенький (10-знаків)\nдля контакту по імені",
    "delete_phone": "Видаляє з контакту телефон \nпо імені і телефону", # TODO перевірити пеерклад видалення телефону з контакту
    "show_phones": "Показує телефони для контактів по імені",
    "add_email": "Долучає емейл (a@bcd.com) для контакту\nза іменем",
    "edit_email": "Оновлює емейл для контакту\nза іменем",
    "delete_email": "Видаляє емейл для контакту\nза іменем",
    "add_address": "Долучає адресу для контакту\nза іменем",
    "edit_address": "Змінює адресу для вказаного контакта",
    "delete_address": "Видаляє адресу контакта",
    "add_birthday": "Долучає день народження (DD.MM.YYYY) для контакту\nза іменем",
    "update_birthday": "Оновлює день народження (DD.MM.YYYY) для контакту\nза іменем",
    "show_birthday": "Показує день народження для контакту за іменем",
    "show_birthdays": "Показує імена та дні народження всіх контактів.",
    "find_birthdays": "Вишукує контакти, день народження яких наступає через\nвказану кількість днів(по замовченю 7 днів).",
    "update_contact": "Поновлює деталі наявного контакту.",
    "delete_contact": "Видаляє у смітник контакт за іменем.",
    "add_note": "Долучає примітку до певного контакту.",
    "edit_note": "Оновлює конкретну примітку контакту.",
    "find_note_by_tag": "Вишукує нотатки за тегом",
    "find_notes": "Вишукує нотатки за текстом пошуку",
    "delete_note": "Видаляє у смітник нотатку за іменем контакту",
}
