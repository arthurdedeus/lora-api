"""
Accounts: Custom providers
"""
###
# Libraries
###
from allauth.socialaccount.adapter import get_adapter
from allauth.socialaccount.models import (
    SocialLogin,
    SocialAccount
)


###
# Auxiliary functions
###
def custom_social_login_from_response(provider, request, response):
    adapter = get_adapter(request)
    uid = provider.extract_uid(response)
    extra_data = provider.extract_extra_data(response)
    common_fields = provider.extract_common_fields(response)
    socialaccount = SocialAccount(
        extra_data=extra_data, uid=uid, provider=provider.id
    )
    common_fields['photo'] = socialaccount.get_avatar_url()
    email_addresses = provider.extract_email_addresses(response)
    provider.cleanup_email_addresses(
        common_fields.get('email'), email_addresses
    )
    sociallogin = SocialLogin(
        account=socialaccount, email_addresses=email_addresses
    )
    if request.user.is_authenticated:
        sociallogin.user = request.user
        sa = SocialAccount.objects.filter(uid=uid, provider=provider.id).first()
        if sa:
            if request.user != sa.user:
                # TODO: Merge
                sa.user.delete()
    else:
        user = sociallogin.user = adapter.new_user(request, sociallogin)
        user.set_unusable_password()
        adapter.populate_user(request, sociallogin, common_fields)

    return sociallogin


###
# Custom classes
###


###
# Signals
###
