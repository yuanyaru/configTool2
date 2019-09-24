var stationId;
var stationName;
function ykTableClick() {
    var elems = document.getElementsByName("yk");
    for(var i=0;i<elems.length;i++){
        elems[i].addEventListener('click',function(evt){
            clearYkTable();
            // jquery对象
            var elm = $(this).parents("li")["1"];
            stationId = $(elm).children().eq(1).text();
            stationName = $(elm).children().eq(2).text();
            show_yk_table();
        })
    }
}
$(document).ready(function () {
    ykTableClick();
});

function show_yk_table() {
    document.getElementById("sta_name").innerText="---"+ stationName;

    document.getElementById("sta_table").style.display="none";
    document.getElementById("yc_table").style.display="none";
　　document.getElementById("yx_table").style.display="none";
　　document.getElementById("yk_table").style.display="block";
　　document.getElementById("yt_table").style.display="none";
　　document.getElementById("soe_table").style.display="none";

    show_db_yk_data();
}

// 清空表格
function clearYkTable() {
    $("#tBody_yk").text("");
}

// 显示数据库的数据
function show_db_yk_data() {
    $.post("/yk_data", {'stationId': stationId}, function(res){
        clearYkTable();
        var resLen = res.length;
        if (resLen > 2) {
            // 将JSON字符串反序列化成JSON对象
            var res2Json = JSON.parse(res);
            for(var i = 0; i<res2Json.length; i++) {
                str = "<tr><td><input type='checkbox' name='yk_ID'/>"
                + "</td><td name='td3'>" + res2Json[i].ID
                + "</td><td>" + res2Json[i].name
                + "</td><td>" + res2Json[i].describe
                + "</td><td>" + res2Json[i].ASDU
                + "</td><td>" + res2Json[i].wordPos
                + "</td><td>" + res2Json[i].bitPos
                + "</td><td>" + res2Json[i].bitLength
                + "</td><td>" + res2Json[i].EnablePoint
                + "</td><td>" + res2Json[i].EnableValue
                + "</td><td>" + res2Json[i].address+ "</td></tr>";

                // 追加到table中
                $("#tBody_yk").append(str);
            }
        } else {
            alert("数据库为空，没有数据可显示！");
        }
    });
}

// 在表格尾部增添一行
function addYkRow(){
    str = "<tr><td><input type='checkbox' class='i-checks' name='yk_ID'/>"
            + "</td><td name='td3'>"
            + "</td><td>"
            + "</td><td>"
            + "</td><td>"
            + "</td><td>"
            + "</td><td>"
            + "</td><td>"
            + "</td><td>"
            + "</td><td>"
            + "</td><td>" + "</td></tr>";

    // 追加到table中
    $("#tBody_yk").append(str);
}

// 删除尾部添加的行
function deleteYkRow() {
    var i = 0
    $("input[type='checkbox'][name='yk_ID']").each(function() {
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
function set_yk_data() {
    var ids = new Array(); var names = new Array();
    var describes = new Array(); var ASDUs = new Array();
    var wordPoss = new Array(); var bitPoss = new Array();
    var bitLengths = new Array(); var EnablePoints = new Array();
    var EnableValues = new Array(); var addresss = new Array();
    var new_data = new Array();

    $("input[type='checkbox'][name='yk_ID']").each(function() {
        if(this.checked) {
            var id = $(this).parents('tr').children().eq(1).text();
            var name = $(this).parents('tr').children().eq(2).text();
            var describe = $(this).parents('tr').children().eq(3).text();
            var ASDU = $(this).parents('tr').children().eq(4).text();
            var wordPos = $(this).parents('tr').children().eq(5).text();
            var bitPos = $(this).parents('tr').children().eq(6).text();
            var bitLength = $(this).parents('tr').children().eq(7).text();
            var EnablePoint = $(this).parents('tr').children().eq(8).text();
            var EnableValue = $(this).parents('tr').children().eq(9).text();
            var address = $(this).parents('tr').children().eq(10).text();

            ids.push(id); names.push(name); describes.push(describe);
            ASDUs.push(ASDU); wordPoss.push(wordPos); bitPoss.push(bitPos);
            bitLengths.push(bitLength); EnablePoints.push(EnablePoint); EnableValues.push(EnableValue);
            addresss.push(address);
        }
    });

    new_data.push(JSON.stringify(ids)); new_data.push(JSON.stringify(names));
    new_data.push(JSON.stringify(describes)); new_data.push(JSON.stringify(ASDUs));
    new_data.push(JSON.stringify(wordPoss)); new_data.push(JSON.stringify(bitPoss));
    new_data.push(JSON.stringify(bitLengths)); new_data.push(JSON.stringify(EnablePoints));
    new_data.push(JSON.stringify(EnableValues)); new_data.push(JSON.stringify(addresss));

    var new_data_ID_len = new_data[0].length;
    if (new_data_ID_len > 2) {
        $.post("/set_yk", {'data': JSON.stringify(new_data),
                           'stationId': stationId}, function(res){
            alert(res);
            show_db_yk_data();
            $("input[type='checkbox']").not(this).prop("checked",false);
        });
    } else {
        alert("请先选择要保存的行！")
    }
}

// 删除
function delete_yk_data() {
    var yk_IDs = new Array();
    $("input[type='checkbox'][name='yk_ID']").each(function() {
        if(this.checked) {
            var yk_ID = $(this).parents('tr').children().eq(1).text();
            yk_IDs.push(yk_ID)
        }
    });

    var yk_IDs_len = yk_IDs.length;
    if (yk_IDs_len > 0) {
        $.post("/delete_yk", {'ids': JSON.stringify(yk_IDs),
                              'stationId': stationId}, function(res){
            alert(res);
            show_db_yk_data();
            $("input[type='checkbox']").not(this).prop("checked",false);
        });
    } else {
        alert("请先选择要删除的行！")
    }
}

// 全选按钮
$(function() {
	$("#selectAllYk").bind("click",function(){
		if($(this).prop("checked")){
			$("input[type='checkbox']").not(this).prop("checked",true);
		}else{
			$("input[type='checkbox']").not(this).prop("checked",false);
		}
	});
});