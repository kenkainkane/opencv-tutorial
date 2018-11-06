# opencv-tutorial
## Windows Installation
1. Download & Install Anaconda Python Package
  - https://www.anaconda.com/download
2. Download and Run OpenCV
  - https://opencv.org/releases.html
3. For Python2.7
  * Go to ```C:\opencv\build\python\2.7\x64```
  * copy ```cv2.py``` and place in ```C:\Users\Anaconda2\Lib\site-packages```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For Python3.6
  * Open command prompt and type :
    ```
    $ pip install opencv-python
    ```
## MacOS Installation
1. Install Xcode
  ```sudo xcode-select --install```
2. Install homebrew and add the following line to the end of ~/.bashrc
  ```export PATH=/usr/local/bin:$PATH```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Use source command to load the changes in corresponding file.
  ```source ~/.bashrc```
3. Install Python
  ```
  brew install python python3
  brew link python
  brew link python3
  ```
4. Install pip3 for python3 
  ```
  brew postinstall python3
  ```
5. Install virtualenv and virtualenvwrapper
  ```
  pip3 install virtualenv virtualenvwrapper
  ```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Add following lines to the ~/.bashrc
  ```
  export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
  export WORKON_HOME=$HOME/.virtualenvsexport
  PROJECT_HOME=$HOME/Develsource /usr/local/bin/virtualenvwrapper.sh
  ```
6. Install OpenCV
  ```
  brew install opencv
  ```
7. Add OpenCV site path to global site path
  ```
  echo /usr/local/opt/opencv/lib/python3.6/site-packages >> /usr/local/lib/python3.6/site-packages/opencv3.pth
  ```
8. Create a virtual environment
  ```
  mkvirtualenv cv-py3 -p python3
  workon cv-py3
  deactivate
  ```
9. Install lib in ~/.virtualenvs.
  ```
  pip install numpy scipy scikit-image matplotlib scikit-learn
  ```
10. Link previously installed OpenCV library to this virtual invironment
  ```
  cd ~/.virtualenvs/cv-py3/lib/python3.6/site-packages/
  ln -s /usr/local/opt/opencv@3/lib/python3.6/site-packages/cv2.cpython-36m-darwin.so cv2.so
  ```
11. Check
  ```
  workon cv-py3
  python3
  import cv2
  print(cv2.__version__)
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
