const figlet = require('figlet');
const fs = require('fs');
const path = require('path');

const outputDir = path.join(__dirname, 'numbers');

if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir);
}


for (let i = 0; i <= 99; i++) {
    const numStr = i.toString();

    let art = figlet.textSync(numStr, { font: 'Terrace' });

    const lines = art.split('\n');

    while (lines.length > 0 && lines[lines.length - 1].trim() === '') {
        lines.pop();
    }

    while (lines.length > 0 && lines[0].trim() === '') {
        lines.shift();
    }

    const cleanedArt = lines.join('\n');

    const fileName = `${numStr.padStart(2, '0')}.txt`;
    fs.writeFileSync(path.join(outputDir, fileName), cleanedArt);
}
