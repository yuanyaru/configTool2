#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Blueprint, request
from iceCon import ice_con
import json
import Ice
Ice.loadSlice("./ice-sqlite.ice")
import StationArea

sta_blu = Blueprint('station', __name__)


def get_station_property():
    DataCommand = ice_con()
    status, result = DataCommand.RPCGetStationProperty()
    return result

# 查找(厂站属性)
@sta_blu.route('/station_data', methods=['GET'])
def get_station_property_send():
    result = get_station_property()
    staproperty = []
    for i in range(len(result)):
        staproperty.append({"ID": result[i].ID, "name": result[i].name,
                            "describe": result[i].describe, "ruleID": result[i].ruleID,
                            "address": result[i].address, "PORT": result[i].PORT,
                            "role": result[i].role})
    return json.dumps(staproperty)

# 添加、修改(厂站属性)
@sta_blu.route('/set_station', methods=['POST'])
def set_station_property():
    DataCommand = ice_con()
    new_station = request.form.get("data")
    StationProperty = json.loads(new_station)
    stationp = []
    for i in range(len(StationProperty)):
        stationp.append(json.loads(StationProperty[i]))
    stap = []
    for j in range(len(stationp[6])):
        spstruct = StationArea.DxPropertyStation(int(stationp[0][j]), stationp[1][j].encode("utf-8"),
                                                 stationp[2][j].encode("utf-8"), int(stationp[3][j]),
                                                 stationp[4][j].encode("utf-8"), int(stationp[5][j]),
                                                 int(stationp[6][j]))
        stap.append(spstruct)
    # spstruct = StationArea.DxPropertyStation(99, "station", "station111", 19,
    #                                          "192.168.100.124", 29, 39)
    # stap.append(spstruct)
    DataCommand.RPCSetStationProperty(stap)
    return '保存成功!'

# 删除(厂站属性)
@sta_blu.route('/delete_station', methods=['POST'])
def delete_station_data():
    DataCommand = ice_con()
    stationIDs = request.form.get("ids")
    stations = json.loads(stationIDs)
    sta = []
    for i in range(len(stations)):
        sta.append(long(stations[i]))
    DataCommand.RPCDelStationProperty(sta)
    return '删除成功!'