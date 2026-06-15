from src.logger import setup_logger
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

from src.logger import setup_logger
from src.exception import MyException
from src.data.data_ingestion import load_data

logging = setup_logger()

class DataValidator:
    """
    A class that basically checks and validates our data,
    to know the quality of the data and identify any missing values, duplicates, 
    or any other issues that might affect our analysis and modeling.
    """

    def __init__(self, data: pd.DataFrame):
        self.data = data
        logging.info("Data validation initiated.....")

    def checking_data_if_empty(self):
        """
        Check if the data is empty and return a boolean value indicating whether it is empty or not,
        if the data is empty, it will log an error message and raise a custom exception.
        """

        try:
            logging.info("Checking if the data is empty or not.....")
            if self.data.empty:
                logging.error("The data is empty, please check your data source and try again.")
                raise MyException("The data is empty, please check your data source ......", sys)
            else:
                logging.info("The data is not empty, proceeding to the next step.....")

        except Exception as e:
            logging.error(f"An error occurred while checking if the data is empty: {e}")
            raise MyException(e, sys)

    def checking_for_missing_values(self):
        """
        Check for missing values in the data 
        """

        missing_values = self.data.isnull().sum()

        if missing_values.sum() > 0:
            logging.warning(f"Missing values detected in the data: {missing_values}")
        else:
            logging.info("No missing values detected in the data, proceeding to the next step.....")
        return missing_values

    def checking_for_duplicates(self):
        """
        This function checks for duplicate records in the data and return the number of duplicate records found.
        If duplicate records are found, it will log a warning message with the number of duplicates.
        If no duplicate records are found, it will log an info message indicating that there are no duplicates.
        """

        try:
            duplicates = self.data.duplicated().sum()

            if duplicates > 0:
                logging.warning(f"Duplicate records detected with the total number of : {duplicates}")
            else:
                logging.info("No duplicate records detected, proceeding to the next step.....")
        except Exception as e:
            logging.error(f"Error occurred while checking for duplicates: {e}")
            raise MyException(e, sys)


def starting_datavalidation(data: pd.DataFrame):
    """
    This function starts the data validation process by calling the other functions in the class to check for empty data, missing values, and duplicates.
    It will log the start and end of the data validation process.
    """

    try:
        logging.info("the data validation pipeline has started.....")
        validator_engine = DataValidator(data)
        validator_engine.checking_data_if_empty()
        validator_engine.checking_for_missing_values()
        validator_engine.checking_for_duplicates()

        logging.info("data validation completed successfully.....")
        logging.info(data.head())

        return data
    except Exception as e:
        logging.error(f"Error occurred during data validation: {e}")
        raise MyException(e, sys)


data = load_data()
starting_datavalidation(data)