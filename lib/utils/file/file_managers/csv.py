import csv
from datetime import datetime

from lib.enums.report import OzonAnalyticsReport
from lib.utils.date import stringify_datetime


class CSVFileManager:

    def __init__(self, filename=None):
        super().__init__()
        self._format = "csv"
        self._filename = filename if filename else f'Report {stringify_datetime(datetime.today())}'

    def generate_csv_ozon_analytics_data_report(self, data):
        parsed_data = self._generate_data_for_csv_analytics_report(data)
        if len(parsed_data) < 1:
            print('Отчет не был сгенерирован, ввиду отсутствия информации от Озона')
            return None
        filename = f'reports/{self._filename}.{self._format}'
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = parsed_data["headers"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()
            for value in parsed_data["values"]:
                obj_data = {}
                for i in range(len(value)):
                    obj_data[parsed_data["headers"][i]] = value[i]
                writer.writerow(obj_data)
        print(f'Отчет успешно загружен в файл {filename}')

    @staticmethod
    def _generate_data_for_csv_analytics_report(responses):
        result = {
            "headers": ["id"],
            "values": list()
        }
        [result["headers"].append(m) for m in list(OzonAnalyticsReport.FIELDS.values())]
        for items in responses:
            for i, data in enumerate(items):
                try:
                    [result["values"][i].append(m) for m in data["metrics"]]
                except IndexError:
                    result["values"].append([m for m in data["metrics"]])
                    result["values"][i].insert(0, int(data["dimensions"][0]["id"]))
        return result
