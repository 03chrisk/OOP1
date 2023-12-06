import numpy as np


class MultipleLinearRegression():
    def __init__(self) -> None:
        self.__coefficients = None

    def get_coefficients(self) -> np.ndarray:
        return self.__coefficients

    def set_coefficients(self, new_val: np.ndarray) -> None:
        self.__coefficients = new_val

    def train(self, X_train: np.ndarray, y_train: np.ndarray) -> None:
        '''
        Fit data to the model based on the matrix approach to Linear Regression

        Args:
            X_train (numpy.ndarray): Independent variables of train data.
            y_train (numpy.ndarray): Dependent variable of train data.

        Returns:
            None

        Raises:
            Value Error when X_train or y_train is not an np.ndarray
            Value Error when matrix is singular and cannot be inverted

        '''

        if not isinstance(X_train, np.ndarray) or not isinstance(y_train,
                                                                 np.ndarray):
            raise ValueError("Training data must be an np.ndarray")

        # Putting the bias term into the coefficient matrix
        X_b = np.c_[np.ones(len(X_train)), X_train]

        try:
            # Find optimal parameter configuration
            result = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y_train)
        except np.linalg.LinAlgError as e:
            raise ValueError("The matrix is singular and cannot be inverted") from e

        self.set_coefficients(result)

    def predict(self, X_test: np.ndarray) -> np.ndarray:
        '''
        Fucntion to predict on new data.

        PARAMETERS:
        X_test (numpy.ndarray): Independent variables data.

        RETURNS:
        y_predict (numpy.ndarray): Predicted dependent variable.

        RAISES:
        Value Error when X_test is not an np.ndarray
        '''
        if not isinstance(X_test, np.ndarray):
            raise ValueError("Testing data must be an np.ndarray")

        coefficients = self.get_coefficients()
        X_test = np.c_[np.ones((len(X_test))), X_test]
        y_predict = np.dot(X_test, coefficients)
        y_predict = y_predict.reshape(-1, 1)

        return y_predict
