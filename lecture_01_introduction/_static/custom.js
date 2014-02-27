function getURLParameter(name) {
  var match = RegExp(name + '=' + '(.+?)(&|$)').exec(location.search);

  if (match)
  {
    return decodeURI(match[1]);
  }
  else
  {
    return null;
  }
}

function print() {
    $("body").css("background", "none");
    $("article").removeClass("far-past");
    $("article").removeClass("past");
    $("article").removeClass("current");
    $("article").removeClass("next");
    $("article").removeClass("far-next");
    $("*.to-build").removeClass("to-build");
    $("article").css("display", "block");
    $("article").css("top", "0");
    $("article").css("left", "0");
    $("article").css("margin", "0 0 9em 0");
    $("article").css("position", "relative");
    $("article").css("transform", "none")
}

$(function() {
  var is_print = getURLParameter("print");
  if (is_print == "true")
  {
    //$('link[href="_static/styles.css"]').attr("media", "print");
    //$('link[href="_static/custom.css"]').attr("media", "print");
    print();
  }
});
