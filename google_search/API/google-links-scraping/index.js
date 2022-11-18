const express = require("express");
const fs = require("fs");
const cors = require("cors");
const app = express();
const PORT = process.env.PORT || 3500;

app.use(express.json());
app.use(cors());

app.post("/api/links", (req, res) => {
  const links = [req.body];
  const jsonData = JSON.stringify(links);
  fs.writeFileSync('./data/data.json', jsonData,{encoding:"utf-8",flag:"w"}, function(err, data){
    if(err){
        res.send(err)
    }
    console.log("file is saved")
  });
  console.log(req.body);
});

app.get("/api/scraping-links", (req, res) => {
    const data = fs.readFileSync('./data/data.json','utf-8', function(err, data){
      if (err){
        return console.log(err)
      }
    })
    res.json(JSON.parse(data))
});

app.listen(PORT, () => {
  console.log(`Listening on the port http://localhost:${PORT}`);
});
