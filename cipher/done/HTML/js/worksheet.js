let fs = require("fs")
let platforms = JSON.parse(fs.readFileSync("resources/web-clients.json"));
platforms.map(function(val){
    //console.log('OSES.put("'+val.value+'", "'+val.deviceName+'");');    
})
platforms.map(function(val){
    //console.log('DEVICES.put("'+val.value+'", "'+val.deviceName+'");');
})
var keys = [];
var all = 0;
platforms.map(function(val){
    all ++;
    if(!keys.includes(val.value)){
        keys.push(val.value);
        console.log('BROWSERS.put("'+val.value+'", "'+val.deviceName+'");');
    }
})
console.log(all,keys.length)


    
