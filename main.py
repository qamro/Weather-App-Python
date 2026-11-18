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
        
        layout = QVBoxLayout()
        layout.addWidget(self.city_label)
        layout.addWidget(self.city_input)
        layout.addWidget(self.get_weather_button)
        layout.addWidget(self.temperature_label)
        layout.addWidget(self.emoji_label)
        layout.addWidget(self.description_label)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv) # this is for initializing the Qt application
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_()) # this is for exiting the application when the window is closed