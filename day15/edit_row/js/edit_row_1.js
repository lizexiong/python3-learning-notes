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
					tr.children().each(function(){
						var td=$(this);
						if(td.attr('edit') == 'True'){
							var text = td.text();
							var temp = "<input type='text' value='" +text+ "'/>";
							td.html(temp);
						}
					})
				}
			}
	})
}

function EditMode(ths,tb){
	var isEditing = $(ths).hasClass('editing');
	if(isEditing){
			$(ths).removeClass('editing');
	}else{
			$(ths).addClass('editing');
	}
}