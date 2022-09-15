var description = null;
try{
    var c = document.querySelector("#productDescription_feature_div");
    description = c.innerText
}catch(err){
    var c = document.querySelector("#aplus3p-2_feature_div");
    description = c.innerText
}
if (!description || description == ""){
    description = document.querySelector("#feature-bullets").innerText
}
return description