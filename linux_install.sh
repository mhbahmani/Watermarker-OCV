echo installing virtualenv

python3 -m pip install --user virtualenv


echo cloning repository and install requirements

git clone https://github.com/mhbahmani/Watermark-Adder
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
