#!/bin/bash

docker run --name configtool -p 5000:5000 -v $PWD:/code/tool --restart always --privileged=true -it configtool
