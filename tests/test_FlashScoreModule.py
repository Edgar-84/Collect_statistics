from selenium import webdriver
from FlashScoreActions.FlashScoreModule import FlashScore
from FlashScoreActions.FlashScoreXpaths import BasicXpaths, TableResultsXpaths as TabXpath
from utils.SeleniumModule import SeleniumDriver


def open_necessary_page() -> webdriver:
    """
    Open neccessary page and return webriver object
    """

    driver = SeleniumDriver()
    url = 'https://www.flashscore.com.ua/football/england/premier-league-2022-2023/#/nunhS7Vn/table/overall'
    FlashScore.open_football_leagues(driver, url=url)
    driver.click_xpath(BasicXpaths.ARCHIVE)
    season_xpath = f'//*[@id="tournament-page-archiv"]/div[3]/div[1]/a'
    season_obj = driver.click_xpath(season_xpath, click=False)
    season_name = season_obj.get_attribute('textContent').strip()
    season_obj.click()
    matches = driver.get_elements('//*[@title="Подробности матча!"]')

    for match in matches:
        match.click()
        windows = driver.get_driver.window_handles
        driver.get_driver.switch_to.window(windows[1])
        driver.click_xpath(TabXpath.STATISTIC_BUTTON)
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
    result = FlashScore.get_all_statistics_game(driver)

    assert result == necessary_result
    assert season_name == 'Премьер-лига 2022/2023'