import time

from selenium import webdriver
from FlashScoreActions.FlashScoreModule import FlashScore
from FlashScoreActions.FlashScoreXpaths import BasicXpaths, TableResultsXpaths as TabXpath
from utils.SeleniumModule import SeleniumDriver


def open_necessary_page(number_match: int = 0,
                        url: str = None,
                        hidden: bool = False,
                        all_matches: bool = False) -> webdriver:
    """
    Open neccessary page and return webriver object
    """

    driver = SeleniumDriver(hidden=hidden)
    url = url if url is not None else 'https://www.flashscore.com.ua/football/england/premier-league-2022-2023/#/nunhS7Vn/table/overall'
    FlashScore.open_football_leagues(driver, url=url)

    if driver.xpath_checker('//*[@id="onetrust-accept-btn-handler"]'):
        driver.click_xpath('//*[@id="onetrust-accept-btn-handler"]')

    driver.click_xpath(BasicXpaths.ARCHIVE)
    season_xpath = f'//*[@id="tournament-page-archiv"]/div[3]/div[1]/a'
    season_obj = driver.click_xpath(season_xpath, click=False)
    season_name = season_obj.get_attribute('textContent').strip()
    season_obj.click()

    if all_matches:
        FlashScore.open_all_season_games(driver)
    matches = driver.get_elements('//*[@title="Подробности матча!"]')

    for number, match in enumerate(matches):
        if number == number_match:
            time.sleep(4)
            match.click()
            windows = driver.get_driver.window_handles
            driver.get_driver.switch_to.window(windows[1])
            return driver, season_name


def test_get_all_statistics_game():
    necessary_result = {'attack': ('Oтборы', '17', '9'),
                        'blows': ('Удары', '14', '6'),
                        'blows_by': ('Удары мимо', '6', '6'),
                        'corner': ('Угловые', '8', '4'),
                        'dangerous_attacks': ('Опасные атаки', '56', '35'),
                        'expected_goals': ('Ожидаемые голы (xG)Ожидаемые голы (xG) - количество '
                                           'вероятных голов, которое могла бы забить команда или '
                                           'игрок, исходя из качества и количества сделанных ударов.',
                                           '2.68',
                                           '0.51'),
                        'face_offs': ('Вбрасывания', '12', '14'),
                        'fouls': ('Фолы', '8', '11'),
                        'offsides': ('Офсайды', '1', '0'),
                        'penalties': ('Штрафные', '9', '9'),
                        'possession_ball': ('Владение мячом', '51', '49'),
                        'saves': ('Сэйвы', '0', '3'),
                        'selections': ('Oтборы', '17', '9'),
                        'shots_on_target': ('Удары в створ', '8', '0'),
                        'total_transmissions': ('Всего передач', '456', '432')}

    driver, season_name = open_necessary_page()
    driver.click_xpath(TabXpath.STATISTIC_BUTTON)
    result = FlashScore.get_all_statistics_game(driver)
    driver.close_driver()
    assert result == necessary_result
    assert season_name == 'Премьер-лига 2022/2023'


def test_get_review_game_without_cards():
    necessary_result = {'first_time_score': ['3', '0'],
                        'info_cards': {'info': [], 'red_cards': 0, 'yellow_cards': 0},
                        'info_goals': {'count': 5,
                                       'info': [{'game_score': '1 - 0',
                                                 'time': '11',
                                                 'who_scored': 'Джака Г.'},
                                                {'game_score': '2 - 0',
                                                 'time': '14',
                                                 'who_scored': 'Джака Г.'},
                                                {'game_score': '3 - 0',
                                                 'time': '27',
                                                 'who_scored': 'Сака Б.'},
                                                {'game_score': '4 - 0',
                                                 'time': '58',
                                                 'who_scored': 'Габриэл Жезус'},
                                                {'game_score': '5 - 0',
                                                 'time': '78',
                                                 'who_scored': 'Кивиор Я.'}]},
                        'second_time_score': ['2', '0'],
                        'substitution': {'count': 10,
                                         'info': [{'come': 'Аит Нури Р.',
                                                   'has_left': 'Буэно У.',
                                                   'time': '46'},
                                                  {'come': 'Невеш Р.',
                                                   'has_left': 'Матеуш Нуньеш',
                                                   'time': '46'},
                                                  {'come': 'Нельсон Р.',
                                                   'has_left': 'Сака Б.',
                                                   'time': '60'},
                                                  {'come': 'Траоре Б.',
                                                   'has_left': 'Хван Хи Чхан',
                                                   'time': '68'},
                                                  {'come': 'Тоти',
                                                   'has_left': 'Килман М.',
                                                   'time': '68'},
                                                  {'come': 'Виейра Ф.',
                                                   'has_left': 'Джака Г.',
                                                   'time': '75'},
                                                  {'come': 'Смит-Роу Э.',
                                                   'has_left': 'Эдегор М.',
                                                   'time': '75'},
                                                  {'come': 'Нкетиа Э.',
                                                   'has_left': 'Троссард Л.',
                                                   'time': '79'},
                                                  {'come': 'Тирни К.',
                                                   'has_left': 'Кивиор Я.',
                                                   'time': '80'},
                                                  {'come': 'Ходж Дж.',
                                                   'has_left': 'Joao Gomes',
                                                   'time': '84'}]}}

    driver, season_name = open_necessary_page()
    result = FlashScore.get_review_game(driver)
    driver.close_driver()
    assert season_name == 'Премьер-лига 2022/2023'
    assert result == necessary_result


