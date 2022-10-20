class OzonAnalyticsReport(object):
    FIELDS = {
        "hits_view_pdp": "показы на карточке товара",
        "hits_view": "всего показов",
        "hits_tocart_search": "в корзину из поиска или категории",
        "hits_tocart_pdp": "в корзину из карточки товара",
        "hits_tocart": "всего добавлено в корзину",
        "session_view_search": "сессии с показом в поиске или в категории",
        "session_view_pdp": "сессии с показом на карточке товара",
        "session_view": "всего сессий",
        "conv_tocart_search": "конверсия в корзину из поиска или категории",
        "conv_tocart_pdp": "общая конверсия в корзину",
        "revenue": "заказано на сумму",
        "returns": "возвращено товаров",
        "cancellations": "отменено товаров",
        "ordered_units": "заказано товаров",
        "adv_view_pdp": "показы на карточке товара, спонсорские товары",
        "adv_view_search_category": "показы в поиске и в категории, спонсорские товары",
        "adv_view_all": "показы всего, спонсорские товары",
        "adv_sum_all": "всего расходов на рекламу",
        "position_category": "позиция в поиске и категории",
        "postings": "отправления",
        "postings_premium": "отправления с подпиской Premium"
    }
    METRICS_COUNT_MAX_VALUE = 14
