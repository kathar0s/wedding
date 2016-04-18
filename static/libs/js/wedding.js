$(document).ready(function(e){

    // Back 버튼 액션 등록
    $('.btn-back').on('click', function(e){
        //if (document.referrer.indexOf('article') != -1) {
        //    window.history.go(-2);
        //} else {
        window.history.back();
        //}
    });

    $('[href]').on('click', function(e){
        var href = $(this).attr('href');

        if ($(this)[0].tagName != 'A') {
            if ($(this).data('method') == 'replace') {
                location.replace(href);
            } else {
                location.href = href;
            }
        }

    });
});

String.prototype.string = function(len){var s = '', i = 0; while (i++ < len) { s += this; } return s;};
String.prototype.zf = function(len){return "0".string(len - this.length) + this;};
Number.prototype.zf = function(len){return this.toString().zf(len);};
Date.prototype.format = function(f) {
    if (!this.valueOf()) return " ";

    var weekName = ["일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일"];
    var d = this;

    return f.replace(/(yyyy|yy|M|MM|d|dd|E|hh|h|mm|m|ss|a\/p)/g, function($1) {
        switch ($1) {
            case "yyyy": return d.getFullYear();
            case "yy": return (d.getFullYear() % 1000).zf(2);
            case "MM": return (d.getMonth() + 1).zf(2);
            case "M": return (d.getMonth() + 1);
            case "dd": return d.getDate().zf(2);
            case "d": return d.getDate();
            case "E": return weekName[d.getDay()];
            case "HH": return d.getHours().zf(2);
            case "hh": return ((h = d.getHours() % 12) ? h : 12).zf(2);
            case "h": return ((h = d.getHours() % 12) ? h : 12);
            case "mm": return d.getMinutes().zf(2);
            case "m": return d.getMinutes();
            case "ss": return d.getSeconds().zf(2);
            case "a/p": return d.getHours() < 12 ? "오전" : "오후";
            default: return $1;
        }
    });
};

function setCookie(name, value, days) {
    var expires;

    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toGMTString();
    } else {
        expires = "";
    }
    document.cookie = encodeURIComponent(name) + "=" + encodeURIComponent(value) + expires + "; path=/";
}

function getCookie(name) {
    var nameEQ = encodeURIComponent(name) + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) === ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) === 0) return decodeURIComponent(c.substring(nameEQ.length, c.length));
    }
    return null;
}

function clearCookie( name ) {
    setCookie(name, '', -1);
}

function deserialize(value) {
    var vars = value.split('&');
    var result = {}
    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split('=');
        result[decodeURIComponent(pair[0])] = decodeURIComponent(pair[1])
    }
    return result;
}