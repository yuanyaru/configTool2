#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, render_template
from iceCon import ice_con
import sys
import Ice
Ice.loadSlice("./ice-sqlite.ice")
from staproperty import sta_blu, get_station_property
from yxproperty import yx_blu
from ycproperty import yc_blu
from ykproperty import yk_blu
from ytproperty import yt_blu
from soeproperty import soe_blu

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.register_blueprint(sta_blu)
app.register_blueprint(yx_blu)
app.register_blueprint(yc_blu)
app.register_blueprint(yk_blu)
app.register_blueprint(yt_blu)
app.register_blueprint(soe_blu)


def get_property_table():
    DataCommand = ice_con()
    status, stationtable, yctable, yxtable, yktable, yttable, soetable = \
        DataCommand.RPCGetPropertyTable()
    table = [stationtable, yctable, yxtable, yktable, yttable, soetable]
    return table


@app.route('/')
def index():
    table = get_property_table()
    result = get_station_property()
    return render_template('data.html', tValue=table, staValue=result, staLen=len(result))


if __name__ == '__main__':
    app.run(debug=True)


