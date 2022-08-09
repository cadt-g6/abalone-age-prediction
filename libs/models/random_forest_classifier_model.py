from libs.models.base_model import BaseModel
from sklearn.ensemble import RandomForestClassifier
import sklearn.model_selection as spliter
from sklearn import preprocessing


class RandomForestClassifierModel(BaseModel):
    def construct_model(self):
        return RandomForestClassifier()

    def train_test_split(self):
        X_train, X_test, y_train, y_test = spliter.train_test_split(
            self.X, self.y, test_size=0.1, random_state=0)

        encoder = preprocessing.LabelEncoder()
        y_train = encoder.fit_transform(y_train)
        y_test = encoder.fit_transform(y_test)

        return X_train, X_test, y_train, y_test
