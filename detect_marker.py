# import cv2
# import cv2.aruco as aruco

# # Choose the ArUco dictionary
# aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

# # Initialize the detector parameters using default values
# parameters = aruco.DetectorParameters()
# detector = aruco.ArucoDetector(aruco_dict, parameters)

# # Use 0 for webcam or provide a video file path
# # cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("http://192.168.81.124:8080/video")  # Replace with your actual IP


# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Convert frame to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Detect markers
#     corners, ids, _ = detector.detectMarkers(gray)

#     # Draw detected markers and their IDs
#     if ids is not None:
#         aruco.drawDetectedMarkers(frame, corners, ids)

#     # Display the result
#     cv2.imshow("ArUco Marker Detection", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
import cv2
import cv2.aruco as aruco

# Choose the ArUco dictionary
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

# Initialize the detector parameters using default values
parameters = aruco.DetectorParameters()
detector = aruco.ArucoDetector(aruco_dict, parameters)

# ========== SELECT ONE CAMERA SOURCE BELOW ==========

# Option 1: Default laptop webcam
# cap = cv2.VideoCapture(0)

# Option 2: IP Camera (e.g., DroidCam over WiFi)
# cap = cv2.VideoCapture("http://192.168.81.124:8080/video")  # Replace with your actual IP

# Option 3: DroidCam Wired USB connection (usually creates a virtual camera device)
cap = cv2.VideoCapture(0)  # Try 1, 2, 3... until DroidCam works via USB

# ====================================================

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect markers
    corners, ids, _ = detector.detectMarkers(gray)

    # Draw detected markers and their IDs
    if ids is not None:
        aruco.drawDetectedMarkers(frame, corners, ids)

    # Display the result
    cv2.imshow("ArUco Marker Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
