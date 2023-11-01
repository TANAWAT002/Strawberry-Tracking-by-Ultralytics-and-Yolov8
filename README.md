# Strawberry-Tracking-by-Ultralytics-and-Yolov8
Welcome to my project "Develop Strawberry Tracking System and Movement Conditions of the Strawberry Harvesting Robot" in this repository I would show you **How to use** custom model Yolov8 for Strawberry Tracking and create Movement Condition of Harvesting Robot and run on Nvidia Jetson Nano.
# Material, Device, Program, Package and Library 
* **Material**

  1. Plastic Strawberries
   
     ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/30b403a1-a904-48fc-9571-bbb6f216821b)

* **Decive**

  1. Nvidia [Jetson Nano](https://developer.nvidia.com/embedded/jetson-nano-developer-kit)
   
      ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/e309b90c-3f78-4bf3-94a7-3888a4c7f786)
   
  2. LCD Touch screen Display 7 in (1024 x 600) Model: [CLB7INH](https://m.indiamart.com/proddetail/7-inch-lcd-touchscreen-17363059997.html?pos=4&pla=n)
   
      ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/7e8f3081-4d4a-4252-b5d5-aea087fea08a)

  3. HDMI cable
  4. Micro-usb cable
  5. Keyborad
  6. Mouse
  7. Usb Camera "[Mycobot Camera Flag](https://shop.elephantrobotics.com/en-th/products/mycobot-camera-flange)"
   
      ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/5d38dbb9-1c0e-4e3f-b8c9-6131e178cf85)

* **Program**
  1. Visual Studio Code  ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/a1c5c743-12e9-4a61-805c-e00c960ee41d)

  2. Balena Etcher  ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/59df7308-dacd-41a9-91a6-bb7fecc00ad1)

  3. SD Card Formatter  ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/e5edd90b-1fb7-4453-bcfd-5e31bacac7ff)

  4. Nvidia GPU Computing Toolkit (CUDA)  ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/55780945-f840-4674-b591-c167aa7f1073)

* **Package and Library**
  1. Python  ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/7b1e9399-a003-4ce2-b876-ef9cf19979f8)

  2. Opencv  ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/74ea8c1c-03fc-4479-80f7-f2b848195f40)

  3. Pytorch  ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/642753f8-fe8b-4fc1-af69-873f6e72a1b7)

  4. Ultralytics  ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/5378007f-2157-4c87-b48d-86feaaa2c39f)

