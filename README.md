<h1 align="center">Watermark Adder</h1>

`Watermark Adder` is a python code which helps you to add watermark (logo) to images

## Installation
****1-Semi Automatic:****
1- We want to copy the main python script and set your terminal to know `watermark` as a command.
- Run install.sh file directly with one of these two commands:
  - MacOS and Linux:
    - using wget:
      * `bash -c "$(wget -q -O- https://raw.githubusercontent.com/mhbahmani/Watermark-Adder/master/linux_install.sh)"`
    - using curl:
      * `bash -c "$(curl -L -fsS -r 5 https://raw.githubusercontent.com/mhbahmani/Watermark-Adder/master/linux_install.sh)"`

2- This is the hard part! Installing OpenCV. This is a short toturial for installing OpenCV on ubuntu.

  - First, check installed packages are up-to-date or not.
    * `sudo apt-get update`
    * `sudo apt-get upgrade`

  - Then, we have to install some prerequirements for packages.
    * `sudo apt-get install build-essential cmake git pkg-config`

  - Next, we're going to install some additional libraries that are specifcally for reading image formats.
    * `sudo apt-get install libjpeg-dev libtiff5 libjasper-dev libpng12-dev`

  - Now, same thing for video formats.
   * `sudo apt-get install libavcode-dev libavformat-dev libswscale-dev libv4l-dev`

  - Then, we want to install sth tath allows us to use OpneCV's user interface features.
    * `sudo apt-get install libgtk2.0-dev`

  - This package will helps us to optimize OpenCV comamnds.
    * `sudo apt-get install libatlas-base-dev gfortran`

  - Install python or check your python vesion using `python --version`.
  - Then install pip tool.
  - Install numpy using `sudo pip isntall numpy`

  - Now, go for the head! clone this repo and checkout to a stabl branch.
    * `git clone https://github.com/Itseez/opencv_contrib.git`

  - Also clone this one and checkout to a stabl branch.
    * `git clone https://gitbub.com/Itseez/opencv.git`
    * `cd opencv`
    * `mkdir build`
    * `cd build`
    * `cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXPAMPLES=ON -D OPENCV_EXTRA_MODULES_PATH="previus repo that we downloaded path" -D BUILD_EXPAMPLES=ON ..`
     * `make -j4`

  - Now, we can install OpenCV.
    * `sudo make install`
    * `sudo ldconfig`

  - You can check installation.
    * `ls /usr/local/lib/python3.5/stie-packages/`
  or
    * `ls /usr/local/lib/python3.5/dist-packages/`

  - It shulde be a .so file created in this folder.
  - Python folder can be change depend on what python version that you are using.


****2- Manual:****
Make sure you have python3 using `python3 --version`
- We need virtualenv. So, if you don't have, install it.
  - MacOS and Linux: `python3 -m pip install --user virtualenv`
  - Windows: `py -m pip install --user virtualenv`

- Clone the repository
  - `git clone https://github.com/mhbahmani/Watermark-Adder`

- Now we have to create a virtual environment with python3:
  - MacOS and Linux: `virtualenv -p python3 venv`
  - Windows: `py -m venv venv`

- Then, we should activate it:
  - MacOs and Linux: `source venv/bin/activate`
  - Windows: `.\venv\Scripts\activate`

- Install requiered packages:
  - `pip install -r requirements.txt`

**Done. It's ready to use!**

## How to use
- Just Type `watermark` and pass watermark and image path. 

- You can add these arguments and options to this command:

| **Options**                       | **Description**                                       |
|:----------------------------------|:------------------------------------------------------|
|`-i <main image file path>`        | Script looks for image in given path                  |
|`-l <watermark file path>`         | Script looks for watermark in given path              |
|`-p <watermark scale percents>`    | Declare watermark should be how many percents of image|

*Default path for image and watermark is beside of script and names image.jpg and watermark.png*
*Default value for watermark scale percents is 6*

| **Arguments**                     | **Description**                                       |
|:----------------------------------|:------------------------------------------------------|
|`[watermark coordiantes]`          | You can use `top`, `bottom`, `right` and `left` to set specified place for watermark |

*Default place for watermark is bottom left*

- Example:
  - `watermark -i $Home/image.jpg -l channel_logo.png`
    - *(Watermark file is channel_logo.png and it is in same directory with main.py)*
  -  `watermark main.py -i image.png right bottom`
  
## Bug Report and Feedback
 * Please let me know if there is any bug
 * If you had any Feedback on `Watermark Adder`, i'll be glad to hear it.
 * You can contact me via:
   * email: mhbahmani79@gmail.com / mhbahmani@ce.sharif.edu
