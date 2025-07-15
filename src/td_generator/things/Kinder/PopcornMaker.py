from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@context": ["https://www.w3.org/2019/wot/td/v1"],
            "id": "popcorn_maker",
            "title": "Popcorn maker",
            "@type": "Popcorn maker",
            "description": "A popcorn making appliance",
            "base": "http://127.0.0.1:5000",
            "securityDefinitions": {"basic_sc": {"scheme": "basic", "in": "header"}},
            "security": ["basic_sc"],
            "properties": {
                "power": {
                    "type": "boolean",
                    "title": "Popcorn Maker Power Status",
                    "description": "True if machine is turned on and ready for use",
                    "forms": [
                        {
                            "mqv:topic": "popcorn_maker",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                }
            },
            "actions": {
                "toggle": {
                    "title": "Toggle On/Off",
                    "description": "Turns the device on or off based on the current state",
                    "forms": [
                        {
                            "mqv:topic": "popcorn_maker/toggle",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "add corn": {
                    "title": "Add Corn",
                    "description": "Adds corn to the heating section of the maker",
                    "forms": [
                        {
                            "mqv:topic": "popcorn_maker/add_corn",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "add sugar": {
                    "title": "Add Sugar",
                    "description": "Adds sugar to the heating section making the popcorn sweet",
                    "forms": [
                        {
                            "mqv:topic": "popcorn_maker/add_sugar",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "add salt": {
                    "title": "Add Salt",
                    "description": "Adds salt to the heating section making the popcorn salty",
                    "forms": [
                        {
                            "mqv:topic": "popcorn_maker/add_salt",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "heat": {
                    "title": "Start Popcorn Maker",
                    "description": "Start heating up the heating section, turning added corn into popcorn",
                    "forms": [
                        {
                            "mqv:topic": "popcorn_maker/heat",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
        }
    )
