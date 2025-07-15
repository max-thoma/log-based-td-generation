from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "title": "Thermostat",
            "@context": [
                "https://www.w3.org/2022/wot/td/v1.1",
                "https://webthings.io/schemas",
            ],
            "@type": "Thermostat",
            "profile": [
                "https://www.w3.org/2022/wot/profile/http-basic/v1",
                "https://www.w3.org/2022/wot/profile/http-sse/v1",
            ],
            "description": "A thermostat that can be uses the measure the room temperature and set the cooling as well as heating temperature",
            "mqv:topic": "things/id-24",
            "properties": {
                "temperature": {
                    "name": "temperature",
                    "value": 20,
                    "title": "Temperature",
                    "description": "Currently measured temperature in degree celsius",
                    "type": "number",
                    "@type": "TemperatureProperty",
                    "unit": "degree celsius",
                    "minimum": 17,
                    "maximum": 28,
                    "readOnly": True,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-24/properties/temperature"},
                        {
                            "mqv:topic": "things/id-24/properties/temperature",
                            "op": ["observeproperty", "unobserveproperty"],
                            "subprotocol": "sse",
                        },
                    ],
                },
                "heatingTargetTemperature": {
                    "name": "heatingTargetTemperature",
                    "value": 19,
                    "title": "Heating Target",
                    "description": "The target heating temperature",
                    "type": "number",
                    "@type": "TargetTemperatureProperty",
                    "unit": "degree celsius",
                    "minimum": 10,
                    "maximum": 38,
                    "multipleOf": 0.1,
                    "links": [],
                    "forms": [
                        {
                            "mqv:topic": "things/id-24/properties/heatingTargetTemperature"
                        },
                        {
                            "mqv:topic": "things/id-24/properties/heatingTargetTemperature",
                            "op": ["observeproperty", "unobserveproperty"],
                            "subprotocol": "sse",
                        },
                    ],
                },
                "coolingTargetTemperature": {
                    "name": "coolingTargetTemperature",
                    "value": 25,
                    "title": "Cooling Target",
                    "description": "The target cooling temperature",
                    "type": "number",
                    "@type": "TargetTemperatureProperty",
                    "unit": "degree celsius",
                    "minimum": 10,
                    "maximum": 38,
                    "multipleOf": 0.1,
                    "links": [],
                    "forms": [
                        {
                            "mqv:topic": "things/id-24/properties/coolingTargetTemperature"
                        },
                        {
                            "mqv:topic": "things/id-24/properties/coolingTargetTemperature",
                            "op": ["observeproperty", "unobserveproperty"],
                            "subprotocol": "sse",
                        },
                    ],
                },
                "heatingCooling": {
                    "name": "heatingCooling",
                    "description": "Select between cooling, heating, or turning both off",
                    "value": "heating",
                    "title": "Heating/Cooling",
                    "type": "string",
                    "@type": "HeatingCoolingProperty",
                    "enum": ["off", "heating", "cooling"],
                    "readOnly": True,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-24/properties/heatingCooling"},
                        {
                            "mqv:topic": "things/id-24/properties/heatingCooling",
                            "op": ["observeproperty", "unobserveproperty"],
                            "subprotocol": "sse",
                        },
                    ],
                },
                "thermostatMode": {
                    "name": "thermostatMode",
                    "value": "heat",
                    "title": "Mode",
                    "description": "The thermostate supports the modes heat, cool, off or auto.",
                    "type": "string",
                    "@type": "ThermostatModeProperty",
                    "enum": ["off", "heat", "cool", "auto"],
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-24/properties/thermostatMode"},
                        {
                            "mqv:topic": "things/id-24/properties/thermostatMode",
                            "op": ["observeproperty", "unobserveproperty"],
                            "subprotocol": "sse",
                        },
                    ],
                },
            },
            "actions": {},
            "events": {},
            "links": [
                {
                    "rel": "alternate",
                    "type": "text/html",
                    "mqv:topic": "things/id-24",
                },
                {
                    "rel": "alternate",
                    "mqv:topic": "wss://plugfest.webthings.io/things/id-24",
                },
            ],
            "forms": [
                {
                    "mqv:topic": "things/id-24/properties",
                    "op": ["readallproperties", "writemultipleproperties"],
                },
                {
                    "mqv:topic": "things/id-24/properties",
                    "op": ["observeallproperties", "unobserveallproperties"],
                    "subprotocol": "sse",
                },
            ],
            "layoutIndex": 22,
            "selectedCapability": "Thermostat",
            "iconHref": "null",
            "group_id": "null",
            "id": "https://plugfest.webthings.io/things/id-24",
            "base": "https://plugfest.webthings.io/",
            "securityDefinitions": {
                "oauth2_sc": {
                    "scheme": "oauth2",
                    "flow": "code",
                    "authorization": "https://plugfest.webthings.io/oauth/authorize",
                    "token": "https://plugfest.webthings.io/oauth/token",
                    "scopes": [
                        "/things/id-24:readwrite",
                        "/things/id-24",
                        "/things:readwrite",
                        "/things",
                    ],
                }
            },
            "security": "oauth2_sc",
        }
    )
