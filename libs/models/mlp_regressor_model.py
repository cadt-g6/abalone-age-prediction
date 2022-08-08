from libs.models.base_model import BaseModel
from sklearn.neural_network import MLPRegressor
import sklearn.model_selection as spliter
import pandas as pd


class MLPRegressorModel(BaseModel):
    def construct_model(self):
        return MLPRegressor(
            hidden_layer_sizes=(2, 100),
            activation='relu',
            solver='adam',
            learning_rate_init=0.1,
            max_iter=1000
        )

    def train_test_split(self):
        return spliter.train_test_split(self.X, self.y, test_size=0.1, random_state=0)

    def has_loss_curve(self):
        return True

    def plot_loss_curve(self):
        pd.DataFrame(self.model.loss_curve_).plot()
