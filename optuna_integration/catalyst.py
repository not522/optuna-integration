import optuna
from optuna._deprecated import deprecated_class
from packaging import version

from optuna_integration._imports import try_import


with try_import() as _imports:
    import catalyst

    if version.parse(catalyst.__version__) < version.parse("21.3"):
        raise ImportError(
            f"You don't have Catalyst>=21.3 installed! Catalyst version: {catalyst.__version__}"
        )
    from catalyst.dl import OptunaPruningCallback

if not _imports.is_successful():
    OptunaPruningCallback = object  # NOQA


@deprecated_class("2.7.0", "4.0.0")
class CatalystPruningCallback(OptunaPruningCallback):
    """Catalyst callback to prune unpromising trials.

    This class is an alias to Catalyst's
    `OptunaPruningCallback <https://catalyst-team.github.io/catalyst/api/callbacks.html?highlight=optuna#catalyst.callbacks.optuna.OptunaPruningCallback>`_.

    See the Catalyst's documentation for the detailed description.
    """  # NOQA

    def __init__(
        self,
        trial: "optuna.Trial",
        loader_key: str,
        metric_key: str,
        minimize: bool,
        min_delta: float = 1e-6,
    ):
        _imports.check()
        super().__init__(trial, loader_key, metric_key, minimize, min_delta)
