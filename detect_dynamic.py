import cv2
import cv2.aruco as aruco

# Load the predefined dictionary
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
parameters = aruco.DetectorParameters()
detector = aruco.ArucoDetector(aruco_dict, parameters)

# Map marker IDs to parking slot names
slot_map = {
    0: "Slot A",
    1: "Slot B",
    2: "Slot C",
    3: "Slot D",
    4: "Slot E",
    5: "Slot F"
}

# Start video capture (change to 0 for webcam or IP/video file)
cap = cv2.VideoCapture(1)  # Or replace with your phone's IP cam URL

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, _ = detector.detectMarkers(gray)

    if ids is not None:
        ids = ids.flatten()
        for i, corner in zip(ids, corners):
            corner = corner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = corner.astype(int)

            # Draw the bounding box of the marker
            cv2.polylines(frame, [corner.astype(int)], True, (0, 255, 0), 2)

            # Compute and display the center of the marker
            cX = int((topLeft[0] + bottomRight[0]) / 2.0)
            cY = int((topLeft[1] + bottomRight[1]) / 2.0)

            slot_name = slot_map.get(i, f"Unknown {i}")
            cv2.putText(frame, f"{slot_name}", (cX - 20, cY - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    else:
        cv2.putText(frame, "No markers visible (slots may be occupied)",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    cv2.imshow("Parking Slot Detection with ArUco", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# trying github