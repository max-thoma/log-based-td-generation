from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@context": ["https://www.w3.org/2019/wot/td/v1"],
            "id": "feeding_bowl",
            "title": "food dispenser",
            "description": "An animal food dispenser that can switch between manual and automatic feeding",
            "@type": "Animal feeder",
            "base": "http://127.0.0.1:5000",
            "owl:sameAs": "test",
            "securityDefinitions": {"basic_sc": {"scheme": "basic", "in": "header"}},
            "security": ["basic_sc"],
            "properties": {
                "automatic": {
                    "type": "boolean",
                    "title": "Automatic Mode Status",
                    "description": "States if the device is set on automatic or manual food dispension",
                    "forms": [
                        {
                            "mqv:topic": "feeding_bowl/automatic_enabled",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "stored": {
                    "type": "boolean",
                    "title": "Food Available",
                    "description": "Indicates whether enough food is available for the next dispension process",
                    "forms": [
                        {
                            "mqv:topic": "feeding_bowl/stored",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
            "actions": {
                "dispense": {
                    "title": "Dispense Food",
                    "description": "Manually dispenses food for the animal",
                    "forms": [
                        {
                            "mqv:topic": "feeding_bowl/dispense",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "refill": {
                    "title": "Refill Food Dispenser",
                    "description": "refills the stored food",
                    "forms": [
                        {
                            "mqv:topic": "feeding_bowl/refill",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "set_state": {
                    "title": "Set Feeding Mode",
                    "description": "Sets the feeding bowl to automatic or manual",
                    "forms": [
                        {
                            "mqv:topic": "feeding_bowl/automatic",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                    "input": {
                        "type": "string",
                        "enum": ["manual", "automatic"],
                        "description": "Set state to either 'manual' or 'automatic'",
                    },
                },
            },
        }
    )
