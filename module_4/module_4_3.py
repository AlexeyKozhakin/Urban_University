def send_email(message, recipient, *, sender='urban.teacher@mail.ru'):
    if (("@" in recipient and '@' in sender) or
            (recipient.endswith('.com' or '.ru' or '.net') and sender.endswith('.com' or '.ru' or '.net'))):
        if sender == recipient:
            print('Нельзя отправить письмо самому себе')
        else:
            if sender == "university.help@gmail.com":
                print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
            else:
                print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)

    else:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
# Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
# НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
# Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
# Нельзя отправить письмо самому себе!