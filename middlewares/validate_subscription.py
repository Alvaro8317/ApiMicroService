def validate_subs(subscription, subscription_list):
    if (subscription in subscription_list.keys()):
        return True
    else:
        return False
