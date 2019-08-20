#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Blueprint, request
from iceCon import ice_con
import json
import Ice
Ice.loadSlice("./ice-sqlite.ice")
import YCArea

yc_blu = Blueprint('yc', __name__)

# 查找(遥测属性)
@yc_blu.route('/yc_data', methods=['POST'])
def get_yc_property_send():
    stationId = request.form.get("stationId")
    station = json.loads(stationId)
    DataCommand = ice_con()
    status, result = DataCommand.RPCGetYCProperty(station)
    ycproperty = []
    for i in range(len(result)):
        ycproperty.append({"id": result[i].ID, "name": result[i].name,
                           "describe": result[i].describe, "unit": result[i].unit,
                           "kval": result[i].kval, "bval": result[i].bval,
                           "address": result[i].address, "uplimt": result[i].uplimt,
                           "downlimt": result[i].downlimt})
    return json.dumps(ycproperty)

# 添加、修改(遥测属性)
@yc_blu.route('/set_yc', methods=['POST'])
def set_yc_property():
    DataCommand = ice_con()
    stationId = request.form.get("stationId")
    station = json.loads(stationId)
    newyc = request.form.get("data")
    YcProperty = json.loads(newyc)
    ycp = []
    for i in range(len(YcProperty)):
        ycp.append(json.loads(YcProperty[i]))
    ycproperty = []
    for j in range(len(ycp[1])):
        ycpstruct = YCArea.DxPropertyYC(int(ycp[0][j]), ycp[1][j].encode("utf-8"),
                                        ycp[2][j].encode("utf-8"), ycp[3][j].encode("utf-8"),
                                        float(ycp[4][j]), float(ycp[5][j]),
                                        ycp[6][j].encode("utf-8"), float(ycp[7][j]),
                                        float(ycp[8][j]))
        ycproperty.append(ycpstruct)
    DataCommand.RPCSetYCProperty(station, ycproperty)
    return '保存成功!'

# 删除(遥测属性)
@yc_blu.route('/delete_yc', methods=['POST'])
def delete_yc_data():
    DataCommand = ice_con()
    stationId = request.form.get("stationId")
    station = json.loads(stationId)
    ycIDs = request.form.get("ids")
    yc_IDs = json.loads(ycIDs)
    pIDs = []
    for i in range(len(yc_IDs)):
        pIDs.append(long(yc_IDs[i]))
    DataCommand.RPCDelYCProperty(station, pIDs)
    return '删除成功!'