from abc import abstractmethod
from sklearn import metrics


class BaseModel:
    def __init__(self, X, y) -> None:
        self.model = self.construct_model()
        self.X = X
        self.y = y

    def fit(self):
        self.X_train, self.X_test, self.y_train, self.y_test = self.train_test_split()
        self.model.fit(X=self.X_train, y=self.y_train)
        self.y_test_predicted = self.model.predict(self.X_test)

    def log_evaluation(self):
        mse = metrics.mean_squared_error(self.y_test, self.y_test_predicted)
        mae = metrics.mean_absolute_error(self.y_test, self.y_test_predicted)
        r2 = metrics.r2_score(self.y_test, self.y_test_predicted)

        print(type(self.model).__name__)
        print('Mean sqaue error: ', mse)
        print('Mean absolute error: ', mae)
        print('R2 score: ', r2)
        print('Score: ', self.model.score(self.X_test, self.y_test))

    @abstractmethod
    def construct_model(self):
        pass

    @abstractmethod
    def train_test_split(self):
        pass

    @abstractmethod
    def plot_loss_curve(self):
        pass

    def has_loss_curve(self):
        False
