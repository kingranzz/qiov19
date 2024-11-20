const fs = require("fs");

const fileName = "decoded.qio.js";

async function decode(filename, layer = 0) {
    const readFile = fs.readFileSync(filename).toString();
    if (
        readFile.includes("eval") &&
        (readFile.includes("zlib") || readFile.includes("crypto"))
    ) {
        const replaced = readFile.replace("eval", "resolve");
        const execute = await eval(
            `(function(){ return new Promise((resolve) => { ${replaced} })})()`
        );
        const output = `decode/${layer}.${fileName}`;

        fs.writeFileSync(output, Buffer.from(execute));
        return decode(output,layer+1);
    } else {
        console.log("Decoded");
        return readFile;
    }
}

decode(fileName);
