status = [
	{'id':1,'text':"����"},
	{'id':2,'text':"����"}
];

business = [
	{'id'=1,'text'="����"},
	{'id'=2,'text'='�ܽ���'},
	{'id'=3,'text'='����Ѹ'}
]


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
					RowIntoEditModeEx(tr)
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
					RowIntoEditModeEx(tr);
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
				}else{
					tr.children().each(function(){
						var td=$(this);
						if(td.attr('edit') == 'True'){
							//�������children()ʲô��û�л�ȡ������ô�㲻��ִ�У������ǰ�ֵ����Ϊ��
							//����Ҳ������һ��Сbug�ɡ�
							ii = td.find('input').length;
							console.log(ii)
							if(ii>0){
								var inp = td.children().val();
								td.text(inp);
							}
						}
					})
				}
			})
	}else{
			$(ths).addClass('editing');
			$(ths).text('�˳��༭ģʽ')
			$(tb).children().each(function(){
				var tr = $(this);
				var isChecked = tr.find(":checkbox").prop('checked');
				if(isChecked == true){
					RowIntoEditModeEx(tr);
				}
			})
	}
}

function RowIntoEditMode(tr){
			tr.children().each(function(){
				var td=$(this);
				if(td.attr('edit') == 'True'){
						var text = td.text();
						var temp =  "<input type='text' value='" +text+ "'/>";
						td.html(temp);
				}
			})
}

function RowIntoEditModeEx(tr){
	tr.children().each(function(){
	var td=$(this);
	if(td.attr('edit') == 'True'){
			// ii = td.children().length;
			ii = td.find('input').length;
			if(ii>0){
				var inp = td.children(':first'); 
				var input_value=inp.val();
				td.text(input_value);
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
						td.text(input_value);
					}
				})
}


