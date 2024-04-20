import data
import configuration
import requests


def post_new_order(create_new_order: dict):
    response = requests.post(configuration.URL + configuration.POST_NEW_ORDER,
                             json=create_new_order, headers=data.headers)
    return response


def get_order_with_track(track_id: str):
    response = requests.get(configuration.URL + configuration.GET_ORDERS_WITH_TRACK + track_id,
                            headers=data.headers)
    return response


def test_get_order_with_track():
    track = post_new_order(data.create_new_order)
    track_id = track.json()
    response = get_order_with_track(str(track_id.get("track")))
    assert response.status_code == 200
    print(f"status code={response.status_code}")

# Новиков Сергей, 15-я когорта — Финальный проект. Инженер по тестированию плюс