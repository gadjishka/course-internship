from dataclasses import dataclass
from datetime import datetime
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    @staticmethod
    def data_int(date: datetime):
        tmp = str(date).split('-')
        return [int(tmp[0]), int(tmp[1]), int(tmp[2].split()[0])]

    @staticmethod
    def ex_date(date_1: list, date_2: list):
        if date_1[0] != date_2[0]:
            return 1
        elif date_1[1] != date_2[1]:
            return 2
        else:
            return 0

    @classmethod
    def date_schedule(cls, ex, start, end):
        ans = []
        if ex == 0:
            for i in range(start[2], end[2] + 1):
                ans.append(datetime(start[0], start[1], i))
        elif ex == 2:
            for i in range(start[2], cls.month[start[1] - 1] + 1):
                ans.append(datetime(start[0], start[1], i))
            if end[1] - start[1] == 1:
                for i in range(1, end[2] + 1):
                    ans.append(datetime(end[0], end[1], i))
            else:
                for i in range(start[1], end[1]):
                    for j in range(1, cls.month[i - 1] + 1):
                        ans.append(datetime(end[0], i, j))
                for i in range(1, end[2] + 1):
                    ans.append(datetime(end[0], end[1], i))
        elif ex == 1:
            for i in range(start[1], 13):
                for j in range(1, cls.month[i - 1] + 1):
                    ans.append(datetime(start[0], i, j))
            for i in range(start[0] + 1, end[0]):
                for j in range(1, 13):
                    for h in range(1, cls.month[j - 1] + 1):
                        ans.append(datetime(i, j, h))
            for i in range(1, end[1]):
                for j in range(1, cls.month[i - 1] + 1):
                    ans.append(datetime(end[0], i, j))
            for i in range(1, end[2] + 1):
                ans.append(datetime(end[0], end[1], i))
        return ans

    def schedule(self):  # -> Generator[datetime, None, None]:
        ans = []
        start_1 = self.data_int(self.dates[0][0])
        end_1 = self.data_int(self.dates[0][1])
        start_2 = self.data_int(self.dates[1][0])
        end_2 = self.data_int(self.dates[1][1])
        ex_1 = self.ex_date(start_1, end_1)
        ex_2 = self.ex_date(start_2, end_2)
        ans += self.date_schedule(ex_1, start_1, end_1)
        ans += self.date_schedule(ex_2, start_2, end_2)
        return ans


m = Movie('sw', [
    (datetime(2020, 1, 1), datetime(2020, 1, 7)),
    (datetime(2020, 1, 15), datetime(2020, 2, 7))
])

for d in m.schedule():
    print(d)
