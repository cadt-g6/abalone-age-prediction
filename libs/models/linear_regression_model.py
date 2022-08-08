from libs.models.base_model import BaseModel
from sklearn.linear_model import LinearRegression
import sklearn.model_selection as spliter


class LinearRegressionModel(BaseModel):
    def construct_model(self):
        return LinearRegression()

    def train_test_split(self):
        return spliter.train_test_split(self.X, self.y, test_size=0.1, random_state=0)
