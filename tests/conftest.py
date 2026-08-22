import pytest

from cdpify.generator.schemas import (
    Command,
    Domain,
    Event,
    Parameter,
    ProtocolSpec,
    ProtocolVersion,
    TypeDefinition,
)


@pytest.fixture
def simple_domain() -> Domain:
    """A small but realistic domain covering the common code paths."""
    return Domain(
        domain="Sample",
        types=[
            TypeDefinition(
                id="NodeId",
                type="integer",
                description="Unique DOM node identifier.",
            ),
            TypeDefinition(
                id="Color",
                type="string",
                enum=["red", "green", "blue"],
                description="A color enum.",
            ),
            TypeDefinition(
                id="Box",
                type="object",
                description="A bounding box.",
                properties=[
                    Parameter(name="width", type="integer"),
                    Parameter(name="height", type="integer"),
                    Parameter(name="label", type="string", optional=True),
                ],
            ),
        ],
        commands=[
            Command(
                name="getNode",
                description="Fetches a node by id.",
                parameters=[Parameter(name="nodeId", ref="NodeId")],
                returns=[Parameter(name="box", ref="Box")],
            ),
            Command(name="clear", description="Clears all nodes."),
            Command(
                name="legacyOp",
                deprecated=True,
                parameters=[Parameter(name="value", type="string")],
            ),
        ],
        events=[
            Event(
                name="nodeAdded",
                description="Fired when a node is added.",
                parameters=[
                    Parameter(name="nodeId", ref="NodeId"),
                    Parameter(name="parentId", ref="NodeId", optional=True),
                ],
            ),
            Event(name="cleared"),
        ],
    )


@pytest.fixture
def empty_domain() -> Domain:
    return Domain(domain="Empty")


@pytest.fixture
def cross_domain() -> Domain:
    """Domain referencing types from another domain."""
    return Domain(
        domain="Animation",
        types=[
            TypeDefinition(
                id="Track",
                type="object",
                properties=[Parameter(name="target", ref="DOM.NodeId")],
            ),
        ],
        commands=[
            Command(
                name="play",
                parameters=[Parameter(name="target", ref="DOM.NodeId")],
                returns=[
                    Parameter(
                        name="frames",
                        type="array",
                        items={"$ref": "DOM.NodeId"},
                    )
                ],
            ),
        ],
    )


@pytest.fixture
def sample_protocol_spec(simple_domain: Domain) -> ProtocolSpec:
    return ProtocolSpec(
        version=ProtocolVersion(major="1", minor="3"),
        domains=[simple_domain],
    )
