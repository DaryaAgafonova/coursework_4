class Vacancy:

    """ Класс для работы с вакансиями. """

    def __init__(self, title, url, salary_from, salary_to, work_experience, platform):

        """
        Инициализация атрибутов класса.

        title - название вакансии,
        url - ссылка на вакансию,
        salary_from - зарплата от,
        salary_to - зарплато до,
        work_experience - требуемый опыт работы,
        platform - платформа.
        """

        self.title = title
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.work_experience = work_experience
        self.platform = platform


    def __str__(self):

        """ Метод вывода информации для пользователя. """

        return f"""Название вакансии: {self.title}.
Зарплата от {self.salary_from} до {self.salary_to}.
Требуемый опыт работы: {self.work_experience}.
Ссылка на вакансию: {self.url},
Платформа: {self.platform}"""


    def __le__(self, other):

        """ Метод сравнения "меньше или равно" вакансий между собой по зарплате. """

        return self.salary_from <= other.salary_from


    def __ge__(self, other):

        """ Метод сравнения "больше или равно" вакансий между собой по зарплате. """

        return self.salary_from >= other.salary_from