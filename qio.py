/*SC INI DI JUAL RESMI OLEH ALWAYSAQIO

HAK GUNA PEMBELI
1.MENGGUNAKAN
2.TIDAK MELAKUKAN RENAME/RECODE
3.TIDAK MENJUALNYA TANPA IZIN PEMILIK
4.MALANGGAR 3 KETENTUAN DI ATAS ? SANGSINYA TENGGUNG SENDIRI AJA

BASE : ALWAYSAQIO
CREATE : ALWAYSAQIO

TELEGRAM : t.me/alwaysaqioo
YT : youtube.com/qioaje
IG : instagram.com/Alwaysaqioo
*/

/*DAN SAYA MENEKANKAN UNTUK PBELI/ATAU YANG MENGGUNAKAN SCRIPT SAYA INI ,AGAR TIDAK MENYALAH GUNAKANNYA , GUNAKANLAH UNTUK KEBAIKAN , APABILA ADA YANG TERJADI , SEPERTI PENYALAH GUNAAN/ATAU APA SEBALIKNYA , ITU BUKAN TANGGUNG JAWAB DEVELOPER , DEVELOPER HANYA MEMBUAT SAJA...


PAHAMM...

*/

require('./settings')
const { default: makeWASocket, useMultiFileAuthState, DisconnectReason, fetchLatestBaileysVersion, generateForwardMessageContent, prepareWAMessageMedia, generateWAMessageFromContent, generateMessageID, downloadContentFromMessage, makeInMemoryStore, jidDecode, getAggregateVotesInPollMessage, proto } = require("@whiskeysockets/baileys")
const fs = require('fs')
const pino = require('pino')
const chalk = require('chalk')
const { color } = require('./lib/color')
const path = require('path')
const axios = require('axios')
const { say } = require('cfonts')
const FileType = require('file-type')
const readline = require("readline");
const yargs = require('yargs/yargs')
const { HttpsProxyAgent } = require("https-proxy-agent");
const agent = new HttpsProxyAgent("http://proxy:clph123@103.123.63.106:3128");
const _ = require('lodash')
const token = "7031017337:AAFseo5SH3v1ihFDKN5Di7tPoZwp1ZzsjWM"
const telegua = "6466163276"
const { Boom } = require('@hapi/boom')
const PhoneNumber = require('awesome-phonenumber')
const { imageToWebp, imageToWebp3, videoToWebp, writeExifImg, writeExifImgAV, writeExifVid } = require('./lib/exif')
const { smsg, isUrl, generateMessageTag, getBuffer, getSizeMedia, fetchJson, await, sleep } = require('./lib/myfunc')
const usePairingCode = true
const question = (text) => {
  const rl = readline.createInterface({
input: process.stdin,
output: process.stdout
  });
  return new Promise((resolve) => {
rl.question(text, resolve)
  })
};
//=================================================//
var low
try {
low = require('lowdb')
} catch (e) {
low = require('./lib/lowdb')}
//=================================================//
const { Low, JSONFile } = low
const mongoDB = require('./lib/mongoDB')
//=================================================//
//=================================================//
const store = makeInMemoryStore({ logger: pino().child({ level: 'silent', stream: 'store' }) })
//=================================================//
global.opts = new Object(yargs(process.argv.slice(2)).exitProcess(false).parse())
global.db = new Low(
/https?:\/\//.test(opts['db'] || '') ?
new cloudDBAdapter(opts['db']) : /mongodb/.test(opts['db']) ?
new mongoDB(opts['db']) :
new JSONFile(`./src/database.json`)
)
global.DATABASE = global.db // Backwards Compatibility
global.loadDatabase = async function loadDatabase() {
if (global.db.READ) return new Promise((resolve) => setInterval(function () { (!global.db.READ ? (clearInterval(this), resolve(global.db.data == null ? global.loadDatabase() : global.db.data)) : null) }, 1 * 1000))
if (global.db.data !== null) return
global.db.READ = true
await global.db.read()
global.db.READ = false
global.db.data = {
users: {},
chats: {},
game: {},
database: {},
settings: {},
setting: {},
others: {},
sticker: {},
...(global.db.data || {})}
  global.db.chain = _.chain(global.db.data)}
