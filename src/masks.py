def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер карты по правилу: XXXX XX** **** XXXX
    """
    card_str = str(card_number)

    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    masked = card_str[:4] + " " + card_str[4:6] + "** " + "**** " + card_str[12:]
    return masked


def get_mask_account(number_score: int) -> str:
    """
    Маскирует номер счёта, оставляя видимыми только последние 4 цифры.
    """
    score_str = str(number_score)
    visible_part = score_str[-4:]
    mask = "**" + visible_part

    return mask
