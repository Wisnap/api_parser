from api.marketplace.ozon import OzonApiManager
from lib.utils.date import OzonDateParser, is_date_valid
from lib.utils.file.file_managers.csv import CSVFileManager

from dynaconf import Dynaconf
from datetime import date, timedelta

settings = Dynaconf(envvar_prefix=False, load_dotenv=True)


def main():
    date_from = str(input('Введите дату начала в формате Год-Месяц-День, например: 2022-09-19 \n'
                          'Если дата не введена введется дата по умолчанию (1 месяц назад) \n') or
                    OzonDateParser(date.today() - timedelta(days=30)).stringify_date_for_analytics())
    if not is_date_valid(date_from):
        raise Exception(f'Дата начала {date_from} не валидна или не соответствует формату YYYY-MM-DD')
    date_to = str(input('Введите дату окончания в формате Год-Месяц-День, например: 2022-09-19 \n'
                        'Если дата не введена введется дата по умолчанию (сегодняшний день) \n') or
                  OzonDateParser(date.today()).stringify_date_for_analytics())
    if not is_date_valid(date_to):
        raise Exception(f'Дата окончания {date_to} не валидна или не соответствует формату YYYY-MM-DD')
    limit = int(input('Введите кол-во записей (MAX=1000) \n'
                      'Если значение не введено то по умолчанию выведется 1000 записей\n') or 1000)
    if limit == 0 or limit > 1000:
        raise Exception('Количество записей некорректное')
    ozon_client = OzonApiManager(
        credentials={
            "client_id": str(settings.OZON_CLIENT_ID),
            "api_token": settings.OZON_API_KEY
        },
    )
    responses = ozon_client.get_common_analytics_data(
        date_from=date_from,
        date_to=date_to,
        limit=limit
    )
    CSVFileManager().generate_csv_ozon_analytics_data_report(
        responses
    )


if __name__ == '__main__':
    main()
