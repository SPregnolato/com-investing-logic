import numpy as np
import matplotlib.pyplot as plt

import plotly.graph_objs as go


class ComProcessor:
    """_summary_"""

    def __init__(
        self,
        current_price: float,
        price_array: np.ndarray,
        qty_array: np.ndarray,
        total_capital: float,
    ):
        self.current_price = current_price
        self.price_array = price_array
        self.qty_array = qty_array
        self.qty_invested = sum(qty_array)
        self.capital_invested = np.dot(self.price_array, self.qty_array)
        self.capital_invested_percentage = (self.capital_invested / total_capital) * 100
        self.capital_available = total_capital - self.capital_invested
        self.calculate_com()
        self.calculate_com_relative_to_current_price()

    def calculate_com(self) -> None:
        self.com = self.capital_invested / self.qty_invested
        return

    def calculate_com_relative_to_current_price(self) -> None:
        self.com_relative = ((self.current_price - self.com) / self.com) * 100
        return

    def calculate_potential_com(self, qty: float) -> float:
        potential_com = (self.capital_invested + self.current_price * qty) / (
            self.qty_invested + qty
        )
        return potential_com


if __name__ == "__main__":
    current_price = 5

    price_array = np.array([5, 3, 6])
    qty_array = np.array([10, 10, 10])
    total_capital = 500

    comProcessor = ComProcessor(current_price, price_array, qty_array, total_capital)

    purchase_range = np.array(
        range(-comProcessor.capital_invested + 1, comProcessor.capital_available)
    )

    qty_range = purchase_range / current_price

    potential_com_array = np.array(
        list(map(comProcessor.calculate_potential_com, qty_range))
    )

    potential_com_array_relative = (
        potential_com_array - comProcessor.com
    ) / comProcessor.com

    potential_qty_array = comProcessor.qty_invested + qty_range
    potential_qty_array_relative = (
        potential_qty_array - comProcessor.qty_invested
    ) / comProcessor.qty_invested

    # # Plotting the time series of individual dots
    # plt.figure(figsize=(8, 4))
    # plt.scatter(
    #     purchase_range, potential_com_array_relative, color="red"
    # )  # Scatter plot
    # plt.title("CoM ratio based on qty")
    # plt.xlabel("Qty")
    # plt.ylabel("CoM_Potential/CoM")
    # plt.grid(True)
    # plt.tight_layout()
    # plt.show()
    # Create a scatter plot with Plotly
    fig = go.Figure(
        data=go.Scatter(x=qty_range, y=potential_com_array_relative, mode="markers")
    )
    fig.update_layout(
        title="CoM ratio based on qty",
        xaxis=dict(title="Qty"),
        yaxis=dict(title="CoM_Potential/CoM"),
        hovermode="x",  # Show hover information at the nearest point along the x-axis
        showlegend=False,  # Hide legend for this example
    )
    fig.show()

    fig = go.Figure(
        data=go.Scatter(x=qty_range, y=potential_qty_array_relative, mode="markers")
    )
    fig.update_layout(
        title="Qty ratio based on qty",
        xaxis=dict(title="Qty"),
        yaxis=dict(title="Qty_Potential/Qty"),
        hovermode="x",  # Show hover information at the nearest point along the x-axis
        showlegend=False,  # Hide legend for this example
    )
    fig.show()
