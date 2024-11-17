import hashlib


def hash_password(password):
    # Преобразуем пароль в байты
    password_bytes = password.encode('utf-8')

    # Создаем объект для хэширования с помощью SHA-256
    hash_object = hashlib.sha256(password_bytes)

    # Получаем хэш в виде шестнадцатеричной строки
    password_hash = hash_object.hexdigest()

    return password_hash


# Пример использования
hashed_password = hash_password("my_secure_password")
print(f"Hashed password: {hashed_password}")
print(type(hashed_password))
print(len(hashed_password))