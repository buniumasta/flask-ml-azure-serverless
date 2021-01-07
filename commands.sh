#!/usr/bin/env bash

az webapp up -n flask-ml-myservice

git clone
make install
make all
python3 -m venv ~/.flask-ml-azure
source ~/.flask-ml-azure/bin/activate
