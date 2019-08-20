#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Blueprint, request
from iceCon import ice_con
import json
import Ice
Ice.loadSlice("./ice-sqlite.ice")
import YXArea

yx_blu = Blueprint('yx', __name__)

# 查找(遥信属性)
@yx_blu.route('/yx_data', methods=['POST'])
def get_yx_property_send():
    stationId = request.form.get("stationId")
    station = json.loads(stationId)
    DataCommand = ice_con()
    status, result = DataCommand.RPCGetYXProperty(station)
    yxproperty = []
    for i in range(len(result)):
        yxproperty.append({"ID": result[i].ID, "name": result[i].name,
                           "describe": result[i].describe, "ASDU": result[i].ASDU,
                           "wordPos": result[i].wordPos, "bitPos": result[i].bitPos,
                           "bitLength": result[i].bitLength, "LinkPoint1": result[i].LinkPoint1,
                           "LinkPoint2": result[i].LinkPoint2, "OneToZero": result[i].OneToZero,
                           "ZeroToOne": result[i].ZeroToOne, "address": result[i].address})
    return json.dumps(yxproperty)

# 添加、修改(遥信属性)
@yx_blu.route('/set_yx', methods=['POST'])
def set_yx_property():
    DataCommand = ice_con()
    stationId = request.form.get("stationId")
    station = json.loads(stationId)
    newyx = request.form.get("data")
    YxProperty = json.loads(newyx)
    yxp = []
    for i in range(len(YxProperty)):
        yxp.append(json.loads(YxProperty[i]))
    yxproperty = []
    for j in range(len(yxp[1])):
        yxpstruct = YXArea.DxPropertyYX(int(yxp[0][j]), yxp[1][j].encode("utf-8"),
                                        yxp[2][j].encode("utf-8"), int(yxp[3][j]),
                                        int(yxp[4][j]), int(yxp[5][j]),
                                        int(yxp[6][j]), int(yxp[7][j]),
                                        int(yxp[8][j]), yxp[9][j].encode("utf-8"),
                                        yxp[10][j].encode("utf-8"), yxp[11][j].encode("utf-8"))
        yxproperty.append(yxpstruct)
    DataCommand.RPCSetYXProperty(station, yxproperty)
    return '保存成功!'

# 删除(遥信属性)
@yx_blu.route('/delete_yx', methods=['POST'])
def delete_yx_data():
    DataCommand = ice_con()
    stationId = request.form.get("stationId")
    station = json.loads(stationId)
    yxIDs = request.form.get("ids")
    yx_IDs = json.loads(yxIDs)
    pIDs = []
    for i in range(len(yx_IDs)):
        pIDs.append(long(yx_IDs[i]))
    DataCommand.RPCDelYXProperty(station, pIDs)
    return '删除成功!'