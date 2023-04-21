

(function(arg){
    // jQuery.fn.extend
    arg.fn.extend({
      check: function() {
        return "lizexiong-extend-fn"
      },
    });

    // var ret = $('#id').check();
    // alert(ret)


    //jQuery.extend(object)
    arg.extend({
      check: function() {
        return "lizexiong-extend"
      },
    });

})(jQuery)


