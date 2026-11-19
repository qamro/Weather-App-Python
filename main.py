import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout 
from PyQt5.QtCore import Qt 


class WeatherApp (QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel("Weather will be displayed here.", self)
        self.emoji_label = QLabel("☀️", self)
        self.description_label = QLabel("Sunny", self)

    
    def initUI(self):
        self.setWindowTitle("Qamro Weather App") # set a title to the app's window
        
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
        
        
    def Get_Weather(self):
        pass
    
    def display_error(self, message):
        pass
    
    def display_weather(self, data):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv) # this is for initializing the Qt application
    weather_app = WeatherApp()
    weather_app.initUI()
    weather_app.show()
    sys.exit(app.exec_()) # this is for exiting the application when the window is closed