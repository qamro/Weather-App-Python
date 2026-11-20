import os
import sys
from dotenv import load_dotenv
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout 
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QIcon

load_dotenv()  # reads .env and loads its variables into the environment
class WeatherApp (QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Qamro Weather App") # set a title to the app's window
        self.setGeometry(700, 300, 300, 350) # set the window geometry
        self.setWindowIcon(QIcon("qamro_weather_icon.svg"))  # set the window icon
        
        # Create a vertical layout to organize the widgets
        virtual_box = QVBoxLayout()
        virtual_box.addWidget(self.city_label)
        virtual_box.addWidget(self.city_input)
        virtual_box.addWidget(self.get_weather_button)
        virtual_box.addWidget(self.temperature_label)
        virtual_box.addWidget(self.emoji_label)
        virtual_box.addWidget(self.description_label)
        self.setLayout(virtual_box)

        # centralize (align) the different widgets
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        
        # set object names for styling
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        
        # set the stylesheet for the widgets
        self.setStyleSheet("""
            #city_label {
                font-size: 18px;
                font-weight: bold;
            }
            #city_input {
                font-size: 16px;
                padding: 5px;
            }
            #get_weather_button {
                font-size: 16px;
                padding: 5px;
                background-color: #0EA5E9;
                color: white;
            }
            #temperature_label {
                font-size: 16px;
                font-weight: bold;
            }
            #emoji_label {
                font-size: 48px;
            }
            #description_label {
                font-size: 16px;
            }
        """)
        
        # connect the button click event to the get_weather method
        self.get_weather_button.clicked.connect(self.get_weather)
        
    def get_weather(self):
        
        api_key = os.getenv("OPENWEATHER_API_KEY")
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        
        # get our data and handle all the exceptions(http responses)
        try:
            response = requests.get(url)
            response.raise_for_status() # raise the HTTPexceptions cuz normally try alone cant do that
            data = response.json()
        
            if data["cod"] == 200:
                self.display_weather(data)
        
        except requests.exceptions.HTTPError: # to handle all the http errors
            match response.status_code:
                case 400:
                    self.display_error("Bad request\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized \n Invalid API Key")
                case 402:
                    self.display_error("Payment required \n Payment Required")
                case 403:
                    self.display_error("Forbidden \n Access is denied")
                case 404:
                    self.display_error("Not Found \n City not found")
                case 500:
                    self.display_error("Internal server error \n Please try again later")
                case 502:
                    self.display_error("Bad Gateway \n Invalid response from the server")
                case 503:
                    self.display_error("Service Unavailable \n Server is down")
                case 504:
                    self.display_error("Gateway Timeout \n No response from the server")
                case _:
                    self.display_error("HTTP error occurred!!")
        except requests.exceptions.ConnectionError:
            self.display_error("Connection error: \n Check your internet connection")
        except requests.exceptions.Timeout: 
            self.display_error("Timeout error: \n The request timed out")
        except requests.exceptions.TooManyRedirects: 
            self.display_error("Too many redirects: \n Check the URL")
        except requests.exceptions.RequestException: # to handle network errors, invalid url... these kinda exceptions
            self.display_error("Request error: \n An error occurred while making the request")


    def display_error(self, message):
        self.temperature_label.setStyleSheet("color: red;"
                                            "font-size: 30px;")
        self.temperature_label.setText(message)
        self.description_label.clear()
        self.emoji_label.clear()
        
        
    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 75px;")
        temperature_kelven = data["main"]["temp"]
        temperature_celsius = temperature_kelven - 273.15
        weather_description = data["weather"][0]["description"]
        weather_id = data["weather"][0]["id"]
        
        self.temperature_label.setText(f"{temperature_celsius:.0f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)
    
    
    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 700 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return "❓"

if __name__ == "__main__":
    app = QApplication(sys.argv) # this is for initializing the Qt application
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_()) # this is for exiting the application when the window is closed