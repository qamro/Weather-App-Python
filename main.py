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
        self.setWindowTitle("Qamro Weather App")
        
        virtual_box = QVBoxLayout()
        virtual_box.addWidget(self.city_label)
        virtual_box.addWidget(self.city_input)
        virtual_box.addWidget(self.get_weather_button)
        virtual_box.addWidget(self.temperature_label)
        virtual_box.addWidget(self.emoji_label)
        virtual_box.addWidget(self.description_label)
        self.setLayout(virtual_box)

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

if __name__ == "__main__":
    app = QApplication(sys.argv) # this is for initializing the Qt application
    weather_app = WeatherApp()
    weather_app.initUI()
    weather_app.show()
    sys.exit(app.exec_()) # this is for exiting the application when the window is closed