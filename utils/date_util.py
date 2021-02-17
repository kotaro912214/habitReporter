import datetime


class DateUtil:
    def __init__(self):
        pass

    @staticmethod
    def make_dates_in_year() -> [datetime.datetime]:
        year = datetime.date.today().year

        d1 = datetime.date(year, 1, 1)
        d2 = datetime.date(year, 12, 31)

        delta = d2 - d1
        dates_in_year = [d1 + datetime.timedelta(i) for i in range(delta.days + 1)]
        return dates_in_year

    @staticmethod
    def make_dates_in_year_dic() -> dict:
        dates_in_year = DateUtil.make_dates_in_year()
        dates_in_year_dic = {}
        for date in dates_in_year:
            dates_in_year_dic[str(date)] = 0
        return dates_in_year_dic

    @staticmethod
    def extract_date(file_path) -> str:
        file_name = file_path.split('/')[-1]
        date_str = file_name.split(".")[0]
        year, month, day = map(int, date_str.split("-")[:3])
        return datetime.date(year=year, month=month, day=day)


if __name__ == "__main__":
    print(DateUtil.extract_date("/Users/kotaro-seki/Documents/my-knowledge/report/daily/2021-02-17-水.md"))
