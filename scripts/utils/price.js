var price = null;
try{
    var d = document.querySelector("#color_name_0_price").innerText;
    price = d.innerText
}catch(err){
    try{
        var price_symbol = document.querySelector(".a-price-symbol").innerText;
        var price_int = document.querySelector(".a-price-whole").innerText;
        var price_dec = document.querySelector(".a-price-fraction").innerText;
        price = price_symbol + price_int + price_dec
    }catch(err){}

}
if (!price){
    try{
        var p = document.querySelector("#size_name_0_price") || document.querySelector("#color_name_0_price")
        if (p.innerText.includes("\n")){
            price = p.innerText.split(/\r?\n/)[1]
        }else{
            price = p.innerText.split(" ")[p.innerText.split(" ").length - 1]
        }

    }
    catch(err){
        ;
    }
}
if (!price){
    var tables = document.querySelectorAll("#corePrice_desktop table")
    if(tables){
        for (table of tables){
            if (table.querySelector(".a-price-range span")){
                return table.querySelector(".a-price-range span").innerText;
            }
        }
    }
}
return price