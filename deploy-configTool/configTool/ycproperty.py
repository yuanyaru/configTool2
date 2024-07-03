#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Blueprint, request
from iceCon import ice_con
import json
import Ice
# Ice.loadSlice("./ice-sqlite.ice")
Ice.loadSlice("/code/tool/configTool/ice-sqlite.ice")
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
                           "kval": round(result[i].kval, 7), "bval": round(result[i].bval, 7),
                           "address": result[i].address, "uplimt": round(result[i].uplimt, 7),
                           "downlimt": round(result[i].downlimt, 7)})
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
    num = int(len(ycp[1]) / 8000)
    print(num)
    j = 0
    while j < num:
        for i in range(8000*j, 8000*j+8000):
            ID = ycp[0][i]
            name = ycp[1][i]
            describe = ycp[2][i]
            unit = ycp[3][i]
            kval = ycp[4][i]
            bval = ycp[5][i]
            address = ycp[6][i]
            uplimt = ycp[7][i]
            downlimt = ycp[8][i]
            if ID == "":
                ID = 1000
            if name == "":
                name = "请添加遥测名称"
            if describe == "":
                describe = "请描述遥测"
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
            ycpstruct = YCArea.DxPropertyYC(int(ID), name,
                                            describe, unit,
                                            round(float(kval), 7), round(float(bval), 7),
                                            address, round(float(uplimt), 7),
                                            round(float(downlimt), 7))
            ycproperty.append(ycpstruct)
        DataCommand.RPCSetYCProperty(station, ycproperty)
        print(len(ycproperty))
        ycproperty[:] = []
        j = j + 1
        print(j)
        continue
    for i in range(8000*j, len(ycp[1])):
        ID = ycp[0][i]
        name = ycp[1][i]
        describe = ycp[2][i]
        unit = ycp[3][i]
        kval = ycp[4][i]
        bval = ycp[5][i]
        address = ycp[6][i]
        uplimt = ycp[7][i]
        downlimt = ycp[8][i]
        if ID == "":
            ID = 1000
        if name == "":
            name = "请添加遥测名称"
        if describe == "":
            describe = "请描述遥测"
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
        ycpstruct = YCArea.DxPropertyYC(int(ID), name,
                                        describe, unit,
                                        round(float(kval), 7), round(float(bval), 7),
                                        address, round(float(uplimt), 7),
                                        round(float(downlimt), 7))
        ycproperty.append(ycpstruct)
    DataCommand.RPCSetYCProperty(station, ycproperty)
    print(len(ycproperty))
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
        pIDs.append(int(yc_IDs[i]))
    DataCommand.RPCDelYCProperty(station, pIDs)
    return '删除成功!'