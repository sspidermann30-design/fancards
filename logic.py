import json
import random


def get_random_card():
    # Открываем твой обновленный cards.json
    with open('web/cards.json', 'r', encoding='utf-8') as f:
        cards = json.load(f)

    # Выбираем редкость (шансы: 85% common, 12% rare, 3% epic)
    rarity = random.choices(
        ["common", "rare", "epic"],
        weights=[85, 12, 3]
    )[0]

    # Фильтруем карты по этой редкости
    suitable_cards = [c for c in cards if c['rarity'] == rarity]

    # Если таких карт нет (например, пока нет rare), берем любую из списка
    if not suitable_cards:
        return random.choice(cards)

    return random.choice(suitable_cards)