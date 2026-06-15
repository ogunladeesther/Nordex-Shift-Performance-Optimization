import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import sys


from config.constant import database_path
from src.logger import setup_logger
from src.exception import MyException

logging = setup_logger()

def load_data():
    """
    load data from a database and return it as a pandas DataFrame.
    for the other pipeline to be able to use it
    """

    try:
        logging.info("Data ingestion initiated.....")
        logging.info("Loading data from the database file .....") 
                     
        # Initiating connection to the database file
        connection = sqlite3.connect(database_path)

        # Loading data into a pandas DataFrame
        Shift_Data = pd.read_sql("SELECT * FROM ShiftPerformance", connection)


        logging.info(Shift_Data.head())
        logging.info("Data ingestion completed successfully.....")

        return Shift_Data

    except Exception as e:
        logging.error(f"Error occurred while loading data: {e}")
        raise MyException(e, sys)


load_data()