def test_get_review_game_with_yellow_cards():
    necessary_result = {'first_time_score': ['2', '1'],
                        'info_cards': {'info': [{'Person': 'Ундав Д.', 'time': '12'},
                                                {'Person': 'Кэш М.', 'time': '22'},
                                                {'Person': 'Рэмзи Дж.', 'time': '24'},
                                                {'Person': 'Мингс Т.', 'time': '37'},
                                                {'Person': 'Buonanotte F.', 'time': '63'},
                                                {'Person': 'МакГин Дж.', 'time': '67'},
                                                {'Person': 'Кайседо М.', 'time': '73'},
                                                {'Person': 'Гросс П.', 'time': '88'}],
                                       'red_cards': 0,
                                       'yellow_cards': 8},
                        'info_goals': {'count': 3,
                                       'info': [{'game_score': '1 - 0',
                                                 'time': '8',
                                                 'who_scored': 'Дуглас Луис'},
                                                {'game_score': '2 - 0',
                                                 'time': '26',
                                                 'who_scored': 'Уоткинс О.'},
                                                {'game_score': '2 - 1',
                                                 'time': '38',
                                                 'who_scored': 'Ундав Д.'}]},
                        'second_time_score': ['0', '0'],
                        'substitution': {'count': 6,
                                         'info': [{'come': 'Эступинан П.',
                                                   'has_left': 'Велтман Й.',
                                                   'time': '46'},
                                                  {'come': 'Кайседо М.',
                                                   'has_left': 'Ayari Y.',
                                                   'time': '46'},
                                                  {'come': 'ван Хекке Я. П.',
                                                   'has_left': 'Уэбстер А.',
                                                   'time': '65'},
                                                  {'come': 'Митома К.',
                                                   'has_left': 'Энсисо Х.',
                                                   'time': '65'},
                                                  {'come': 'Буэндия Э.',
                                                   'has_left': 'Бэйли Л.',
                                                   'time': '69'},
                                                  {'come': 'Хиншелвуд Дж,',
                                                   'has_left': 'Ундав Д.',
                                                   'time': '89'}]}}
    driver, season_name = open_necessary_page(1)
    result = FlashScore.get_review_game(driver)
    driver.close_driver()
    assert season_name == 'Премьер-лига 2022/2023'
    assert result == necessary_result


