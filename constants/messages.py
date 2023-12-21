# -- Custom error messages
error_messages = {
    "invalid_command": "Ти шо сі вводиш? Ану напиши по-людськи і заюзай 'help'!",
    "no_command": "Введи команду бо я тебе не андестенд.",
    "no_name": "Назви сі мене або що?!",
    "no_name_and_phone": "Мені потрібен твій одяг, черевики і мотоцикл… ой не то. Дай мені ім’я та телефон :)",
    "no_name_and_phones": "Назви мене, додай телефон для оновлення та новий телефон. Негайно!",
    "no_contact": "Краще цілься! Такого контакту немає.",
    "no_contacts": "У ваших контактиках ще немає контактів.",
    "exist_contact": "Нічосі не вийде! Контакт вже існує.",
    "no_name_and_birthday": "Напиши мені ім'я та день народження. Але все це може бути бути використано проти тебе в суді.",
    "no_name_and_note_data": "Ану сі дай мені ім'я, тег для нотаток і повідомлення.",
    "no_name_and_email": "Напиши мені ім'я та свій email.",
    "no_name_and_address": "Напиши мені ім'я та свою адресу.",
    "no_note_tag": "А додай но мені ще тег для нотаток.",
}

# -- Validation error messages
validation_messages = {
    "invalid_phone": "Ганьба! Телефон введено неправильно.",
    "invalid_date": "Ганьба! Дата введена неправильно.",
    "invalid_email": "Ганьба! Емейл введено неправильно.",
}

# -- User helpers for commands
command_messages = {
    "welcome": "Hello Everybody, це eNote!",
    "commands":  "\nНаявні команди:",
    "enter_command": "Введіть но команду: ",
    "hello": "Hello Everybody,/nчим допомогти?",
    "contact_added": "Перемога! Контакт додано",
    "phone_added": "Перемога! Телефон додано",
    "birthday_added": "Перемога! День народження додано",
    "note_added": "Перемога! Тег додано",
    "email_added": "Перемога! Email додано",
    "address_added": "Перемога! Адресу додано",
    "enter_phone": "Введіть телефон (n - наступний, e - вийти геть з контакту): ",
    "enter_email": "Введіть емейл (n - наступний, e - вийти геть з контакту): ",
    "enter_address": "Введіть адресу (n - наступний, e - вийти геть з контакту): ",
    "enter_birthday": "Введіть день народження (n - наступний, e - вийти геть з контакту): ",
    "enter_note": "Введіть нотатку (n - наступний, e - вийти геть з контакту): ",
    "enter_tag": "Введіть тег (n - наступний, e - вийти геть з контакту): ",
    "prompt_edit_contact": "Агов! Контакт {name} вже існує. Будемо його редагувати?: ",
    "prompt_add_contact": "Та ну немає такого контакту з іменем {name}. Будемо додавати?: ",
    "good_bye": "Обійняв-припідняв і до нової здибанки! І не забувайте донатити на фонд “Повернись живим” щоб єнотів більше не викрадали ;)",
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
    "add_phone": "Долучає новенький телефон (10-знаків) для контакту по імені",
    "add_email": "Долучає email до контакту",
    "add_address": "Долучає адресу до контакту",
    "show_phones": "Показує телефони для контактів по імені",
    "add_birthday": "Долучає день народження (DD.MM.YYYY) для контакту за іменем",
    "show_birthday": "Показує день народження для контакту за іменем",
    "show_birthdays": "Показує імена та дні народження всіх контактів.",
    "find_birthdays": "Вишукує контакти, день народження яких наступає через вказану кількість днів.",
    "update_contact": "Поновлює деталі наявного контакту.",
    "delete_contact": "Видаляє у смітник контакт за іменем.",
    "add_note": "Долучає примітку до певного контакту.",
    "edit_note": "Редагує конкретну примітку контакту.",
    "find_note_by_tag": "Вишукує нотатки за тегом",
    "find_notes": "Вишукує нотатки за текстом пошуку",
    "delete_note": "Видаляє у смітник нотатку за іменем контакту",
}
