var stationId;
var stationName;
function ytTableClick() {
    var elems = document.getElementsByName("yt");
    for(var i=0;i<elems.length;i++){
        elems[i].addEventListener('click',function(evt){
            clearYtTable();
            // jquery对象
            var elm = $(this).parents("li")["1"];
            stationId = $(elm).children().eq(1).text();
            stationName = $(elm).children().eq(2).text();
            show_yt_table();
        })
    }
}

$(document).ready(function () {
    ytTableClick();
    yt_tobody();
});

function show_yt_table() {
    document.getElementById("sta_name").innerText="---"+ stationName;

    document.getElementById("sta_table").style.display="none";
    document.getElementById("yc_table").style.display="none";
　　document.getElementById("yx_table").style.display="none";
　　document.getElementById("yk_table").style.display="none";
    document.getElementById("yt_table").style.display="block";
    document.getElementById("soe_table").style.display="none";

    show_db_yt_data();
}

// 清空表格
function clearYtTable() {
    $("#tBody_yt").text("");
}

// 显示数据库的数据
function show_db_yt_data() {
    $.post("/yt_data", {'stationId': stationId}, function(res){
        clearYtTable();
        var resLen = res.length;
        if (resLen > 2) {
            // 将JSON字符串反序列化成JSON对象
            var res2Json = JSON.parse(res);
            for(var i = 0; i<res2Json.length; i++) {
                str = "<tr><td><input type='checkbox' name='yt_ID'/>"
                + "</td><td name='td4'>" + res2Json[i].id
                + "</td><td>" + res2Json[i].name
                + "</td><td>" + res2Json[i].describe
                + "</td><td>" + res2Json[i].unit
                + "</td><td>" + res2Json[i].kval
                + "</td><td>" + res2Json[i].bval
                + "</td><td>" + res2Json[i].address
                + "</td><td>" + res2Json[i].uplimt
                + "</td><td>" + res2Json[i].downlimt + "</td></tr>";

                // 追加到table中
                $("#tBody_yt").append(str);
            }
        } else {
            document.getElementById("tBody_yt").innerHTML = "没有遥调数据可显示！！！";
        }
    });
}

// 在表格尾部增添一行
function addYtRow(){
    str = "<tr><td><input type='checkbox' class='i-checks' name='yt_ID'/>"
            + "</td><td name='td4'>"
            + "</td><td>"
            + "</td><td>"
            + "</td><td>"
            + "</td><td>"
            + "</td><td>"
            + "</td><td>"
            + "</td><td>"
            + "</td><td>"+ "</td></tr>";

    // 追加到table中
    $("#tBody_yt").append(str);
}

// 删除尾部添加的行
function deleteYtRow() {
    var i = 0
    $("input[type='checkbox'][name='yt_ID']").each(function() {
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
function set_yt_data() {
    var ids = new Array(); var names = new Array();
    var describes = new Array(); var units = new Array();
    var kvals = new Array(); var bvals = new Array();
    var addresss = new Array(); var uplimts = new Array();
    var downlimts = new Array(); var new_data = new Array();

    $("input[type='checkbox'][name='yt_ID']").each(function() {
        if(this.checked) {
            var id = $(this).parents('tr').children().eq(1).text();
            var name = $(this).parents('tr').children().eq(2).text();
            var describe = $(this).parents('tr').children().eq(3).text();
            var unit = $(this).parents('tr').children().eq(4).text();
            var kval = $(this).parents('tr').children().eq(5).text();
            var bval = $(this).parents('tr').children().eq(6).text();
            var address = $(this).parents('tr').children().eq(7).text();
            var uplimt = $(this).parents('tr').children().eq(8).text();
            var downlimt = $(this).parents('tr').children().eq(9).text();

            ids.push(id); names.push(name); describes.push(describe);
            units.push(unit); kvals.push(kval); bvals.push(bval);
            addresss.push(address); uplimts.push(uplimt); downlimts.push(downlimt);
        }
    });

    new_data.push(JSON.stringify(ids)); new_data.push(JSON.stringify(names));
    new_data.push(JSON.stringify(describes)); new_data.push(JSON.stringify(units));
    new_data.push(JSON.stringify(kvals)); new_data.push(JSON.stringify(bvals));
    new_data.push(JSON.stringify(addresss)); new_data.push(JSON.stringify(uplimts));
    new_data.push(JSON.stringify(downlimts));

    var new_data_ID_len = new_data[0].length;
    if (new_data_ID_len > 2) {
        $.post("/set_yt", {'data': JSON.stringify(new_data),
                           'stationId': stationId}, function(res){
            alert(res);
            show_db_yt_data();
            $("input[type='checkbox']").not(this).prop("checked",false);
        });
    } else {
        alert("请先选择要保存的行！")
    }
}

// 删除
function delete_yt_data() {
    var yt_IDs = new Array();
    $("input[type='checkbox'][name='yt_ID']").each(function() {
        if(this.checked) {
            var yt_ID = $(this).parents('tr').children().eq(1).text();
            yt_IDs.push(yt_ID)
        }
    });

    var yt_IDs_len = yt_IDs.length;
    if (yt_IDs_len > 0) {
        if(confirm("确认要删除吗？")) {
            $.post("/delete_yt", {
                'ids': JSON.stringify(yt_IDs),
                'stationId': stationId
            }, function (res) {
                // alert(res);
                show_db_yt_data();
                $("input[type='checkbox']").not(this).prop("checked", false);
            });
        } else {
            $("input[type='checkbox']").not(this).prop("checked", false);
        }
    } else {
        alert("请先选择要删除的行！")
    }
}

// 全选按钮
$(function() {
	$("#selectAllYt").bind("click",function(){
		if($(this).prop("checked")){
			$("input[type='checkbox']").not(this).prop("checked",true);
		}else{
			$("input[type='checkbox']").not(this).prop("checked",false);
		}
	});
});