## Step-by-step instructions
* **Part Installing and Setup on PC**
  1. Download and Install Visual Studio Code from [VScode](https://code.visualstudio.com/)
  2. Install extensions for [easy-use](https://youtu.be/mXt01LRmVMQ?si=8sGPC3R0pdPheCnv) (Python, Path intellisense, Material icon Theme, Eva Theme and Pylance)

     ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/5e6742b5-99d3-41ee-8d15-c4707f6d52a8)

  3. Install package and library
     1. Create folder
     2. Launch Visual Studio Code
     3. File -> Open Folder -> select the folder was created
        
        ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/f68142f9-6d01-4e95-9c36-75ba283d15bf)
        
     4. Open terminal "+" -> Command Prompt
        
        ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/98b8d7b5-8a89-4f54-8232-7fed1dedda21)
        
     5. Install "Opencv" and Ultralytics
        <pre>pip install opencv-contrib-python ultralytics</pre>
      
        ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/ff74da9a-e084-4417-96b9-588ee2874357)
        
    4. Download and Install Nvidia GPU Computing Toolkit from [cuda11.7](https://developer.nvidia.com/cuda-11-7-0-download-archive)
       1. Windows10 -> x86_64 -> exe(local) -> run .exe file for install
       
         ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/a2d1197a-63c8-416c-822f-c2a545fd3e76)

       2. Download Nvidia cuDNN from [cudnn](https://developer.nvidia.com/cudnn)

          ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/b5a87b7d-fca1-4033-bfa0-5e714f66357c)

          Extract .zip file and then move the files in these folders to CUDA.
            <pre>
              bin -> C:/Programe files/Nvidia GPU Computing Toolkit/CUDA/v11.7/bin
              lib -> C:/Programe files/Nvidia GPU Computing Toolkit/CUDA/v11.7/lib
              include -> C:/Programe files/Nvidia GPU Computing Toolkit/CUDA/v11.7/include</pre>
        3. Install [Pytorch](https://pytorch.org/)
             <pre>pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117</pre>
* **Part Coding (Detecttion, Tracking, Movement Condition, User Interface)**
  1. Download custom model is trained
  2. Multiple Object Tracking
     Use custom model for tracking by ultralytics
     1. Import needed package (ultralytics, opencv, pytorch, datetime, os)
        
        ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/8595ea1c-1393-4ade-a508-4ed73f17c610)
        
     2. Import custom model and use GPU for run program by pytorch

        ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/9cff2acd-c775-43cc-b5ef-c8aee32bbd3e)

     3. Open camera (0 is port of camera)

        ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/1757f4c5-272e-4032-a6c8-8b3eebcda481)

     4. Read frame
        
        ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/ce384ff7-afa8-4f80-bbb8-e57135718280)

     5. Use ultralytics for Tracking assign in "results"

        ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/edfc31f7-3bd2-4795-a717-9bc6063f3315)

        You can get "Bounding boxes" (int format, use gpu, to list)

          ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/2cf9578b-0d51-4d59-a850-8aa66a847757)

        or "Object ID" (int format, use gpu, to list)

          ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/8e1c6f9b-4bbb-4dc1-a0ab-29ed62addde0)

        or "Data" (Bounding boxes, object id, confidence, class id) (float format, use gpu, to list)

          ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/8d133781-d1ad-4e8e-9a70-090a17b9260e)

       6. Show realtime output on display

          ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/e482cf48-5b96-4d5c-a28e-6bebabf1a4be)

    3. Movement Condition of Strawberry Harvesting Robot
       Robot movement conditions Set the robot's movement status to be m_status (m_status = 1 is the robot moves, m_staus = 0 is the robot has stopped moving). Start by setting m_status = 1 until one of the strawberry fruits is found close to the edge. The left side of the image frame therefore gives m_status = 0 and m_status = 1 only if the number of strawberries is less than or equal to 1, shown as a working diagram as follows.
 
       1. Strawberry edge collision detection function (*endTheEdge(...)*)
          
          This function checks if there are any strawberries hitting the left edge of the frame. Include bounging boxes (track_xyxy), i = 0, edge_status = 0 and return edge_status (0:non-Hit the edge, 1:Hit the edge)
 
           <pre>
             def endTheEdge(track_xyxy, i=0, edge_status=0):
                detections = []
                for det in track_xyxy:
                  detections.append(det)
                  if detections[i][0] < 10:
                    edge_status = 1
                    break
                  else:
                    edge_status = 0
                  i += 1
                print("Edge status in endTheEdge function : " + str(edge_status))
                return edge_status</pre>

           ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/34528ace-ea10-41c2-aa97-6bc83bd7c66c)
       
       2. Strawberry counting function (*countSTB(...)*)
          
          This function counts the number of strawberries in the current frame. Include bounging boxes (track_xyxy), num_stb = 0 and return num_stb (number(s) of strawberry)

          <pre>
            def countSTB(track_xyxy, num_stb=0):
              for _ in track_xyxy:
                num_stb += 1
              cv2.putText(frame, f"Number(s) of Strawberry : {num_stb}", (200, 40), cv2.FONT_HERSHEY_DUPLEX, 0.5, WHITE, 3)
              cv2.putText(frame, f"Number(s) of Strawberry : {num_stb}", (200, 40), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 127, 0), 1)
              print("Numder(s) of STB in countSTB function : " + str(num_stb))
              return num_stb
          </pre>

          ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/e4952c57-57c2-4697-883a-3212616644aa)

       3. Strawberry detection function at the right end of the frame (*max_x1(...)*)
          
          Function for checking which strawberry is rightmost. Include bounging boxes (track_xyxy), max_sublist = [ ] and return max_sublist (x1, y1, x2, y2 format)
      
          <pre>
            def max_x1(track_xyxy,max_sublist=[]):
              if track_xyxy == []:
                max_sublist = [20, 20, 30, 30]
              else:
                max_sublist = max(track_xyxy, key=lambda x: x[0])
              cv2.rectangle(frame, (max_sublist[0], max_sublist[1]), (max_sublist[2], max_sublist[3]), RED, 2)
              print("MAX x1 : " + str(max_sublist))
              return max_sublist
          </pre>

          ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/ef5af7ec-228d-4556-a42f-492c0dec5d86)

       4. Function to determine the robot's movement status (*movementStatus(...)*)
      
          Set the movement state for the strawberry harvesting robot. Include bounging boxes (track_xyxy), edge_status from endTheEdge(...) and return m_status (m_status = 1 is the robot moves, m_staus = 0 is the robot has stopped moving)

          <pre>
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
          </pre>

          ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/be6d3528-eb1a-46a4-b2c4-09c933a1e044)

          ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/c599f426-993a-4134-87e3-58bd75d93ec6)

       5. Main Code (*Robot_moving_track_008.py*)
          
          This flowchart shows you how the code works.

          ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/408d0836-c9f2-4a96-8c90-333625155fd4)
          
          ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/e05e76f9-7ca9-4215-9f80-6a05f41a9cc2)

          ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/bee8010c-ca1b-4ccd-9865-38b5740c0799)

          ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/a8920165-c5dc-4fcd-9196-60f4f32fa6fb)
