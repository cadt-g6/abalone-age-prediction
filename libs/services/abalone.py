import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn import metrics
from datetime import datetime


class AbaloneModelService:
    def __init__(self):
        with open("models/model.pkl", "rb") as f:
            self.model = pickle.load(f)

        cleaned_data = pd.read_csv("datasets/cleaned/abalone.csv")

        self.y = cleaned_data["Age"]
        self.X = cleaned_data.drop(["Age"], axis=1)

    def pre_train_until_count(self, count=100, show_log=False):
        print("Start training...")
        print("Target count:", count)
        print("\n\n\n")
        best = 0

        for _ in range(count):
            X_train, X_test, y_train, y_test = train_test_split(
                self.X, self.y, test_size=0.2, random_state=0
            )
            self.model.fit(X_train, y_train)
            y_pred = self.model.predict(X_test)
            score = metrics.r2_score(y_test, y_pred)

            with open("logs/daily.log", "a") as f:
                date = str(datetime.now())
                predict_percentage = f"{round(score * 100)} %"
                logs = """\n======= Saved Model =======\nDate: {}\nScore: {}\nPredict Percentages: {}\n===========================\n""".format(
                    date[:19], score, predict_percentage
                )
                f.write(logs)

            if show_log:
                print(f"Current score: {score}")

            if score > best:
                best = score
                with open("models/model.pkl", "wb") as f:
                    pickle.dump(self.model, f)

                with open("logs/new_model.log", "a") as f:
                    date = str(datetime.now())
                    predict_percentage = f"{round(score * 100)} %"
                    logs = """\n===== New Model Saved =====\nDate: {}\nScore: {}\nPredict Percentages: {}\n===========================\n""".format(
                        date[:19], score, predict_percentage
                    )
                    f.write(logs)

                if show_log:
                    print(logs)

        date = str(datetime.now())
        print("========== Final ==========")
        print("Date:", date[:19])
        print("Score:", best)
        print(f"Predict Percentages: {round(best * 100)} %")
        print("===========================")

    def pre_train_until_score(self, target_score=100, show_log=False):
        print("Start training...")
        print("Target score:", target_score)
        print("\n\n\n")

        target_score = target_score / 100
        best = 0

        while best < target_score:
            X_train, X_test, y_train, y_test = train_test_split(
                self.X, self.y, test_size=0.2, random_state=0
            )
            self.model.fit(X_train, y_train)
            y_pred = self.model.predict(X_test)
            score = metrics.r2_score(y_test, y_pred)

            with open("logs/daily.log", "a") as f:
                date = str(datetime.now())
                predict_percentage = f"{round(score * 100)} %"
                logs = """\n======= Saved Model =======\nDate: {}\nScore: {}\nPredict Percentages: {}\n===========================\n""".format(
                    date[:19], score, predict_percentage
                )
                f.write(logs)

            if show_log:
                print(f"Current score: {score}")

            if score > best:
                best = score
                with open("models/model.pkl", "wb") as f:
                    pickle.dump(self.model, f)

                with open("logs/new_model.log", "a") as f:
                    date = str(datetime.now())
                    predict_percentage = f"{round(score * 100)} %"
                    logs = """\n===== New Model Saved =====\nDate: {}\nScore: {}\nPredict Percentages: {}\n===========================\n""".format(
                        date[:19], score, predict_percentage
                    )
                    f.write(logs)

                if show_log:
                    print(logs)

        date = str(datetime.now())
        print("========== Final ==========")
        print("Date:", date[:19])
        print("Score:", best)
        print(f"Predict Percentages: {round(best * 100)} %")
        print("===========================")

    def predict(self, inputs: dict):
        sample_df = pd.read_csv("datasets/cleaned/abalone.csv")
        sample_df = sample_df.drop(["Age"], axis=1)
        df = pd.DataFrame(columns=sample_df.columns)
        df = df.append(
            {
                "Sex": inputs["Sex"],
                "Length": inputs["Length"],
                "Diameter": inputs["Diameter"],
                "Height": inputs["Height"],
                "Whole weight": inputs["Whole weight"],
                "Shucked weight": inputs["Shucked weight"],
                "Viscera weight": inputs["Viscera weight"],
                "Shell weight": inputs["Shell weight"],
            },
            ignore_index=True,
        )
        return round(self.model.predict(df)[0], 1)
