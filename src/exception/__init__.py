import os
import sys
import logging


def error_message_detail(error: Exception, error_detail: sys) -> str:
    # Extracting the traceback details from the exception information
    _, _, exc_tb = error_detail.exc_info()
    # Getting the file name and line number where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    # create the formatted error message with filename, line number and error message


    # Getting the line number where the exception occurred
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in file: {file_name} at line: {line_number} with error message: {str(error)}"

    logging.error(error_message)  # Log the error message
    return error_message

class MyException(Exception):
    def __init__(self, error_message: str, error_detail: sys) -> None:
        super().__init__(error_message)

        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        # return the error message in proper string format
        return self.error_message