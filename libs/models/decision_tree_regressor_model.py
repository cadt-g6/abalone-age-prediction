from libs.models.base_model import BaseModel
from sklearn.tree import DecisionTreeRegressor
import sklearn.model_selection as spliter


class DecisionTreeRegressorModel(BaseModel):
    def construct_model(self):
        return DecisionTreeRegressor()

    def train_test_split(self):
        return spliter.train_test_split(self.X, self.y, test_size=0.1, random_state=0)
