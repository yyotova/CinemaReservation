from cinema_reservation_system.utls.file_manipulation import write_file
from cinema_reservation_system.config.config_info_file import INFO_FILE

def log_info(method):

    def inner_method(*args, **kwargs):
        write_file(INFO_FILE, method(*args, **kwargs))
    return inner_method
