import json

from api.resource import BaseResource
from lib.enums.report import OzonAnalyticsReport
from lib.enums.urls import ApiBaseUrls, OzonApiRoutes



class OzonApiManager(BaseResource):
    def __init__(self, credentials, **kwargs):
        super().__init__()
        self._base_url = ApiBaseUrls.API_SELLER_OZON.value
        self._api_version = kwargs.get("api_version", "v1/")
        self._client_id = credentials.get("client_id")
        self._api_key = credentials.get("api_token")
        self._headers = {
            "Content-Type": "application/json",
            "Client-Id": self._client_id,
            "Api-Key": self._api_key
        }

    def get_analytics_data(self, **kwargs):
        url = f'{self._base_url}{self._api_version}{OzonApiRoutes.ANALYTICS.value}'
        date_from = kwargs.get(
            "date_from"
        )
        date_to = kwargs.get(
            "date_to"
        )
        metrics = kwargs.get("metrics", [])
        f = ()
        if len(metrics) > OzonAnalyticsReport.METRICS_COUNT_MAX_VALUE:
            f = lambda m, n=OzonAnalyticsReport.METRICS_COUNT_MAX_VALUE: [m[i:i + n] for i in range(0, len(m), n)]
        needed_metrics = f(metrics)
        dimension = kwargs.get("dimension", [])
        filters = kwargs.get("filters", [])
        sort = kwargs.get("sort", [])
        limit = kwargs.get("limit")
        offset = kwargs.get("offset", 0)
        result = list()
        for m in needed_metrics:
            payload = {
                "date_from": date_from,
                "date_to": date_to,
                "metrics": m,
                "dimension": dimension,
                "filters": filters,
                "sort": sort,
                "limit": limit,
                "offset": offset
            }
            result.append(
                self.request(
                    "POST",
                    url,
                    headers=self._headers,
                    json=payload,
                )
            )

        return result

    def get_common_analytics_data(self, **kwargs):
        metrics = [m for m in list(OzonAnalyticsReport.FIELDS.keys())]
        content = self.get_analytics_data(
            metrics=metrics,
            dimension=["sku"],
            **kwargs
        )
        data = [json.loads(c)['result']['data'] for c in content]
        return data
