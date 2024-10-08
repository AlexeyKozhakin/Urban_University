from time import sleep
import hashlib
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f'{self.nickname}'

class Video:
    def __init__(self,title,duration,adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def get_list_names_users(self):
        list_names_users = []
        for user in self.users:
            list_names_users.append(user.nickname)
        return list_names_users

    def get_list_names_videos(self):
        list_names_videos = []
        for video in self.videos:
            list_names_videos.append(video.title)
        return list_names_videos

    def register(self, nickname, password, age):
        if nickname in self.get_list_names_users():
            print(f"Пользователь {nickname} уже существует")
        else:
            hash_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            self.users.append(User(nickname, hash_password, age))
            self.log_in(nickname, password)

    def log_in(self,nickname, password):
        hash_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        for user in self.users:
            if user.nickname == nickname and user.password == hash_password:
                self.current_user = user


    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for new_video in args:
            if new_video.title not in self.get_list_names_videos():
                self.videos.append(new_video)

    def get_videos(self, search_word):
        find_list = []
        for title in self.get_list_names_videos():
            if search_word.lower() in title.lower():
                find_list.append(title)
        return find_list

    def find_video(self, watch_title_video):
        for video in self.videos:
            if watch_title_video == video.title:
                return video
        return False

    def watch_video(self, watch_title_video):
        if self.current_user == None:
            print( f"Войдите в аккаунт, чтобы смотреть видео")
        elif self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else:

            current_video = self.find_video(watch_title_video)
            if current_video:
                for duration in range(current_video.time_now+1, current_video.duration + 1):
                    sleep(1)
                    print(duration)
                print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')




