# !/bin/bash

sudo apt-get update &&
sudo apt-get install  -y wget build-essential xutils-dev bison zlib1g-dev flex \
      libglu1-mesa-dev git g++ libssl-dev libxml2-dev libboost-all-dev git g++ \
      libxml2-dev vim python-setuptools build-essential python-pip &&
python3 -m venv .venv && 
source .venv/bin/activate &&
pip3 install -r requirements.txt &&
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 &&
git clone git@github.com:n1mb0606/gpu-app-collection.git