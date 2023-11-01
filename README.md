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

  4. Install package and library
     1. Create folder
     2. Launch Visual Studio Code
     3. File -> Open Folder -> select the folder was created
        
        ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/f68142f9-6d01-4e95-9c36-75ba283d15bf)
        
     4. Open terminal "+" -> Command Prompt
        
        ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/98b8d7b5-8a89-4f54-8232-7fed1dedda21)
        
     5. Install "Opencv" and Ultralytics
        <pre>pip install opencv-contrib-python ultralytics</pre>
      
        ![image](https://github.com/TANAWAT002/Strawberry-Tracking-by-Ultralytics-and-Yolov8/assets/136689717/ff74da9a-e084-4417-96b9-588ee2874357)
