# !/usr/bin/python
# -*- coding:utf-8 -*-


def setIce():
    iceConfig = {
        "ice_IP": "{{.iceIP}}",
        "ice_port": "{{.icePort}}"
    }
    return iceConfig

