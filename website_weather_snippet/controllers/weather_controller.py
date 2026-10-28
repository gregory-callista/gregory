from odoo import http


class CustomWebsiteBlockDemo(http.Controller):
    @http.route("/weather_api/get_weather", auth="public", type="jsonrpc")
    def get_weather(self, location=""):
        weather_data = {}
        location = location.lower()

        if location == "brussels":
            weather_data = {
                "daily": {
                    "time": [
                        "2025-09-18",
                        "2025-09-19",
                        "2025-09-20",
                        "2025-09-21",
                        "2025-09-22",
                        "2025-09-23",
                        "2025-09-24",
                    ],
                    "temperature_2m_max": [11.2, 11.3, 11.6, 11.9, 10.0, 11.0, 9.6],
                    "weathercode": [0, 80, 18, 3, 61, 3, 61],
                }
            }
        elif location == "amsterdam":
            weather_data = {
                "daily": {
                    "time": [
                        "2025-09-18",
                        "2025-09-19",
                        "2025-09-20",
                        "2025-09-21",
                        "2025-09-22",
                        "2025-09-23",
                        "2025-09-24",
                    ],
                    "temperature_2m_max": [10.5, 9.6, 15.6, 8.5, 6.0, 10.0, 9.6],
                    "weathercode": [15, 80, 0, 80, 61, 15, 61],
                }
            }

        return weather_data
