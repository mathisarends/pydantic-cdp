import pytest

from cdpify.exceptions import CDPCommandException
from cdpify.shared.decorators import deprecated


def test_cdp_command_exception_uses_defaults() -> None:
    error = CDPCommandException({})

    assert error.code == -1
    assert error.message == "Unknown error"
    assert error.data is None
    assert str(error) == "CDP Error -1: Unknown error"


def test_deprecated_sync_function_logs_warning(
    caplog: pytest.LogCaptureFixture,
) -> None:
    @deprecated()
    def old_fn(value: int) -> int:
        return value + 1

    with caplog.at_level("WARNING"):
        result = old_fn(1)

    assert result == 2
    assert "old_fn is deprecated" in caplog.text


@pytest.mark.asyncio
async def test_deprecated_async_function_logs_warning(
    caplog: pytest.LogCaptureFixture,
) -> None:
    @deprecated()
    async def old_async_fn(value: int) -> int:
        return value + 2

    with caplog.at_level("WARNING"):
        result = await old_async_fn(1)

    assert result == 3
    assert "old_async_fn is deprecated" in caplog.text
