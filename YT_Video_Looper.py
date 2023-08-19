import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView

class VideoPlayerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YouTube Video Player")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)

        self.play_button = QPushButton("Play Video")
        self.play_button.clicked.connect(self.play_video)
        layout.addWidget(self.play_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.video_url = "https://www.youtube.com/watch?v=MwPb7g_BlXQ"  # Replace with your YouTube video URL
        self.start_time = 30  # Start time in seconds

    def play_video(self):
        full_url = f"{self.video_url}?start={self.start_time}"
        self.web_view.setUrl(QUrl(full_url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoPlayerApp()
    window.show()
    sys.exit(app.exec_())
