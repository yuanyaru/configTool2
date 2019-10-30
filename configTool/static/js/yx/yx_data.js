var stationId;
var stationName;
function yxTableClick() {
    var elems = document.getElementsByName("yx");
    for(var i=0;i<elems.length;i++){
        elems[i].addEventListener('click',function(evt){
            clearYxTable();
            // jquery对象
            var elm = $(this).parents("li")["1"];
            stationId = $(elm).children().eq(1).text();
            stationName = $(elm).children().eq(2).text();
            show_yx_table();
        })
    }
}

$(document).ready(function () {
    var ss=document.getElementById('time').getElementsByTagName('span');
    function changeTime() {
        var time = new Date();
        ss[0].innerHTML = time.getFullYear().toString();
        ss[1].innerHTML = time.getMonth()+1;
        ss[2].innerHTML = time.getDate().toString();
        ss[3].innerHTML = time.getHours().toString();
        ss[4].innerHTML = time.getMinutes().toString();
        ss[5].innerHTML = time.getSeconds().toString();
    }
    changeTime();
    setInterval(function(){
        changeTime();
    },1000)

    yxTableClick();

    $("#contect").click(function () {
        window.confirm("感谢您的使用 ！\n" +
                        "如果您在使用过程中有任何疑问，请联系平台研发部yyr !");
    });

    $("#about").click(function () {
        window.confirm("本产品：点表配置工具\n" +
                       "版   本：v1.0.0");
    });

    $("#browser").treeview();

    var monitoring_url = document.getElementById("monitoring_id");
    monitoring_url.addEventListener("click", function () {
        url_value = "http://" + setURL().monitoring_IP + ":" + setURL().monitoring_port + "/THPBuilder/viewer.html";
        monitoring_url.setAttribute("href", url_value);
    })
});

function show_yx_table() {
    document.getElementById("sta_name").innerText="---"+ stationName;

    document.getElementById("sta_table").style.display="none";
    document.getElementById("yc_table").style.display="none";
　　document.getElementById("yx_table").style.display="block";
    document.getElementById("yk_table").style.display="none";
    document.getElementById("yt_table").style.display="none";
    document.getElementById("soe_table").style.display="none";

    show_db_yx_data();
}

// 清空表格
function clearYxTable() {
    $("#tBody_yx").text("");
}

// 显示数据库的数据
function show_db_yx_data() {
    $.post("/yx_data", {'stationId': stationId}, function(res){
        clearYxTable();
        var resLen = res.length;
        if (resLen > 2) {
            // 将JSON字符串反序列化成JSON对象
            var res2Json = JSON.parse(res);
            for(var i = 0; i<res2Json.length; i++) {
                str = "<tr><td><input type='checkbox' name='yx_ID'/>"
                + "</td><td name='td2'>" + res2Json[i].ID
                + "</td><td>" + res2Json[i].name
                + "</td><td>" + res2Json[i].describe
                + "</td><td>" + res2Json[i].ASDU
                + "</td><td>" + res2Json[i].wordPos
                + "</td><td>" + res2Json[i].bitPos
                + "</td><td>" + res2Json[i].bitLength
                + "</td><td>" + res2Json[i].LinkPoint1
                + "</td><td>" + res2Json[i].LinkPoint2
                + "</td><td>" + res2Json[i].OneToZero
                + "</td><td>" + res2Json[i].ZeroToOne
                + "</td><td>" + res2Json[i].address+ "</td></tr>";

                // 追加到table中
                $("#tBody_yx").append(str);
            }
        } else {
            alert("数据库为空，没有数据可显示！");
        }
    });
}

// 在表格尾部增添一行
function addYxRow(){
    str = "<tr><td><input type='checkbox' class='i-checks' name='yx_ID'/>"
            + "</td><td name='td2'>"
            + "</td><td>"
            + "</td><td>"
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
    $("#tBody_yx").append(str);
}

// 删除尾部添加的行
function deleteYxRow() {
    var i = 0
    $("input[type='checkbox'][name='yx_ID']").each(function() {
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
function set_yx_data() {
    var ids = new Array(); var names = new Array();
    var describes = new Array(); var ASDUs = new Array();
    var wordPoss = new Array(); var bitPoss = new Array();
    var bitLengths = new Array(); var LinkPoint1s = new Array();
    var LinkPoint2s = new Array(); var OneToZeros = new Array();
    var ZeroToOnes = new Array(); var addresss = new Array();
    var new_data = new Array();

    $("input[type='checkbox'][name='yx_ID']").each(function() {
        if(this.checked) {
            var id = $(this).parents('tr').children().eq(1).text();
            var name = $(this).parents('tr').children().eq(2).text();
            var describe = $(this).parents('tr').children().eq(3).text();
            var ASDU = $(this).parents('tr').children().eq(4).text();
            var wordPos = $(this).parents('tr').children().eq(5).text();
            var bitPos = $(this).parents('tr').children().eq(6).text();
            var bitLength = $(this).parents('tr').children().eq(7).text();
            var LinkPoint1 = $(this).parents('tr').children().eq(8).text();
            var LinkPoint2 = $(this).parents('tr').children().eq(9).text();
            var OneToZero = $(this).parents('tr').children().eq(10).text();
            var ZeroToOne = $(this).parents('tr').children().eq(11).text();
            var address = $(this).parents('tr').children().eq(12).text();

            ids.push(id); names.push(name); describes.push(describe);
            ASDUs.push(ASDU); wordPoss.push(wordPos); bitPoss.push(bitPos);
            bitLengths.push(bitLength); LinkPoint1s.push(LinkPoint1); LinkPoint2s.push(LinkPoint2);
            OneToZeros.push(OneToZero); ZeroToOnes.push(ZeroToOne); addresss.push(address);
        }
    });

    new_data.push(JSON.stringify(ids)); new_data.push(JSON.stringify(names));
    new_data.push(JSON.stringify(describes)); new_data.push(JSON.stringify(ASDUs));
    new_data.push(JSON.stringify(wordPoss)); new_data.push(JSON.stringify(bitPoss));
    new_data.push(JSON.stringify(bitLengths)); new_data.push(JSON.stringify(LinkPoint1s));
    new_data.push(JSON.stringify(LinkPoint2s)); new_data.push(JSON.stringify(OneToZeros));
    new_data.push(JSON.stringify(ZeroToOnes)); new_data.push(JSON.stringify(addresss));

    var new_data_ID_len = new_data[0].length;
    if (new_data_ID_len > 2) {
        $.post("/set_yx", {'data': JSON.stringify(new_data),
                           'stationId': stationId}, function(res){
            alert(res);
            show_db_yx_data();
            $("input[type='checkbox']").not(this).prop("checked",false);
        });
    } else {
        alert("请先选择要保存的行！")
    }
}

// 删除
function delete_yx_data() {
    var yx_IDs = new Array();
    $("input[type='checkbox'][name='yx_ID']").each(function() {
        if(this.checked) {
            var yx_ID = $(this).parents('tr').children().eq(1).text();
            yx_IDs.push(yx_ID)
        }
    });

    var yx_IDs_len = yx_IDs.length;
    if (yx_IDs_len > 0) {
        if(confirm("确认要删除吗？")) {
            $.post("/delete_yx", {
                'ids': JSON.stringify(yx_IDs),
                'stationId': stationId
            }, function (res) {
                // alert(res);
                show_db_yx_data();
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
	$("#selectAllYx").bind("click",function(){
		if($(this).prop("checked")){
			$("input[type='checkbox']").not(this).prop("checked",true);
		}else{
			$("input[type='checkbox']").not(this).prop("checked",false);
		}
	});
});