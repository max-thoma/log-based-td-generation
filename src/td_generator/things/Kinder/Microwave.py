from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@context": ["https://www.w3.org/2019/wot/td/v1"],
            "id": "microwave",
            "title": "Microwave",
            "@type": "Microwave",
            "description": "An microwave appliance",
            "base": "http://127.0.0.1:5000",
            "owl:sameAs": "test",
            "securityDefinitions": {"basic_sc": {"scheme": "basic", "in": "header"}},
            "security": ["basic_sc"],
            "properties": {
                "running": {
                    "type": "boolean",
                    "title": "Microwave On/Off",
                    "description": "Property stating if the microwave is currently running or not",
                    "forms": [
                        {
                            "mqv:topic": "microwave",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                }
            },
            "actions": {
                "start": {
                    "title": "Start heating",
                    "description": "Starts the heating process",
                    "forms": [
                        {
                            "mqv:topic": "microwave/start",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "stop": {
                    "title": "Stop Heating",
                    "description": "Stops the heating process",
                    "forms": [
                        {
                            "mqv:topic": "microwave/stop",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
        }
    )
