# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import datetime
import logging
import time
import azure.durable_functions as df
import azure.functions as func


def main(context: func.Context, name: str) -> str:
    timeout = datetime.timedelta(seconds=10)
    deadline = datetime.datetime.utcnow() + timeout

    while datetime.datetime.utcnow() < deadline:
        time.sleep(1)

    #raise Exception("ActivityFunction timed out")
    logging.info("Hello delayed{name}!")
    return f"Hello delayed {name}!"