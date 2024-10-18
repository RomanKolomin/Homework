from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def show_info(self):
        return print(self.nickname, self.password, self.age)

    def return_name(self):
        return self.nickname

    def return_password(self):
        return self.password

    def return_age(self):
        return int(self.age)


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def return_name(self):
        return self.title

    def return_adult_mode(self):
        return self.adult_mode

    def return_duration(self):
        return int(self.duration)


class UrTube:
    def __init__(self):
        self.users = {}
        self.videos = {}
        self.current_user = None

    def log_in(self, nickname, password):
        if nickname not in self.users:
            print(f'Пользователь {nickname} не найден')
        elif User.return_password(self.users[nickname]) == hash(password):
            self.current_user = nickname
            # print(f'Пользователь {nickname} зашел в систему')
        else:
            print(f'Пароль пользователя {nickname} введен неверно')

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.update({nickname: User(nickname, password, age)})
            # print(f'Пользователь {nickname} зарегистрирован')
            UrTube.log_in(self, nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            self.videos.update({Video.return_name(video): video})

    def get_videos(self, title):
        list_of_videos = []
        for video in self.videos:
            if title.lower() in video.lower():
                list_of_videos.append(video)
        return list_of_videos

    def watch_video(self, title):
        if title not in self.videos:
            # print(f'Видео "{title}" не существует')
            pass
        elif not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
        elif (User.return_age(self.users[self.current_user]) < 18
                and Video.return_adult_mode(self.videos[title])):
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
        else:
            current_time = 0
            for second in range(Video.return_duration(self.videos[title])):
                sleep(1)
                current_time += 1
                print(current_time, " ", end='')
            print("Конец видео")


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
