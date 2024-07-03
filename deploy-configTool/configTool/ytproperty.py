#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Blueprint, request
from iceCon import ice_con
import json
import Ice
# Ice.loadSlice("./ice-sqlite.ice")
Ice.loadSlice("/code/tool/configTool/ice-sqlite.ice")
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
                           "kval": round(result[i].kval, 7), "bval": round(result[i].bval, 7),
                           "address": result[i].address, "uplimt": round(result[i].uplimt, 7),
                           "downlimt": round(result[i].downlimt, 7)})
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
    num = int(len(ytp[1])/8000)
    print(num)
    j = 0
    while j < num:
        for i in range(8000*j, 8000*j+8000):
            ID = ytp[0][i]
            name = ytp[1][i]
            describe = ytp[2][i]
            unit = ytp[3][i]
            kval = ytp[4][i]
            bval = ytp[5][i]
            address = ytp[6][i]
            uplimt = ytp[7][i]
            downlimt = ytp[8][i]
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
            ytpstruct = YTArea.DxPropertyYT(int(ID), name,
                                            describe, unit,
                                            round(float(kval), 7), round(float(bval), 7),
                                            address, round(float(uplimt), 7),
                                            round(float(downlimt), 7))
            ytproperty.append(ytpstruct)
        DataCommand.RPCSetYTProperty(station, ytproperty)
        print(len(ytproperty))
        ytproperty[:] = []
        j = j + 1
        print(j)
        continue
    for i in range(8000*j, len(ytp[1])):
        ID = ytp[0][i]
        name = ytp[1][i]
        describe = ytp[2][i]
        unit = ytp[3][i]
        kval = ytp[4][i]
        bval = ytp[5][i]
        address = ytp[6][i]
        uplimt = ytp[7][i]
        downlimt = ytp[8][i]
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
        ytpstruct = YTArea.DxPropertyYT(int(ID), name,
                                        describe, unit,
                                        round(float(kval), 7), round(float(bval), 7),
                                        address, round(float(uplimt), 7),
                                        round(float(downlimt), 7))
        ytproperty.append(ytpstruct)
    DataCommand.RPCSetYTProperty(station, ytproperty)
    print(len(ytproperty))
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
        pIDs.append(int(yt_IDs[i]))
    DataCommand.RPCDelYTProperty(station, pIDs)
    return '删除成功!'