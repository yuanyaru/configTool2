function readWorkbook_sta(workbook) {
	var sheetNames = workbook.SheetNames; // 工作表名称集合
	var worksheet = workbook.Sheets[sheetNames[0]]; // 这里我们只读取第一张sheet
	var csv = XLSX.utils.sheet_to_csv(worksheet);
	var rows = csv.split('\n');
	delete rows[0];
	rows.pop(); // 最后一行没用的
    clearStaTable();
	rows.forEach(function(row) {
	    var html = "";
		var columns = row.split(',');
		html += "<tr><td><input type='checkbox' class='i-checks' name='station_ID'/>";
		columns.forEach(function(column) {
			html += '<td>'+column+'</td>';
		});
		html += '</td></tr>';
		$("#tBody_sta").append(html);
	});
}

function loadstaData(e) {
	var files = e.target.files;
	if(files.length == 0) return;
	var f = files[0];
	if(!/\.xlsx$/g.test(f.name)) {
		alert('仅支持读取xlsx格式！');
		return;
	}
	document.getElementById("tBody_sta").innerHTML = "<span style='font-size:22px; color:red;'>正在努力加载数据！！！</span>";
	readWorkbookFromLocalFile(f, function(workbook) {
		readWorkbook_sta(workbook);
	});
}

// 局部刷新
function staload() {
    $("#staload").load(location.href+" #staload");
}

function selectStaFile() {
	staload();
	document.getElementById('stafile').click();
	document.getElementById('stafile').addEventListener('change', loadstaData);
}

// 把table数据导出到excel中
function exportExcel_sta() {
    var sheet = XLSX.utils.table_to_sheet($('table')[0]);
    openDownloadDialog(sheet2blob(sheet), 'station.xlsx');
}
