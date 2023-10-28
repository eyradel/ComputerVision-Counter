# ComputerVision-Counter

# People Counter with ROI, Contour Mapping, and Heat Mapping

This is a computer vision-based people counter application that utilizes Region of Interest (ROI), contour mapping, and heat mapping to count individuals entering and exiting a location. The system also provides the functionality to save recordings frame by frame with a timestamp, date, and unique ID.

## Features:
1. **Region of Interest (ROI)**: Allows users to define specific areas of the video frame to focus the analysis on.
2. **Contour Mapping**: Detects and maps the outline of people within the ROI.
3. **Heat Mapping**: Provides a visual representation of the traffic flow over time, indicating the most traversed areas.
4. **Recording Output**: Saves video and picture outputs frame by frame.
5. **Timestamp and ID**: Each frame is labeled with its capture date, time, and a unique ID.

## Prerequisites:
- Python 3.x
- OpenCV (cv2)
- Numpy



## Outputs:
- **Video Output**: A video recording with the ROI, contour mapping, and heat map overlay.
- **Heat Map**: A heat map indicating the areas with the most traffic.
- **Picture Outputs**: Individual frames saved with a timestamp, date, and unique ID.

## Considerations:
- For optimal performance, ensure good lighting conditions in the video.
- Avoid obstructions in the ROI.
- The system might have variations in accuracy based on the camera angle, distance, and resolution.


This README provides a basic outline for the described project. To fully flesh out this project, more specific details related to the actual implementation, any datasets used, post-processing steps, etc., would be needed.
