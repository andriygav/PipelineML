from metaflow import FlowSpec, step

import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


class LinearModelFlow(FlowSpec):
    """
    Попытка создать пайплайн для обучения линейной модели с подбором гиперпараметров.
    """
    @step
    def start(self):
        """
        Здесь мы генерим синтетические данные, но можно можно и загружать с файла
        """
        self.X, self.Y = make_classification(n_samples=400, n_features=2, 
                                             n_informative=2, n_classes=2, 
                                             n_redundant=0,
                                             n_clusters_per_class=1,
                                             random_state=0)
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(
            self.X, self.Y, test_size=100, random_state=0)
        self.next(self.model)

    @step
    def model(self):
        """
        Определяем гиперпараметры модели
        """
        self.Cs = np.e**np.linspace(-3, 3, 10)
        self.next(self.model_fit, foreach='Cs')
        
    @step
    def model_fit(self):
        """
        Обучаем модель
        """
        self.C = self.input
        self.log_reg = LogisticRegression(C=self.C)
        print("fit model with C={}".format(self.input))
        
        self.log_reg.fit(self.X_train, self.Y_train)
        
        self.score = self.log_reg.score(self.X_test, self.Y_test)
        
        self.next(self.join)

    @step
    def join(self, inputs):
        """
        Объединяем результаты разных моделек
        """
        # Merge results from the genre specific computations.
        self.scores = {'C={}'.format(inp.C): {'score': inp.score} for inp in inputs}

        self.next(self.end)
        
    @step
    def end(self):
        """
        Конец обучения
        """
        print(self.scores)


if __name__ == '__main__':
    LinearModelFlow()