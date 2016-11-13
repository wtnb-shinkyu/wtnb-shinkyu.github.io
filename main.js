const pug = require('pug');
const fs = require('fs');

const compiled = pug.compileFile('src/index.pug');
fs.writeFile('index.html', compiled());
