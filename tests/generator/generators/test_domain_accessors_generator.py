from cdpify.generator.generators import accessors
from cdpify.generator.schemas import Domain


def test_generates_typed_cached_domain_accessors() -> None:
    output = accessors.generate([Domain(domain="Page"), Domain(domain="DOMStorage")])

    assert "class CDPDomains(CDPCommandSender):" in output
    assert "from .page import PageClient" in output
    assert "from .domstorage import DOMStorageClient" in output
    assert "@cached_property" in output
    assert "def page(self) -> PageClient:" in output
    assert "def dom_storage(self) -> DOMStorageClient:" in output
