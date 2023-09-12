from class_with_sites import HeadHunter, SuperJob
from class_json_saver import JSONSaver


print("\nПривет, рады тебя видеть здесь :)\n")

""" Бесконечный цикл, в котором пользователь выбирает платформу для просмотра вакансий,
далее вводит ключевое слово для поиска или выводит и повторяет цикл, 
если пользователь ввел платформу, которой нет. """

while True:
    print("""Чтобы посмотреть вакансии, тебе нужно выбрать:
1) Head Hunter - напиши "hh", 
2) Super Job - напиши "sj".\n""")

    user_platform = input().lower().strip()
    if user_platform == "hh":
        print("\nВведите ключевое слово для поиска вакансии.\n")
        global variable
        user_keyword = input().lower().strip()

        head_hunter = HeadHunter(user_keyword)
        vacansies = head_hunter.get_vacancies()
        jsonsaver = JSONSaver("head_hunter.json")

        jsonsaver.writing_vacancies_to_file(vacansies)
        data = jsonsaver.load_vacansies()
        break
    elif user_platform == "sj":
        print("\nВведите ключевое слово для поиска вакансии.\n")
        user_keyword = input().lower().strip()

        super_job = SuperJob(user_keyword)
        vacansies = super_job.get_vacancies()
        jsonsaver = JSONSaver("super_job.json")

        jsonsaver.writing_vacancies_to_file(vacansies)
        data = jsonsaver.load_vacansies()
        break
    else:
        print("""\nТакого сервиса у нас пока что, к сожалению, нет :(
Попробуй другой.\n""")
        continue

""" Бесконечный цикл, в котором пользователь выбирает критерии вывода вакансий, 
если нет нужной цифры - повторяет цикл. """

while True:
    print("""\nПо каким критериям будем искать вакансии?
1) Показать все вакансии - нажмите "1",
2) По зарплате - нажмите "2",
3) Выход - напишите "0".\n""")

    user_criteria = input().lower().strip()
    if user_criteria == "1":
        for element in data:
            print(f"{element}\n")
            print("-" * 50)
        break
    elif user_criteria == "2":
        sorted_salary = list(sorted(data, reverse=True, key=lambda vacancy: vacancy.salary_from))
        for salary_from in sorted_salary:
            print(f"\n{salary_from}\n")
            print("-" * 50)
        break
    elif user_criteria == "0":
        print("\nВсего хорошего, надеемся увидеть вас здесь вновь! :)\n")
        break
    else:
        print("\nПока что в разработке, выберите другую цифру для поиска.")
        continue