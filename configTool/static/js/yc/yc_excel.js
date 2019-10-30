function selectYcFile() {
    document.getElementById('ycfile').click();
}

function readWorkbook_yc(workbook) {
	var sheetNames = workbook.SheetNames; // 工作表名称集合
	var worksheet = workbook.Sheets[sheetNames[0]]; // 这里我们只读取第一张sheet
	var csv = XLSX.utils.sheet_to_csv(worksheet);
	var rows = csv.split('\n');
	delete rows[0];
	rows.pop(); // 最后一行没用的
    clearYcTable();
	rows.forEach(function(row) {
	    var html = "";
		var columns = row.split(',');
		// console.log(columns);
		html += "<tr><td><input type='checkbox' class='i-checks' name='yc_ID'/>";
		columns.forEach(function(column) {
			html += '<td>'+column+'</td>';
		});
		html += '</td></tr>';
		$("#tBody_yc").append(html);
	});
}

$(function() {
	document.getElementById('ycfile').addEventListener('change', function(e) {
		var files = e.target.files;
		if(files.length == 0) return;
		var f = files[0];
		if(!/\.xlsx$/g.test(f.name)) {
			alert('仅支持读取xlsx格式！');
			return;
		}
		readWorkbookFromLocalFile(f, function(workbook) {
			readWorkbook_yc(workbook);
		});
	});
});

// 把table数据导出到excel中
function exportExcel_yc() {
    var sheet = XLSX.utils.table_to_sheet($('table')[1]);
    openDownloadDialog(sheet2blob(sheet), '导出.xlsx');
}
