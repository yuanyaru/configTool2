# !/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import traceback
import Ice
Ice.loadSlice("./ice-sqlite.ice")
import CommandArea


def ice_con():
    ic = None
    status = 0
    try:
        ic = Ice.initialize(sys.argv)
        base = ic.stringToProxy("DataCommand:ws -h 192.168.100.170 -p 10010")
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
