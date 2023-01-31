function getUrlVars() { 
    var vars = {}; 
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi,
        function(m, key, value) { 
            vars[key] = value; 
        });
    
    return vars; 
}

var pdf = getUrlVars()["file"];

const elem = document.getElementById('iframeID');
elem.src = "static/pdfjs/viewer.html?file=".concat(pdf);