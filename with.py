class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read().lower()
                for char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    content = content.replace(char, '')
                words = content.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word) + 1
            else:
                result[file_name] = None
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)
        return result

# Пример выполнения программы:
if __name__ == "__main__":
    finder = WordsFinder('test_file.txt')
    print(finder.get_all_words())
    print(finder.find('TEXT'))
    print(finder.count('teXT'))