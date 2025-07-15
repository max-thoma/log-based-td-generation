# Introduction

This repository holds the prototypical implementation of the proposed methodology for the paper “Utilizing Large Language Models for Log-Based Automated Thing Description Generation” submitted to the SEMANTICS 2025. Moreover, we also included a full usage example. The original dataset of the paper can be found [here](https://doi.org/10.5281/zenodo.15526223).

## Paper TLDR

Web of Things (WoT) [Thing Descriptions](https://www.w3.org/TR/wot-thing-description11/) (TDs) can increase the semantic interoperability in IoT systems. However, for many new and existing devices no TD has been created yet. This hinders the adoption of the WoT. Therefore, we propose an LLM based methodology that generates TDs from MQTT message logs. We specifically target brownfield systems that have already been set up and want to adopt the WoT ecosystem. MQTT message log have the advantage that they do not require special tooling to create. Simply subscribing to the wildcard topic: `*` and writing the messages to a file is sufficient. In the following we present the methodology with a concrete example from one of our experiments using Google's `gemini-flash-2.0` LLM. The full trace of the experiment can be found in `data/llm_results/gemini.json`. For the sources of the device please refer to the [Custom Dataset](#custom-dataset) section.

# Example from Message Logs to TD

Assume that we have logged the following MQTT messages from an *RGB Lightbulb* by subscribing to `application/bulb/*`:

```
topic: application/bulb/status; payload: On; retain: true
topic: application/bulb/status; payload: Off; retain: true
topic: application/bulb/status; payload: Failed; retain: true
topic: application/bulb/set; payload: {'r': 141, 'g': 48, 'b': 194}; retain: false
topic: application/bulb/set; payload: {'r': 194, 'g': 3, 'b': 21}; retain: false
topic: application/bulb/set; payload: {'r': 72, 'g': 160, 'b': 103}; retain: false
topic: application/bulb/set; payload: {'r': 44, 'g': 48, 'b': 63}; retain: false
topic: application/bulb/set; payload: {'r': 15, 'g': 55, 'b': 86}; retain: false
topic: application/bulb/power; payload: true; retain: false
topic: application/bulb/power; payload: false; retain: false
topic: application/bulb/power; payload: true; retain: false
topic: application/bulb/power; payload: false; retain: false
```

We observe that this message log paints a clear picture of the capabilities of the RGB Lightbulb: it can report its status, allows for setting the color, and can be remotely turned on and off. In a WoT TD, these features are called _affordances_ and are categorized into: _actions_, _events_, and _properties_. In the message log, there are three MQTT topics that correspond to an _affordance_ of the device. For each topic, we instruct an LLM to determine what kind of WoT TD _affordance_ would best describe it:

```
Given is the following MQTT message log of an IoT device:

topic: application/bulb/status; payload: On; retain: true
topic: application/bulb/status; payload: Off; retain: true
topic: application/bulb/status; payload: Failed; retain: true
topic: application/bulb/set; payload: {'r': 141, 'g': 48, 'b': 194}; retain: false
topic: application/bulb/set; payload: {'r': 194, 'g': 3, 'b': 21}; retain: false
topic: application/bulb/set; payload: {'r': 72, 'g': 160, 'b': 103}; retain: false
topic: application/bulb/set; payload: {'r': 44, 'g': 48, 'b': 63}; retain: false
topic: application/bulb/set; payload: {'r': 15, 'g': 55, 'b': 86}; retain: false
topic: application/bulb/power; payload: true; retain: false
topic: application/bulb/power; payload: false; retain: false
topic: application/bulb/power; payload: true; retain: false
topic: application/bulb/power; payload: false; retain: false

For this the following part of the message log:

topic: application/bulb/status; payload: On; retain: true
topic: application/bulb/status; payload: Off; retain: true
topic: application/bulb/status; payload: Failed; retain: true


Determine what kind of affordance this is!
```

To ensure that the generated _affordance_ is compliant with the WoT TD specification, we modeled part of the TD specification as a Python class. With the help of the [Instructor](https://python.useinstructor.com) library, we provide this as a shema to the LLM and check that the response of the LLM is conforming to the schema.

```python
class ClassificationAffordance(BaseModel):
    title: str = Field(description="A short title for the affordance")
    description: str = Field(description="A description of the affordance")
    name: str = Field(
        description="Name of the affordance in camel case e.g. 'myAffordanceName'"
    )
    # Using the official definitions from the WoT TD specification (https://www.w3.org/TR/wot-thing-description11/)
    affordance_type: AffordanceType = Field(
        description="The type of the affordance: actions: An Interaction Affordance that allows to invoke a function of the Thing, which manipulates state (e.g., toggling a lamp on or off) or triggers a process on the Thing (e.g., dim a lamp over time). events: An Interaction Affordance that describes an event source, which asynchronously pushes event data to Consumers (e.g., overheating alerts). property: An Interaction Affordance that exposes state of the Thing. This state can then be retrieved (read) and/or updated (write). Things can also choose to make Properties observable by pushing the new state after a change."
    )
    type: AttributeType = Field(
        alias="@type",
        description="The data type of the affordance. boolean: a boolean data type, it is represented by 'true' and 'false'. number: The most general numeric data type, it is used to represent floating point numbers, but not integers. integer: the data type used to represent integer numbers. object: the data type is used to describe complex, dictionary/JSON like objects. string: the data type is used to describe strings. null: this data type is used to describe null data, i.e., no data, it is indicated by 'null'",
    )
    is_enum: bool = Field(
        description="Whether the affordance is composed of a list of ENUM string values. This is only applicable if the affordance is of type string",
    )
```

After all conformance checks have passed, the LLM returns an _affordance_ that describes what was observed in the MQTT message log:

```json
"properties": {
   "bulbStatus":{
      "title":"Bulb Status",
      "description":"The current status of the bulb (On, Off, Failed)",
      "type":"string",
      "enum":[
         "On",
         "Off",
         "Failed"
      ],
      "properties":{},
      "forms":[
         {
            "href":"mqtt://broker.emqx.io:1883",
            "mqv:topic":"application/bulb/status",
            "mqv:retain":true
         }
      ]
   }
}
```

After instructing the LLM for all _affordances_ that are found in the message log, we bundle them, and prompt the LLM to create the "toplevel" description of the device.

```
Give is the following partial Thing Description (TD)
{
    "properties": {...},
    "events": {...},
    "actions": {...}
}

Determine for what kind of device this Thing Description models!
```

As before, the LLM also receives a schema that it has to follow for this step:

```python
class ClassificationTD(BaseModel):
    type: str = Field(
        alias="@type",
        description="Is the type of the Thing that the Thing Description models",
    )
    title: str = Field(description="A short title that describes the Thing")
    id: str = Field(description="A URN")
    description: str = Field(description="A short description of the Thing")
```

Then, everything is assembled to a final TD (some null values were removed for brevity):

```json
{
   "@context": [
      "https://www.w3.org/2022/wot/td/v1.1"
   ],
   "@type": "SmartBulb",
   "title": "Smart Bulb",
   "id": "urn:example:smartbulb",
   "securityDefinitions": {
      "nosec_sc": {
         "scheme": "nosec"
      }
   },
   "security": [
      "nosec_sc"
   ],
   "description": "A smart bulb that can be controlled remotely.",
   "properties": {
      "bulbStatus": {
         "title": "Bulb Status",
         "description": "The current status of the bulb (On, Off, Failed)",
         "type": "string",
         "enum": [
            "On",
            "Off",
            "Failed"
         ],
         "properties": {},
         "forms": [
            {
               "href": "mqtt://broker.emqx.io:1883",
               "contentType": null,
               "mqv:topic": "application/bulb/status",
               "mqv:retain": true
            }
         ]
      },
      "powerStatus": {
         "title": "Power Status",
         "description": "Control the power state of the bulb.",
         "type": "boolean",
         "enum": null,
         "properties": {},
         "forms": [
            {
               "href": "mqtt://broker.emqx.io:1883",
               "contentType": null,
               "mqv:topic": "application/bulb/power",
               "mqv:retain": false
            }
         ]
      }
   },
   "events": {},
   "actions": {
      "setColor": {
         "title": "Set Color",
         "description": "Sets the color of the bulb using RGB values.",
         "input": {
            "title": "",
            "description": "",
            "type": "object",
            "enum": null,
            "properties": {
               "r": {
                  "title": "",
                  "description": "",
                  "type": "integer",
                  "enum": null,
                  "properties": {}
               },
               "g": {
                  "title": "",
                  "description": "",
                  "type": "integer",
                  "enum": null,
                  "properties": {}
               },
               "b": {
                  "title": "",
                  "description": "",
                  "type": "integer",
                  "enum": null,
                  "properties": {}
               }
            }
         },
         "output": {
            "title": "",
            "description": "",
            "type": "null",
            "enum": null,
            "properties": {}
         },
         "forms": [
            {
               "href": "mqtt://broker.emqx.io:1883",
               "contentType": null,
               "mqv:topic": "application/bulb/set",
               "mqv:retain": false
            }
         ]
      }
   }
}
```
The LLM chose to model the `powerStatus` not as an _action_, but as a _property_. This highlights that in asynchronous protocols such as MQTT the lines between the affordance types _action_, _event_ and _property_ a more blurred.

# Basic Usage

It is recommended to us [poetry](https://python-poetry.org) and the `pyproject.toml` file to install the dependencies of this project.

```bash
cd src/
poetry install
```

The main implementation of our methodology can be found in `classification.py`. To run call:

```bash
poetry run python classification.py -m MODEL_NAME -t TEMPERATURE -i ITERATIONS -r RETRIES [-b BASE_URL] [--think]
```

Do not forget to save your API keys as environment variables, or in a `.env` file in the `src/td_generator` directory.

```
OPENAI_API_KEY=""
LOCAL_AI_API_KEY=""
GOOGLE_API_KEY=""
```

## Arguments

- `-m` or `--model`: Required. The name of the model to use. Available options:
  
  - gpt-4o
  - cogito:70b
  - And more (see code for full list)

- `-t` or `--temperature`: Required. Float value for temperature setting

- `-i` or `--iterations_per_td`: Required. Integer value for iterations per test data point

- `-r` or `--number_of_retries`: Required. Integer value for the number of retries in case the LLM fails

- `-b` or `--base_url`: Optional. Base URL for the experiment (defaults to None)

- `--think`: Optional. Boolean flag for thinking mode (defaults to False)

## Examples

```bash
# Run experiment with gpt-4o
poetry run python classification.py -m GPT-4o -t 0.7 -i 5 -r 10

# Run experiment with cogito:70b and local ollama instance
poetry run python classification.py -m cogito:70b -t 0.5 -i 5 -r 3 -b http://localhost:11434/v1/
```

# Result Analysis

The script `functional_equivalence.py` generates the report of the functional accuracy metrics, and the script `manual_desriptive_equivalence.py` generates the tables for the descriptive accuracy metrics.

For both scripts, set the path to the output file of the `classification.py.` Per default, it is set to analyze our results. For the `manual_desriptive_equivalence.py` script, you may also have to set the `api_key` if you want to use the text embedding analysis.

Our results used in the paper can be found in the `data` directory.

| Directory                 | Description                                   |
| ------------------------- | --------------------------------------------- |
| data/automatic_evaluation | The cosine-similarity and correlation results |
| data/llm_results          | The raw output of the LLM experiment          |
| data/manual_evaluation    | The manually scored dataset                   |
| data/devices              | A list of all device types                    |
| data/percent_affordances  | The distribution of affordances               |

# Custom Dataset

The `things` module holds all our reference TD.

For General inspiration, we consulted the following sources.

| Project                        | Link                                                                           |
| ------------------------------ | ------------------------------------------------------------------------------ |
| HomeAssistant Integration      | https://www.home-assistant.io/integrations/                                    |
| EVCC documentation             | https://evcc.io                                                                |
| SmartDataModels                | https://smartdatamodels.org                                                    |
| WoT TD Specification           | https://www.w3.org/TR/wot-thing-description11/                                 |
| WoT MQTT Binding Specification | https://w3c.github.io/wot-binding-templates/bindings/protocols/mqtt/index.html |
| Eclipse ThingWeb               | https://thingweb.io                                                            |
| Wikipedia SAE J1772 Article    | https://en.wikipedia.org/wiki/SAE_J1772                                        |
| WebThings                      | https://webthings.io                                                           |
| Tasmota                        | https://github.com/arendst/Tasmota                                             |

See the table below to see what was the primary source of inspiration for each TD.

| Thing Description        | Main source of inspiration                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Alarm Control Panel      | https://www.home-assistant.io/integrations/alarm_control_panel.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Alarm Siren              | https://www.home-assistant.io/integrations/siren.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Binary Window Contact    | https://www.home-assistant.io/integrations/binary_sensor.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Button                   | https://www.home-assistant.io/integrations/button.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Ceiling Fan              | https://www.home-assistant.io/integrations/fan.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Door Lock                | https://www.home-assistant.io/integrations/lock.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Doorbell                 | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Electric Vehicle         | https://docs.evcc.io/docs/devices/vehicles                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Electric Vehicle Charger | https://docs.evcc.io/docs/devices/chargers                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Humidifier               | https://www.home-assistant.io/integrations/humidifier.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                           |
| HVAC Unit                | https://www.home-assistant.io/integrations/climate.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Illuminance Sensor       | https://w3c.github.io/wot-binding-templates/bindings/protocols/mqtt/index.html#conformance,  <br/>https://www.w3.org/TR/wot-thing-description11/#example-69                                                                                                                                                                                                                                                                                                                           |
| Lawn Mower               | https://www.home-assistant.io/integrations/lawn_mower.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Lightbulb (RGB)          | https://www.home-assistant.io/integrations/light.mqtt/, <br/>https://www.w3.org/TR/wot-thing-description11/                                                                                                                                                                                                                                                                                                                                                                           |
| Lightbulb (Single Color) | https://www.home-assistant.io/integrations/light.mqtt/, <br/>https://www.w3.org/TR/wot-thing-description11/                                                                                                                                                                                                                                                                                                                                                                           |
| Location Tracker (GPS)   | https://www.home-assistant.io/integrations/device_tracker.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Photovoltaic Inverter    | https://github.com/smart-data-models/dataModel.GreenEnergy/tree/master/PhotovoltaicMeasurement,  <br/>https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.GreenEnergy/PhotovoltaicDevice/swagger.yaml,  <br/>https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.S4BLDG/SolarDevice/swagger.yaml,  <br/>https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Energy/SolarEnergy/swagger.yaml |
| Photovoltaic Panel       | https://github.com/smart-data-models/dataModel.GreenEnergy/tree/master/PhotovoltaicMeasurement,  <br/>https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.GreenEnergy/PhotovoltaicDevice/swagger.yaml,  <br/>https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.S4BLDG/SolarDevice/swagger.yaml,  <br/>https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Energy/SolarEnergy/swagger.yaml |
| Smart Meter              | https://docs.evcc.io/docs/devices/meters                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Switch                   | https://www.home-assistant.io/integrations/switch.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Vacuum Cleaner           | https://www.home-assistant.io/integrations/vacuum.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Window Cover             | https://www.home-assistant.io/integrations/cover.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                                |

See the table down below to see which licenses these projects use.

| Project                        | License                                                       |
| ------------------------------ | ------------------------------------------------------------- |
| HomeAssistant Integration      | Attribution-NonCommercial-ShareAlike 4.0 International        |
| EVCC documentation             | MIT License                                                   |
| SmartDataModels                | Creative Commons Attribution 4.0 International Public License |
| WoT TD Specification           | Software and Document license - 2023 version                  |
| WoT MQTT Binding Specification | Software and Document license - 2015 version                  |

# W3C WebThings Dataset

[Source](https://github.com/w3c/wot-testing/tree/037c8d686ad8c145dd4fe01c2123ad26eca0e185/data/input_2022/TD/WebThings)

Changes:

- Removed non-devices and demo TD
- Changed the `href` to `mqv:topic`
- Added enum values to some string attributes
- Added missing descriptions
- Removed any reference to being a virtual device
- Deleted double entries (smart plug) etc

License: Unspecified, presumably Software and Document license - 2023 version

# Kinder et. al Dataset

[Source](https://gitlab.kit.edu/lukas.kinder/plannning_with_thing_descriptions_akr3/-/tree/main/WoT-TD?ref_type=heads)

Changes:

- Converted to MQTT topics
- Added some missing descriptions
- Removed Automated Warehouse as not in our domain
- Removed Chiller no forms data
- Naturally extended topics and made them unique
  - i.e., boolean properties with `is_` or `_enabled`, `_full`, `has_`
  - Boolean and non-boolean: extended by affordance name
- Added missing titles
- Removed redDotImage from counter-
- Unified affordance titles (e.g., Smart Display)

License: Lukas Kinder