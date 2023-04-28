status1 = [
	{'id':1, 'text': "����"},
	{'id':2, 'text': "����"}
];

business = [
	{'id':1,'text': "����"},
	{'id':2,'text': "�ܽ���"},
	{'id':3,'text': "����Ѹ"} 
];


function CheckAll(mode,tb){
	//1.ѡ��checkbox������Ѿ�����༭ģʽ����ѡ���н���༭ģʽ��
	$(tb).children().each(function(){
			//$(this)����ѭ��������,ÿһ��tr,ÿһ������
			//����Ҫʹ��forѭ����tr�ó�������Ϊ�кܶ��tr
			var tr=$(this);
			var isChecked = $(this).find(':checkbox').prop('checked');
			if(isChecked == true){
			}else{
				$(this).find(':checkbox').prop('checked',true);
				//����Ѿ�����༭ģʽ����ѡ���б�Ϊ�༭״̬
				var isEditMode = $(mode).hasClass('editing');
				if(isEditMode){
					RowIntoEditMode(tr)
				}
			}
	})
}


function CheckReverse(mode,tb){
	//�Ƿ����༭ģʽ
	isEditMode = $(mode).hasClass('editing');
	if(isEditMode){
		//��������tr
		$(tb).children().each(function(){
			var tr = $(this)
			var check_box = tr.children().first().find(':checkbox');
			if(check_box.prop('checked')){
				check_box.prop('checked',false);
				RowOutEditMode(tr);
			}else{
					check_box.prop('checked',true);
					RowIntoEditMode(tr);
			}
		})
	}else{
				$(tb).children().each(function(){
					var tr=$(this);
					var check_box =tr.children().first().find(":checkbox");
					if(check_box.prop('checked')){
						check_box.prop('checked',false);
					}else{
						check_box.prop('checked',true);
					}
				})
			}
}


function CheckCancel(mode,tb){
		//1.ȡ��ѡ��checkbox
		//2.����Ѿ�����༭ģʽ����ѡ�����˳��༭״̬
	$(tb).children().each(function(){
		var tr = $(this)
		var isChecked = tr.find(":checkbox").prop('checked');
		if(isChecked == true){
			tr.find(":checkbox").prop('checked',false);
			var isEditing = $(mode).hasClass('editing');
			if(isEditing){
				//��ǰ�У��˳��༭ģʽ
				RowOutEditMode(tr);
			}
		}
		
	})
}

function EditMode(ths,tb){
	var isEditing = $(ths).hasClass('editing');
	if(isEditing){
			$(ths).removeClass('editing');
			$(ths).text('����༭ģʽ');
			$(tb).children().each(function(){
				var tr= $(this);
				var isChecked = tr.find(":checkbox").prop('checked');
				if(isChecked){
					RowOutEditMode(tr);
				}
			})
	}else{
			$(ths).addClass('editing');
			$(ths).text('�˳��༭ģʽ')
			$(tb).children().each(function(){
				var tr = $(this);
				var isChecked = tr.find(":checkbox").prop('checked');
				if(isChecked == true){
					RowIntoEditMode(tr);
				}
			})
	}
}


function RowIntoEditMode(tr){
	tr.children().each(function(){
	var td=$(this);
	if(td.attr('edit') == 'True'){
		if(td.attr('edit-type') == "select"){
			var all_values = window[td.attr('global-key')];
			var select_val = td.attr('select_val');
			select_val = parseInt(select_val);
			var options = "";
			$.each(all_values, function(index, value){
				if(select_val == value.id){
					options += "<option selected='selected'>" + value.text + "</option>"
				}else{
						options += "<option>" + value.text + "</option>"
				}
			})
			var temp = "<select>" + options + "</select>";
			td.html(temp);	
		}else{
			
				var text = td.text();
				var temp = "<input type='text' value='" +text+ "'/>";
				td.html(temp);
			}
		}
	})
}

function RowOutEditMode(tr){
		tr.children().each(function(){
					var td=$(this);
					if(td.attr('edit') == 'True'){
						var inp =td.children();
						var input_value = inp.val();
						console.log(inp)
						td.text(input_value);
					}
				})
}

$(function(){
	$('#tb').find(':checkbox').click(function(){
		var tr=$(this).parent().parent();
		if($('#edit_mode').hasClass('editing')){
			if($(this).prop('checked')){
				RowIntoEditMode(tr);
			}else{
				RowOutEditMode(tr);
				//console.log($(this).prop('checked'))
			}
		}
	})
})