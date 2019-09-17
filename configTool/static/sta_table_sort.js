function sortNumberAS(a, b) {
    return a - b
}

function sortNumberDesc(a, b){
    return b - a
}

function SortTable_sta(obj){
    var td0s=document.getElementsByName("td0");
    var tdArray0=[];

    for(var i=0;i<td0s.length;i++){
        tdArray0.push(parseInt(td0s[i].innerHTML));
    }

    var tds=document.getElementsByName("td"+obj.id.substr(2,1));
    var columnArray=[];
    for(var i=0;i<tds.length;i++){
        columnArray.push(parseInt(tds[i].innerHTML));
    }
    var orginArray=[];
    for(var i=0;i<columnArray.length;i++){
        orginArray.push(columnArray[i]);
    }
    if(obj.className=="as"){
        columnArray.sort(sortNumberAS);               //排序后的新值
        obj.className="desc";
    }else{
        columnArray.sort(sortNumberDesc);             //排序后的新值
        obj.className="as";
    }

    for(var i=0;i<columnArray.length;i++){
        for(var j=0;j<orginArray.length;j++){
            if(orginArray[j]==columnArray[i]){
                document.getElementsByName("td0")[i].innerHTML=tdArray0[j];
                orginArray[j]=null;
                break;
            }
        }
    }
}