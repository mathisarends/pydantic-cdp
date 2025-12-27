"""Generated command models from CDP specification"""
# Domain: WebAuthn Commands

from pydantic_cpd.cdp.base import CDPModel

from .types import *


class EnableParams(CDPModel):
    """Enable the WebAuthn domain and start intercepting credential storage and
    retrieval with a virtual authenticator."""

    enable_u_i: bool | None = None


class AddvirtualauthenticatorParams(CDPModel):
    """Creates and adds a virtual authenticator."""

    options: VirtualAuthenticatorOptions


class AddvirtualauthenticatorResult(CDPModel):
    authenticator_id: AuthenticatorId


class SetresponseoverridebitsParams(CDPModel):
    """Resets parameters isBogusSignature, isBadUV, isBadUP to false if they are not present."""

    authenticator_id: AuthenticatorId
    is_bogus_signature: bool | None = None
    is_bad_u_v: bool | None = None
    is_bad_u_p: bool | None = None


class RemovevirtualauthenticatorParams(CDPModel):
    """Removes the given authenticator."""

    authenticator_id: AuthenticatorId


class AddcredentialParams(CDPModel):
    """Adds the credential to the specified authenticator."""

    authenticator_id: AuthenticatorId
    credential: Credential


class GetcredentialParams(CDPModel):
    """Returns a single credential stored in the given virtual authenticator that
    matches the credential ID."""

    authenticator_id: AuthenticatorId
    credential_id: str


class GetcredentialResult(CDPModel):
    credential: Credential


class GetcredentialsParams(CDPModel):
    """Returns all the credentials stored in the given virtual authenticator."""

    authenticator_id: AuthenticatorId


class GetcredentialsResult(CDPModel):
    credentials: list[Credential]


class RemovecredentialParams(CDPModel):
    """Removes a credential from the authenticator."""

    authenticator_id: AuthenticatorId
    credential_id: str


class ClearcredentialsParams(CDPModel):
    """Clears all the credentials from the specified device."""

    authenticator_id: AuthenticatorId


class SetuserverifiedParams(CDPModel):
    """Sets whether User Verification succeeds or fails for an authenticator.
    The default is true."""

    authenticator_id: AuthenticatorId
    is_user_verified: bool


class SetautomaticpresencesimulationParams(CDPModel):
    """Sets whether tests of user presence will succeed immediately (if true) or fail to resolve (if false) for an authenticator.
    The default is true."""

    authenticator_id: AuthenticatorId
    enabled: bool


class SetcredentialpropertiesParams(CDPModel):
    """Allows setting credential properties.
    https://w3c.github.io/webauthn/#sctn-automation-set-credential-properties"""

    authenticator_id: AuthenticatorId
    credential_id: str
    backup_eligibility: bool | None = None
    backup_state: bool | None = None
