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
        	alert('你输入的是：' + e.data  || '');
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
        	alert('你的是删除：' + e.data  || '');
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
        	alert('你输入的是：' + e.data  || '');
        }else{
            alert('请按照要求输入！');
        }
      },
      onCancel: function(e) {
        
      }
    });
  });
});