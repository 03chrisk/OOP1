import matplotlib.pyplot as plt
from typing import Any
import numpy as np


class RegressionPlotter:
    def __init__(self, model: Any) -> None:
        self.__model = model

    def get_model(self) -> Any:
        return self.__model

    def plot_model(self,
                   X_test: np.ndarray,
                   y_test: np.ndarray,
                   plot_type: str = None) -> None:
        """
        Plots a linear regression line or plane on top of a scatterplot of
        data.

        This can 2D or 3D depending on the number of features and whether
        'generic' is specified as plot_type.

        Args:
            X_test: test data to be plotted (independent variable)
            y_test: target to be plotted (dependet variable)
            plot_type: string that specifies what plot type should be. Can be
                       either 'generic' or left out.

        Returns:
            None

        Raises:
            Value Error when testing data is not an np.ndarray
            Value Error when plot type is specified but not a string 
            Value error when plot type is a string but not 'generic'
        """

        if not isinstance(X_test, np.ndarray) or not isinstance(y_test,
                                                                np.ndarray):
            raise ValueError("Testing data must be an np.ndarray")

        if not isinstance(plot_type, str) and plot_type is not None:
            raise ValueError("Plot type has to be the string 'generic' or left out")

        elif isinstance(plot_type, str) and plot_type != 'generic':
            raise ValueError("Check your spelling. Plot type must be 'generic' or left out")

        num_features = X_test.shape[1]

        if plot_type == 'generic':
            self.__plot_generic(X_test, y_test)
        elif num_features == 1:
            self.__plot_regression(X_test, y_test)
        elif num_features == 2:
            self.__plot_3d_regression(X_test, y_test)
        else:
            self.__plot_generic(X_test, y_test)

    def __plot_regression(self, X_test: np.ndarray, y_test: np.ndarray) -> None:
        """
        Plot a regression line given 1 feature and a target
        """

        if not isinstance(X_test, np.ndarray) or not isinstance(y_test,
                                                                np.ndarray):
            raise ValueError("Testing data must be an np.ndarray")

        # Make predictions
        model = self.get_model()
        y_pred_test = model.predict(X_test)

        # Plot the test set
        plt.scatter(X_test, y_test, color='green', label='Actual Test')
        plt.plot(X_test,
                 y_pred_test,
                 color='orange',
                 linewidth=2,
                 label='Predicted Test')

        plt.title('Multiple Linear Regression')
        plt.xlabel('Feature')
        plt.ylabel('Target')
        plt.legend()
        plt.show()

    def __plot_3d_regression(self, X_test: np.ndarray,
                           y_test: np.ndarray) -> None:
        """
        Plot a regression plane given 2 features and a target
        """

        if not isinstance(X_test, np.ndarray) or not isinstance(y_test,
                                                                np.ndarray):
            raise ValueError("Testing data must be an np.ndarray")

        if X_test.shape[1] != 2:
            raise ValueError("This method is designed for 2 features only.")

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x1, x2 = X_test[:, 0], X_test[:, 1]
        model = self.get_model()
        y_pred_test = model.predict(X_test)

        ax.scatter(x1, x2, y_test, color='green', label='Actual Test')
        ax.scatter(x1, x2, y_pred_test, color='orange', label='Predicted Test')

        # Creating a meshgrid for the plane
        x1_plane = np.linspace(min(x1), max(x1), 100)
        x2_plane = np.linspace(min(x2), max(x2), 100)
        x1_plane, x2_plane = np.meshgrid(x1_plane, x2_plane)
        y_plane = model.predict(np.c_[x1_plane.ravel(),
                                      x2_plane.ravel()]).reshape(x1_plane.shape)

        # Plotting the plane
        ax.plot_surface(x1_plane,
                        x2_plane,
                        y_plane,
                        alpha=0.5,
                        color='blue',
                        label='Regression Plane',
                        rstride=100,
                        cstride=100)

        ax.set_xlabel('Feature 1')
        ax.set_ylabel('Feature 2')
        ax.set_zlabel('Target')

        plt.legend()
        plt.show()

    def __plot_generic(self, X_test: np.ndarray, y_test: np.ndarray) -> None:
        """
        Plot a sequence of p plots of 1 feature against the target given a p features and a target.
        """

        if not isinstance(X_test, np.ndarray) or not isinstance(y_test,
                                                                np.ndarray):
            raise ValueError("Testing data must be an np.ndarray")

        model = self.get_model()
        num_features = X_test.shape[1]
        weights = model.get_coefficients()
        intercept = weights[0]

        for i in range(num_features):
            slope = weights[i+1]
            feature_values = X_test[:, i]

            y_pred = slope * feature_values + intercept

            plt.plot(feature_values,
                     y_pred,
                     color='blue',
                     linewidth=2,
                     label='Regression Line')
            plt.scatter(feature_values,
                        y_test,
                        color='green',
                        label='Actual Test')

            plt.legend()
            plt.title('Multiple Linear Regression')
            plt.xlabel(f'feature {i+1}')
            plt.ylabel('Target')
            plt.tight_layout()
            plt.show()
