# YouTube-Videoplayer-App
YT Video Player app made with python
YouTube Video Player Application

The "YouTube Video Player Application" is a Python program that utilizes the PyQt5 library to create a simple and interactive graphical interface for playing YouTube videos. The application opens a window containing an embedded web view and a "Play Video" button. Its primary functionality is to allow users to watch YouTube videos directly within the application window and start playback from a specified time.

Key Components:

Import Statements: The program begins by importing necessary modules from the PyQt5 library. These modules include components for managing the application's GUI, interacting with web content, and handling user interactions.

Class Definition - VideoPlayerApp: The program defines a class named VideoPlayerApp, which inherits from QMainWindow. This class serves as the main application window and contains the necessary components for the GUI.

Application Window Setup: Inside the __init__ method of the VideoPlayerApp class, the application window is configured. The window's title is set to "YouTube Video Player," and its dimensions are set to 800x600 pixels.

Layout and Widgets: The program sets up the main layout of the application using a QVBoxLayout. Within this layout, two main components are added:

A QWebEngineView widget: This widget serves as an embedded web browser, allowing the application to display web content.
A QPushButton widget: This button, labeled "Play Video," is used to initiate the playback of the YouTube video.
Widget Container: The layout is added to a QWidget container, which is then set as the central widget of the main application window.

Video URL and Start Time: The program initializes two variables within the class:

self.video_url: This variable holds the URL of the YouTube video to be played. Users can replace this URL with the link to the desired video.
self.start_time: This variable represents the starting time in seconds from which the video should begin playing. By default, it is set to 30 seconds.
Video Playback Functionality: The play_video method is defined to handle the playback of the YouTube video. It constructs the full video URL by appending the start time parameter to the video URL. The QWebEngineView widget is then set to display this URL, effectively playing the video from the specified start time.

Application Execution: The program includes a block that checks whether the script is being run directly (not imported as a module). If it is the main script being executed, an instance of the VideoPlayerApp class is created, the application window is displayed, and the PyQt5 event loop is started.

Overall, this code creates a user-friendly application that combines the functionality of playing YouTube videos and the flexibility of starting the video from a specific time, all within a dedicated graphical interface.
