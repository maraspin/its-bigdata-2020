process.env["NODE_TLS_REJECT_UNAUTHORIZED"] = 0;

const start = new Date()
let end = 0;

const axios = require('axios');

axios.get('https://www.mocky.io/v2/5ed60dcf3400007b0006d626?mocky-delay=1000ms').then(resp => {
    console.log(resp.data);
    end = new Date();
    console.log("Elapsed Time: " + (end - start) + " seconds");
});