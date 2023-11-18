import numpy as np


class ComProcessor:
    """_summary_"""

    def __init__(
        self, current_price: float, price_array: np.ndarray, qty_array: np.ndarray
    ):
        self.current_price = current_price
        self.price_array = price_array
        self.qty_array = qty_array

    def calculate_com(self) -> float:
        self.com = np.dot(self.price_array, self.qty_array) / sum(self.qty_array)
        return

    def calculate_com_relative(self) -> float:
        self.com_relative = ((self.current_price - self.com) / self.com) * 100
        return
