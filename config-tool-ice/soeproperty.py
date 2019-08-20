#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Blueprint, request
from iceCon import ice_con
import json
import Ice
Ice.loadSlice("./ice-sqlite.ice")
import SOEArea

soe_blu = Blueprint('soe', __name__)

# 查找(SOE属性)
@soe_blu.route('/soe_data', methods=['POST'])
def get_soe_property_send():
    stationId = request.form.get("stationId")
    station = json.loads(stationId)
    DataCommand = ice_con()
    status, result = DataCommand.RPCGetSOEProperty(station)
    soeproperty = []
    for i in range(len(result)):
        soeproperty.append({"num": result[i].num, "level": result[i].level,
                           "NowTime": result[i].NowTime, "time": result[i].time,
                           "StationName": result[i].StationName, "SOEName": result[i].SOEName,
                           "pointID": result[i].pointID, "status": result[i].status,
                           "Operater": result[i].Operater, "SOEOper": result[i].SOEOper})
    return json.dumps(soeproperty)

# 添加、修改(SOE属性)
@soe_blu.route('/set_soe', methods=['POST'])
def set_soe_property():
    DataCommand = ice_con()
    stationId = request.form.get("stationId")
    station = json.loads(stationId)
    newsoe = request.form.get("data")
    SoeProperty = json.loads(newsoe)
    soep = []
    for i in range(len(SoeProperty)):
        soep.append(json.loads(SoeProperty[i]))
    soeproperty = []
    for j in range(len(soep[1])):
        soepstruct = SOEArea.DxPropertySOE(int(soep[0][j]), int(soep[1][j]),
                                           soep[2][j].encode("utf-8"), soep[3][j].encode("utf-8"),
                                           soep[4][j].encode("utf-8"), soep[5][j].encode("utf-8"),
                                           int(soep[6][j]), soep[7][j].encode("utf-8"),
                                           soep[8][j].encode("utf-8"), soep[9][j].encode("utf-8"))
        soeproperty.append(soepstruct)
    DataCommand.RPCSetSOEProperty(station, soeproperty)
    return '保存成功!'

# 删除(SOE属性)
@soe_blu.route('/delete_soe', methods=['POST'])
def delete_soe_data():
    DataCommand = ice_con()
    stationId = request.form.get("stationId")
    station = json.loads(stationId)
    soeIDs = request.form.get("ids")
    soe_IDs = json.loads(soeIDs)
    pIDs = []
    for i in range(len(soe_IDs)):
        pIDs.append(long(soe_IDs[i]))
    DataCommand.RPCDelSOEProperty(station, pIDs)
    return '删除成功!'