class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for i in range(len(self.file_names)):
            with open(self.file_names[i], encoding='utf-8') as file:
                text = file.read().lower()
                for symbol in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(symbol, "")
                words = text.split()
                all_words.update({self.file_names[i]: words})
        return all_words

    def find(self, word):
        dict_ = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                dict_.update({key: int(value.index(word.lower()) + 1)})
        return dict_

    def count(self, word):
        dict_ = {}
        for key, value in self.get_all_words().items():
            count = 0
            for i in range(len(value)):
                if word.lower() == value[i]:
                    count += 1
            dict_.update({key: count})
        return dict_


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
