"""Generated command models from CDP specification"""
# Domain: ServiceWorker Commands

from pydantic_cpd.cdp.base import CDPModel

from .types import *


class DeliverpushmessageParams(CDPModel):
    origin: str
    registration_id: RegistrationID
    data: str


class DispatchsynceventParams(CDPModel):
    origin: str
    registration_id: RegistrationID
    tag: str
    last_chance: bool


class DispatchperiodicsynceventParams(CDPModel):
    origin: str
    registration_id: RegistrationID
    tag: str


class SetforceupdateonpageloadParams(CDPModel):
    force_update_on_page_load: bool


class SkipwaitingParams(CDPModel):
    scope_u_r_l: str


class StartworkerParams(CDPModel):
    scope_u_r_l: str


class StopworkerParams(CDPModel):
    version_id: str


class UnregisterParams(CDPModel):
    scope_u_r_l: str


class UpdateregistrationParams(CDPModel):
    scope_u_r_l: str
