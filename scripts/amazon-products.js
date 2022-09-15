const asd = () =>{
    var alls = []
    var a = document.querySelectorAll("div[data-component-id][data-asin]");
    for (var b = 0; b < a.length;b++){
        try{
            img = a[b].querySelector("img").src;
            link = a[b].querySelector("a").href;
            alls.push({
                "image" : img,
                "link": link
            })
        }
        catch{
            console.log(a[b])
        }
        }
    return alls
}
return asd()