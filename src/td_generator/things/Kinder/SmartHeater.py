from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@context": ["https://www.w3.org/2019/wot/td/v1"],
            "id": "heater",
            "title": "Smart Heater",
            "description": "A space heating appliance",
            "@type": "Heating device",
            "base": "http://127.0.0.1:5000",
            "owl:sameAs": "test",
            "securityDefinitions": {"basic_sc": {"scheme": "basic", "in": "header"}},
            "security": ["basic_sc"],
            "properties": {
                "level": {
                    "title": "Heating Level",
                    "type": "integer",
                    "minimum": 0,
                    "maximum": 6,
                    "description": "Integer Value indicating the current heating level of the device. Higher values represent higher temperatures. Maximum value is 6, minumum value is 0",
                    "forms": [
                        {
                            "mqv:topic": "heater/level",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "status": {
                    "title": "Heating Status",
                    "type": "boolean",
                    "description": "Boolean Value that describes if the device is on or off",
                    "forms": [
                        {
                            "mqv:topic": "heater/status",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
            "actions": {
                "turn on": {
                    "title": "Start Heating",
                    "description": "Turns the Heating Device on",
                    "forms": [
                        {
                            "mqv:topic": "heater/turn_on",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "turn off": {
                    "title": "Stop Heating",
                    "description": "Turns the Heating device off",
                    "forms": [
                        {
                            "mqv:topic": "heater/turn_off",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "increase level": {
                    "title": "Increase Heating Level",
                    "description": "Increases the Heating level of the device.",
                    "forms": [
                        {
                            "mqv:topic": "heater/increase_temp",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "decrease level": {
                    "title": "Decrease Heating Level",
                    "description": "Decreases the Heating level of the device.",
                    "forms": [
                        {
                            "mqv:topic": "heater/decrease_temp",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
        }
    )
