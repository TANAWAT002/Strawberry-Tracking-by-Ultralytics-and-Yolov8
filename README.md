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

       5. Main Code (*Robot_performance_test_001.py*)
          
          This flowchart shows you how the code works.

          ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/408d0836-c9f2-4a96-8c90-333625155fd4)
          
          ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/e05e76f9-7ca9-4215-9f80-6a05f41a9cc2)

          ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/bee8010c-ca1b-4ccd-9865-38b5740c0799)

          ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/a8920165-c5dc-4fcd-9196-60f4f32fa6fb)

* **Part Performance Test**
  
  Performance test to compare the movement time of a typical robot(*1*) with the movement of the new robot(*2*) from ***“[Design and Test of Tomatoes Harvesting Robot](https://ieeexplore.ieee.org/document/7279423)”*** found that the average time to harvest 1 tomato is 24 seconds. Therefore, the time to harvest 1 strawberry was determined to be 24 seconds.

  ***Objective***
  
      1. To compare the movement time of a typical robot. with the movement of new robots
      2. To test the performance of the Real-time strawberry tracking system.
       
  ***Hypothesis***

      Typical robot movement time More than a new kind of robot movement

  ***Initial variable***
  
      Typical robot movements and new robot movements
  
  ***Dependent variable***
  
      Robot movement time
  
  ***Control variables***
  
      1. 5, 10, and 20 red plastic strawberries
      2. Simulate an environment similar to the strawberry planting tracks in Plant Factory.
      3. Strawberry picking time: 24 seconds/fruit

  ***Experimental method***
  
    1. Simulate an environment similar to a strawberry growing trough in Plant Factory with 5, 10, and 20 fully red strawberry fruits.
    2. Write a program to define the conditions of robot movement.
       
        **(*1*)** is the general robot movement. (*Robot_performance_test_002.py*)
      mobile robot until any strawberries are in the center of the frame Have the robot stop moving, timed for 24 seconds, then let the robot continue moving. Repeat until all pictures are complete.

          **5 ea.**
 
          ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/e118ff3f-01ef-4079-b6b9-8699fba1ec2f)
  
          **10 ea.**
       
          ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/7d0266c7-f39f-4e2c-940a-b36d92beff0b)

          **20 ea.**
 
          ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/82b84be2-c4c4-40cf-a659-f2dcd1b9df1f)

        **(*2*)** is the new robot movement. (*Robot_performance_test_001.py*)
      mobile robot Until any strawberries were found Located along the far left edge of the image frame. Make the robot stop moving. Count the total number of strawberries (n) in the frame, timer 24(n -1) seconds, then let the robot continue moving. Repeat until all balls are complete.

          **5 ea.**
 
          ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/e7089f80-7b51-4ed7-8dfd-8b6fee2fe545)

          **10 ea.**
       
          ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/70378847-dca4-4919-aee6-3032f9b7abfb)

          **20 ea.**
 
          ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/64d7bc72-4044-46c1-9cf1-34bcfaaa7deb)

    4. Record the experimental results in the results recording table.

        ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/ed6d0929-365b-414f-8571-73eb4498e82d)

    5. Analyze, summarize and discuss results.
 
       ***Analyze results***
       
        - To collect 5 strawberries, the trypical robot movement took 156 seconds (2 minutes 36 seconds) and the new robot movement took 151 seconds (2 minutes 31 seconds), 3.31 percent faster.
          
        - To collect 10 strawberries, the trypical robot movement took 289 seconds (4 minutes 49 seconds) and the new robot movement took 151 seconds (4 minutes 21 seconds), 20.42 percent faster.
          
        - To collect 20 strawberries, the trypical robot movement took 554 seconds (9 minutes 14 seconds) and the new robot movement took 482 seconds (8 minutes 2 seconds), 14.94 percent faster.

* **Installing and Setup on Nvidia Jetson Nano**
  
  1. Download **[Ubuntu 20.04](https://ubuntu.com/)** 1. Download Ubuntu 20.04 with CUDA, Opencv, Python, Pytorch, TensorRT installed in the operating system at [Qengineering/Jetson-Nano-Ubuntu-20-image](https://github.com/Qengineering/Jetson-Nano-Ubuntu-20-image)
 
  2. Install the program for Format SD Card and Flash OS.
     
     1. [Balena Etcher](https://etcher.balena.io/)
    
        ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/5db86a1e-0f21-4004-a56f-bb33eb818242)

     2. [SD Cart Formatter](https://www.sdcard.org/downloads/formatter/sd-memory-card-formatter-for-windows-download/)
    
        ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/45ee749c-0603-4eb6-ae37-8fe9ab448fc8)

   3. Format micro-SD Card (64GB) with SD Card Formatter program.
 
      ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/38ea802f-b590-466c-8355-eca94e69d0e9)

   4. Fash OS downloaded from step (i) into the formatted micro-SD Card from step (iii) with the Balena Etcher program.

      Select file **->** select micro-SD Card **->** flash.

      ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/82acc7a3-53b3-4b18-b891-16f6be57d858)

      ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/19add400-034c-4c1a-97e2-ad0c44009da1)

   5. After the OS is finished flashing, insert it into the micro-SD Card slot of the Nvidia Jetson Nano with the Keyboard, Mouse, Display, already connected (the installed OS has already registered the system; password: jetson)
 
   6. Expand the partition size from the original 32 GB to 64 GB with the gparted program.
 
      1. Open Terminal
      2. Update apt
         
         <pre>sudo apt update</pre>
 
         ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/11f35c18-2770-4315-b660-2ff023206179)

         Install gparted
         
               sudo apt install gparted

         ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/ece0378f-d5e7-44d5-b6fb-d712a3d21234)

       3. Launch gparted
     
                gparted

          ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/48d98115-5727-47fa-84bd-23caf249e023)

       4. Right click on the current partition **->** resize/move **->** select adjust the value to maximum (59GB).
     
          ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/553e5ae3-fd18-4674-b1cb-88a3f988a844)

       5. Check the partition size using the jtop command in Terminal.
     
                jtop
     
          ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/18705efa-ea09-412a-8494-488ec98f8269)
