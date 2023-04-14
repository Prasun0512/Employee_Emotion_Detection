
# Employee Emotion Detection using DeepFace

This project uses the DeepFace library to detect the emotion of an employee in real-time, based on their facial expressions. The system captures images of employees at specific times and sends them to a server for analysis. The server then processes the images and determines the employee's current emotional state, and sends an email to the manager with the employee's mood.

## Requirements

To run this project, you need to have the following software installed:

-   Python 3.x
-   DeepFace library
-   OpenCV library
-   Flask library

## Installation

To install the required libraries, you can run the following command:

Copy code

`pip install deepface opencv-python flask` 

## Usage

To use this project, you need to run two main files:

-   `capture.py`: This file captures images of the employees and sends them to the server.
-   `server.py`: This file receives the images from the `capture.py` script, processes them using the DeepFace library, and sends an email to the manager with the employee's mood.

You can run the `capture.py` script on a schedule using a tool like cron, or you can run it manually whenever you want to capture an image of the employees.

To run the server, simply run the `server.py` script using the following command:

Copy code

`python server.py` 

## Configuration

To configure the project, you can modify the following parameters:

-   `capture_time`: The time interval between capturing the employee images.
-   `email_sender`: The email address from which the email will be sent.
-   `email_password`: The password for the email account.
-   `email_recipient`: The email address to which the email will be sent.

You can modify these parameters in the `config.py` file.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments

This project was inspired by the DeepFace library and the emotion detection technology it provides. Special thanks to the developers of the DeepFace library and the open-source community for making this project possible.

