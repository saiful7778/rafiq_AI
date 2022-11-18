function scrapeLinks(){
    const links = document.querySelectorAll('#b_results li h2 a');
    const hrefs = [];
    for(let i = 0; i < links.length; i++){
        hrefs.push(links[i].href)
    };
    return hrefs;
};
function setStyle(){
    const elements = document.querySelectorAll("#b_results li h2 a");
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
fetch(url,options)