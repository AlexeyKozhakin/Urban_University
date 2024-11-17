def check_email(email):
    if (
        "@" in email and
        email.endswith((".com",".ru",".net"))):
        result = True
    else:
        result = False
    return result

def send_email(message, recipient, *,sender = "university.help@gmail.com"):

    if not (check_email(sender) and check_email(recipient)):
        output = f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}"
    elif sender == recipient:
        output = "Нельзя отправить письмо самому себе!"
    elif sender == "university.help@gmail.com":
        output = f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}."
    else:
        output = f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}."
    print(output)


send_email('Вы видите это сообщение как лучший студент курса!',
            'urban.fan@mail.ru',
                     sender='urban.info@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!',
            'urban.fan@mail.ru',
                     sender = 'urbamail.com')
