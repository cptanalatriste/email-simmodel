""" Data utilities for email process simulation"""
import logging
import time
import gtconfig
import jsonpickle

if gtconfig.is_windows:
    import winsound

ALL_EMAIL_JSON = "E:\Google Drive\phd2\lucene_mail_data\lucene\lucene-threads_sample.json"

logger = gtconfig.get_logger("maildata", "maildata.txt", level=logging.INFO)


def get_mail_threads():
    with open(ALL_EMAIL_JSON) as json_file:
        json_string = json_file.read()
        email_threads = jsonpickle.decode(json_string)

        logger.info("Gathering " + str(len(email_threads)) + " email threads from " + ALL_EMAIL_JSON)

        return email_threads


if __name__ == "__main__":
    start_time = time.time()

    try:
        get_mail_threads()
    finally:
        if gtconfig.is_windows:
            winsound.Beep(2500, 1000)

    print("Execution time in seconds " + str(time.time() - start_time))
