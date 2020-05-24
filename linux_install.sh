mkdir Watermark\ Adder/
echo installing virtualenv

python3 -m pip install --user virtualenv


echo cloning repository and install requirements

git clone https://github.com/mhbahmani/Watermark-Adder
mv Watermark-Adder/main.py ./
mv Watermark-Adder/LICENCE ./
mv Watermark-Adder/requirements.txt ./
mv Watermark-Adder/README.md ./
rm -rf Watermark-Adder

virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
