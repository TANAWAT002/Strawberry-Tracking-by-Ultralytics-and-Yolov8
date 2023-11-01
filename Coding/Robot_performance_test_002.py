# Combine Tracking and Movement Condition
import cv2                      # for analyze frame
from ultralytics import YOLO    # for use custom model yolov8
import datetime                 # for use date, time, calculate fps
import torch                    # for use GPU
import os                       # for operate path

file_name = os.path.basename(__file__)
date = datetime.date.today()

# define Colors (BGR format)
WHITE = (255, 255, 255)
BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLACK = (0, 0, 0)

model_path = './test_deep-sort-realtime/last_261epochs_8n.pt'   # define path of custom model
model = YOLO(model_path).to(torch.device(0))                    # define custom model and select to use GPU by pytorch

# Open webcam
cap = cv2.VideoCapture(0)

# Get the VDO properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))            # get frame width
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))          # get frame height
fps = cap.get(cv2.CAP_PROP_FPS)                                 # get fps

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')                                                # define file type .mp4
output_path = "test_deep-sort-realtime/output_performance_test_002_20ea.mp4"     # define output path
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))            # output VDO

# define initial of movement status (m_status) and edge status (edge_status)
m_status = 1
edge_status = 0

def old_movementStatus(track_xyxy, edge_status):
    num_stb = countSTB(track_xyxy)
    if num_stb > 0 :
        if edge_status == 0:
            m_status = 1
        else :
            m_status = 0
    else :
        m_status = 1
    cv2.putText(frame, f"Movement status : {m_status}", (10, 40), cv2.FONT_HERSHEY_DUPLEX, 0.5, WHITE, 3)
    cv2.putText(frame, f"Movement status : {m_status}", (10, 40), cv2.FONT_HERSHEY_DUPLEX, 0.5, BLUE, 1)
    print(f"M_STATUS : {m_status}")
    return m_status

def movementStatus(track_xyxy, edge_status):
    max_sublist = max_x1(track_xyxy)
    print(max_sublist[0])
    num_stb = countSTB(track_xyxy)
    if edge_status == 1:
        print(f"If edge_status == 1 : num_stb = {num_stb}, max_sublist[0] = {max_sublist[0]}")
        if num_stb > 1:
            m_status = 0
            print("If cond (num_stb > 1) in movement status")
        elif num_stb == 1 :
            if max_sublist[0] < 10:
                m_status = 0
                print("Elif(if) cond (num_stb == 1 & max_sublist < 10) in movement status")
            else:
                m_status = 1
                print("Elif(else) cond (num_stb == 1) in movement status")
        else:
            m_status = 1
            print("Else cond in movement status")
    else:
        m_status = 1
        print("Else in movement status")
    print("Movement status : " + str(m_status))
    cv2.putText(frame, f"Movement status : {m_status}", (10, 40), cv2.FONT_HERSHEY_DUPLEX, 0.5, WHITE, 3)
    cv2.putText(frame, f"Movement status : {m_status}", (10, 40), cv2.FONT_HERSHEY_DUPLEX, 0.5, BLUE, 1)
    return m_status

def endTheEdge(track_xyxy, i=0, edge_status=0):
    detections = []
    for det in track_xyxy:
        detections.append(det)
        if 260 <= detections[i][0] <= 330:
            edge_status = 1
            break
        else:
            edge_status = 0
        i += 1
    print("Edge status in endTheEdge function : " + str(edge_status))
    return edge_status

def countSTB(track_xyxy, num_stb=0):
    for _ in track_xyxy:
        num_stb += 1
    cv2.putText(frame, f"Number(s) of Strawberry : {num_stb}", (200, 40), cv2.FONT_HERSHEY_DUPLEX, 0.5, WHITE, 3)
    cv2.putText(frame, f"Number(s) of Strawberry : {num_stb}", (200, 40), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 127, 0), 1)
    print("Numder(s) of STB in countSTB function : " + str(num_stb))
    return num_stb

def max_x1(track_xyxy,max_sublist=[]):
    if track_xyxy == []:
        max_sublist = [20, 20, 30, 30]
    else:
        max_sublist = max(track_xyxy, key=lambda x: x[0])
        cv2.rectangle(frame, (max_sublist[0], max_sublist[1]), (max_sublist[2], max_sublist[3]), RED, 2)
        print("MAX x1 : " + str(max_sublist))
    return max_sublist

