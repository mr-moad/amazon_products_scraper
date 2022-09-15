const asd = () => {
    var linkss = [];
    var a = document.querySelectorAll('.hmenu.hmenu-translateX-right');
    for (b of a){
        var links = b.querySelectorAll("a");
        for (c of links){
            linkss.push({
                link : c.href,
                text: c.text
            });
        }
    }
    return linkss;
}
return asd()