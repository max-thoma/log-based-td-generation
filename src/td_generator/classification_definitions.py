import datetime
from typing import List

from pydantic import BaseModel, Field

from td import (
    AffordanceType,
    AttributeType,
    Forms,
    BaseProperty,
    Action,
    Event,
    Property,
    ThingDescription,
)


class ExperimentResult(BaseModel):
    base_td: ThingDescription
    prompts: List[str] = []
    msg_log: str = "N/A"
    successful: int
    failed: int
    llm_td_lst: List[ThingDescription]


class ExperimentResultList(BaseModel):
    model: str
    temperature: float
    number_of_retries: int
    iterations_per_td: int
    time_elapsed: datetime.time
    think_enabled: bool
    results: List[ExperimentResult]


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

    def __str__(self):
        return f"title: '{self.title}' description: '{self.description}' affordance_type: '{self.affordance_type.value}' type: '{self.type.value}' is_enum: '{self.is_enum}'"


class ThingDescriptionSkeleton(BaseModel):
    properties: dict = Field(default_factory=dict)
    events: dict = Field(default_factory=dict)
    actions: dict = Field(default_factory=dict)

    def add_affordance(
        self,
        classification: ClassificationAffordance,
        form: Forms,
        enum: List[str],
        properties=None,
    ):
        prop = BaseProperty()
        prop.type = classification.type
        _enum = None
        if classification.is_enum:
            prop.enum = enum
            _enum = enum

        if properties is not None:
            prop.properties = properties

        match classification.affordance_type:
            case AffordanceType.action:
                assert self.actions.get(classification.name, None) is None
                self.actions[classification.name] = Action(
                    title=classification.title,
                    description=classification.description,
                    input=prop,
                    output=BaseProperty(),
                    forms=[form],
                )
            case AffordanceType.event:
                assert self.events.get(classification.name, None) is None
                self.events[classification.name] = Event(
                    title=classification.title,
                    description=classification.description,
                    data=prop,
                    forms=[form],
                )
            case AffordanceType.property:
                assert self.properties.get(classification.name, None) is None
                self.properties[classification.name] = Property(
                    title=classification.title,
                    description=classification.description,
                    enum=_enum,  # otherwise the enum is only saved in properties.enum
                    type=classification.type,
                    forms=[form],
                    properties=prop.properties,
                )
            case _:
                assert False


class _ClassificationProperty(BaseModel):
    type: AttributeType = AttributeType.null


class ClassificationObject(BaseModel):
    properties: dict[str, _ClassificationProperty]

    def convert(self):
        """
        Converts a ClassificationObject to a TD BaseProperty
        :return: a BaseProperty
        """
        d = {}
        for key, value in self.properties.items():
            d[key] = BaseProperty(type=value.type)

        return BaseProperty(properties=d)


class ClassificationTD(BaseModel):
    type: str = Field(
        alias="@type",
        description="Is the type of the Thing that the Thing Description models",
    )
    title: str = Field(description="A short title that describes the Thing")
    id: str = Field(description="A URN")
    description: str = Field(description="A short description of the Thing")
