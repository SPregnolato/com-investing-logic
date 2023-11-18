import numpy as np


class ComProcessor:
    """_summary_"""

    def __init__(self, price_array: np.ndarray, qty_array: np.ndarray):
        self.price_array = price_array
        self.qty_array = qty_array

    def calculate_com(self) -> float:
        # Method to process inputs, can be extensive
        # ...
        return np.dot(self.price_array, self.qty_array) / sum(self.qty_array)
