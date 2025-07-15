from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@context": ["https://www.w3.org/2019/wot/td/v1"],
            "id": "watering_system",
            "title": "Sprinkler",
            "@type": "Sprinkler",
            "description": "A sprinkler for watering plants with an external water tank",
            "base": "http://127.0.0.1:5000",
            "owl:sameAs": "test",
            "securityDefinitions": {"basic_sc": {"scheme": "basic", "in": "header"}},
            "security": ["basic_sc"],
            "properties": {
                "water": {
                    "type": "boolean",
                    "title": "Water Reservoir Status",
                    "description": "States whether the water tank is full or empty. If True water is still remaining in the tank and the device is ready for usage otherwise water needs to be refilled",
                    "forms": [
                        {
                            "mqv:topic": "watering_system/has_water",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "on": {
                    "type": "boolean",
                    "title": "Sprinkler On/Off Status",
                    "description": "Describes whether the device is turned on (if True) or off (if False)",
                    "forms": [
                        {
                            "mqv:topic": "watering_system/on",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
            "actions": {
                "Power on": {
                    "title": "Power On Sprinkler",
                    "description": "Turns power of the watering system on",
                    "forms": [
                        {
                            "mqv:topic": "watering_system/power_on",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "Power off": {
                    "title": "Power Off Sprinkler",
                    "description": "Turns power of the watering system off",
                    "forms": [
                        {
                            "mqv:topic": "watering_system/power_off",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "Sprinkle": {
                    "title": "Start Sprinkling",
                    "description": "Initiates watering process wetting all surrounding plants",
                    "forms": [
                        {
                            "mqv:topic": "watering_system/sprinkle",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "Refill": {
                    "title": "Refill Reservoir",
                    "description": "Refills water tank",
                    "forms": [
                        {
                            "mqv:topic": "watering_system/refill",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
        }
    )
