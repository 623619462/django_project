$(function() {
  $('#video-conf-form').validator({
    onValid: function(validity) {
      $(validity.field).closest('.am-form-group').find('.am-alert').hide();
    },

    onInValid: function(validity) {
      var $field = $(validity.field);
      var $group = $field.closest('.am-form-group');
      var $alert = $group.find('.am-alert');
      // 使用自定义的提示信息 或 插件内置的提示信息
      var msg = $field.data('validationMessage') || this.getValidationMessage(validity);

      if (!$alert.length) {
        $alert = $('<div class="am-alert am-alert-danger"></div>').hide().
          appendTo($group);
      }

      $alert.html(msg).show();
    }
  });
  $('#add-conf-form').validator({
    onValid: function(validity) {
      $(validity.field).closest('.am-form-group').find('.am-alert').hide();
    },

    onInValid: function(validity) {
      var $field = $(validity.field);
      var $group = $field.closest('.am-form-group');
      var $alert = $group.find('.am-alert');
      // 使用自定义的提示信息 或 插件内置的提示信息
      var msg = $field.data('validationMessage') || this.getValidationMessage(validity);

      if (!$alert.length) {
        $alert = $('<div class="am-alert am-alert-danger"></div>').hide().
          appendTo($group);
      }

      $alert.html(msg).show();
    }
  });
  $('#modify-conf').on('click', function() {
    $('#modify-prompt').modal({
      relatedTarget: this,
      onConfirm: function(e) {
        if($('#video-conf-form').validator('isFormValid')){
        	alert('你输入的是：' + e.data[2]  || '');
			$.ajax({
				url:"http://127.0.0.1:8000/reconf/",
				data:{
					"cameraId" : e.data[0],
					"cameraName" : e.data[1],
					"algorithm" : e.data[2],
					"cameraAddress" : e.data[3],
					"addressPrefix" : e.data[4],
					"addressSuffix" : e.data[5]
				},
				type:"post",
				dataType:'json',
				success:function(data) {
					alert(data);
					window.location.reload();
				},
				error : function(){
					alert("异常！");
				}
			});
        }else{
            alert('请按照要求输入！');
        }
      },
      onCancel: function(e) {
        
      }
    });
  });
  $('#delete-conf').on('click', function() {
    $('#delete-prompt').modal({
      relatedTarget: this,
      onConfirm: function(e) {
          $.ajax({
			  url:"http://127.0.0.1:8000/delconf/",
			  data:{
				"cameraId" : e.data,  
			  },
			  type:"post",
			  dataType:'json',
			  success:function(data) {
					alert(data);
					window.location.reload();
				},
			  error : function(){
					alert("异常！");
				}
		  })
      },
      onCancel: function(e) {
        
      }
    });
  });
  $('#add-conf').on('click', function() {
    $('#add-prompt').modal({
      relatedTarget: this,
      onConfirm: function(e) {
        	if($('#add-conf-form').validator('isFormValid')){
        	alert('你输入的是：' + e.data[1]  || '');
			$.ajax({
				url:"http://127.0.0.1:8000/addconf/",
				data:{
					"cameraName" : e.data[0],
					"algorithm" : e.data[1],
					"cameraAddress" : e.data[2],
					"addressPrefix" : e.data[3],
					"addressSuffix" : e.data[4]
				},
				type:"post",
				dataType:'json',
				success:function(data) {
					alert(data);
					window.location.reload();
				},
				error : function(){
					alert("异常！");
				}
			});
        }else{
            alert('请按照要求输入！');
        }
      },
      onCancel: function(e) {
        
      }
    });
  });
});
