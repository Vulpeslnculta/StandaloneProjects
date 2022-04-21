const fs = require("fs")

const getTimer = (hours, minutes, seconds) => {

    return `
    setTimeout(() => {
        console.log('${hours}:${minutes}:${seconds}');
    }, (${hours*3600 + minutes*60 + seconds} * 1000));
    `
}

let result = '';

for (let hour = 0; hour < 24; hour++) {
    for (let minute = 0; minute < 60; minute++) {
        for (let second = 0; second < 60; second++) {
            result = result + getTimer(hour, minute, second);
        }
    }
}

fs.writeFile('timer.js', result, console.log)