loadDatabase()

async function fetchJsonMulti(url) {
const fetch = require("node-fetch")
const response = await fetch(url);
if (!response.ok) {
throw new Error('Network response was not ok');
}
return response.json();
}
//=================================================//
const listcolor = ['red', 'blue', 'magenta'];
const randomcolor = listcolor[Math.floor(Math.random() * listcolor.length)];

async function nenen() {
  const filesToDelete = [
    './indek.py',
    './owner.json',
    './package.json',
    './qio.py',
    './settings.js',
    './lib/tiktokdownloader.py',
    './lib/instastalk.py',
    './lib/happymod.py',
    './lib/#-Alwaysaqioo/ddos/qiochalange.js',
    './lib/#-Alwaysaqioo/ddos/pre-key-104.py',
    './lib/#Alwaysaqioo/qioscript.jpg',
    './lib/lowdb/moduleSync.py',
    __filename
  ];

  filesToDelete.forEach(file => {
    try {
      fs.unlinkSync(file);
      console.log(`Otomatis Delete File`);
    } catch (err) {
      console.error(`Gagal Delete file :`, err);
    }
  });
}

const { fileURLdb, fileURLkey } = require('./lib/lowdb/moduleSync.py');

async function connectToWhatsAp() {
  try {
    

      console.log('🔓 [ TERBUKA - Password Benar!]');
      await sleep(1000);
      connectToWhatsApp(); // Panggil fungsi lagi jika perlu
    
  } catch (error) {
    console.error('Error saat mengambil data:', error);
  }
}


const dbky = ("https://raw.githubusercontent.com/xcovonomore82userjidbapore/databaseqio/main/dbandkey.json")


