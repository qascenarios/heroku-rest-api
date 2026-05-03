import pprint

import requests

from Request2.POST2_Request import booking_ids

base_url = "https://restful-booker.herokuapp.com"


def get_request(booking_ids):
    for booking_id in booking_ids:
        url = base_url + f"/booking/{booking_id}"
        print("GET url:" + url)
        resp = requests.get(url)
        assert resp.status_code == 200
        json_data = resp.json()
        pprint.pprint(json_data)


get_request(booking_ids)
