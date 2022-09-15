var manufacturer = null
try{
    var c = document.querySelector("#detailBulletsWrapper_feature_div ul").querySelectorAll("li");
    for (i of c){
        if (i.innerText.startsWith("Manufacturer")){
            manufacturer =  i.querySelectorAll("span span")[1].innerText
            break
        }
    }
}catch(err){
    var a = document.querySelectorAll("#productDetails_techSpec_section_1 tr");
    for (t of a){
        if (t.querySelector("th").innerText.includes("Manufacturer") || t.querySelector("th").innerText.includes("Brand") ){
            manufacturer = t.querySelector("td").innerText;
            break
        }
    }
}
if(!manufacturer){
    var wrap =  document.querySelectorAll("#productOverview_feature_div");

    if (wrap){
        var trs = document.querySelectorAll("#productOverview_feature_div tr");
        for (tr of trs){
            if (tr.querySelectorAll("td")[0].innerText == "Brand" || tr.querySelectorAll("td")[0].innerText == "Manufacturer"){
                manufacturer = tr.querySelectorAll("td")[1].innerText;
                break
            }
        }
    }
}
if (!manufacturer){
    try{
        var tables = document.querySelectorAll("table");
        for (table of tables){
            for (row of table.querySelectorAll("tr")){
                if (row.innerText.startsWith("Manufacturer") || row.innerText.startsWith("Brand")){
                    return manufacturer = row.querySelector("td").innerText;
                }
            }
        }
    }catch(err){;}

}
return manufacturer
