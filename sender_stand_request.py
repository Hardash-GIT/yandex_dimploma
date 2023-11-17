import configuration
import requests
import data

# ---------------------- МЕТОДЫ ----------------------
def post_new_order(body): # создание нового заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, 
                         json=body,
                         headers=data.headers)


def get_order_by_track(track): # получение заказа по трек номеру
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                         params={'t': track},
                         headers=data.headers)


# ----------------- ПРОВЕРКА ФУНКЦИЙ -----------------
response = post_new_order(data.order_body)
print(response.status_code)
print(response.json())
track = response.json()["track"]
print(track)
response = get_order_by_track("track")
print(response)

