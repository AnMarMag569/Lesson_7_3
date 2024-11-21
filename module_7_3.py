class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for plik_name in self.file_names:
            with open(plik_name, 'r', encoding='utf-8') as plik:
                words = []
                for line in plik:
                    line = line.lower()
                    p = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for pn in p:
                        line = line.replace(pn, '')
                    words.extend(line.split())
                all_words[plik_name] = words
        return all_words
    def find(self, word):
        slo1 = {}
        word = word.lower()
        for plik_name, words in self.get_all_words().items():
            if word in words:
                return {plik_name: words.index(word) + 1}
            else:
                return slo1

    def count(self, word):
        slo2 = {}
        word = word.lower()
        for plik_name, words in self.get_all_words().items():
            if word in words:
                return {plik_name: words.count(word)}
            else:
                return slo2






finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего