# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 11:00:07 2026

@author: Alexis Root
"""

import pandas as pd

"""
Transaction retrieval function for the bank database.
"""


def get_transactions_by_month(connection, month: int, year: int):
    """
    Retrieve transactions for a given month and year.

    Parameters:
    connection : psycopg2 connection #Database connection object.
    month : int
        Month (1-12)
    year : int
        Year (2000-2004)

    Returns dataFrame of transactions without account_id column.
    If invalid month/year, returns one-row DataFrame with all -1 values.
    """
    if month < 1 or month > 12 or year < 2000 or year > 2004:
        print("WARNING: Invalid month or year supplied.")

        columns = [
            "txn_id",
            "txn_date",
            "txn_type_cd",
            "amount",
            "funds_avail_date",
            "teller_emp_id",
            "execution_branch_id",
            "trial104"
        ]

        return pd.DataFrame([[-1] * len(columns)], columns=columns)

    query = """
        SELECT  "txn_id",
         "txn_date",
         "txn_type_cd",
         "amount",
         "funds_avail_date",
         "teller_emp_id",
         "execution_branch_id",
         "trial104"
        FROM transaction
        WHERE EXTRACT(MONTH FROM txn_date) = %s
        AND EXTRACT(YEAR FROM txn_date) = %s
    """

    df = pd.read_sql(query, connection, params=(month, year))

    return df
