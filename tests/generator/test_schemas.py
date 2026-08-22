from cdpify.generator.schemas import (
    CDPSpecs,
    Domain,
    ProtocolSpec,
    ProtocolVersion,
)


class TestParameterAlias:
    def test_ref_accepts_dollar_prefix(self) -> None:
        from cdpify.generator.schemas import Parameter

        param = Parameter.model_validate({"name": "p", "$ref": "NodeId"})
        assert param.ref == "NodeId"

    def test_ref_accepts_field_name(self) -> None:
        from cdpify.generator.schemas import Parameter

        param = Parameter(name="p", ref="NodeId")
        assert param.ref == "NodeId"


class TestCDPSpecs:
    def _make_specs(
        self, browser_domains: list[str], js_domains: list[str]
    ) -> CDPSpecs:
        version = ProtocolVersion(major="1", minor="3")
        return CDPSpecs(
            browser=ProtocolSpec(
                version=version,
                domains=[Domain(domain=name) for name in browser_domains],
            ),
            js=ProtocolSpec(
                version=version,
                domains=[Domain(domain=name) for name in js_domains],
            ),
        )

    def test_all_domains_concatenates(self) -> None:
        specs = self._make_specs(["DOM", "Page"], ["Runtime"])
        names = [d.domain for d in specs.all_domains]
        assert names == ["DOM", "Page", "Runtime"]

    def test_version_string(self) -> None:
        specs = self._make_specs([], [])
        assert specs.version_string == "1.3"

    def test_get_domain_finds_browser_domain(self) -> None:
        specs = self._make_specs(["DOM"], [])
        domain = specs.get_domain("DOM")
        assert domain is not None
        assert domain.domain == "DOM"

    def test_get_domain_finds_js_domain(self) -> None:
        specs = self._make_specs([], ["Runtime"])
        domain = specs.get_domain("Runtime")
        assert domain is not None
        assert domain.domain == "Runtime"

    def test_get_domain_returns_none_when_missing(self) -> None:
        specs = self._make_specs(["DOM"], [])
        assert specs.get_domain("Nonexistent") is None
