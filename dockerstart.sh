#!/bin/bash
sudo docker build -t liviu_rebreanu .
sudo docker run -p 5000:5000 liviu_rebreanu
