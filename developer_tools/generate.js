const figlet = require('figlet');
const fs = require('fs');
const path = require('path');

const outputDir = path.join(__dirname, 'szamok');

if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir);
}

console.log('Generálás precíz sorvágással...');

for (let i = 0; i <= 99; i++) {
    const numStr = i.toString();
    
    // 1. Generálás
    let art = figlet.textSync(numStr, { font: 'Terrace' });

    // 2. Sorokra bontjuk, és csak azokat tartjuk meg, amik nem teljesen üresek
    // De a sorok elején lévő szóközöket MEGHAGYJUK a struktúra miatt
    const lines = art.split('\n');
    
    // Alulról felfelé haladva levágjuk az üres sorokat
    while (lines.length > 0 && lines[lines.length - 1].trim() === '') {
        lines.pop();
    }
    
    // Felülről lefelé is levágjuk az üres sorokat
    while (lines.length > 0 && lines[0].trim() === '') {
        lines.shift();
    }

    const cleanedArt = lines.join('\n');

    const fileName = `${numStr.padStart(2, '0')}.txt`;
    fs.writeFileSync(path.join(outputDir, fileName), cleanedArt);
}

console.log('Kész! A struktúra megmaradt, az extra alsó/felső sorok eltűntek.');