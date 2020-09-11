// window.onload = function(){
function yc_tobody() {
    var oTop = document.getElementById("yc_to_top");
    //获取可视区域宽度
    var screenw = document.documentElement.clientWidth || document.getElementById("tBody_yc").clientWidth;
    //获取可视区域高度
    var screenh = document.documentElement.clientHeight || document.getElementById("tBody_yc").clientHeight;
    //确定按钮距离屏幕可视区域左边的位置
    oTop.style.left = screenw - oTop.offsetWidth +"px";
    oTop.style.top = screenh - oTop.offsetHeight +"px";
    document.getElementById("tBody_yc").onscroll = function(){
        //获取滚动条的滚动高度
        var scrolltop = document.documentElement.scrollTop || document.getElementById("tBody_yc").scrollTop;
        if(scrolltop>0){
            // alert("a");
            document.getElementById("yc_to_top").style.display="block";
            oTop.style.top = screenh - oTop.offsetHeight + scrolltop +"px";
            oTop.style.left = screenw - oTop.offsetWidth +"px";
        } else {
            document.getElementById("yc_to_top").style.display="none";
        }
    };
    oTop.onclick = function(){
        document.documentElement.scrollTop = document.getElementById("tBody_yc").scrollTop =0;
    }
};