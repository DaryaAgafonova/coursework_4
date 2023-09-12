import json

from class_vacancy import Vacancy


class JSONSaver:

    """ Класс для записи в JSON файл и его чтения. """

    def __init__(self, filename):

        """ Инициализация атрибутов класса. """

        self.filename = filename


    def writing_vacancies_to_file(self, data):

        """ Функция записи вакансий в отельные JSON файлы. """

        try:
            with open(self.filename, "w", encoding="utf-8") as json_file:
                json.dump(data, json_file, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Ошибка при записи в файл: {e}")


    def load_vacansies(self):

        """ Функция чтения JSON файла. """

        try:
            with open(self.filename, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)

                vacansies = []
                for vacancy in data:
                    vacansies.append(Vacancy(**vacancy))

                return vacansies
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return None