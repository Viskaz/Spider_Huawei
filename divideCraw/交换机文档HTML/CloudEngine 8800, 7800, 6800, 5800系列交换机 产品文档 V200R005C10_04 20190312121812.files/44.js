var navTitleEn=" Related Topics";
var navTitleZh=" 相关推荐";

var idRelatedTopicsTitle="idNavTitle";
var idRelatedTopicsBody="idRelatedTopicsBody";
var idObjectRelatedTopics="idObjectRelatedTopics";

var objectRelatedTopics = null;
var hasInitedObjectEle = false;

$$(document).ready(function(){
	var navTitleEle = document.createElement("div");
	navTitleEle.setAttribute("id",idRelatedTopicsTitle);
	navTitleEle.setAttribute("class","srNavTitle");
	navTitleEle.setAttribute("style","display:block");
	var lang = $$("meta[name='DC.Language']").get(0).content;
	var navTitle = "";
	if(lang!=null && lang=='en-us'){
		navTitle = navTitleEn;
	}else{
		navTitle = navTitleZh;
	}
	var src = $$("script[src$='44.files/2.js']").get(0).src+"http://127.0.0.1:7890/icon-arrowrt.gif";
	navTitleEle.innerHTML = '<img src="'+src+'" id="searchRecommendButton"></img><a href="javascript:void(0);" style="text-decoration:none">'+navTitle+'</a>';
	document.body.appendChild(navTitleEle);
	$$("#"+idRelatedTopicsTitle).addClass("srNavTitle");
	$$("#"+idRelatedTopicsBody).addClass("srNavBody");
	$$("#"+idRelatedTopicsBody).hide(0);
	$$("#"+idRelatedTopicsTitle).click(function(){doSearchRecommendShow(this);});
	
	objectRelatedTopics=$$("#"+idObjectRelatedTopics);
	objectRelatedTopics.attr("width","400px");
	objectRelatedTopics.attr("height","600px");
	objectRelatedTopics.detach();
});
function doSearchRecommendShow(_self){
	var ele = $$('#'+idRelatedTopicsBody);
	var img = $$('#'+"searchRecommendButton");
	var display = ele.attr("display");
	
	if(display==null || display=="none" || display==""){	
		$$("#"+idRelatedTopicsBody).show(600,function(){
				img.attr("src",img.attr("src").replace(http://127.0.0.1:7890/arrowrt.gif/i,"http://127.0.0.1:7890/pages/31180APE/04/31180APE/04/resources/public_sys-resources/arrowdn.gif"));
				ele.attr("display","block");
			}
		);

	}else{
		$$("#"+idRelatedTopicsBody).hide(600,function(){
				img.attr("src",img.attr("src").replace(http://127.0.0.1:7890/arrowdn.gif/i,"http://127.0.0.1:7890/pages/31180APE/04/31180APE/04/resources/public_sys-resources/arrowrt.gif"));
				ele.attr("display","none");
			}
		);
	}
}