#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Blueprint, request
from iceCon import ice_con
import json
import Ice
# Ice.loadSlice("./ice-sqlite.ice")
Ice.loadSlice("/code/tool/configTool/ice-sqlite.ice")
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
    num = int(len(yxp[1])/8000)
    j = 0
    while j < num:
        for i in range(8000*j, 8000*j+8000):
            ID = yxp[0][i]
            name = yxp[1][i]
            describe = yxp[2][i]
            ASDU = yxp[3][i]
            wordPos = yxp[4][i]
            bitPos = yxp[5][i]
            bitLength = yxp[6][i]
            LinkPoint1 = yxp[7][i]
            LinkPoint2 = yxp[8][i]
            OneToZero = yxp[9][i]
            ZeroToOne = yxp[10][i]
            address = yxp[11][i]
            if ID == "":
                ID = 1000
            if name == "":
                name = "请添加遥信名称"
            if describe == "":
                describe = "请描述遥信"
            if ASDU == "":
                ASDU = 0
            if wordPos == "":
                wordPos = 0
            if bitPos == "":
                bitPos = 0
            if bitLength == "":
                bitLength = 1
            if LinkPoint1 == "":
                LinkPoint1 = 0
            if LinkPoint2 == "":
                LinkPoint2 = 0
            if OneToZero == "":
                OneToZero = "由分到合"
            if ZeroToOne == "":
                ZeroToOne = "由合到分"
            if address == "":
                address = "0"
            yxpstruct = YXArea.DxPropertyYX(int(ID), name,
                                            describe, int(ASDU),
                                            int(wordPos), int(bitPos),
                                            int(bitLength), int(LinkPoint1),
                                            int(LinkPoint2), OneToZero,
                                            ZeroToOne, address)
            yxproperty.append(yxpstruct)
        DataCommand.RPCSetYXProperty(station, yxproperty)
        print(len(yxproperty))
        yxproperty[:] = []
        j = j + 1
        print(j)
        continue
    for i in range(8000*j, len(yxp[1])):
        ID = yxp[0][i]
        name = yxp[1][i]
        describe = yxp[2][i]
        ASDU = yxp[3][i]
        wordPos = yxp[4][i]
        bitPos = yxp[5][i]
        bitLength = yxp[6][i]
        LinkPoint1 = yxp[7][i]
        LinkPoint2 = yxp[8][i]
        OneToZero = yxp[9][i]
        ZeroToOne = yxp[10][i]
        address = yxp[11][i]
        if ID == "":
            ID = 1000
        if name == "":
            name = "请添加遥信名称"
        if describe == "":
            describe = "请描述遥信"
        if ASDU == "":
            ASDU = 0
        if wordPos == "":
            wordPos = 0
        if bitPos == "":
            bitPos = 0
        if bitLength == "":
            bitLength = 1
        if LinkPoint1 == "":
            LinkPoint1 = 0
        if LinkPoint2 == "":
            LinkPoint2 = 0
        if OneToZero == "":
            OneToZero = "由分到合"
        if ZeroToOne == "":
            ZeroToOne = "由合到分"
        if address == "":
            address = "0"
        yxpstruct = YXArea.DxPropertyYX(int(ID), name,
                                        describe, int(ASDU),
                                        int(wordPos), int(bitPos),
                                        int(bitLength), int(LinkPoint1),
                                        int(LinkPoint2), OneToZero,
                                        ZeroToOne, address)
        yxproperty.append(yxpstruct)
    DataCommand.RPCSetYXProperty(station, yxproperty)
    # 测试写函数，不能超过约10000条数据
    # for i in range(10000):
    #     ID = i
    #     name = "AU桥臂故障模块过多故障（=18）"
    #     describe = "station1_YX_1"
    #     ASDU = 1
    #     wordPos = 0
    #     bitPos = 0
    #     bitLength = 1
    #     LinkPoint1 = 0
    #     LinkPoint2 = 0
    #     OneToZero = "由合到分"
    #     ZeroToOne = "由分到合"
    #     address = "0"
    #     yxpstruct = YXArea.DxPropertyYX(int(ID), name.encode("utf-8"),
    #                                     describe.encode("utf-8"), int(ASDU),
    #                                     int(wordPos), int(bitPos),
    #                                     int(bitLength), int(LinkPoint1),
    #                                     int(LinkPoint2), OneToZero.encode("utf-8"),
    #                                     ZeroToOne.encode("utf-8"), address.encode("utf-8"))
    #     yxproperty.append(yxpstruct)
    return '保存成功!'

"""
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
        ID = yxp[0][j]
        name = yxp[1][j]
        describe = yxp[2][j]
        ASDU = yxp[3][j]
        wordPos = yxp[4][j]
        bitPos = yxp[5][j]
        bitLength = yxp[6][j]
        LinkPoint1 = yxp[7][j]
        LinkPoint2 = yxp[8][j]
        OneToZero = yxp[9][j]
        ZeroToOne = yxp[10][j]
        address = yxp[11][j]
        if ID == "":
            ID = 1000
        if name == "":
            name = "请添加遥信名称"
        if describe == "":
            describe = "请描述遥信"
        if ASDU == "":
            ASDU = 0
        if wordPos == "":
            wordPos = 0
        if bitPos == "":
            bitPos = 0
        if bitLength == "":
            bitLength = 1
        if LinkPoint1 == "":
            LinkPoint1 = 0
        if LinkPoint2 == "":
            LinkPoint2 = 0
        if OneToZero == "":
            OneToZero = "由分到合"
        if ZeroToOne == "":
            ZeroToOne = "由合到分"
        if address == "":
            address = "0"
        yxpstruct = YXArea.DxPropertyYX(int(ID), name.encode("utf-8"),
                                        describe.encode("utf-8"), int(ASDU),
                                        int(wordPos), int(bitPos),
                                        int(bitLength), int(LinkPoint1),
                                        int(LinkPoint2), OneToZero.encode("utf-8"),
                                        ZeroToOne.encode("utf-8"), address.encode("utf-8"))
        yxproperty.append(yxpstruct)
    DataCommand.RPCSetYXProperty(station, yxproperty)
    return '保存成功!'
"""


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
        pIDs.append(int(yx_IDs[i]))
    DataCommand.RPCDelYXProperty(station, pIDs)
    return '删除成功!'