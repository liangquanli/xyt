
<!--失败的框-->
function modal2(data){
	var div;
	div = document.createElement('div');	
	div.innerHTML='<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"><div class="modal-dialog"><div class="modal-content"style="color:#ff5340;"><div class="modal-body">在这里添加一些文本</div></div></div>';	
	document.body.appendChild(div, document.body.childNodes[0]);
	$('#myModal').modal('show');	
	$(".modal-body").html(data);
	/*setTimeout(function(){
		$('#myModal').modal('hide');	
	},3000);*/
}
<!--成功的框-->
function modal3(data){
	var div;
	div = document.createElement('div');	
	div.innerHTML='<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"><div class="modal-dialog"><div class="modal-content"style="color:#f8595c;"><div class="modal-body">在这里添加一些文本</div></div></div>';	
	document.body.appendChild(div, document.body.childNodes[0]);
	$('#myModal').modal('show');	
	$(".modal-body").html(data);
	setTimeout(function(){
		$('#myModal').modal('hide');	
	},3000);
}
<!--删除的框-->		
function modal_shanchu(data){
	var div;
	div = document.createElement('div');	
	div.innerHTML='<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"><div class="modal-dialog"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-hidden="true"> &times; </button><h4 class="modal-title" id="myModalLabel">慧育儿 </h4></div><div class="modal-body">在这里添加一些文本</div><div class="modal-footer">  <div class="row "> <div class="col-xs-6 text-left"><button type="button" class="btn btn-pink form-control btn_shi" >是</button></div><div class="col-xs-6 text-right" ><button type="button" class="btn btn-default form-control" data-dismiss="modal">否</button></div></div> </div> </div></div></div></div>';	
	document.body.appendChild(div, document.body.childNodes[0]);
	$('#myModal').modal('show');	
	$(".modal-body").html(data);	
}	
