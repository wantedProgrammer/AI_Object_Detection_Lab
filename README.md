<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors](https://img.shields.io/github/contributors/wantedProgrammer/AI_Object_Detection_Lab.svg?style=for-the-badge)](https://github.com/wantedProgrammer/AI_Object_Detection_Lab/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/wantedProgrammer/AI_Object_Detection_Lab.svg?style=for-the-badge)](https://github.com/wantedProgrammer/AI_Object_Detection_Lab/network/members)
[![Stargazers](https://img.shields.io/github/stars/wantedProgrammer/AI_Object_Detection_Lab.svg?style=for-the-badge)](https://github.com/wantedProgrammer/AI_Object_Detection_Lab/stargazers)
[![Issues](https://img.shields.io/github/issues/wantedProgrammer/AI_Object_Detection_Lab.svg?style=for-the-badge)](https://github.com/wantedProgrammer/AI_Object_Detection_Lab/issues)



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/wantedProgrammer/AI_Object_Detection_Lab">
    <h1>🎯</h1>
  </a>

  <h3 align="center">YOLOv8 Object Detection and Tracking Lab</h3>

  <p align="center">
    Object detection and tracking across images, video, and a live webcam feed with YOLOv8.
    <br />
    <a href="#getting-started"><strong>Get started »</strong></a>
    <br />
    <br />
    <a href="#results">View Results</a>
    ·
    <a href="https://github.com/wantedProgrammer/AI_Object_Detection_Lab/issues">Report Bug</a>
    ·
    <a href="https://github.com/wantedProgrammer/AI_Object_Detection_Lab/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#features">Features</a></li>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#project-structure">Project Structure</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#results">Results</a>
      <ul>
        <li><a href="#image-detection">Image Detection</a></li>
        <li><a href="#video-tracking">Video Tracking</a></li>
        <li><a href="#command-line-runs">Command Line Runs</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Object detection on an Asian market scene](runs/detect/predict2/Asian%20market.jpg)

A practical computer vision project that uses the pretrained YOLOv8 nano model (`yolov8n.pt`) to detect and track objects in images, video files, and a live webcam feed. It was developed as part of the CMPG 313 Artificial Intelligence module.

### Features

* 🖼️ **Image detection:** detects and labels objects in static images with confidence scores
* 🚗 **Video tracking:** tracks objects across video frames with persistent IDs
* 📷 **Live webcam detection:** real-time object detection from a webcam feed
* 🏷️ **Automated annotation:** saves output files with bounding boxes and class labels to `runs/detect`
* 🔀 **Multiple input sources:** supports images, video files, and live camera streams
* ✅ **Setup check:** a script that confirms the environment is ready before running

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
* [![Ultralytics YOLOv8](https://img.shields.io/badge/Ultralytics_YOLOv8-111F68?style=for-the-badge)](https://docs.ultralytics.com/)
* [![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
* [![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Project Structure

```
├── CMD Screenshots/                   # Terminal output from each run
├── runs/detect/
│   ├── predict2/                      # Detection result on the market image
│   ├── track2/                        # Tracking result on the road footage
│   └── track5/                        # Tracking result from the webcam
├── Asian market.jpg                   # Input image
├── Cars Moving On Road Footage.mp4    # Input video
├── check_setup.py                     # Checks the environment is ready
├── lab_1.py                           # Runs detection and tracking
└── yolov8n.pt                         # Pretrained YOLOv8 nano weights
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

* Python 3.8 or later
* pip package manager
* A webcam (only for live detection)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/wantedProgrammer/AI_Object_Detection_Lab.git
   cd AI_Object_Detection_Lab
   ```
2. Install Ultralytics (this also installs PyTorch and OpenCV)
   ```sh
   pip install ultralytics
   ```
3. Check that everything is set up
   ```sh
   python check_setup.py
   ```
4. Run detection and tracking
   ```sh
   python lab_1.py
   ```
5. Find the annotated results in `runs/detect`

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- RESULTS -->
## Results

### Image Detection

![Detection result on the market image](runs/detect/predict2/Asian%20market.jpg)

### Video Tracking

GitHub can't play videos inside a README, so open the folders to download the tracked videos:

* 🚗 [Road footage tracking](runs/detect/track2)
* 📷 [Webcam tracking](runs/detect/track5)

### Command Line Runs

| Run 1 | Run 2 | Run 3 |
|---|---|---|
| ![CMD run 1](CMD%20Screenshots/Screenshot%202026-03-09%20210633.png) | ![CMD run 2](CMD%20Screenshots/Screenshot%202026-03-09%20212009.png) | ![CMD run 3](CMD%20Screenshots/Screenshot%202026-03-09%20213444.png) |

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Object detection on an image
- [x] Object tracking on a video
- [x] Live webcam detection
- [ ] Try larger models (YOLOv8s, YOLOv8m) and compare accuracy
- [ ] Train on a custom dataset
- [ ] Count objects crossing a line in the road footage

See the [open issues](https://github.com/wantedProgrammer/AI_Object_Detection_Lab/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

GitHub: [@wantedProgrammer](https://github.com/wantedProgrammer)

Project Link: [https://github.com/wantedProgrammer/AI_Object_Detection_Lab](https://github.com/wantedProgrammer/AI_Object_Detection_Lab)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* CMPG 313 Artificial Intelligence module
* [Ultralytics YOLOv8](https://docs.ultralytics.com/)
* [OpenCV](https://opencv.org/)
* [PyTorch](https://pytorch.org/)
* [Img Shields](https://shields.io)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
