// https://gist.github.com/klmr/3135217

var createSlideNumbering = function (skipFirstN) {
    var num = 0;
    $('.slides article').each(function () {
        num += 1;
        if (num <= skipFirstN)
            return;

        jQuery('<div/>', {
            class: 'counter',
            text: num - skipFirstN
        }).appendTo($(this));
    });
}

$(window).load(function () {
    createSlideNumbering(1);
});
