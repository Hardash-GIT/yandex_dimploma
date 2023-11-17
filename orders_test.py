import sender_stand_request
import data

# Евгений Бондарь, 10-я когорта — Финальный проект. Инженер по тестированию плюс
def test_create_order_positive():
    response = sender_stand_request.post_new_order(data.order_body)
    assert response.status_code == 201
    
    track = response.json()['track']
    order_response = sender_stand_request.get_order_by_track(track)
    assert order_response.status_code == 200