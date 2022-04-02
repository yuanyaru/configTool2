# !/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import traceback
import Ice
# Ice.loadSlice("./ice-sqlite.ice")
Ice.loadSlice("/code/tool/configTool/ice-sqlite.ice")
import CommandArea
from iceConfig import setIce


def ice_con():
    ic = None
    status = 0
    ice_IP = setIce()["ice_IP"]
    ice_port = setIce()["ice_port"]
    try:
        ic = Ice.initialize(['--Ice.MessageSizeMax=5120'])
        base = ic.stringToProxy("DataCommand:ws -h " + ice_IP + " -p " + ice_port)
        DataCommand = CommandArea.DataCommandPrx.checkedCast(base)
        if not DataCommand:
            raise RuntimeError("Invalid proxy")
        else:
            print("ICE连接成功!")
            return DataCommand
    except:
        traceback.print_exc()
        status = 1

    if ic:
        try:
            ic.destroy()
        except:
            traceback.print_exc()
            status = 1
    sys.exit(status)


if __name__ == '__main__':
    ice_con()
