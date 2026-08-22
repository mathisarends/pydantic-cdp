from cdpify.generator.generators.base import BaseGenerator
from cdpify.generator.generators.utils import to_pascal_case
from cdpify.generator.generators.views import ImportBlockView
from cdpify.generator.rendering import render_template
from cdpify.generator.schemas import Domain


class InitGenerator(BaseGenerator):
    filename = "__init__.py"

    def generate(self, domain: Domain) -> str:
        type_names = [t.id for t in domain.types]
        command_names = self._command_names(domain)
        event_names = self._event_names(domain, type_names)
        client_name = f"{domain.domain}Client"

        event_exports = [self._exported_name(name) for name in event_names]
        all_names = sorted([*type_names, *command_names, *event_exports, client_name])

        return render_template(
            "domain_init.py.jinja2",
            header=self.HEADER,
            domain_name=domain.domain,
            import_blocks=tuple(
                ImportBlockView(module, tuple(names))
                for module, names in (
                    ("types", type_names),
                    ("commands", command_names),
                    ("events", event_names),
                )
                if names
            ),
            client_name=client_name,
            exports=tuple(all_names),
        )

    def _command_names(self, domain: Domain) -> list[str]:
        if not domain.commands:
            return []

        names = [f"{domain.domain}Command"]
        for cmd in domain.commands:
            pascal = to_pascal_case(cmd.name)
            if cmd.parameters:
                names.append(f"{pascal}Params")
            if cmd.returns:
                names.append(f"{pascal}Result")
        return sorted(names)

    def _event_names(self, domain: Domain, type_names: list[str]) -> list[str]:
        if not domain.events:
            return []

        enum_name = f"{domain.domain}Event"
        if enum_name in type_names:
            enum_name = f"{enum_name} as {enum_name}Name"

        names = [enum_name]
        names.extend(f"{to_pascal_case(e.name)}Event" for e in domain.events)
        return sorted(names)

    def _exported_name(self, imported_name: str) -> str:
        return imported_name.rsplit(" as ", maxsplit=1)[-1]
