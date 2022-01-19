from datetime import date, datetime
import os
from calendar import month_name, monthrange
from shutil import copyfile

BASE_DIR = "~"
TEMPLATE = "./template.md"


def get_year():
    return (date.today()).year


def get_month():
    return (date.today()).month


def get_day():
    return (date.today()).day


def get_path(path):
    return os.path.exists(path=path)


def create_days(month, year, path):
    num_days = monthrange(year, month)[1] + 1
    for day in range(1, num_days):
        if check_if_weekday(day):
            file_path = f"{path}/{day}.md"
            copyfile(TEMPLATE, file_path)


def check_if_weekday(day):
    d = datetime(get_year(), get_month(), day)
    # weekdays are 0 to 4
    return d.weekday() <= 4


if __name__ == "__main__":
    if get_day() == 1:
        my_dir = os.path.expanduser(BASE_DIR)
        notes_dir = f"{my_dir}/notes"
        if not get_path(notes_dir):
            os.mkdir(notes_dir)
        year_directory_path = f"{notes_dir}/{get_year()}"
        if not get_path(year_directory_path):
            os.mkdir(year_directory_path)
        month_name = month_name[get_month()]
        month_directory_path = f"{year_directory_path}/{month_name}"
        if not get_path(month_directory_path):
            os.mkdir(month_directory_path)
        create_days(get_month(), get_year(), month_directory_path)
