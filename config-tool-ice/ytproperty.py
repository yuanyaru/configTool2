#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Blueprint, request
from iceCon import ice_con
import json
import Ice
Ice.loadSlice("./ice-sqlite.ice")
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
        ytpstruct = YTArea.DxPropertyYT(int(ytp[0][j]), ytp[1][j].encode("utf-8"),
                                        ytp[2][j].encode("utf-8"), ytp[3][j].encode("utf-8"),
                                        float(ytp[4][j]), float(ytp[5][j]),
                                        ytp[6][j].encode("utf-8"), float(ytp[7][j]),
                                        float(ytp[8][j]))
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