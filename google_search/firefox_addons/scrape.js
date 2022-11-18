function scrapeLinks(){
    const links = document.querySelectorAll('.yuRUbf a');
    const hrefs = [];
    for(let i = 0; i < links.length; i++){
        hrefs.push(links[i].href)
    };
    return hrefs;
};
function setStyle(){
    const elements = document.querySelectorAll(".yuRUbf a h3");
    elements.forEach(function(value){
        value.style.cssText = `border: 1px solid red; padding: 0 10px; border-radius:5px; color: #ffffff;`;
    })
};

const url = "https://google-links-scraping.herokuapp.com/api/links";
const options = {
    method: "POST",
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(scrapeLinks())
}
fetch(url,options).then(res => res.json()).then(res => console.log(res));