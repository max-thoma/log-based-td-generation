from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@context": ["https://www.w3.org/2019/wot/td/v1"],
            "id": "oven",
            "title": "Oven",
            "description": "A baking oven with different heating modes and preheating capabilities",
            "@type": "Baking Device",
            "base": "http://127.0.0.1:5000",
            "owl:sameAs": "test",
            "securityDefinitions": {"basic_sc": {"scheme": "basic", "in": "header"}},
            "security": ["basic_sc"],
            "properties": {
                "on": {
                    "type": "boolean",
                    "title": "Oven Power Status",
                    "description": "Property stating if the oven is currently turned on or off",
                    "forms": [
                        {
                            "mqv:topic": "oven/on",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "heating_method": {
                    "title": "Oven Heating Mode",
                    "type": "string",
                    "enum": ["convection", "top_and_bottom"],
                    "description": "States the current heating method that is selected",
                    "characteristics": ["convection", "top and bottom"],
                    "forms": [
                        {
                            "mqv:topic": "oven",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
            "actions": {
                "switch on": {
                    "title": "Turn On Oven",
                    "description": "Turns the oven on",
                    "forms": [
                        {
                            "mqv:topic": "oven/switch_on",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "switch off": {
                    "title": "Turn Off Oven",
                    "description": "Turns the oven off",
                    "forms": [
                        {
                            "mqv:topic": "oven/switch_off",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "change heating method": {
                    "title": "Toggle Heating Mode",
                    "description": "Changes the currently selected heating method from convection to top and bottom or vice versa",
                    "forms": [
                        {
                            "mqv:topic": "oven/change_heating_method",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "preheat": {
                    "title": "Preheat Oven",
                    "description": "Starts preheating the oven to 180 Degrees Celcius",
                    "forms": [
                        {
                            "mqv:topic": "oven/preheat",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
        }
    )
