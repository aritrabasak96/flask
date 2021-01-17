const express = require("express")
const parser = require("body-parser")
const axios = require("axios")

const app = express();

app.use(parser.json())


axios("http://localhost:5000/hellonode")
.then((value)=>{
  // json data
   console.log(value);
})
.catch(err => console.log(err))

app.listen(8000,()=>{
  console.log('lisning');
});
