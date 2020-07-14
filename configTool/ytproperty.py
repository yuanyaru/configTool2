#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Blueprint, request
from iceCon import ice_con
import json
import Ice
Ice.loadSlice("./ice-sqlite.ice")
# Ice.loadSlice("/code/tool/configTool/ice-sqlite.ice")
import YTArea

yt_blu = Blueprint('yt', __name__)


# 查找(遥调属性)
@yt_blu.route('/yt_data', methods=['POST'])
def get_yt_property_send():
    stationId = request.form.get("stationId")
    station = json.loads(stationId)
    DataCommand = ice_con()
    status, result = DataCommand.RPCGetYTProperty(station)
    ytproperty = []
    for i in range(len(result)):
        ytproperty.append({"id": result[i].ID, "name": result[i].name,
                           "describe": result[i].describe, "unit": result[i].unit,
                           "kval": result[i].kval, "bval": result[i].bval,
                           "address": result[i].address, "uplimt": result[i].uplimt,
                           "downlimt": result[i].downlimt})
    return json.dumps(ytproperty)


# 添加、修改(遥调属性)
@yt_blu.route('/set_yt', methods=['POST'])
def set_yt_property():
    DataCommand = ice_con()
    stationId = request.form.get("stationId")
    station = json.loads(stationId)
    newyt = request.form.get("data")
    YtProperty = json.loads(newyt)
    ytp = []
    for i in range(len(YtProperty)):
        ytp.append(json.loads(YtProperty[i]))
    ytproperty = []
    for j in range(len(ytp[1])):
        ID = ytp[0][j]
        name = ytp[1][j]
        describe = ytp[2][j]
        unit = ytp[3][j]
        kval = ytp[4][j]
        bval = ytp[5][j]
        address = ytp[6][j]
        uplimt = ytp[7][j]
        downlimt = ytp[8][j]
        if ID == "":
            ID = 1000
        if name == "":
            name = "请添加遥调名称"
        if describe == "":
            describe = "请描述遥调"
        if unit == "":
            unit = "请添加单位"
        if kval == "":
            kval = 1.0
        if bval == "":
            bval = 0.0
        if address == "":
            address = "0"
        if uplimt == "":
            uplimt = 2000.0
        if downlimt == "":
            downlimt = 0.0
        ytpstruct = YTArea.DxPropertyYT(int(ID), name.encode("utf-8"),
                                        describe.encode("utf-8"), unit.encode("utf-8"),
                                        float(kval), float(bval),
                                        address.encode("utf-8"), float(uplimt),
                                        float(downlimt))
        ytproperty.append(ytpstruct)
    DataCommand.RPCSetYTProperty(station, ytproperty)
    return '保存成功!'


# 删除(遥调属性)
@yt_blu.route('/delete_yt', methods=['POST'])
def delete_yt_data():
    DataCommand = ice_con()
    stationId = request.form.get("stationId")
    station = json.loads(stationId)
    ytIDs = request.form.get("ids")
    yt_IDs = json.loads(ytIDs)
    pIDs = []
    for i in range(len(yt_IDs)):
        pIDs.append(long(yt_IDs[i]))
    DataCommand.RPCDelYTProperty(station, pIDs)
    return '删除成功!'