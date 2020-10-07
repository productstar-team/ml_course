import pandas as pd

from time import sleep


def basic_answer(mode=None):
    if mode is None:
        print("Думаю...")
        sleep(1)
    else:
        print("Запускаю тестирование...")
        sleep(1)
        print("Проверяю метрики...")
        sleep(1)


class ChurnPrediction:
    """
    Класс для проверки задания на предсказание оттока клиентов. Берет на вход
    """

    def __init__(self):
        self.name = ""
        self._drop_runs_number = 0
        self._null_runs_number = 0
        self._new_feature_runs_number = 0
        self._model_runs_number = 0
        print('Привет! Приятно познакомиться!')

    def test_task(self, df=None):
        if df is None:
            print(
                "Давайте представим, что здесь написано очень интересное задание!"
            )
        elif isinstance(df, pd.DataFrame):
            basic_answer()
            print(
                "Ого! Датасет, сейчас мы будем его исследовать, интересно, что в нем."
            )
            print("Сам я не справляюсь - нужна твоя помощь")

    def drop_task(self, df=None, answer="Условие"):
        """
        Метод для проверки задания на удаление колонок с большим количесвто уникальных значений. А также персонализированной колонки Surname
        :return: None
        """

        if df is None:
            print(
                "В датафрейме есть несколько колонок, в которых слишком много уникальных значений, нужно их найти и удалить."
                "А получившийся датафрейм передать мне в параметрах."
            )
        else:
            if not isinstance(answer, pd.DataFrame):
                basic_answer()
                print("Ой-ой. Я тебя не понимаю, мне нужен pd.DataFrame без колонок, в которых слишком много уникальных значений")
            else:
                basic_answer()
                self._drop_runs_number += 1
                if (self._drop_runs_number == 2) & ("RowNumber" in df.columns):
                    print("Тут может пригодиться метод .nunique()")
                elif "RowNumber" in df.columns:
                    print(
                        "Нужно ответить на очень важный вопрос - сколько уникальных значений имеет каждый признак."
                    )
                elif "CustomerId" in df.columns:
                    print(
                        "Нужно ответить на очень важный вопрос - сколько уникальных значений имеет каждый признак."
                    )

                elif "Surname" in df.columns:
                    print(
                        "Осталась еще одна колонка. У людей есть важный почти уникальный признак. А как тебя зовут?"
                    )

                elif (
                    ("RowNumber" not in df.columns)
                    & ("CustomerId" not in df.columns)
                    & ("Surname" not in df.columns)
                ):
                    basic_answer()
                    print("Кодовая фраза Data")
                    print("Ура! Первое задание позади!")

    def null_task(self, answer=None):
        if answer is None:
            print(
                "Нужно понять есть ли в датафрейме пропущенные значения и отправить ответ мне\n"
                "Я понимаю только 'Да' или 'Нет'"
            )
        else:
            basic_answer()
            if answer.lower() == "нет":
                print("Ура! Второе задание позади!")
                print("Следующая кодовая фраза Science")
            elif answer.lower() == "да":
                print(
                    "Увы :( Тут поможет метод .isnull().sum() попробуй еще раз"
                )
            else:
                print("Ой-ой я понимаю только да или нет :)")

    def production_quality(self, answer=None):


        if answer is None:
            print(
                "Я умею оценивать качество на тесте. Метрика, которую я измеряю ROC-AUC."
                "Тут можно отправлять сделанные предсказания. Чтобы я не запутался куда какие предсказания, давай будем присылать в виде датафрейма "
                "у которого первая колонка 'RowNumber', а вторая 'predict'. Пример посылки попробуем, когда отправим submission."
            )
        else:
            if not isinstance(answer, pd.DataFrame):
                basic_answer()
                print("Ой-Ой. Я тебя не понимаю - мне нужен pd.DataFrame с колонками RowNumber и predict. predict - это предсказание твоей модели")
            else:
                basic_answer(mode="test")
                from sklearn.metrics import roc_auc_score
                import random

                merged = pd.read_csv("./data/meta_file.csv").merge(
                    answer, on=["RowNumber"]
                )
                score = roc_auc_score(merged["Exited"], merged["predict"])
                print(
                    f"Твой результат: {roc_auc_score(merged['Exited'], merged['predict'])}"
                )
                if score == 0.5:
                    print("Ого! Да это же самое хитрое решение - хоть я и простой бот, "
                          "но монетку подбросить и наугад сказать даже я смогу."
                          "Я уверен - как-то точно можно улучшить предсказания!")

                elif score >= 0.8:
                    print(
                        "Наконец-то мы  сэкономили денег! Чтобы себя порадовать - можно посчитать примерные значения в деньгах, как мы посчитали с бейзлайном :)."
                        " Финальная кодовая фраза '- моя любимая наука' "
                        "Если вспомнить все предыдущие получится: Data Science - моя любимая наука"
                        "Что-то правда, то правда - обожаю анализировать данные, особенно, когда мне помогают"
                    )
                else:
                    basic_answer()
                    answers = ["А что если попробовать бустинг?",
                        "Ты же помнишь, что ROC-AUC считается по вероятностям?",
                        "А что если построить случайный лес?",
                        "Нужно качество больше 0.80, я верю - у тебя получится!"]
                    print(random.choice(answers))
