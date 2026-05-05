# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 10:33:17 2026

@author: Alexis Root
"""
import psycopg2
from sqlalchemy import create_engine


"""
Contains a function to establish a PostgreSQL connection using credentials 
stored in a vault file.
"""


def get_connection(vault_filename: str):
    """
    vault_filename : str
        Name of file containing username (line 1)
        and password (line 2).
    Raises FileNotFoundError if vault file does not exist.
    Raises psycopg2.DatabaseError if connection fails.
    """
    with open(vault_filename, "r", encoding="utf-8") as file:
        username = file.readline().strip()
        password = file.readline().strip()
        
    conn = create_engine(
        f"postgresql+psycopg2://{username}:{password}@localhost:5432/bank"
    )

    connection = psycopg2.connect( #Returns a connection- psycopg2 connection object
        dbname="bank",
        user=username,
        password=password,
        host="localhost",
        port="5432"
    )

    return connection
