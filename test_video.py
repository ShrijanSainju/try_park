# # import cv2

# # # Load the video file
# # cap = cv2.VideoCapture('parking_lot.mp4')

# # while True:
# #     ret, frame = cap.read()
# #     if not ret:
# #         break

# #     # Display the video frame
# #     cv2.imshow('Parking Lot Video', frame)

# #     # Press 'q' to exit the video display
# #     if cv2.waitKey(25) & 0xFF == ord('q'):
# #         break

# # # Release the video capture object and close display window
# # cap.release()
# # cv2.destroyAllWindows()



# import cv2

# # Load the video file
# cap = cv2.VideoCapture('parking_lot.mp4')

# # Define parking slot coordinates
# parking_slots = [
#     (60, 0, 150, 60-4),
#     (60, 60-4, 150, 120-4),
#     (60, 120-4, 150, 180-4),
#     (60, 180-4, 150, 240-4),
#     (60, 240-4, 150, 300-4),
#     (60, 300-4, 150, 360-4),
#     (60, 360-4, 150, 420-4),
#     # Add more slots as needed
# ]

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     for idx, (x, y, w, h) in enumerate(parking_slots):
#         # Extract the parking slot region
#         slot = frame[y:y+h, x:x+w]

#         # Convert to grayscale
#         gray = cv2.cvtColor(slot, cv2.COLOR_BGR2GRAY)

#         # Apply thresholding
#         _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

#         # Count non-zero pixels
#         non_zero = cv2.countNonZero(thresh)

#         # Determine occupancy based on pixel count
#         status = 'Occupied' if non_zero < (w * h * 0.5) else 'Vacant'

#         # Draw rectangle and status text
#         color = (0, 0, 255) if status == 'Occupied' else (0, 255, 0)
#         cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
#         cv2.putText(frame, status, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

#     # Display the video frame with annotations
#     cv2.imshow('Parking Lot Occupancy', frame)

#     # Press 'q' to exit the video display
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         break

# # Release the video capture object and close display window
# cap.release()
# cv2.destroyAllWindows()


import cv2

# Load the video
cap = cv2.VideoCapture('parking_lot.mp4')

# Define parking slot coordinates (x, y, w, h)
parking_slots = [
    # x, y, w, h
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
occupancy_threshold = 0.35 # Lower = more sensitive to cars

while True:
    ret, frame = cap.read()
    if not ret:
        break

    for idx, (x, y, w, h) in enumerate(parking_slots):
        # Crop parking slot
        slot = frame[y:y+h, x:x+w]

        # Convert to grayscale
        gray = cv2.cvtColor(slot, cv2.COLOR_BGR2GRAY)

        # Adaptive Thresholding (handles uneven lighting)
        adaptive_thresh = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY_INV, 11, 2
        )

        # Canny Edge Detection (detects car edges)
        edges = cv2.Canny(gray, 50, 150)

        # Combine both methods
        combined = cv2.bitwise_or(adaptive_thresh, edges)

        # Count non-zero (white) pixels
        non_zero = cv2.countNonZero(combined)

        # Decide occupied or vacant
        total_pixels = w * h
        status = 'Occupied' if non_zero > total_pixels * occupancy_threshold else 'Vacant'

        # Draw result on original frame
        color = (0, 0, 255) if status == 'Occupied' else (0, 255, 0)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(frame, status, (x, y - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

    # Show the processed frame
    cv2.imshow('Improved Parking Detection', frame)

    # Press 'q' to quit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
