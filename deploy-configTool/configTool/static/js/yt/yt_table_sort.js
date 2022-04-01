function SortTable_yt(obj){
    var td4s=document.getElementsByName("td4");
    var tdArray4=[];

    for(var i=0;i<td4s.length;i++){
        tdArray4.push(parseInt(td4s[i].innerHTML));
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
                document.getElementsByName("td4")[i].innerHTML=tdArray4[j];
                orginArray[j]=null;
                break;
            }
        }
    }
}