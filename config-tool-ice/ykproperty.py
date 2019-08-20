#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Blueprint, request
from iceCon import ice_con
import json
import Ice
Ice.loadSlice("./ice-sqlite.ice")
import YKArea

yk_blu = Blueprint('yk', __name__)

# 查找(遥控属性)
@yk_blu.route('/yk_data', methods=['POST'])
def get_yk_property_send():
    stationId = request.form.get("stationId")
    station = json.loads(stationId)
    DataCommand = ice_con()
    status, result = DataCommand.RPCGetYKProperty(station)
    ykproperty = []
    for i in range(len(result)):
        ykproperty.append({"ID": result[i].ID, "name": result[i].name,
                           "describe": result[i].describe, "ASDU": result[i].ASDU,
                           "wordPos": result[i].wordPos, "bitPos": result[i].bitPos,
                           "bitLength": result[i].bitLength, "EnablePoint": result[i].EnablePoint,
                           "EnableValue": result[i].EnableValue, "address": result[i].address})
    return json.dumps(ykproperty)

# 添加、修改(遥控属性)
@yk_blu.route('/set_yk', methods=['POST'])
def set_yk_property():
    DataCommand = ice_con()
    stationId = request.form.get("stationId")
    station = json.loads(stationId)
    newyk = request.form.get("data")
    YkProperty = json.loads(newyk)
    ykp = []
    for i in range(len(YkProperty)):
        ykp.append(json.loads(YkProperty[i]))
    ykproperty = []
    for j in range(len(ykp[1])):
        ykpstruct = YKArea.DxPropertyYK(int(ykp[0][j]), ykp[1][j].encode("utf-8"),
                                        ykp[2][j].encode("utf-8"), int(ykp[3][j]),
                                        int(ykp[4][j]), int(ykp[5][j]),
                                        int(ykp[6][j]), int(ykp[7][j]),
                                        int(ykp[8][j]), ykp[9][j].encode("utf-8"))
        ykproperty.append(ykpstruct)
    DataCommand.RPCSetYKProperty(station, ykproperty)
    return '保存成功!'

# 删除(遥控属性)
@yk_blu.route('/delete_yk', methods=['POST'])
def delete_yk_data():
    DataCommand = ice_con()
    stationId = request.form.get("stationId")
    station = json.loads(stationId)
    ykIDs = request.form.get("ids")
    yk_IDs = json.loads(ykIDs)
    pIDs = []
    for i in range(len(yk_IDs)):
        pIDs.append(long(yk_IDs[i]))
    DataCommand.RPCDelYKProperty(station, pIDs)
    return '删除成功!'