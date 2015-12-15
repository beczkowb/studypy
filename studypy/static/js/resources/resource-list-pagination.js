$('.pagination-link').click(function (e) {
    e.preventDefault();
    var search = window.location.search;
    var searchObj = querystringToObject(search);
    console.log(searchObj);
    var tagsParameters = '';
    if (searchObj.tags !== undefined) {
        for (var i = 0; searchObj.tags.length > i; i++) {
            tagsParameters += '&tags=' + searchObj.tags[i];
        }
    }
    window.location.href = this.href + tagsParameters;
});

function querystringToObject(querystring) {
    if (querystring[0] === '?')
        querystring = querystring.slice(1);
    var parameters = querystring.split('&');
    var result = {};
    for (var i = 0; i < parameters.length; i++) {
        var splited_parameter = parameters[i].split('=');
        var key = splited_parameter[0];
        var value = splited_parameter[1];
        if (result[key] === undefined) {
            result[key] = [];
        }
        result[key].push(value);
    }
    return result;
}