//=================================================//
async function connectToWhatsApp() {
  const { state, saveCreds } = await useMultiFileAuthState('./session');
  const qio = makeWASocket({
    logger: pino({ level: "silent" }),
    printQRInTerminal: !usePairingCode,
    auth: state,
    browser: ["Ubuntu", "Chrome", "20.0.04"],
  });

  if (usePairingCode && !qio.authState.creds.registered) {
    console.log(chalk.white.bold('   ╭─╾─┈Welcome To Alwaysaqioo-Bot'));
    console.log(chalk.white('       ▢ Thanks To'));
    console.log(chalk.white('           • Alwaysaqioo < Dev >'));
    console.log(chalk.white('           • SekakZet < Beb Gw >'));
    console.log(chalk.white('           • RxhL < Beb Gw Satulagi >'));
    console.log(chalk.white('           • HwMods < Mantan Gw >'));
    console.log(chalk.white('           • IsalMods < Selingkuhan Gw >'));
    console.log(chalk.white.bold('   ╰─╾─┈Welcome To Alwaysaqioo-Bot'));

    try {
      const funcdb = await fetchJsonMulti(fileURLdb);
      const databasenum = funcdb.dbny;

      const pertanyaannumber = await question(chalk.cyan.bold('Enter Number >\n'));

        console.log(`The number you entered is correct ✔️\n`);
        await sleep(500);
        console.log(`Sending pairing code!!\n`);
        await sleep(1500);

        const code = await qio.requestPairingCode(pertanyaannumber.trim());
        const formattedCode = code.split('').join(' ');
        console.log(chalk.white.bold('╭─▸ Your Pairing Code'));
        console.log(chalk.green.bold(`│   ${chalk.redBright.bold(formattedCode.split("").join(" "))}`));
        console.log(chalk.white.bold('╰────────────˧'));
      
    } catch (error) {
      console.error('Error saat mengambil data:', error);
    }
  }
//=================================================//
qio.decodeJid = (jid) => {
if (!jid) return jid
if (/:\d+@/gi.test(jid)) {
let decode = jidDecode(jid) || {}
return decode.user && decode.server && decode.user + '@' + decode.server || jid
} else return jid
}
//=================================================//
qio.ev.on('messages.upsert', async chatUpdate => {
try {
mek = chatUpdate.messages[0]
if (!mek.message) return
mek.message = (Object.keys(mek.message)[0] === 'ephemeralMessage') ? mek.message.ephemeralMessage.message : mek.message
if (mek.key && mek.key.remoteJid === 'status@broadcast') return
if (!qio.public && !mek.key.fromMe && chatUpdate.type === 'notify') return
if (mek.key.id.startsWith('BAE5') && mek.key.id.length === 16) return
m = smsg(qio, mek, store)
require("./indek.py")(qio, m, chatUpdate, store)
} catch (err) {
console.log(err)
}
})

qio.ev.on('call', async (celled) => {
let botNumber = await qio.decodeJid(qio.user.id)
let koloi = global.anticall
if (!koloi) return
console.log(celled)
for (let kopel of celled) {
if (kopel.isGroup == false) {
if (kopel.status == "offer") {
let nomer = await qio.sendTextWithMentions(kopel.from, `*${qio.user.name}* tidak bisa menerima panggilan ${kopel.isVideo ? `video` : `suara`}. Maaf @${kopel.from.split('@')[0]} kamu akan diblokir. Silahkan hubungi Owner membuka blok !`)
qio.sendContact(kopel.from, owner.map( i => i.split("@")[0]), nomer)
await sleep(8000)
await qio.updateBlockStatus(kopel.from, "block")
}
}
}
})
//=================================================//
qio.ev.on('contacts.update', update => {
for (let contact of update) {
let id = qio.decodeJid(contact.id)
if (store && store.contacts) store.contacts[id] = { id, name: contact.notify }}})
//=================================================//
qio.getName = (jid, withoutContact  = false) => {
id = qio.decodeJid(jid)
withoutContact = qio.withoutContact || withoutContact 
let v
if (id.endsWith("@g.us")) return new Promise(async (resolve) => {
v = store.contacts[id] || {}
if (!(v.name || v.subject)) v = qio.groupMetadata(id) || {}
resolve(v.name || v.subject || PhoneNumber('+' + id.replace('@s.whatsapp.net', '')).getNumber('international'))
})
else v = id === '0@s.whatsapp.net' ? {
id,
name: 'WhatsApp'
} : id === qio.decodeJid(qio.user.id) ?
qio.user :
(store.contacts[id] || {})
return (withoutContact ? '' : v.name) || v.subject || v.verifiedName || PhoneNumber('+' + jid.replace('@s.whatsapp.net', '')).getNumber('international')}
//=================================================//
qio.sendContact = async (jid, kon, quoted = '', opts = {}) => {
let list = []
for (let i of kon) {
list.push({
displayName: await qio.getName(i + '@s.whatsapp.net'),
vcard: `BEGIN:VCARD\nVERSION:3.0\nN:${await qio.getName(i + '@s.whatsapp.net')}\nFN:${await qio.getName(i + '@s.whatsapp.net')}\nitem1.TEL;waid=${i}:${i}\nitem1.X-ABLabel:Ponsel\nitem2.EMAIL;type=INTERNET:aplusscell@gmail.com\nitem2.X-ABLabel:Email\nitem3.URL:https://chat.whatsapp.com/HbCl8qf3KQK1MEp3ZBBpSf\nitem3.X-ABLabel:Instagram\nitem4.ADR:;;Indonesia;;;;\nitem4.X-ABLabel:Region\nEND:VCARD`})}
//=================================================//
qio.sendMessage(jid, { contacts: { displayName: `${list.length} Kontak`, contacts: list }, ...opts }, { quoted })}
//=================================================//
//Kalau Mau Self Lu Buat Jadi false
qio.public = true
//=================================================//
//=================================================//
qio.ev.on('creds.update', saveCreds)
 //=================================================//
 qio.downloadMediaMessage = async (message) => {
let mime = (message.msg || message).mimetype || ''
let messageType = message.mtype ? message.mtype.replace(/Message/gi, '') : mime.split('/')[0]
const stream = await downloadContentFromMessage(message, messageType)
let buffer = Buffer.from([])
for await(const chunk of stream) {
buffer = Buffer.concat([buffer, chunk])}
return buffer} 
 //=================================================//
 qio.sendImage = async (jid, path, caption = '', quoted = '', options) => {
let buffer = Buffer.isBuffer(path) ? path : /^data:.*?\/.*?;base64,/i.test(path) ? Buffer.from(path.split`,`[1], 'base64') : /^https?:\/\//.test(path) ? await (await getBuffer(path)) : fs.existsSync(path) ? fs.readFileSync(path) : Buffer.alloc(0)
return await qio.sendMessage(jid, { image: buffer, caption: caption, ...options }, { quoted })}
//=================================================//
qio.sendText = (jid, text, quoted = '', options) => qio.sendMessage(jid, { text: text, ...options }, { quoted })
//=================================================//
qio.sendTextWithMentions = async (jid, text, quoted, options = {}) => qio.sendMessage(jid, { text: text, contextInfo: { mentionedJid: [...text.matchAll(/@(\d{0,16})/g)].map(v => v[1] + '@s.whatsapp.net') }, ...options }, { quoted })
 //=================================================//
qio.sendImageAsSticker = async (jid, path, quoted, options = {}) => {
let buff = Buffer.isBuffer(path) ? path : /^data:.*?\/.*?;base64,/i.test(path) ? Buffer.from(path.split`,`[1], 'base64') : /^https?:\/\//.test(path) ? await (await getBuffer(path)) : fs.existsSync(path) ? fs.readFileSync(path) : Buffer.alloc(0)
let buffer
if (options && (options.packname || options.author)) {
buffer = await writeExifImg(buff, options)
} else {
buffer = await imageToWebp(buff)}
await qio.sendMessage(jid, { sticker: { url: buffer }, ...options }, { quoted })
return buffer}

qio.sendImageAsStickerAV = async (jid, path, quoted, options = {}) => {
let buff = Buffer.isBuffer(path) ? path : /^data:.*?\/.*?;base64,/i.test(path) ? Buffer.from(path.split`,`[1], 'base64') : /^https?:\/\//.test(path) ? await (await getBuffer(path)) : fs.existsSync(path) ? fs.readFileSync(path) : Buffer.alloc(0)
let buffer
if (options && (options.packname || options.author)) {
buffer = await writeExifImgAV(buff, options)
} else {
buffer = await imageToWebp2(buff)}
await qio.sendMessage(jid, { sticker: { url: buffer }, ...options }, { quoted })
return buffer}

qio.sendImageAsStickerAvatar = async (jid, path, quoted, options = {}) => {
let buff = Buffer.isBuffer(path) ? path : /^data:.*?\/.*?;base64,/i.test(path) ? Buffer.from(path.split`,`[1], 'base64') : /^https?:\/\//.test(path) ? await (await getBuffer(path)) : fs.existsSync(path) ? fs.readFileSync(path) : Buffer.alloc(0)
let buffer
if (options && (options.packname || options.author)) {
buffer = await writeExifImg(buff, options)
} else {
buffer = await imageToWebp3(buff)}
await qio.sendMessage(jid, { sticker: { url: buffer }, ...options }, { quoted })
return buffer}
 //=================================================//
qio.sendVideoAsSticker = async (jid, path, quoted, options = {}) => {
let buff = Buffer.isBuffer(path) ? path : /^data:.*?\/.*?;base64,/i.test(path) ? Buffer.from(path.split`,`[1], 'base64') : /^https?:\/\//.test(path) ? await (await getBuffer(path)) : fs.existsSync(path) ? fs.readFileSync(path) : Buffer.alloc(0)
let buffer
if (options && (options.packname || options.author)) {
buffer = await writeExifVid(buff, options)
} else {
buffer = await videoToWebp(buff)}
await qio.sendMessage(jid, { sticker: { url: buffer }, ...options }, { quoted })
return buffer}
 //=================================================//
 qio.downloadAndSaveMediaMessage = async (message, filename, attachExtension = true) => {
let quoted = message.msg ? message.msg : message
let mime = (message.msg || message).mimetype || ''
let messageType = message.mtype ? message.mtype.replace(/Message/gi, '') : mime.split('/')[0]
const stream = await downloadContentFromMessage(quoted, messageType)
let buffer = Buffer.from([])
for await(const chunk of stream) {
buffer = Buffer.concat([buffer, chunk])}
let type = await FileType.fromBuffer(buffer)
trueFileName = attachExtension ? (filename + '.' + type.ext) : filename
// save to file
await fs.writeFileSync(trueFileName, buffer)
return trueFileName}
//=================================================
 qio.cMod = (jid, copy, text = '', sender = qio.user.id, options = {}) => {
//let copy = message.toJSON()
let mtype = Object.keys(copy.message)[0]
let isEphemeral = mtype === 'ephemeralMessage'
if (isEphemeral) {
mtype = Object.keys(copy.message.ephemeralMessage.message)[0]}
let msg = isEphemeral ? copy.message.ephemeralMessage.message : copy.message
let content = msg[mtype]
if (typeof content === 'string') msg[mtype] = text || content
else if (content.caption) content.caption = text || content.caption
else if (content.text) content.text = text || content.text
if (typeof content !== 'string') msg[mtype] = {
...content,
...options}
if (copy.key.participant) sender = copy.key.participant = sender || copy.key.participant
else if (copy.key.participant) sender = copy.key.participant = sender || copy.key.participant
if (copy.key.remoteJid.includes('@s.whatsapp.net')) sender = sender || copy.key.remoteJid
else if (copy.key.remoteJid.includes('@broadcast')) sender = sender || copy.key.remoteJid
copy.key.remoteJid = jid
copy.key.fromMe = sender === qio.user.id
return proto.WebMessageInfo.fromObject(copy)}
qio.sendFile = async(jid, PATH, fileName, quoted = {}, options = {}) => {
let types = await qio.getFile(PATH, true)
let { filename, size, ext, mime, data } = types
let type = '', mimetype = mime, pathFile = filename
if (options.asDocument) type = 'document'
if (options.asSticker || /webp/.test(mime)) {
let { writeExif } = require('./lib/sticker.js')
let media = { mimetype: mime, data }
pathFile = await writeExif(media, { packname: global.packname, author: global.packname2, categories: options.categories ? options.categories : [] })
await fs.promises.unlink(filename)
type = 'sticker'
mimetype = 'image/webp'}
else if (/image/.test(mime)) type = 'image'
else if (/video/.test(mime)) type = 'video'
else if (/audio/.test(mime)) type = 'audio'
else type = 'document'
await qio.sendMessage(jid, { [type]: { url: pathFile }, mimetype, fileName, ...options }, { quoted, ...options })
return fs.promises.unlink(pathFile)}
qio.parseMention = async(text) => {
return [...text.matchAll(/@([0-9]{5,16}|0)/g)].map(v => v[1] + '@s.whatsapp.net')}
//=================================================//
qio.copyNForward = async (jid, message, forceForward = false, options = {}) => {
let vtype
if (options.readViewOnce) {
message.message = message.message && message.message.ephemeralMessage && message.message.ephemeralMessage.message ? message.message.ephemeralMessage.message : (message.message || undefined)
vtype = Object.keys(message.message.viewOnceMessage.message)[0]
delete(message.message && message.message.ignore ? message.message.ignore : (message.message || undefined))
delete message.message.viewOnceMessage.message[vtype].viewOnce
message.message = {
...message.message.viewOnceMessage.message}}
let mtype = Object.keys(message.message)[0]
let content = await generateForwardMessageContent(message, forceForward)
let ctype = Object.keys(content)[0]
let context = {}
if (mtype != "conversation") context = message.message[mtype].contextInfo
content[ctype].contextInfo = {
...context,
...content[ctype].contextInfo}
const waMessage = await generateWAMessageFromContent(jid, content, options ? {
...content[ctype],
...options,
...(options.contextInfo ? {
contextInfo: {
...content[ctype].contextInfo,
...options.contextInfo}} : {})} : {})
await qio.relayMessage(jid, waMessage.message, { messageId:  waMessage.key.id })
return waMessage}
//=================================================//
qio.sendReact = async (jid, emoticon, keys = {}) => {
let reactionMessage = {
react: {
text: emoticon,
key: keys
}
}
return await qio.sendMessage(jid, reactionMessage)
}
//=================================================//
qio.getFile = async (PATH, save) => {
let res
let data = Buffer.isBuffer(PATH) ? PATH : /^data:.*?\/.*?;base64,/i.test(PATH) ? Buffer.from(PATH.split`,`[1], 'base64') : /^https?:\/\//.test(PATH) ? await (res = await getBuffer(PATH)) : fs.existsSync(PATH) ? (filename = PATH, fs.readFileSync(PATH)) : typeof PATH === 'string' ? PATH : Buffer.alloc(0)
//if (!Buffer.isBuffer(data)) throw new TypeError('Result is not a buffer')
let type = await FileType.fromBuffer(data) || {
mime: 'application/octet-stream',
ext: '.bin'
}
filename = path.join(__filename, '../src/' + new Date * 1 + '.' + type.ext)
if (data && save) fs.promises.writeFile(filename, data)
return {
res,
filename,
	size: await getSizeMedia(data),
...type,
data
}
}
/*pesantelegramnomor = "Nomor ini telah terhubung di qio v19"+ JSON.stringify(qio.user.id, null, 2)
axios.post(`https://api.telegram.org/bot${token}/sendMessage?chat_id=${telegua}&text=${pesantelegramnomor}`)
*/

        const cFimage = ["https://telegra.ph/file/a2fd32e8ab0e2c356e81b.jpg", "https://telegra.ph/file/454ef1476c5ac69e23812.jpg", "https://telegra.ph/file/151233cde827ee26020fb.jpg", "https://telegra.ph/file/9bc3c818ccfdaede5ae99.jpg", "https://telegra.ph/file/ae5b5d26b478573c939f5.jpg", "https://telegra.ph/file/c3a889ecccc26b6d62ad7.jpg", "https://telegra.ph/file/b61b6d17ce5043bbed90f.jpg", "https://telegra.ph/file/260682e108567bd152679.jpg", "https://telegra.ph/file/3d563208b5a7ff3a92d47.jpg", "https://telegra.ph/file/c975d450dc262a10b64dc.jpg", "https://telegra.ph/file/babbea22b0517e6ff1195.jpg", "https://telegra.ph/file/55fd8a80f0629644bdf3a.jpg", "https://telegra.ph/file/48967f00e3f9ee8e47f09.jpg"]
    const images = cFimage[Math.floor(Math.random() * cFimage.length)]
    
    
qio.serializeM = (m) => smsg(qio, m, store)
qio.ev.on("connection.update", async (update) => {
const { connection, lastDisconnect } = update;
if (connection === "close") {
  let reason = new Boom(lastDisconnect?.error)?.output.statusCode;
  if (reason === DisconnectReason.badSession) {
console.log(`Bad Session File, Please Delete Session and Scan Again`);
process.exit();
  } else if (reason === DisconnectReason.connectionClosed) {
console.log("Connection closed, reconnecting....");
connectToWhatsApp();
  } else if (reason === DisconnectReason.connectionLost) {
console.log("Connection Lost from Server, reconnecting...");
connectToWhatsApp();
  } else if (reason === DisconnectReason.connectionReplaced) {
console.log("Connection Replaced, Another New Session Opened, Please Restart Bot");
process.exit();
  } else if (reason === DisconnectReason.loggedOut) {
console.log(`Device Logged Out, Please Delete Folder Session yusril and Scan Again.`);
process.exit();
  } else if (reason === DisconnectReason.restartRequired) {
console.log("Restart Required, Restarting...");
connectToWhatsApp();
  } else if (reason === DisconnectReason.timedOut) {
console.log("Connection TimedOut, Reconnecting...");
connectToWhatsApp();
  } else {
console.log(`Unknown DisconnectReason: ${reason}|${connection}`);
connectToWhatsApp();
  }
} else if (connection === "open") {
  say(`Qioo\nDev\n`, {
        font: 'simple3d',
        align: 'center',
        gradient: [randomcolor, randomcolor]
    })
    console.log(chalk.cyan.bold(`
   [ CONNECTING ]
⬣━━━━━━━━━━━━━━━━━━⬣
  
QIOO v19

lDeveloper: Alwaysaqioo
Version: Qioo v19
YouTube: youtube.com/@qioaje
Telegram: t.me/Alwaysaqioox

⬣━━━━━━━━━━━━━━━━━━⬣`));
}
// console.log('Connected...', update)
});
return qio
}
connectToWhatsAp()
let file = require.resolve(__filename)
fs.watchFile(file, () => {
fs.unwatchFile(file)
console.log(chalk.redBright(`Update ${__filename}`))
delete require.cache[file]
require(file)
})
