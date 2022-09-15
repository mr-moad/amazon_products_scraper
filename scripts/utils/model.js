var model = null
var tables = document.querySelectorAll("table");
for (table of tables){
    for (tr of table.querySelectorAll("tr")){
        if(tr.innerText.includes("Item model")){
            model = tr.querySelectorAll("td")[0].innerText;
        }
    }
}
if(!model){
    var tables = document.querySelectorAll("ul");
    for (table of tables){
        for (tr of table.querySelectorAll("li")){
            if(tr.innerText.includes("Item model")){
                model = tr.querySelectorAll("span")[2].innerText
                break
            }
        }
    }
}
return model