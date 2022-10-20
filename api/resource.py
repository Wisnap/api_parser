import requests

class BaseResource:

    def __init__(self):
        self._request = requests

    def get(self, path, headers=None, params=None, **kwargs):
        headers = headers or {}
        params = params or {}
        return self._request.get(path, headers=headers, params=params, **kwargs)

    def post(self, path, headers=None, json=None, **kwargs):
        headers = headers or {}
        json = json or {}
        return self._request.post(path, headers=headers, json=json, **kwargs)

    def put(self, path, headers=None, json=None, **kwargs):
        headers = headers or {}
        json = json or {}
        return self._request.put(path, headers=headers, json=json, **kwargs)

    def delete(self, path, headers=None, json=None, **kwargs):
        headers = headers or {}
        json = json or {}
        return self._request.delete(path, headers=headers, json=json, **kwargs)

    def request(
            self,
            method,
            resource_path,
            headers=None,
            params=None,
            json=None,
            **kwargs,
    ):
        request_method = getattr(self._request, method.lower())
        if not request_method:
            raise Exception(f"Вызван неподдерживаемый метод {method}")

        response = request_method(
            resource_path,
            params={k: v for k, v in params.items() if v is not None}
            if params
            else None,
            headers=headers,
            json=json or None,
            **kwargs,
        )

        if not response:
            raise Exception(
                f"Не удалось выполнить запрос: "
                f"\n status: {response.status_code} "
                f"\n content: {response.content}"
            )

        return response.content
