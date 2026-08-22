"""Runtime behavior shared by generated CDP models and events."""

from dataclasses import dataclass, field

from cdpify.codec import decode_cdp, encode_cdp
from cdpify.domains.accessibility import AXNode
from cdpify.domains.dom.commands import GetOuterHTMLParams
from cdpify.domains.page.events import LifecycleEventEvent


@dataclass(kw_only=True, slots=True)
class _Sample:
    value: int = field(metadata={"cdp_name": "value"})
    cdp_session_id: str | None = field(
        default=None,
        repr=False,
        compare=False,
        metadata={"cdp": False},
    )


class TestSessionCapture:
    def test_regular_models_do_not_carry_session_metadata(self) -> None:
        params = GetOuterHTMLParams(backend_node_id=7)

        assert not hasattr(params, "cdp_session_id")

    def test_captures_injected_cdp_session_id(self) -> None:
        model = decode_cdp(_Sample, {"value": 1}, cdp_session_id="SESSION-A")
        assert model.value == 1
        assert model.cdp_session_id == "SESSION-A"

    def test_defaults_to_none_for_root_session(self) -> None:
        # Root-target events arrive with no session id.
        model = decode_cdp(_Sample, {"value": 1})
        assert model.cdp_session_id is None

    def test_instances_do_not_share_session_id(self) -> None:
        a = decode_cdp(_Sample, {"value": 1}, cdp_session_id="A")
        b = decode_cdp(_Sample, {"value": 2}, cdp_session_id="B")
        root = decode_cdp(_Sample, {"value": 3})
        assert (a.cdp_session_id, b.cdp_session_id, root.cdp_session_id) == (
            "A",
            "B",
            None,
        )

    def test_session_id_excluded_from_outbound_params(self) -> None:
        model = decode_cdp(_Sample, {"value": 1}, cdp_session_id="A")
        params = encode_cdp(model)
        assert "cdpSessionId" not in params
        assert "cdp_session_id" not in params

    def test_models_are_mutable_and_slotted(self) -> None:
        model = _Sample(value=1)

        assert not hasattr(model, "__dict__")
        model.value = 2
        assert model.value == 2

    def test_works_on_generated_event_models(self) -> None:
        event = decode_cdp(
            LifecycleEventEvent,
            {
                "frameId": "F1",
                "loaderId": "L1",
                "name": "networkIdle",
                "timestamp": 12.5,
            },
            cdp_session_id="SESSION-Z",
        )
        assert event.name == "networkIdle"
        assert event.cdp_session_id == "SESSION-Z"


class TestAcronymFieldNames:
    """Field names come from the generator's snake case; from_cdp has to use
    the same one. A mismatch is silent — the field just stays None."""

    def test_fills_field_behind_an_acronym_wire_key(self) -> None:
        node = decode_cdp(
            AXNode, {"nodeId": "1", "ignored": False, "backendDOMNodeId": 42}
        )
        assert node.backend_dom_node_id == 42

    def test_round_trips_acronym_field_back_to_the_wire_name(self) -> None:
        params = GetOuterHTMLParams(backend_node_id=7, include_shadow_dom=True)
        assert encode_cdp(params) == {
            "backendNodeId": 7,
            "includeShadowDOM": True,
        }
