import os

BOT_TOKEN = os.environ.get('5766686242:AAFiIbZXaQfy76oorGpv0t7Ir_BixhtbLvM')
YANDEX_GEOCODER_API_TOKEN = os.environ.get('4a00fed2-d30c-4f32-8c1f-f3e83eb3c3e4')
OPEN_WEATHER_API_TOKEN = os.environ.get('c68f02470380fc3863df73f6553eda7b')


def check_all_tokens_set():
    """Проверка на то, что установлены все переменные глобального окружения, необходимые для работы бота"""
    return BOT_TOKEN is not None and YANDEX_GEOCODER_API_TOKEN is not None and OPEN_WEATHER_API_TOKEN is not None