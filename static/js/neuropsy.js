function isValidDate(str) {
    console.log(str, Date.parse(str))
  return !isNaN(Date.parse(str));
}

function ajaxError(element, errmsg, xhr, func) {
     $('#'+element).html('<div class="alert alert-primary alert-dismissible fade show" role="alert"><strong>' + errmsg + '</strong><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">×</span></button></div>');
    console.log(func + ": " + xhr.status + ": " + xhr.responseText);
}


