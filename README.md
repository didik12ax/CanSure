# CanSure
AI-based prototype for detecting lung abnormalities using YOLOv8. Built with Flask, Docker, and deployed on Google Cloud's Vertex AI.

# Lung Detection Prototype

This repository contains a machine learning-based prototype for detecting lung abnormalities using YOLOv8. The system is built using Flask and Docker and deployed on Google Cloud's Vertex AI for scalability and real-time inference.

---

## Features
- **Lung Abnormality Detection**: Detect and localize potential lung abnormalities.
- **Scalable Deployment**: Hosted on Google Cloud Vertex AI for real-time predictions.

## File Structure
lungdetection/
├── Dockerfile          
├── app.py               
├── requirements.txt     
├── modelbest.pt         
├── README.md 

## Model Information
Model: YOLOv8 (modified for lung abnormality detection)
Trained On: A dataset of labeled chest X-ray images.
Output: Bounding boxes, labels, and confidence scores.
File: modelbest.pt (stored locally or in cloud storage).

## Requirements
To run this project, you need the following:
1. Python 3.9+
2. Docker (for containerized deployment)
3. Python libraries:
4. Flask
5. Flask-Cors
6. YOLOv8 (via ultralytics library)
7. OpenCV
8. Pillow

## Credits
This project was created as part of the Google Cloud Hackathon. We used the credits and infrastructure provided by Google Cloud to train, deploy, and demonstrate this prototype.



