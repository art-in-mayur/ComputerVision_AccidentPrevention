# Accident Prevention using Computer Vision

Accident Prevention using Computer Vision is a project that aims to enhance road safety by detecting driver drowsiness or inattention through the use of computer vision techniques. The project focuses on detecting closed eyes for an extended period, which could indicate that the driver is not paying attention to the road. Upon detection, the system can trigger various safety measures such as applying breaks, alerting the driver, or stopping the vehicle.

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
  
## Description

This project utilizes computer vision libraries, particularly OpenCV, to process the video feed from a camera placed inside the vehicle. It detects both faces and eyes in real-time using pre-trained Haar cascades. If the system detects that the driver's eyes are closed for an extended duration, it triggers an alert to prevent potential accidents caused by driver drowsiness.

## Requirements

To run this project, you will need the following:

- Python (version 3.6 or higher)
- OpenCV library (cv2)
- Haar Cascade XML files for face and eye detection (provided in the repository)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/art-in-mayur/ComputerVision_AccidentPrevention
   cd ComputerVision_AccidentPrevention
   ```

2. Install the required libraries using pip:

   ```bash
   pip install opencv-python
   ```

3. Download the Haar Cascade XML files for face and eye detection and place them in the project directory.

## Usage

1. Connect a camera (webcam) to your computer.
2. Run the project by executing the Python script:

   ```bash
   python accident_prevention_cv.py
   ```

3. The script will open a video stream showing the camera feed.
4. The system will detect faces and eyes in the video feed and mark them with rectangles and circles respectively.
5. If the system detects closed eyes for more than 3 seconds, it will print a warning message, indicating that the driver's eyes are closed, and trigger appropriate actions such as displaying an alert, applying brakes, or stopping the vehicle (simulation).

**Note:** This project is a demonstration and should not be used as a fully functional safety system without proper testing and validation.

## Contributing

Contributions to this project are welcome! If you have any ideas for improvement or bug fixes, feel free to fork the repository and submit a pull request.


---

*Disclaimer: This project is developed for educational and demonstrative purposes only. It is not intended to replace or replicate actual safety systems used in vehicles. Always prioritize safe driving practices and adhere to road safety regulations.*
