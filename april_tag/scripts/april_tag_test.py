# import the necessary packages
import apriltag
import cv2
import numpy as np

def get_distance_and_angle(pose_matrix):
    # Extract translation vector (first 3 elements of the last column)
    translation_vector = pose_matrix[:3, 3]
    distance = np.linalg.norm(translation_vector)
    rotation_matrix = pose_matrix[:3, :3]

    euler_angles_rad = np.arccos((np.trace(rotation_matrix) - 1) / 2)
    angle_degrees = np.degrees(euler_angles_rad)

    return distance, angle_degrees

# Camera intrinsic parameters (example values)
focal_length_x = 547.7837  # example focal length in pixels
focal_length_y = 547.8070
principal_point_x = 303.9048  # example principal point (image center)
principal_point_y = 243.7748

tag_height_meters = 0.05
# define the AprilTags detector options
options = apriltag.DetectorOptions(families="tag36h11")
detector = apriltag.Detector(options, searchpath=apriltag._get_dll_path())

# start video capture from the default camera (index 0)
print("[INFO] starting video stream...")
vs = cv2.VideoCapture(0)
pose = []

# loop over frames from the video stream
while True:
    # grab the next frame from the video stream
    ret, frame = vs.read()

    # convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect AprilTags in the grayscale frame
    results, overlay = apriltag.detect_tags(gray,
                                            detector,
                                            camera_params=(focal_length_x, focal_length_y, principal_point_x, principal_point_y),
                                            tag_size=0.0762,
                                            vizualization=3,
                                            verbose=3,
                                            annotation=True
                                              )
    # results = detector.detect(gray)
    # print((overlay[0][0]))
    print(len(results))
    i = 0
    while (i < len(results)):
        print("CORNERS: ", results[i].corners)
        print("CENTERS: ", results[i].center)
        # print("POSE: ", results[i + 1])
        print(get_distance_and_angle(results[i + 1]))
        
            # extract the bounding box (x, y)-coordinates for the AprilTag
        (ptA, ptB, ptC, ptD)  = results[i].corners
        # print(results[i].corners)
        # ptA = results[i].corners[0]
        # ptB = results[i].corners[1]
        # ptC = results[i].corners[2]
        # ptD = results[i].corners[3]
        ptB = (int(ptB[0]), int(ptB[1]))
        ptC = (int(ptC[0]), int(ptC[1]))
        ptD = (int(ptD[0]), int(ptD[1]))
        ptA = (int(ptA[0]), int(ptA[1]))

        cX = int(results[i].center[0])
        cY = int(results[i].center[1])

        # draw the bounding box of the AprilTag detection
        cv2.line(frame, ptA, ptB, (0, 255, 0), 2)
        cv2.line(frame, ptB, ptC, (0, 255, 0), 2)
        cv2.line(frame, ptC, ptD, (0, 255, 0), 2)
        cv2.line(frame, ptD, ptA, (0, 255, 0), 2)
        # # draw the center (x, y)-coordinates of the AprilTag
        cv2.circle(frame, (cX, cY), 5, (0, 0, 255), -1)




        i += 4

        

        # draw the tag family on the frame
        # tagFamily = r.tag_family.decode("utf-8")
        # cv2.putText(frame, tagFamily, (ptA[0], ptA[1] - 15),
                    # cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        # print("[INFO] tag family: {}".format(tagFamily))
        
    # if (results):
    #     print("for detection: ")
    #     # if (results[0].corners.any()):
    #     #     print("CORNERS: ", r.corners)
    #     # if (results[0].center.any()):
    #     #     print("CENTER: ",  r.center)
    #     print(results[0].corners)


    # # loop over the AprilTag detection results
    # for r in results:
    #     # extract the center (x, y)-coordinates of the AprilTag
    #     (cX, cY) = (int(r.center[0]), int(r.center[1]))

    #     # calculate physical coordinates using camera calibration
    #     x_physical = (cX - principal_point_x) / focal_length_x
    #     y_physical = (cY - principal_point_y) / focal_length_y
    #     z_physical = 1  # assuming the AprilTag is in the same plane as the camera (z=1)
        
	# 	# distance = (tag_height_meters * focal_length_y) / (ptA[1] - ptD[1])
    #     # # Print the calculated distance
    #     # print("[INFO] Distance to AprilTag: {:.2f} meters".format(distance))

    #     # print the physical coordinates
    #     print("[INFO] AprilTag center physical coordinates (x, y, z): ({:.2f}, {:.2f}, {:.2f})".format(
    #         x_physical, y_physical, z_physical))

		

    

    # display the frame with AprilTag detection
    cv2.imshow("AprilTag Detection", frame)

    # check for the 'q' key to quit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the video stream and close any open windows
vs.release()
cv2.destroyAllWindows()
