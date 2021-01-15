
// WEB STORAGE
function storageAvailable(type) {
    try {
        var storage = window[type],
        x = '__storage_test__';
        storage.setItem(x, x);
        storage.removeItem(x);
        return true;
    }
    catch (e) {
        return e instanceof DOMException && (
        e.code === 22 ||
        e.code === 1014 ||
        e.name === 'QuotaExceededError' ||
        e.name === 'NS_ERROR_DOM_QUOTA_REACHED') &&
        storage.length !== 0;
    }
}


// COOKIES - in browser console
function getCookie (cookie_name) {
    var name = cookie_name + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split (';');
    for ( var i = 0; i < ca.length; i++) {
        var c = ca [i];
        while (c.charAt(0) == ' ') {
            c = c.substring (1) ;
        }
        if (c.indexOf(name) == 0) {
            return c.substring (name.length, c.length);
        }
    }
    return "";
}

document.cookie = "username=McPenquen";
document . cookie = "password = secret ; expires =Thu , 18 Dec 2019 12:00:00 UTC ";
var docCook = document.cookie;
console.log(docCook);