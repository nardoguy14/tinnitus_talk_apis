import requests
import moment

WHOSOFF_HOST = 'https://wr1.whosoff.com'
AUTH_KEY = 'dd43cfcb982d'


def get_days_off(start_date: str, end_date: str):
    start_str = moment.date(start_date).format("DD-MMM-YYYY")
    end_date = moment.date(end_date).format("DD-MMM-YYYY")
    url = f"{WHOSOFF_HOST}/api/V2/whosoff"
    params = {
        'start_date': start_str,
        'end_date': end_date
    }
    headers = {
        'AUTH-KEY': AUTH_KEY
    }
    response = requests.get(url, params=params, headers=headers)

    print(response.text)

    return response.json()


def get_staff():
    url = f"{WHOSOFF_HOST}/api/v3/staff/"
    headers = {
        'AUTH-KEY': AUTH_KEY
    }
    response = requests.get(url, params={}, headers=headers)
    print(response.text)

    return response.json()
