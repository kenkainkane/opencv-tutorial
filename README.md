# opencv-tutorial
## Windows Installation
1. Download & Install Anaconda Python Package
  - https://www.anaconda.com/download
2. Download and Run OpenCV
  - https://opencv.org/releases.html
3. For Python2.7
  * Go to "C:\opencv\build\python\2.7\x64"
  * copy cv2.py and place in "C:\Users\Anaconda2\Lib\site-packages"

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For Python3.6
  * Open command prompt and type :
    ```
    $ pip install opencv-python
    ```
  
## Linux Installation
1. Enter these command in Terminal
  ```
  $ sudo apt-get update 
  $ sudo apt-get upgrade 
  $ sudo apt-get install build-essential   cmake git pkg-config 
  $ sudo apt-get install libjpeg8-dev   libtiff4-dev libjasper-dev libpng12-dev 
  $ sudo apt-get install libgtk2.0-dev 
  $ sudo apt-get install libavcodec-dev   libavformat-dev libswscale-dev libv4l-dev 
  $ sudo apt-get install   libatlas-base-dev gfortran 
  $ cd ~ 
  $ git clone   https://github.com/Itseez/opencv.git 
  $ cd opencv 
  $ git checkout 3.0.0 
  $ cd ~/opencv 
  $ mkdir build 
  $ cd build 
  $ cmake -D CMAKE_BUILD_TYPE=RELEASE \ 
          -D   CMAKE_INSTALL_PREFIX=/usr/local \ 
          -D   INSTALL_C_EXAMPLES=ON \ 
          -D   INSTALL_PYTHON_EXAMPLES=ON \ 
          -D   OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \        
          -D   BUILD_EXAMPLES=ON .. 
  $ make -j4
  $ sudo make install
  $ sudo ldconfig
  ```
