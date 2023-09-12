from abc import ABC, abstractmethod

import os
import requests

from loading_error import LoadingError


api_key = os.getenv("X-Api-App-Id")


class Basic(ABC):

    """ Основной абстрактный класс для работы с API сайтов с вакансиями. """

    @abstractmethod
    def get_requests(self):

        """ Абстрактный метод вывода списка вакансий. """

        pass


    @abstractmethod
    def get_vacancies(self):

        """ Абстрактный метод. """

        pass


class HeadHunter(Basic):

    """ Дочерний класс Basic для работы с HeadHunter. """

    def __init__(self, text):

        """
        self.url_hh - ссылка на API.

        self.params - параметры = {
            "per_page" - количество элементов (по умолчанию 20, максимальное значение - 50),
            "page" - номер страницы (по умолчанию - 0),
            "text": text - ключевое слово,
            "archive": False - вакансии не находящиеся в архиве.
            }
        """

        self.url_hh = "https://api.hh.ru/vacancies"
        self.params = {
            "per_page": 20,
            "page": 0,
            "text": text,
            "archive": False
        }


    def get_requests(self):

        """ Метод вывода списка вакансий с сайта hh.ru в json
        или вывод исключения. """

        response = requests.get(self.url_hh, params=self.params)
        if response.status_code != 200:
            raise LoadingError(f"Ошибка получения вакансии! Статус {response.status_code}.")
        else:
            return response.json()["items"]


    def get_vacancies(self):

        """ Метод формирования вывода вакансии с сайта hh.ru. """

        vacancies = self.get_requests()

        generated_vacancies = []

        for vacancy in vacancies:
            if not vacancy["salary"]:
                salary_from = 0
                salary_to = 0
            else:
                if vacancy["salary"]["from"]:
                    salary_from = vacancy["salary"]["from"]
                else:
                    salary_from = 0

            changing_vacancy = {
                "title": vacancy["name"],
                "url": vacancy["alternate_url"],
                "salary_from": salary_from,
                "salary_to": salary_to,
                "work_experience": vacancy["experience"]["name"],
                "platform": "Head Hunter"
            }
            generated_vacancies.append(changing_vacancy)

        return generated_vacancies


class SuperJob(Basic):

    """ Дочерний класс Basic для работы с SuperJob. """

    def __init__(self, text):

        """
        self.url_sj - ссылка на API.

        self.params - параметры = {
            "count" - количество элементов (по умолчанию 20, максимальное значение - 50),
            "page" - номер страницы (по умолчанию - 0),
            "keyword": text - ключевое слово,
            "archive": False - вакансии не находящиеся в архиве.
        }
        """

        self.url_sj = "https://api.superjob.ru/2.0/vacancies"
        self.headers = {"X-Api-App-Id": "v3.h.4520658.0a666e6cae442ba091ee4ce3655146477abe0dbc.330133918c7b5b59791f305b6726e57ed8257bb7"}
        self.params = {
            "count": 20,
            "page": 0,
            "keyword": text,
            "archive": False
        }


    def get_requests(self):

        """ Метод вывода списка вакансий в json с сайта superjob.ru
        или вывод исключения. """

        response = requests.get(self.url_sj, headers=self.headers, params=self.params)
        if response.status_code != 200:
            raise LoadingError(f"Ошибка получения вакансии! Статус {response.status_code}.")
        else:
            return response.json()["objects"]


    def get_vacancies(self):

        """ Метод формирования вывода вакансии с сайта superjob.ru. """

        vacancies = self.get_requests()

        generated_vacancies = []

        for vacancy in vacancies:
            changing_vacancy = {
                "title": vacancy["profession"],
                "url": vacancy["link"],
                "salary_from": vacancy["payment_from"],
                "salary_to": vacancy["payment_to"],
                "work_experience": vacancy["experience"]["title"],
                "platform": "Super Job"
            }
            generated_vacancies.append(changing_vacancy)

        return generated_vacancies