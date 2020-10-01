import pandas as pd
import numpy as np

from time import sleep


def basic_answer():
    print("Дай подумать...")
    sleep(1)


class churn_prediction:
    """
    Класс для проверки задания на предсказание оттока клиентов. Берет на вход
    """

    def __init__():
        self.name = ""
        self.drop_runs_number = 0
        self.null_runs_number = 0
        self.new_feature_runs_number = 0
        self.model_runs_number = 0

    def test_task(self, answer="Условие"):
        if answer == "Условие":
            print("Описание тестового задание! Как интереесно!")
        elif isinstance(answer, pd.DataFrame):
            print("Ого! Датасет, сейчас мы будем его исследовать, интересно, что в нем.")
            answer.head()
            print("Сам я не справляюсь - нужна твоя помощь")

    def drop_task(self, df, answer="Условие"):
        """
        Метод для проверки задания на удаление колонок с большим количесвто уникальных значений. А также персонализированной колонки Surname
        :return: None
        """
        self.drop_runs_number += 1

        if answer == "Условие":
            print(
                "В датафрейме есть несколько колонок, в которых слишком много уникальных значений, нужно их найти и удалить."
                "А получившийся датафрейм передать мне в параметрах."
            )
        else:
            basic_answer()
            if self.drop_runs_number == 2:
                print("тут поможет метод nunique()")

            elif "RowNumber" in df.columns:
                print(
                    "Нужно ответить на очень важный вопрос - сколько уникальных значений имеет каждый признак."
                )

            elif "CustomerId" in df.columns:
                print(
                    "Нужно ответить на очень важный вопрос - сколько уникальных значений имеет каждый признак."
                )

            elif ("Surname" in df.columns) & (self.drop_runs_number > 5):
                print("У людей есть важный почти уникальный признак. А как тебя зовут?")

            elif (
                ("RowNumber" not in df.columns)
                & ("RowNumber" not in df.columns)
                & ("RowNumber" not in df.columns)
            ):
                print("Кодовая фраза Data")
                print("Ура! Первое задание позади!")

    def null_task(self, answer):
        if answer == "Условие":
            print(
                "Нужно понять есть ли в датафрейме пропущенные значения и отправить ответ мне"
            )
        else:
            if answer.lower() == "нет":
                print("Ура! Второе задание позади!")
                print("Кодовая фраза Science")
            elif answer.lower() == "да":
                print("Увы :( Тут поможет метод .isnull().sum() попробуй еще раз")
            else:
                print("Ой-ой я понимаю только да или нет :)")

    def score_task(self, answer, df=None):

        if df==None:
            print('Мне нужен тестовый датасет, чтобы посчитать качество :(')
        if answer == "Условие":
            print(
                "А теперь самое интересное! Нужно построить модель, которая на тестовом файле будет давать х качество"
            )
        else:


            if isinstance(answer, LogisticRegression):