def test_get_review_game_with_red_cards():
    necessary_result = {'first_time_score': ['1', '0'],
                        'info_cards': {'info': [{'Person': 'Рейс Л.', 'time': '15'},
                                                {'Person': 'Сухонен А.', 'time': '69'},
                                                {'Person': 'Кенигсдорффер Р.', 'time': '73'},
                                                {'Person': 'Каразор А.', 'time': '76'}],
                                       'red_cards': 1,
                                       'yellow_cards': 3},
                        'info_goals': {'count': 3,
                                       'info': [{'game_score': '1 - 0',
                                                 'time': '1',
                                                 'who_scored': 'Мавропанос К.'},
                                                {'game_score': '2 - 0',
                                                 'time': '51',
                                                 'who_scored': 'Вагноман Дж.'},
                                                {'game_score': '3 - 0',
                                                 'time': '54',
                                                 'who_scored': 'Гирасси С.'}]},
                        'second_time_score': ['2', '0'],
                        'substitution': {'count': 7,
                                         'info': [{'come': 'Сухонен А.',
                                                   'has_left': 'Рейс Л.',
                                                   'time': '60'},
                                                  {'come': 'Кенигсдорффер Р.',
                                                   'has_left': 'Домпе Ж.',
                                                   'time': '65'},
                                                  {'come': 'Томас Т.',
                                                   'has_left': 'Фухрих К.',
                                                   'time': '68'},
                                                  {'come': 'Пфайффер Л.',
                                                   'has_left': 'Гирасси С.',
                                                   'time': '68'},
                                                  {'come': 'Нарти Н.',
                                                   'has_left': 'Каразор А.',
                                                   'time': '84'},
                                                  {'come': 'Эглофф Л.',
                                                   'has_left': 'Мийо Э.',
                                                   'time': '84'},
                                                  {'come': 'Загаду Д.',
                                                   'has_left': 'Антон В.',
                                                   'time': '90+2'}]}}
    driver, season_name = open_necessary_page(
        number_match=1,
        url='https://www.flashscore.com.ua/football/germany/bundesliga/#/OWq2ju22/table/overall')
    result = FlashScore.get_review_game(driver)
    driver.close_driver()

    assert 'Бундеслига 2022/2023' == season_name
    assert result == necessary_result


def test_get_review_game_with_auto_goal():
    necessary_result = {'first_time_score': ['2', '1'],
                        'info_cards': {'info': [{'Person': 'Брюннер К.', 'time': '20'},
                                                {'Person': 'Хайдара А.', 'time': '41'},
                                                {'Person': 'Польтер С.', 'time': '63'},
                                                {'Person': 'Нкунку К.', 'time': '90+5'}],
                                       'red_cards': 0,
                                       'yellow_cards': 4},
                        'info_goals': {'count': 6,
                                       'info': [{'game_score': '1 - 0',
                                                 'time': '10',
                                                 'who_scored': 'Лаймер К.'},
                                                {'game_score': '2 - 0',
                                                 'time': '19',
                                                 'who_scored': 'Нкунку К.'},
                                                {'game_score': '2 - 1',
                                                 'time': '28',
                                                 'who_scored': 'Камински М.'},
                                                {'game_score': '2 - 2',
                                                 'time': '49',
                                                 'who_scored': 'Орбан В.'},
                                                {'game_score': '3 - 2',
                                                 'time': '82',
                                                 'who_scored': 'Поульсен Ю.'},
                                                {'game_score': '4 - 2',
                                                 'time': '90+4',
                                                 'who_scored': 'Нкунку К.'}]},
                        'second_time_score': ['2', '1'],
                        'substitution': {'count': 8,
                                         'info': [{'come': 'Кампл К.',
                                                   'has_left': 'Хайдара А.',
                                                   'time': '46'},
                                                  {'come': 'Мор Т.',
                                                   'has_left': 'Залазар Р.',
                                                   'time': '56'},
                                                  {'come': 'Шлагер К.',
                                                   'has_left': 'Лаймер К.',
                                                   'time': '61'},
                                                  {'come': 'Поульсен Ю.',
                                                   'has_left': 'Вернер Т.',
                                                   'time': '61'},
                                                  {'come': 'Раум Д.',
                                                   'has_left': 'Хальстенберг М.',
                                                   'time': '61'},
                                                  {'come': 'Собослаи Д.',
                                                   'has_left': 'Форсберг Э.',
                                                   'time': '68'},
                                                  {'come': 'Ауэян Т.',
                                                   'has_left': 'Matriciani H.',
                                                   'time': '70'},
                                                  {'come': 'Караман К.',
                                                   'has_left': 'Латца Д.',
                                                   'time': '75'}]}}
    driver, season_name = open_necessary_page(
        number_match=8,
        url='https://www.flashscore.com.ua/football/germany/bundesliga/#/OWq2ju22/table/overall',
        all_matches=True)
    result = FlashScore.get_review_game(driver)
    time.sleep(5)
    driver.close_driver()

    assert 'Бундеслига 2022/2023' == season_name
    assert result == necessary_result


# TODO проверить на все виды ошибок
