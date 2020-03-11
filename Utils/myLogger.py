import logging,os,sys
from settings import LOG_DIR

def getMyLogger(log_file_name, name):
        log_file_name = os.path.join(LOG_DIR, log_file_name)
        log_msg_format = '%(name)s:%(asctime)s:%(levelname)s: -- %(message)s  '
        log_date = '%d/%m/%Y %H:%M:%S'
        formatter = logging.Formatter(log_msg_format, log_date)
        file_handler = logging.FileHandler(log_file_name, mode='w')
        file_handler.setFormatter(formatter)
        # file_handler.setLevel(logging.INFO)

        conn_logger = logging.getLogger(name)
        conn_logger.setLevel(logging.DEBUG)
        conn_logger.addHandler(file_handler)

        return conn_logger

if __name__ == '__main__':
        getMyLogger("test.log","vegito")
