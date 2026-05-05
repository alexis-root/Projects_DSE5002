# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 09:01:38 2026

@author: Alexis Root
"""

import matplotlib.pyplot as plt
import pandas as pd
from db_connection import get_connection
from transactions import get_transactions_by_month



class BankManager:
    """
    BankManager class for managing database access and transaction analysis.
    """

    def __init__(self, vault_filename: str):
        """
        Initialize BankManager with vault file.

        Parameters
        ----------
        vault_filename : str
            Name of vault file containing postgres credentials- Pat.
        """
        self.vault_filename = vault_filename
        self.connection = get_connection(vault_filename)
        self.data = None

    def get_month_transactions(self, month: int, year: int):
        """
        Retrieve transactions for a given month and year.
        """
        self.data = get_transactions_by_month(
            self.connection, month, year
        )
        return self.data

    def plot_transactions_by_day(self, month: int, year: int):
        """
        Generate a bar plot of transaction counts by day.
        """
        df = self.get_month_transactions(month, year)

        # Check for empty or invalid data
        if df.empty or df.iloc[0].eq(-1).all():
            print("No valid data to plot.")
            return

        # Extract day from txn_date
        df["day"] = pd.to_datetime(df["txn_date"]).dt.day

        # Count transactions per day
        counts = df.groupby("day").size()

        # Create bar plot
        ax = counts.plot(kind="bar", figsize=(10, 5))

        # Customize labels
        plt.title(f"Transactions per Day ({month}/{year})")
        plt.xlabel("Day")
        plt.ylabel("Number of Transactions")

        # Rotate x-axis labels for readability
        plt.xticks(rotation=0)  # 0 = horizontal

        plt.tight_layout()
        plt.show()
