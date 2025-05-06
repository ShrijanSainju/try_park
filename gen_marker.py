# import cv2
# import cv2.aruco as aruco

# # Use getPredefinedDictionary instead of Dictionary_get
# aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

# # Generate the marker with ID 0 and size 200x200
# marker_image = aruco.generateImageMarker(aruco_dict, 0, 200)

# # Save the marker as an image
# cv2.imwrite("aruco_marker_0.png", marker_image)

# print("Marker saved as aruco_marker_0.png")


import cv2
import cv2.aruco as aruco

aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

for marker_id in range(6):  # IDs from 0 to 5
    marker_image = aruco.generateImageMarker(aruco_dict, marker_id, 200)
    file_name = f"marker_{marker_id}.png"
    cv2.imwrite(file_name, marker_image)
    print(f"Saved {file_name}")
