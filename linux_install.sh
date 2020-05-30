mkdir Watermark\ Adder/
echo installing virtualenv

python3 -m pip install --user virtualenv

echo cloning repository and install requirements

git clone https://github.com/mhbahmani/Watermark-Adder
mv Watermark-Adder/Watermark ./
chmod +x watermark
mv Watermark-Adder/LICENCE ./
mv Watermark-Adder/requirements.txt ./
mv Watermark-Adder/README.md ./
rm -rf Watermark-Adder

script_path=/usr/local/bin/watermark
sudo tee $script_path << EOF > /dev/null
#!/usr/bash
PATH=~/Codes/Python/watermark

source $PATH/venv/bin/activate
python watermark.py "$@"
EOF

sudo chmod +x $script_path

virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