def putProperties_ID(frame, track_data, m_status):

    for det in track_data:
            x1, y1, x2, y2, object_id, conf, class_id = det
            # cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), GREEN, 2)
            cv2.putText(frame, "Coor : "f"{int(x1)} {int(y1)}", (int(x2)+5, int(y1)+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, WHITE, 0)
            cv2.putText(frame, "ID :" + f"{int(object_id)}", (int(x2)+5, int(y1)+40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, WHITE, 0)
            cv2.putText(frame, "CONF :" + f"{conf:.2f}", (int(x2)+5, int(y1)+60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, WHITE, 0)
            cv2.putText(frame, "C_ID :" + f"{int(class_id)}", (int(x2)+5, int(y1)+80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, WHITE, 0)
            if m_status == 0:
                 print("!!! STOP MOVING !!!")
                 cv2.putText(frame, "!!! STOP MOVING !!!", (100, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.5, BLACK, 8)
                 cv2.putText(frame, "!!! STOP MOVING !!!", (100, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.5, WHITE, 2)

def putProperties_noneID(frame, track_data, m_status):

    for det in track_data:
            x1, y1, x2, y2, conf, class_id = det
            # cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), GREEN, 2)
            cv2.putText(frame, "Coor : "f"{int(x1)} {int(y1)}", (int(x2)+5, int(y1)+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, WHITE, 0)
            cv2.putText(frame, "CONF :" + f"{conf:.2f}", (int(x2)+5, int(y1)+60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, WHITE, 0)
            cv2.putText(frame, "C_ID :" + f"{int(class_id)}", (int(x2)+5, int(y1)+80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, WHITE, 0)
            if m_status == 0:
                 print("!!! STOP MOVING !!!")
                 cv2.putText(frame, "!!! STOP MOVING !!!", (100, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.5, BLACK, 8)
                 cv2.putText(frame, "!!! STOP MOVING !!!", (100, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.5, WHITE, 2)

# Loop through the video frames
while cap.isOpened():
    time_now = datetime.datetime.now().time().strftime("%H:%M:%S")

    start = datetime.datetime.now()         # define start time for calculate fps

    # Read a frame from the video
    success, frame = cap.read()             # success(bool) is can read ?, frame is numpy array of cap frame by frame
    frame = cv2.flip(frame, 1)              # flip frame 0 = flip vertical, 1 = flip horizontal

    if success:
        # Run YOLOv8 tracking on the frame, persisting tracks between frames
        results = model.track(source=frame, persist=True, iou=0.6, conf=0.4)    # iou = Intersection over Union, conf = Confidence
        
        track_xyxy = results[0].boxes.xyxy.int().cuda().tolist()                # xyxy get bounding boxes in integer format, to "list", by use cuda core (GPU) 

        edge_status = endTheEdge(track_xyxy)
        # if m_status == 1:                                                       # if "True" update edge_status. First m_status = 1 (initial value), next frame gets the m_status from "movementStatus(track_xyxy, edge_status)"
            # edge_status = endTheEdge(track_xyxy)
            
        # elif m_status == 0:                                                     # if "True" let "edge_status = 1"
            # edge_status = 1
            # pass
        
        print("Edge pre-movementStatus : " + str(edge_status))
        m_status = old_movementStatus(track_xyxy, edge_status)                      # Movement status (m_status) gets the value returned from the "movementStatus(track_xyxy, edge_status)" function.
        '''        
        track_data = results[0].boxes.data.float().cuda().tolist()              # data get bounding boxes, object_id, confidence, class_id in float format, to "list", by use cuda core (GPU)

        if results[0].boxes.id is None:                                         # if object_id is "None" ---> "putProperties_noneID(frame, track_data, m_status)"
            putProperties_noneID(frame, track_data, m_status)
        else:  
            track_ids = results[0].boxes.id.int().cuda().tolist()               # id get object_id in integer format, to "list", by use cuda core (GPU) 
            putProperties_ID(frame, track_data, m_status)
            print("Track id : " + str(track_ids))
        '''

        # put text "file name"
        cv2.putText(frame, f"File name : {file_name}", (200, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, WHITE, 3)
        cv2.putText(frame, f"File name : {file_name}", (200, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, BLACK, 1)

        # put text "date"
        cv2.putText(frame, f"Date : {date}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, WHITE, 3)
        cv2.putText(frame, f"Date : {date}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, BLACK, 1)

        # put time now
        cv2.rectangle(frame, (249, 55), (380, 75), WHITE, -1)
        cv2.putText(frame, f"Time : {time_now}", (250, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, RED, 1)

        # Draw middle line 
        cv2.line(frame, (320, 80), (320, 460), BLACK, 3)
        cv2.line(frame, (320, 80), (320, 460), WHITE, 1)

        # end time to compute the fps
        end  = datetime.datetime.now()

        # show the time it took to process 1 frame
        print(f"Time to process 1 frame : {(end - start).total_seconds() * 1000:.0f} milliseconds")

        # calulate the frame per second and draw it on the frame
        fps = f"FPS : {1 / (end - start).total_seconds():.2f}"

        cv2.putText(frame, fps, (460, 40), cv2.FONT_HERSHEY_DUPLEX, 0.5, WHITE, 3)
        cv2.putText(frame, fps, (460, 40), cv2.FONT_HERSHEY_DUPLEX, 0.5, RED, 1)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # write the frame to the output video file
        out.write(annotated_frame)

        # Display the annotated frame
        cv2.imshow("YOLOv8 Tracking", annotated_frame)

        # # Display the "frame"
        cv2.imshow("frame", frame)
        
        # Break the loop if 'e' is pressed
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break

    else:
        # Break the loop if the end of the video is reached
        print("Failed to read frame !!!")
        break

# Release the video capture object and close the display window
cap.release()
out.release()
cv2.destroyAllWindows()