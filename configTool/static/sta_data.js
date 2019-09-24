function show_sta_table() {
    document.getElementById("sta_name").innerText="";

　　document.getElementById("sta_table").style.display="block";
    document.getElementById("yc_table").style.display="none";
    document.getElementById("yx_table").style.display="none";
    document.getElementById("yk_table").style.display="none";
    document.getElementById("yt_table").style.display="none";
    document.getElementById("soe_table").style.display="none";

    show_db_sta_data();
}

// 清空表格
function clearStaTable() {
    $("#tBody_sta").text("");
}

// 刷新左侧树
function getStation() {
    $.get("/station_data", function(res){
        $("#station").empty();
        str1 = '<li id="station" class="closed"><span class="folder" onclick="show_sta_table()">厂站列表</span></li>';
        $("#sta").html(str1);
        // 将JSON字符串反序列化成JSON对象
        var res2Json = JSON.parse(res);
        for(var i = 0; i<res2Json.length; i++) {
            str2 = '<ul><li class="closed">'+
                '<span class="folder" id="staId" style="display: none;">'+ res2Json[i].ID +'</span>'+
                '<span class="folder" id="staName">'+ res2Json[i].name +'</span>'+
                '<ul><li>'+'<span class="file" name="yx">遥信</span>'+'</li></ul>'+
                '<ul><li>'+'<span class="file" name="yc">遥测</span>'+'</li></ul>'+
                '<ul><li>'+'<span class="file" name="yk">遥控</span>'+'</li></ul>'+
                '<ul><li>'+'<span class="file" name="yt">遥调</span>'+'</li></ul>'+
                '<ul><li>'+'<span class="file" name="soe">SOE</span>'+'</li></ul>'+
                '</li></ul>';

            $("#station").append(str2);
        }
        $("#browser").treeview();
        ycTableClick();
        yxTableClick();
        ykTableClick();
        ytTableClick();
        soeTableClick();
    });
}

// 显示数据库的数据
function show_db_sta_data() {
    $.get("/station_data", function(res){
        clearStaTable();
        var resLen = res.length;
        if (resLen > 2) {
            // 将JSON字符串反序列化成JSON对象
            var res2Json = JSON.parse(res);
            // var res2Json = eval(res);
            for(var i = 0; i<res2Json.length; i++) {
                str = "<tr><td><input type='checkbox' name='station_ID'/>"
                        + "</td><td name='td0'>" + res2Json[i].ID
                        + "</td><td>" + res2Json[i].name
                        + "</td><td>" + res2Json[i].describe
                        + "</td><td>" + res2Json[i].ruleID
                        + "</td><td>" + res2Json[i].address
                        + "</td><td>" + res2Json[i].PORT
                        + "</td><td>" + res2Json[i].role + "</td></tr>";

                // 追加到table中
                $("#tBody_sta").append(str);
            }
        } else {
            alert("数据库为空，没有数据可显示！");
        }
    });
}

// 在表格尾部增添一行
function addStaRow(){
    str = "<tr><td><input type='checkbox' class='i-checks' name='station_ID'/>"
            + "</td><td name='td0'>"
            + "</td><td>"
            + "</td><td>"
            + "</td><td>"
            + "</td><td>"
            + "</td><td>"
            + "</td><td>" + "</td></tr>";

    // 追加到table中
    $("#tBody_sta").append(str);
}

// 删除尾部添加的行
function deleteStaRow() {
    var i = 0
    $("input[type='checkbox'][name='station_ID']").each(function() {
        if(this.checked) {
            i = i + 1;
            $(this).parents('tr').remove();
        }
    });
    if (i > 0) {
        alert("删除成功！")
    }
    else {
        alert("请先选择要删除的行！")
    }
}

// 添加和修改
function set_sta_data() {
    var IDs = new Array(); var names = new Array();
    var describes = new Array(); var ruleIDs = new Array();
    var addresss = new Array(); var PORTs = new Array();
    var roles = new Array(); var new_data = new Array();

    $("input[type='checkbox'][name='station_ID']").each(function() {
        if(this.checked) {
            var ID = $(this).parents('tr').children().eq(1).text();
            if(!/^[0-9]+$/.test(ID)) {
                alert('输入的ID有误，请重新输入！');
            } else {
                var name = $(this).parents('tr').children().eq(2).text();
                var describe = $(this).parents('tr').children().eq(3).text();
                var ruleID = $(this).parents('tr').children().eq(4).text();
                if(!/^[0-9]+$/.test(ruleID)) {
                    alert('输入的ruleID有误，请重新输入！');
                } else {
                    var address = $(this).parents('tr').children().eq(5).text();
                    var PORT = $(this).parents('tr').children().eq(6).text();
                    if(!/^[0-9]+$/.test(PORT)) {
                        alert('输入的PORT有误，请重新输入！');
                    } else {
                        var role = $(this).parents('tr').children().eq(7).text();
                        if(!/^[0-9]+$/.test(role)) {
                            alert('输入的role有误，请重新输入！');
                        }
                    }
                }
            }
            IDs.push(ID); names.push(name); describes.push(describe);
            ruleIDs.push(ruleID); addresss.push(address); PORTs.push(PORT);
            roles.push(role);
        }
    });

    new_data.push(JSON.stringify(IDs));
    new_data.push(JSON.stringify(names)); new_data.push(JSON.stringify(describes));
    new_data.push(JSON.stringify(ruleIDs)); new_data.push(JSON.stringify(addresss));
    new_data.push(JSON.stringify(PORTs)); new_data.push(JSON.stringify(roles));

    var new_data_ID_len = new_data[0].length;
    if (new_data_ID_len > 2) {
        $.post("/set_station", {'data': JSON.stringify(new_data)}, function(res){
            alert(res);
            show_db_sta_data();
            $("input[type='checkbox']").not(this).prop("checked",false);
            getStation();
        });
    } else {
        alert("请先选择要保存的行！")
    }
}

// 删除
function delete_sta_data() {
    var station_IDs = new Array();
    $("input[type='checkbox'][name='station_ID']").each(function() {
        if(this.checked) {
            var station_ID = $(this).parents('tr').children().eq(1).text();
            station_IDs.push(station_ID)
        }
    });

    var station_IDs_len = station_IDs.length;
    if (station_IDs_len > 0) {
        $.post("/delete_station", {'ids': JSON.stringify(station_IDs)}, function(res){
            alert(res);
            show_db_sta_data();
            $("input[type='checkbox']").not(this).prop("checked",false);
            getStation();
        });
    } else {
        alert("请先选择要删除的行！")
    }
}

// 全选按钮
$(function() {
	$("#selectAllSta").bind("click",function(){
		if($(this).prop("checked")){
			$("input[type='checkbox']").not(this).prop("checked",true);
		}else{
			$("input[type='checkbox']").not(this).prop("checked",false);
		}
	});
});