import csv
import json
from typing import Any
import numpy as np


class ModelSaver:
    def __init__(self) -> None:
        pass

    def save_model(self, model: Any, format_type: str, filename: str) -> None:
        """
        Saves model coefficients for a machine learning model as a json or
        csv file based on user specification.

        Args:
            model: any machine learning model who's coefficients you want to
            save
            format_type: a string specifying the format, eiter 'json' or 'csv'
            filename: a string specifying the file name

        Retruns:
            None

        Raises:
            Value Error when format_type or filename are not strings
            Value Error ehen format_type is not 'csv' or 'json'
        """

        if not isinstance(format_type, str) or not isinstance(filename, str):
            raise ValueError("Format_type and filename have to be strings")

        coefficients = model.get_coefficients()

        if format_type == 'csv':
            self.__save_csv(coefficients, filename)
        elif format_type == 'json':
            self.__save_json(coefficients, filename)
        else:
            raise ValueError("Unsupported format type.")

    def load_model(self, format_type: str, filename: str) -> np.ndarray:
        """
        Loads model coefficients for a machine learning model from a json or
        csv file based on user specification.

        Args:
            model: any machine learning model who's coefficients you want to
            save
            format_type: a string specifying the format, eiter 'json' or 'csv'
            filename: a string specifying the file name

        Retruns:
            Weights for the machine learning model

        Raises:
            Value Error when format_type or filename are not strings
            Value Error ehen format_type is not 'csv' or 'json'
        """

        if not isinstance(format_type, str) or not isinstance(filename, str):
            raise ValueError("Format_type and filename have to be strings")

        if format_type == 'csv':
            weights = self.__load_csv(filename)
        elif format_type == 'json':
            weights = self.__load_json(filename)
        else:
            raise ValueError("Unsupported format type.")

        return weights

    def __save_csv(self, coefficients: np.ndarray, filename: str) -> None:

        if not isinstance(coefficients, np.ndarray):
            raise ValueError("Coefficients must be an np.ndarray")

        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(coefficients.flatten())

    def __save_json(self, coefficients: np.ndarray, filename: str) -> None:

        if not isinstance(coefficients, np.ndarray):
            raise ValueError("Coefficients must be an np.ndarray")

        with open(filename, 'w') as jsonfile:
            json.dump({'coefficients': coefficients.flatten().tolist()},
                      jsonfile)

    def __load_json(self, filename: str) -> np.ndarray:
        with open(filename, 'r') as jsonfile:
            data = json.load(jsonfile)
            return np.array(data['coefficients'])

    def __load_csv(self, filename: str) -> np.ndarray:
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            return np.array(next(reader), dtype=float)
