var images = document.querySelectorAll("#altImages input")
for (image of images){
    image.click()
}
var c = []
images = document.querySelectorAll('.imgTagWrapper img')
for (image of images){
    c.push(image.src)
}
return c