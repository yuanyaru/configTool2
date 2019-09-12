#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Blueprint, request
from iceCon import ice_con
import json
import Ice
Ice.loadSlice("./ice-sqlite.ice")
# Ice.loadSlice("/code/tool/configTool/ice-sqlite.ice")
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
        soeproperty.append({"ID": result[i].ID, "name": result[i].name,
                           "describe": result[i].describe, "level": result[i].level})
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
        ID = soep[0][j]
        name = soep[1][j]
        describe = soep[2][j]
        level = soep[3][j]
        if ID == "":
            ID = 1000
        if name == "":
            name = "请添加SOE名称"
        if describe == "":
            describe = "请描述SOE"
        if level == "":
            level = 1
        soepstruct = SOEArea.DxPropertySOE(int(ID), name.encode("utf-8"),
                                           describe.encode("utf-8"), int(level))
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