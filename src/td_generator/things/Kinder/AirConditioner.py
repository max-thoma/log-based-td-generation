from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@context": ["https://www.w3.org/2019/wot/td/v1"],
            "id": "ac",
            "title": "Air Conditioner",
            "description": "An air conditioning unit with temperature control",
            "@type": "Cooling and heating system",
            "base": "http://127.0.0.1:5000",
            "owl:sameAs": "test",
            "securityDefinitions": {"basic_sc": {"scheme": "basic", "in": "header"}},
            "security": ["basic_sc"],
            "properties": {
                "Goal Temperature": {
                    "type": "integer",
                    "title": "AC Goal Temperature",
                    "description": "Indicates temperature the air conditioner aims to reach. When set temperature is reached the air conditioner unit will stop the respective cooling or heating process",
                    "minimum": 10,
                    "maximum": 35,
                    "forms": [
                        {
                            "mqv:topic": "ac/goal_temperature",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "status": {
                    "type": "boolean",
                    "title": "AC Status",
                    "description": "Staus of the device indicating if the device is turned on(True) or off (False)",
                    "forms": [
                        {
                            "mqv:topic": "ac/status",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
            "actions": {
                "toggle": {
                    "title": "Toggle Status",
                    "description": "Toggles status property, turning the device either off or on depending on the current status",
                    "forms": [
                        {
                            "mqv:topic": "ac/toggle",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "Temperature Up": {
                    "title": "Temperature Increase",
                    "description": "Increases the goal temperature by 1 degree celsius.",
                    "forms": [
                        {
                            "mqv:topic": "ac/temp_up",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "Temperature Down": {
                    "title": "Temperature Decrease",
                    "description": "Decreases the goal temperature by 1 degree celsius.",
                    "forms": [
                        {
                            "mqv:topic": "ac/temp_down",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
        }
    )
