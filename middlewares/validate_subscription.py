def validate_subs(subscription):
    subscription_list = ["free", "basic", "premium"]
    if (subscription in subscription_list):
        return True
    else:
        return False
