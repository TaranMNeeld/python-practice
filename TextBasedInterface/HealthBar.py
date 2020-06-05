def render_bar(max_hp, current_hp):
    text_color = ''
    bar_length = 50
    fill_ratio = int((current_hp / max_hp) * bar_length)
    empty_ratio = bar_length - fill_ratio

    if fill_ratio >= 35:
        text_color = '\033[32m'
    elif 35 > fill_ratio > 20:
        text_color = '\033[33m'
    else:
        text_color = '\033[31m'

    filler_text = f'{text_color}|' * fill_ratio
    empty_text = '-' * empty_ratio
    health_bar = f'{current_hp}/{max_hp} [{filler_text}{empty_text}\033[0m]'
    print(health_bar)



