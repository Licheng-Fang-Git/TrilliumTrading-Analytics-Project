"""
Helpers for using the LinkedIn OAuth token that allauth stores per user.

Fetching organization-level data (company page posts, follower counts) requires
LinkedIn's Community Management API / Marketing Developer Platform product, which
LinkedIn only grants after a manual app review tied to a specific Company Page,
plus additional scopes (e.g. r_organization_social, rw_organization_admin) beyond
the basic "Sign In" scopes configured for login. Until that product is approved,
calls to organization endpoints below will fail regardless of code changes.
"""
from allauth.socialaccount.models import SocialToken


def get_linkedin_access_token(user):
    """Return the stored LinkedIn access token for this user, or None if absent."""
    token = SocialToken.objects.filter(
        account__user=user, account__provider='linkedin_oauth2'
    ).first()
    return token.token if token else None
