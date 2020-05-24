<h1 align="center">Watermark Adder</h1>

`Watermark Adder` is a python code which helps you to add watermark (logo) to images

## Installation
***1- Automatic:***
Just run install.sh file directly with one of these two commands:
   - using wget:
     * `bash -c "$(wget -q -O- https://raw.githubusercontent.com/mhbahmani/Watermark_Adder/master/install.sh)"`
   - using curl:
     * `bash -c "$(curl -L -fsS -r 5 https://raw.githubusercontent.com/mhbahmani/Watermark_Adder/master/install.sh)"`

***2- Manual:***
Make sure you have python3 using `python3 --version`
- We need pip and virtualenv. So, if you don't have these, install them.
  - pip:
    - MacOS and Linux: 
      - `python3 -m pip install --user --upgrade pip`
    - Windows: The Python installers for Windows include pip. You can make sure it's up-to-date:
      - `py -m pip install --upgrade pip`
  - virtualenv:
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
- Go to script directory in terminal or command prompt.

- Activate created virtualenv:
  * MacOs and Linux: `source venv/bin/activate`
  * Windows: `.\env\Scripts\activate`
 
- Then run main.py script:
  * `python main.py`

- You can also add these arguments and options to this command:

| **Options**                       | **Description**                                       |
|:----------------------------------|:------------------------------------------------------|
|`-i <main image file path>`        | Script looks for image in given path                  |
|`-l <watermark file path>`         | Script looks for watermark in given path              |

*Default path for image and watermark is beside of script and names image.jpg and watermark.png*

| **Arguments**                     | **Description**                                       |
|:----------------------------------|:------------------------------------------------------|
|`[watermark coordiantes]`          | You can use `top`, `bottom`, `right` and `left` to set specified place for watermark                                                               |

*Default place for watermark is bottom left*

- Example:
  - `python main.py -i $Home/image.jpg -l channel_logo.png`
     * (Watermark file is channel_logo.png and it is in same directory with main.py)*
  -  `python main.py -i image.png right bottom`
  
## Bug Report and Feedback
 * Please let me know if there is any bug
 * If you had any Feedback on `Watermark Adder`, i'll be glad to hear it.
 * You can contact me via:
   * email: mhbahmani79@gmail.com / mhbahmani@ce.sharif.edu
