let convertArray = (aIn) => {
    aIn.forEach(dataObj => {
       Object.keys(dataObj).forEach( (dataProp)=> {
        let dataValue = dataObj[dataProp];
        if (dataProp === "minRoll" || dataProp === "maxRoll"){
            return
        }

        if (typeof dataValue == "number"){
            dataObj[dataProp] = { damage : dataValue , crit : "NA"}
           } else {
            let aDataValue = dataValue.split("");
            let crit = aDataValue.pop();
            let bValidCritValue = ["A", "B", "C", "D", "E", "F"].some(value => value === "crit")
            if (bValidCritValue){    
            let dmg = aDataValue.join("");
            let dmgNumber = Number.parseInt(dmg);
            dataObj[dataProp] =  { damage : dmgNumber, crit }
            } else {
                
            }
           }
       })
    })
    return aIn
}

let convertData = require("./dataStore/AT1_HandedSlash.json");
let convertData2 = require("./dataStore/AT2_1HandedConcussion.json");
let convertData3 = require("./dataStore/AT3_2HandedWeapon.json");
let convertData4 = require("./dataStore/AT4_MissileWeapons.json");

let conv1 = convertArray(convertData);
let conv2 = convertArray(convertData2);
let conv3 = convertArray(convertData3);
let conv4 = convertArray(convertData4);

let printWithSep = (printContent) => {
    console.log("----------------------\n");
    console.log(JSON.stringify(printContent));
    console.log("\n----------------------");
}

printWithSep(conv1);
printWithSep(conv2);
printWithSep(conv3);
printWithSep(conv4);

console.log("finished");

