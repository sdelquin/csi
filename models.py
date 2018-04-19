import config
import csv
from collections import defaultdict, OrderedDict
from decorators import check_load


class Assistant:
    def __init__(self, year):
        self.datafile = config.DATAFILE.format(year)
        self.__load__()

    def __load__(self):
        with open(self.datafile) as file:
            self.data = list(csv.DictReader(file, delimiter=";"))
        self.changed_data = False

    @check_load
    def all(self):
        return self.data

    @check_load
    def get_assistants(self):
        return sorted([i["name"] for i in self.data])

    @check_load
    def get_books(self):
        return sorted([i["book"] for i in self.data if i["book"]])

    @check_load
    def favproglang_stats(self):
        r = defaultdict(int)
        total_responses = 0
        for d in self.data:
            if d["favproglang"]:
                r[d["favproglang"]] += 1
                total_responses += 1
        for k in r.keys():
            r[k] = (r[k] / total_responses) * 100
        return OrderedDict(sorted(r.items(), key=lambda t: -t[1]))

    def write(self, data):
        with open(self.datafile, "a") as file:
            w = csv.writer(file, delimiter=";")
            w.writerow(data)
        self.changed_data = True
