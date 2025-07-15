from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@context": ["https://www.w3.org/2019/wot/td/v1"],
            "id": "lock",
            "title": "Smart Lock",
            "description": "A lock that can be monitored, locked and unlocked remotely",
            "@type": "Home Security Device",
            "base": "http://127.0.0.1:5000",
            "owl:sameAs": "test",
            "securityDefinitions": {"basic_sc": {"scheme": "basic", "in": "header"}},
            "security": ["basic_sc"],
            "properties": {
                "locked": {
                    "title": "Locking Mechanism Status",
                    "type": "boolean",
                    "description": "Property stating if the locked is currently locked(True) or unlocked(False)",
                    "forms": [
                        {
                            "mqv:topic": "lock",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                }
            },
            "actions": {
                "lock": {
                    "title": "Lock",
                    "description": "Locks the lock securing connected objects",
                    "forms": [
                        {
                            "mqv:topic": "lock/lock",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "unlock": {
                    "title": "Unlock",
                    "description": "Unlocks the lock making connected objects accessible.",
                    "forms": [
                        {
                            "mqv:topic": "lock/unlock",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
        }
    )
