from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@context": ["https://www.w3.org/2019/wot/td/v1"],
            "id": "ventilator",
            "title": "Ventilator",
            "@type": "Ventilator",
            "description": "A ventilator with three different intensity levels",
            "base": "http://127.0.0.1:5000",
            "owl:sameAs": "test",
            "securityDefinitions": {"basic_sc": {"scheme": "basic", "in": "header"}},
            "security": ["basic_sc"],
            "properties": {
                "status": {
                    "type": "string",
                    "enum": ["on", "off"],
                    "title": "Ventilator Operating Mode",
                    "description": "Displays the current status of the device",
                    "forms": [
                        {
                            "mqv:topic": "ventilator/status",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "level": {
                    "type": "integer",
                    "title": "Fan Speed Level",
                    "enum": [1, 2, 3],
                    "description": "Displays the current fan speed level",
                    "forms": [
                        {
                            "mqv:topic": "ventilator/level",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
            "actions": {
                "start": {
                    "title": "Activate Ventilator",
                    "description": "Starts the ventilator",
                    "forms": [
                        {
                            "mqv:topic": "ventilator/start",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "stop": {
                    "title": "Stop Ventilator",
                    "description": "Stops the ventilator",
                    "forms": [
                        {
                            "mqv:topic": "ventilator/stop",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "speed up": {
                    "title": "Increase Fan Speed",
                    "description": "Increases fan level",
                    "forms": [
                        {
                            "mqv:topic": "ventilator/up",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "speed down": {
                    "title": "Decrease Fan Speed",
                    "description": "Decreases fan level",
                    "forms": [
                        {
                            "mqv:topic": "ventilator/down",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
        }
    )
