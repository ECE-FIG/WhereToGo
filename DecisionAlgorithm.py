def moneyOptions(moneyList: list, budget: int):
    oneStar = [business for business in moneyList if
                len(business.get('price')) <= 1]
    twoStar = [business for business in moneyList if
                len(business.get('price')) <= 2]
    threeStar = [business for business in moneyList if
                len(business.get('price')) <= 3]
    fourStar = [business for business in moneyList if
                len(business.get('price')) <= 4]
    if budget == 1: return oneStar
    if budget == 2: return twoStar
    if budget == 3: return threeStar
    if budget == 4: return fourStar