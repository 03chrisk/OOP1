from src.multiple_linear_regression import MultipleLinearRegression
from src.regression_plotter import RegressionPlotter
from src.model_saver import ModelSaver

from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np

from sklearn.linear_model import LinearRegression


def Create_Dataset(n):
    X, y = datasets.make_regression(n_samples=100,
                                    n_features=n,
                                    noise=10,
                                    random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    return X_train, X_test, y_train, y_test


def test_regression_model(model, X_test, y_test):
    # Compare predictions to the ground truth by outputting
    prediction = model.predict(X_test).flatten()

    print("Model predictions: ", prediction)
    print("Ground truth: ", y_test)


def compare_model_coefficients(ourmodel, skmodel):
    our_coefficients = ourmodel.get_coefficients()
    sk_coefficients = skmodel.coef_
    sk_intercept = skmodel.intercept_

    coefficients_with_intercept = np.concatenate(([sk_intercept],
                                                  sk_coefficients))

    print("Our Coefficients: ", our_coefficients)
    print("Sklearn Coefficients:", coefficients_with_intercept)


def test_regression_plotter(model, X_test, y_test):
    plotter = RegressionPlotter(model)
    plotter.plot_model(X_test, y_test)


def test_regression_plotter_generic(model, X_test, y_test):
    plotter = RegressionPlotter(model)
    plotter.plot_model(X_test, y_test, plot_type='generic')


def test_model_saver(model, format):
    print("Coefficients of the model we are saving: ")
    print(model.get_coefficients())

    saver = ModelSaver()
    saver.save_model(model, format_type=format, filename='saved_model')

    coefficients = saver.load_model(format_type=format, filename='saved_model')
    model2 = MultipleLinearRegression()
    model2.set_coefficients(coefficients)
    print("Coefficients of the loaded model: ")
    print(model2.get_coefficients())


if __name__ == "__main__":
    # Create dataset with 1 features
    X_train, X_test, y_train, y_test = Create_Dataset(1)
    # Creater a dataset with 2 features to test the 3D plotter
    X_train2, X_test2, y_train2, y_test2 = Create_Dataset(2)
    # Create dataset with 4 features to test generic plotter
    X_train4, X_test4, y_train4, y_test4 = Create_Dataset(4)

    # Create and train the models
    model = MultipleLinearRegression()
    model.train(X_train, y_train)

    skmodel = LinearRegression()
    skmodel.fit(X_train, y_train)

    model2 = MultipleLinearRegression()
    model2.train(X_train2, y_train2)

    model4 = MultipleLinearRegression()
    model4.train(X_train4, y_train4)

    # Testing the mulltiple linear regression class
    input("Press ENTER to continue to test our regression model")
    test_regression_model(model, X_test, y_test)
    input("Press ENTER to continue to see the sklearn model results")
    test_regression_model(skmodel, X_test, y_test)
    input("Press ENTER to continue to compare our model coefficients to the sklearn model coefficients")
    compare_model_coefficients(model, skmodel)

    # Testing 1 feature plot (2D)
    input("Press ENTER to continue to test the regression plotter with 1 feature")
    test_regression_plotter(model, X_test, y_test)

    # Testing 2 feature plot (3D)
    input("Press ENTER to continue to test the regression plotter with 2 features (3D)")
    test_regression_plotter(model2, X_test2, y_test2)
    input("Press ENTER to continue to test the regression plotter with 2 features (Generic)")
    test_regression_plotter_generic(model2, X_test2, y_test2)

    # Testing 4 feature plot (generic)
    input("Press ENTER to continue to test the regression plotter with 4 features (Generic)")
    test_regression_plotter(model4, X_test4, y_test4)

    # Testing the saver class
    input("Press ENTER to continue to testing the saver")

    print("SAVER TEST .json")
    test_model_saver(model, format='json')

    print("")

    print("SAVER TEST .csv")
    test_model_saver(model, format='csv')
