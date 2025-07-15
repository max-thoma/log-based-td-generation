from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@context": ["https://www.w3.org/2019/wot/td/v1"],
            "id": "coffee_machine",
            "title": "Coffee Machine",
            "@type": "Automated Coffee Machine",
            "description": "A coffee machine that can be controlled remotely",
            "base": "http://127.0.0.1:5000",
            "owl:sameAs": "test",
            "securityDefinitions": {"basic_sc": {"scheme": "basic", "in": "header"}},
            "security": ["basic_sc"],
            "properties": {
                "water": {
                    "title": "Water Level",
                    "type": "boolean",
                    "description": "Illustrates water level of the machine. If False the machine does not contain enough water to make a coffIee and needs to be refilled",
                    "forms": [
                        {
                            "mqv:topic": "coffee_machine/water",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "storage": {
                    "title": "Coffe Ground Waste Bin Status",
                    "type": "boolean",
                    "description": "Indicates the remaining coffee ground storage. If False no space is remaining and the container needs to be emptied",
                    "forms": [
                        {
                            "mqv:topic": "coffee_machine/storage_full",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "on": {
                    "type": "boolean",
                    "title": "Coffee Machine Status",
                    "description": "Displays the current power state of the machine",
                    "forms": [
                        {
                            "mqv:topic": "coffee_machine",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
            "actions": {
                "toggle": {
                    "title": "Toggle On/Off",
                    "description": "Toggles on property of the device",
                    "forms": [
                        {
                            "mqv:topic": "coffee_machine/toggle",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "refill": {
                    "title": "Refill Water Tank",
                    "description": "Refills the water tank of the machine",
                    "forms": [
                        {
                            "mqv:topic": "coffee_machine/refill",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "empty": {
                    "title": "Waste Bin Empty",
                    "description": "Empties coffee ground container",
                    "forms": [
                        {
                            "mqv:topic": "coffee_machine/empty",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "make coffee": {
                    "title": "Make Coffe",
                    "description": "Creates a medium cup of coffee",
                    "forms": [
                        {
                            "mqv:topic": "coffee_machine/make_coffee",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
        }
    )
