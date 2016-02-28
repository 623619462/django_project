// JavaScript Document
function checkForm() { //提交时确定提示 
	if (window.confirm("Are you sure you want to sumbit this form?")){
		return true;
}
		return false;
}
function resetForm() { //重置时确定提示 
	if (window.confirm("Are you sure you want to reset this form?")){
		return true;
}
		return false;
}