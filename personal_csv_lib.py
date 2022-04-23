import csv


class CsvFunc:
    def __init__(self, filename, delimiter=","):
        self.file = filename
        self.delimiter = delimiter

    def create_list_from_csv(self):
        lst = []
        with open(self.file) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=self.delimiter)
            for i in csv_reader:
                lst.append(i)
        return lst

    def create_dicts_from_csv(self):
        lst = []
        with open(self.file) as csvfile:
            csv_dict = csv.DictReader(csvfile, delimiter = self.delimiter)
            for row in csv_dict:
                lst.append(row)
            return lst


    def create_csv_from_dict(self):
        pass

    def add_dict_data_to_csv(self, dct_data):
        pass

    def get_headers_from_csv(self):
        with open(self.file) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=self.delimiter)
            headers = []
            for i in csv_reader:
                headers.append(i)
                break
        print("The headers of the csv file are: ")
        for i in headers:
            print(i)
        return headers
