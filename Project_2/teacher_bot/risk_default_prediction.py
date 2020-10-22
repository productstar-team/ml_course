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
        

class RiskDefaultPrediction:
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

    def production_quality(self, answer=None):


        if answer is None:
            print(
                "Я умею оценивать качество на тесте. Метрика, которую я измеряю ROC-AUC."
                "Тут можно отправлять сделанные предсказания. Чтобы я не запутался куда какие предсказания, давай будем присылать в виде датафрейма "
                "у которого первая колонка 'sk_id_curr', а вторая 'score'. Пример посылки попробуем, когда отправим submission."
            )
        else:
            if not isinstance(answer, pd.DataFrame):
                basic_answer()
                print("Ой-Ой. Я тебя не понимаю - мне нужен pd.DataFrame с колонками 'sk_id_curr', а вторая 'score'. Score - это предсказание твоей модели")
            else:
                basic_answer(mode="test")
                from sklearn.metrics import roc_auc_score
                import random

                merged = pd.read_csv("../data/test_target.csv").merge(
                    answer, on=["sk_id_curr"]
                )
                score = roc_auc_score(merged["target"], merged["score"])
                print(
                    f"Твой результат: {roc_auc_score(merged['target'], merged['score'])}"
                )
                if score == 0.5:
                    print("Ого! Да это же самое хитрое решение - хоть я и простой бот, "
                          "но монетку подбросить и наугад сказать даже я смогу."
                          "Я уверен - как-то точно можно улучшить предсказания!")

                elif score >= 0.77:
                    print(
                        "Ура! Мы получили удовлетворительную по качеству модельку!"
                        " Финальная кодовая фраза 'Data Scientist’ы делают этот мир лучше!' "
                        "Это правда, мы с тобой сделали мир лучше, позволив компании уверенее "
                        "принимать решения на основе данных и увереннее развивать свой бизнес!"
                    )
                else:
                    basic_answer()
                    answers = [
                        "А что если попробовать бустинг?",
                        "Ты же помнишь, что ROC-AUC считается по вероятностям?",
                        "А ты использовал все доступные источники данных?",
                        "Может тебе увеличить сложность модели? Увеличить num_boost_rounds? А early_stopping_rounds?"
                        "Признаки можно создавать не только с помощью агрегаций, но и с помощью отношений (сумма кредита к сумме зарплаты)",
                        "Если ты используешь бустинг, то все реализации ты попробовал? LightGBM? XGBoost? CatBoost?",
                        "Может быть имеет смысл сделать отбор признаков? Удалить все лишнее?"
                        ]
                    print(random.choice(answers))
                    print("Нужно качество больше 0.77, я верю - у тебя получится!")