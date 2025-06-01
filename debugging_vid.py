# # import cv2

# # cap = cv2.VideoCapture('parking_lot.mp4')

# # parking_slots = [
# #     (60, 0, 150, 56),
# #     (60, 56, 150, 56),
# #     # (60, 112, 150, 56),
# #     # (60, 168, 150, 56),
# #     # (60, 224, 150, 56),
# #     # (60, 280, 150, 56),
# #     # (60, 336, 150, 56),
# # ]

# # occupancy_threshold = 0.4

# # while True:
# #     ret, frame = cap.read()
# #     if not ret:
# #         break

# #     for idx, (x, y, w, h) in enumerate(parking_slots):
# #         slot = frame[y:y+h, x:x+w]

# #         # Step 1: Convert to grayscale
# #         gray = cv2.cvtColor(slot, cv2.COLOR_BGR2GRAY)
# #         cv2.imshow(f'Slot {idx+1} - Grayscale', gray)

# #         # Step 2: Adaptive threshold
# #         adaptive_thresh = cv2.adaptiveThreshold(
# #             gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
# #             cv2.THRESH_BINARY_INV, 11, 2
# #         )
# #         cv2.imshow(f'Slot {idx+1} - Threshold', adaptive_thresh)

# #         # Step 3: Canny edges
# #         edges = cv2.Canny(gray, 50, 150)
# #         cv2.imshow(f'Slot {idx+1} - Edges', edges)

# #         # Step 4: Combine
# #         combined = cv2.bitwise_or(adaptive_thresh, edges)
# #         cv2.imshow(f'Slot {idx+1} - Combined', combined)

# #         # Step 5: Count white pixels
# #         non_zero = cv2.countNonZero(combined)
# #         total_pixels = w * h
# #         ratio = non_zero / total_pixels

# #         print(f"Slot {idx+1}: white pixels = {non_zero}, total = {total_pixels}, ratio = {ratio:.2f}")

# #         # Determine status
# #         status = 'Occupied' if ratio > occupancy_threshold else 'Vacant'
# #         color = (0, 0, 255) if status == 'Occupied' else (0, 255, 0)

# #         # Draw result
# #         cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
# #         cv2.putText(frame, status, (x, y - 5),
# #                     cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

# #     cv2.imshow('Improved Parking Detection', frame)

# #     # Press 'q' to quit
# #     if cv2.waitKey(0) & 0xFF == ord('q'):
# #         break

# # cap.release()
# # cv2.destroyAllWindows()



# import cv2

# # Load the video
# cap = cv2.VideoCapture('parking_lot.mp4')

# # Define parking slot coordinates (x, y, w, h)
# parking_slots = [
#     (60, 0, 150, 56),
#     (60, 56, 150, 56),
#     (60, 112, 150, 56),
#     (60, 168, 150, 56),
#     (60, 224, 150, 56),
#     (60, 280, 150, 56),
#     (60, 336, 150, 56),
# ]

# # Threshold ratio for determining occupancy
# occupancy_threshold = 0.1

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     for idx, (x, y, w, h) in enumerate(parking_slots):
#         slot = frame[y:y+h, x:x+w]

#         # Step 1: Convert to grayscale
#         gray = cv2.cvtColor(slot, cv2.COLOR_BGR2GRAY)
#         cv2.imshow(f'Slot {idx+1} - Grayscale', gray)

#         # Step 2: Canny edge detection
#         edges = cv2.Canny(gray, 50, 150)
#         cv2.imshow(f'Slot {idx+1} - Canny Edges', edges)

#         # Debugging output
#         non_zero = cv2.countNonZero(edges)
#         total_pixels = w * h
#         ratio = non_zero / total_pixels

#         print(f"Slot {idx+1}: Edge Pixels = {non_zero}, Total = {total_pixels}, Ratio = {ratio:.2f}")

#         # Decide status based on edge pixel count
#         status = 'Occupied' if ratio > occupancy_threshold else 'Vacant'
#         color = (0, 0, 255) if status == 'Occupied' else (0, 255, 0)

#         # Draw rectangle and status text
#         cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
#         cv2.putText(frame, status, (x, y - 5),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

#     # Display final frame with annotations
#     cv2.imshow('Parking Detection (Grayscale + Canny)', frame)

#     # Wait for keypress to proceed to next frame
#     if cv2.waitKey(0) & 0xFF == ord('q'):
#         break

# # Cleanup
# cap.release()
# cv2.destroyAllWindows()


import cv2

# Load the video
cap = cv2.VideoCapture('parking_lot.mp4')

# Use original coordinates from your first version
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

# Threshold ratio for determining occupancy
occupancy_threshold = 0.1  # Lower = more sensitive

while True:
    ret, frame = cap.read()
    if not ret:
        break

    for idx, (x, y, w, h) in enumerate(parking_slots):
        # Crop slot
        slot = frame[y:y+h, x:x+w]

        # Step 1: Grayscale
        gray = cv2.cvtColor(slot, cv2.COLOR_BGR2GRAY)
        cv2.imshow(f'Slot {idx+1} - Grayscale', gray)

        # Step 2: Canny edge detection
        edges = cv2.Canny(gray, 50, 150)
        cv2.imshow(f'Slot {idx+1} - Canny Edges', edges)

        # Debug info
        non_zero = cv2.countNonZero(edges)
        total_pixels = w * h
        ratio = non_zero / total_pixels
        print(f"Slot {idx+1}: Edge Pixels = {non_zero}, Total = {total_pixels}, Ratio = {ratio:.2f}")

        # Status
        status = 'Occupied' if ratio > occupancy_threshold else 'Vacant'
        color = (0, 0, 255) if status == 'Occupied' else (0, 255, 0)

        # Draw on frame
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(frame, status, (x, y - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

    # Show full frame
    cv2.imshow('Parking Detection (Grayscale + Canny)', frame)

    # Wait for a short time between frames (press 'q' to quit)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
