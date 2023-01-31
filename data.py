import requests
baseURL = "http://127.0.0.1:8010/api/v1/customerdata/"
raw = {
    "data": {
        "count": 5,
        "next": None,
        "previous": None,
        "results": [
            {
                "id": "1b2f7b83-7b4d-441d-a210-afaa970e5b76",
                "data": {
                    "banner_message": "<p><span>Welcome</span> to Mr X's website</p>",
                    "LAST_PAYMENT_DATE": "2020-01-10T09:25:00Z",
                    "theme_name": "Tropical Island",
                    "user_profile_image": "https://i.imgur.com/LMhM8nn.jpg",
                    "ENABLED_FEATURES": {
                        "CERTIFICATES_INSTRUCTOR_GENERATION": True,
                        "ENABLE_COURSEWARE_SEARCH": True,
                        "ENABLE_EDXNOTES": True,
                        "ENABLE_DASHBOARD_SEARCH": True,
                        "INSTRUCTOR_BACKGROUND_TASKS": True,
                        "ENABLE_COURSE_DISCOVERY": True
                    },
                    "displayed_timezone": "America/Bogota",
                    "language_code": "en",
                    "CREATION_DATE": "2013-03-10T02:00:00Z",
                    "user_email": "barack@aol.com",
                    "SUBSCRIPTION": "basic"
                }
            },
            {
                "id": "49a6307e-c261-414d-86f5-c6004bcec8ab",
                "data": {
                    "banner_message": "<h1>Chilling in the snow</h1>",
                    "LAST_PAYMENT_DATE": None,
                    "theme_name": "Candy Crush",
                    "user_profile_image": "https://i.imgur.com/YXOQCIp.png",
                    "ENABLED_FEATURES": {
                        "CERTIFICATES_INSTRUCTOR_GENERATION": False,
                        "ENABLE_COURSEWARE_SEARCH": False,
                        "ENABLE_EDXNOTES": True,
                        "ENABLE_DASHBOARD_SEARCH": False,
                        "INSTRUCTOR_BACKGROUND_TASKS": False,
                        "ENABLE_COURSE_DISCOVERY": False
                    },
                    "displayed_timezone": "Europe/Zurich",
                    "language_code": "de",
                    "CREATION_DATE": "2020-06-19T02:18:00Z",
                    "user_email": "lisaschneider@gmail.com",
                    "SUBSCRIPTION": "free"
                }
            },
            {
                "id": "a237ed14-88fb-45f3-b9b1-471877dbdc60",
                "data": {
                    "banner_message": "<p>Everything is awesome</p>",
                    "LAST_PAYMENT_DATE": "2020-08-10T19:25:00Z",
                    "theme_name": "Mustache Bash",
                    "user_profile_image": "https://i.imgur.com/5ATSCxo.jpg",
                    "ENABLED_FEATURES": {
                        "CERTIFICATES_INSTRUCTOR_GENERATION": True,
                        "ENABLE_COURSEWARE_SEARCH": True,
                        "ENABLE_EDXNOTES": True,
                        "ENABLE_DASHBOARD_SEARCH": True,
                        "INSTRUCTOR_BACKGROUND_TASKS": False,
                        "ENABLE_COURSE_DISCOVERY": False
                    },
                    "displayed_timezone": "America/NewYork",
                    "language_code": "en",
                    "CREATION_DATE": "2016-06-10T02:18:00Z",
                    "user_email": "thegood@gmail.com",
                    "SUBSCRIPTION": "premium"
                }
            },
            {
                "id": "013aa803-9782-49d0-95c7-df86d31e6843",
                "data": [
                    {
                        "test": "testValue"
                    }
                ]
            },
            {
                "id": "d2d5e083-efe4-4790-b2b1-6c49bac8010e",
                "data": "1b2f7b83-7b4d-441d-a210-afaa970e5b76"
            }
        ]
    }
}


def create_data():
    try:
        data = requests.get(baseURL)
        return data.json()
    except Exception as err:
        return raw
