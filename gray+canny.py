import cv2

# Load the video
cap = cv2.VideoCapture('parking_lot.mp4')

# Define parking slot coordinates (x, y, w, h)
parking_slots = [
   (60, 0, 150, 57),
    (60, 56, 150, 57),
    (60, 115, 150, 59),
    (60, 175, 150, 59),
    (60, 235, 150, 59),
    (60, 295, 150, 59),
    (60, 355, 150, 59),
    (212, 0, 150, 57),
    (212, 56, 150, 57),
    (212, 115, 150, 59),
    (212, 175, 150, 59),
    (212, 235, 150, 59),
    (212, 295, 150, 59),
    (212, 355, 150, 59),
]

# Threshold ratio to decide occupancy based on pixel count (can tune)
occupancy_threshold = 0.1  # Lower = more sensitive to cars

while True:
    ret, frame = cap.read()
    if not ret:
        break

    for idx, (x, y, w, h) in enumerate(parking_slots):
        # Crop parking slot
        slot = frame[y:y+h, x:x+w]

        # Convert to grayscale
        gray = cv2.cvtColor(slot, cv2.COLOR_BGR2GRAY)

        # Canny Edge Detection (detects car edges)
        edges = cv2.Canny(gray, 50, 150)

        # Use only Canny output
        non_zero = cv2.countNonZero(edges)

        # Decide occupied or vacant
        total_pixels = w * h
        status = 'Occupied' if non_zero > total_pixels * occupancy_threshold else 'Vacant'

        # Draw result on original frame
        color = (0, 0, 255) if status == 'Occupied' else (0, 255, 0)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(frame, status, (x, y - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

    # Show the processed frame
    cv2.imshow('Parking Detection - Canny Only', frame)

    # Press 'q' to quit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
