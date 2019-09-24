var stationId;
var stationName;
function soeTableClick() {
    var elems = document.getElementsByName("soe");
    for(var i=0;i<elems.length;i++){
        elems[i].addEventListener('click',function(evt){
            clearSoeTable();
            // jquery对象
            var elm = $(this).parents("li")["1"];
            stationId = $(elm).children().eq(1).text();
            stationName = $(elm).children().eq(2).text();
            show_soe_table();
        })
    }
}

$(document).ready(function () {
    soeTableClick();
});

function show_soe_table() {
    document.getElementById("sta_name").innerText="---"+ stationName;

    document.getElementById("sta_table").style.display="none";
    document.getElementById("yc_table").style.display="none";
　　document.getElementById("yx_table").style.display="none";
　　document.getElementById("yk_table").style.display="none";
    document.getElementById("yt_table").style.display="none";
    document.getElementById("soe_table").style.display="block";

    show_db_soe_data();
}

// 清空表格
function clearSoeTable() {
    $("#tBody_soe").text("");
}

// 显示数据库的数据
function show_db_soe_data() {
    $.post("/soe_data", {'stationId': stationId}, function(res){
        clearSoeTable();
        var resLen = res.length;
        if (resLen > 2) {
            // 将JSON字符串反序列化成JSON对象
            var res2Json = JSON.parse(res);
            for(var i = 0; i<res2Json.length; i++) {
                str = "<tr><td><input type='checkbox' name='soe_ID'/>"
                + "</td><td name='td5'>" + res2Json[i].ID
                + "</td><td>" + res2Json[i].name
                + "</td><td>" + res2Json[i].describe
                + "</td><td>" + res2Json[i].level + "</td></tr>";

                // 追加到table中
                $("#tBody_soe").append(str);
            }
        } else {
            alert("数据库为空，没有数据可显示！");
        }
    });
}

// 在表格尾部增添一行
function addSoeRow(){
    str = "<tr><td><input type='checkbox' class='i-checks' name='soe_ID'/>"
            + "</td><td name='td5'>"
            + "</td><td>"
            + "</td><td>"
            + "</td><td>"+ "</td></tr>";

    // 追加到table中
    $("#tBody_soe").append(str);
}

// 删除尾部添加的行
function deleteSoeRow() {
    var i = 0
    $("input[type='checkbox'][name='soe_ID']").each(function() {
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

// 添加、修改
function set_soe_data() {
    var IDs = new Array(); var names = new Array();
    var describes = new Array(); var levels = new Array();
    var new_data = new Array();

    $("input[type='checkbox'][name='soe_ID']").each(function() {
        if(this.checked) {
            var ID = $(this).parents('tr').children().eq(1).text();
            var name = $(this).parents('tr').children().eq(2).text();
            var describe = $(this).parents('tr').children().eq(3).text();
            var level = $(this).parents('tr').children().eq(4).text();

            IDs.push(ID); names.push(name);
            describes.push(describe); levels.push(level);
        }
    });

    new_data.push(JSON.stringify(IDs)); new_data.push(JSON.stringify(names));
    new_data.push(JSON.stringify(describes)); new_data.push(JSON.stringify(levels));

    var new_data_ID_len = new_data[0].length;
    if (new_data_ID_len > 2) {
        $.post("/set_soe", {'data': JSON.stringify(new_data),
                           'stationId': stationId}, function(res){
            alert(res);
            show_db_soe_data();
            $("input[type='checkbox']").not(this).prop("checked",false);
        });
    } else {
        alert("请先选择要保存的行！")
    }
}

// 删除
function delete_soe_data() {
    var soe_IDs = new Array();
    $("input[type='checkbox'][name='soe_ID']").each(function() {
        if(this.checked) {
            var soe_ID = $(this).parents('tr').children().eq(1).text();
            soe_IDs.push(soe_ID)
        }
    });

    var soe_IDs_len = soe_IDs.length;
    if (soe_IDs_len > 0) {
        $.post("/delete_soe", {'ids': JSON.stringify(soe_IDs),
                              'stationId': stationId}, function(res){
            alert(res);
            show_db_soe_data();
            $("input[type='checkbox']").not(this).prop("checked",false);
        });
    } else {
        alert("请先选择要删除的行！")
    }
}

// 全选按钮
$(function() {
	$("#selectAllSoe").bind("click",function(){
		if($(this).prop("checked")){
			$("input[type='checkbox']").not(this).prop("checked",true);
		}else{
			$("input[type='checkbox']").not(this).prop("checked",false);
		}
	});
});