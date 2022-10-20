from enum import Enum


class ApiBaseUrls(Enum):
    API_SELLER_OZON = 'https://api-seller.ozon.ru/'


class OzonApiRoutes(Enum):
    ANALYTICS = 'analytics/data'
