function readWorkbook_soe(workbook) {
	var sheetNames = workbook.SheetNames; // 工作表名称集合
	var worksheet = workbook.Sheets[sheetNames[0]]; // 这里我们只读取第一张sheet
	var csv = XLSX.utils.sheet_to_csv(worksheet);
	var rows = csv.split('\n');
	delete rows[0];
	rows.pop(); // 最后一行没用的
    clearSoeTable();
	rows.forEach(function(row) {
	    var html = "";
		var columns = row.split(',');
		// console.log(columns);
		html += "<tr><td><input type='checkbox' class='i-checks' name='soe_ID'/>";
		columns.forEach(function(column) {
			html += '<td>'+column+'</td>';
		});
		html += '</td></tr>';
		$("#tBody_soe").append(html);
	});
}

function loadsoeData(e) {
	var files = e.target.files;
	if(files.length == 0) return;
	var f = files[0];
	if(!/\.xlsx$/g.test(f.name)) {
		alert('仅支持读取xlsx格式！');
		return;
	}
	readWorkbookFromLocalFile(f, function(workbook) {
		readWorkbook_soe(workbook);
	});
}

// 局部刷新
function soeload() {
    $("#soeload").load(location.href+" #soeload");
}

function selectSoeFile() {
	soeload();
	document.getElementById('soefile').click();
	document.getElementById('soefile').addEventListener('change', loadsoeData);
}

// 把table数据导出到excel中
function exportExcel_soe() {
    var sheet = XLSX.utils.table_to_sheet($('table')[5]);
    openDownloadDialog(sheet2blob(sheet), 'soe.xlsx');
}
