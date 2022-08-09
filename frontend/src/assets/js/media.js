function media(screen, callback){
    var windowMediaMatch = window.matchMedia(`(${screen})`);
    function checkMedia(x){
        var status = false
        if(x.matches){
            status = true
        }
        else{
            status = false
        }
        callback(status)
    }
    checkMedia(windowMediaMatch);
    windowMediaMatch.addListener(checkMedia)
}

export default media