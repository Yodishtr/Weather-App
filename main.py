import sys
import requests
from PyQt5.QtWidgets import QApplication, QSizePolicy, QWidget, QLabel, QLineEdit, QPushButton, \
    QVBoxLayout
from PyQt5.QtCore import Qt

"""A class representing the weather app."""


class WeatherApp(QWidget):
    """Weather App class implementation"""

    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.city_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.city_input.setMinimumHeight(50)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: bold;
            }
            QLineEdit#city_input{
                font-size: 40px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 70px;
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 50px;
            }
        """)
        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        """gets weather info from API"""
        api_key = "3667533e83c428f9c7e3005caa7de24f"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_errors("Bad Request:\nPlease Check Your Input")
                case 401:
                    self.display_errors("Unauthorized:\nInvalid API Key")
                case 403:
                    self.display_errors("Forbidden:\nAccess is denied")
                case 404:
                    self.display_errors("Not Found:\nCity not found")
                case 500:
                    self.display_errors("Internal Server Error:\nPlease try again later")
                case 502:
                    self.display_errors("Bad Gateway:\nInvalid Response from the server")
                case 503:
                    self.display_errors("Service unavailable:\nServer is down")
                case 504:
                    self.display_errors("Gateway Timeout:\nNo Response From The Server")
                case _:
                    self.display_errors(f"HTTP error has occured:\n {http_error}")

        except requests.exceptions.ConnectionError:
            self.display_errors("Connection Error:\nCheck your internet connection")

        except requests.exceptions.Timeout:
            self.display_errors("Timeout Error:\nThe request timed out")

        except requests.exceptions.TooManyRedirects:
            self.display_errors("Too many redirects:\nCheck the url")

        except requests.exceptions.RequestException as req_error:
            self.display_errors(f"request error:\n{req_error}")

    def display_errors(self, message):
        """displays error message from the get_weather api calling function"""
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        """displays info received from api calling function"""
        self.temperature_label.setStyleSheet("font-size: 75px;")
        temperature_k = data['main']['temp']
        temperature_c = temperature_k - 273.15
        # temperature_f=(temperature_k*9/5)-459.67
        weather_id = data['weather'][0]['id']
        weather_description = data['weather'][0]['description']

        self.temperature_label.setText(f"{temperature_c:.1f} °C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(f"{weather_description}")

    @staticmethod
    def get_weather_emoji(weather_id):
        """Displays emoji based on current weather"""
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌧️"
        elif 500 <= weather_id <= 531:
            return "☔️"
        elif 600 <= weather_id <= 622:
            return "☃️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "🌬️"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""











if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
