import time

from config import settings as st
from utils.basic_decorators import working_time
from utils.SeleniumModule import SeleniumDriver
from FlashScoreActions.FlashScoreXpaths import BasicXpaths, TableResultsXpaths as TabXpath, ReviewGameXpath


class FlashScore:
    BLACK_LIST = ['Гол не засчитан - офсайд', 'Незабитый пенальти']

    @staticmethod
    def open_all_season_games(driver: SeleniumDriver):
        """
        Open all games from season on page
        """

        driver.click_xpath(BasicXpaths.RESULTS)

        while True:
            if driver.xpath_checker(BasicXpaths.MORE_EVENTS_BUTTON, pause=2):
                more_events_button = driver.click_xpath(BasicXpaths.MORE_EVENTS_BUTTON, click=False)
                driver.get_driver.execute_script("arguments[0].click();", more_events_button)
                time.sleep(1.5)

            else:
                break

    @classmethod
    def open_football_leagues(cls, driver: SeleniumDriver, url: str):
        """
        Open WebPage on FlashScore with url
        """

        driver.get_driver.get(url)
        driver.while_not_element(BasicXpaths.ARCHIVE)

    @classmethod
    def __get_main_info_match(cls, driver: SeleniumDriver) -> dict:
        """
        Get information about the names of the teams , the score of the game
        and the date of the event
        """

        name_command_one = driver.get_text_xpath(TabXpath.NAME_COMMAND_ONE)
        name_command_two = driver.get_text_xpath(TabXpath.NAME_COMMAND_TWO)
        date_match = driver.get_text_xpath(TabXpath.DATE_MATCH)
        goals_first = driver.get_text_xpath(TabXpath.GOALS_FIRST)
        goals_second = driver.get_text_xpath(TabXpath.GOALS_SECOND)

        result = {
            'name_command_one': name_command_one,
            'name_command_two': name_command_two,
            'date_match': date_match,
            'goals_first': goals_first,
            'goals_second': goals_second,
        }

        return result

    @staticmethod
    @working_time(active=st.work_time_methods)
    def get_all_statistics_game(driver: SeleniumDriver) -> dict:
        """
        Get all the statistics for the game
        """

        descr_expected_goals = driver.get_text_xpath(TabXpath.DESCR_EXPECTED_GOALS)
        expected_goals_first = driver.get_text_xpath(TabXpath.EXPECTED_GOALS_FIRST)
        expected_goals_second = driver.get_text_xpath(TabXpath.EXPECTED_GOALS_SECOND)

        descr_possession_ball = driver.get_text_xpath(TabXpath.DESCR_POSSESSION_BALL)
        possession_ball_first = driver.get_text_xpath(TabXpath.POSSESSION_BALL_FIRST).replace('%', '')
        possession_ball_second = driver.get_text_xpath(TabXpath.POSSESSION_BALL_SECOND).replace('%', '')

        descr_blows = driver.get_text_xpath(TabXpath.DESCR_BLOWS)
        blows_first = driver.get_text_xpath(TabXpath.BLOWS_FIRST)
        blows_second = driver.get_text_xpath(TabXpath.BLOWS_SECOND)

        descr_shots_on_target = driver.get_text_xpath(TabXpath.DESCR_SHOTS_ON_TARGET)
        shots_on_target_first = driver.get_text_xpath(TabXpath.SHOTS_ON_TARGET_FIRST)
        shots_on_target_second = driver.get_text_xpath(TabXpath.SHOTS_ON_TARGET_SECOND)

        descr_blows_by = driver.get_text_xpath(TabXpath.DESCR_BLOWS_BY)
        blows_by_first = driver.get_text_xpath(TabXpath.BLOWS_BY_FIRST)
        blows_by_second = driver.get_text_xpath(TabXpath.BLOWS_BY_SECOND)

        descr_penalties = driver.get_text_xpath(TabXpath.DESCR_PENALTIES)
        penalties_first = driver.get_text_xpath(TabXpath.PENALTIES_FIRST)
        penalties_second = driver.get_text_xpath(TabXpath.PENALTIES_SECOND)

        descr_corner = driver.get_text_xpath(TabXpath.DESCR_CORNER)
        corner_first = driver.get_text_xpath(TabXpath.CORNER_FIRST)
        corner_second = driver.get_text_xpath(TabXpath.CORNER_SECOND)

        descr_offsides = driver.get_text_xpath(TabXpath.DESCR_OFFSIDES)
        offsides_first = driver.get_text_xpath(TabXpath.OFFSIDES_FIRST)
        offsides_second = driver.get_text_xpath(TabXpath.OFFSIDES_SECOND)

        descr_face_offs = driver.get_text_xpath(TabXpath.DESCR_FACE_OFFS)
        face_offs_first = driver.get_text_xpath(TabXpath.FACE_OFFS_FIRST)
        face_offs_second = driver.get_text_xpath(TabXpath.FACE_OFFS_SECOND)

        descr_saves = driver.get_text_xpath(TabXpath.DESCR_SAVES)
        saves_first = driver.get_text_xpath(TabXpath.SAVES_FIRST)
        saves_second = driver.get_text_xpath(TabXpath.SAVES_SECOND)

        descr_fouls = driver.get_text_xpath(TabXpath.DESCR_FOULS)
        fouls_first = driver.get_text_xpath(TabXpath.FOULS_FIRST)
        fouls_second = driver.get_text_xpath(TabXpath.FOULS_SECOND)

        descr_total_transmissions = driver.get_text_xpath(TabXpath.DESCR_TOTAL_TRANSMISSIONS)
        total_transmissions_first = driver.get_text_xpath(TabXpath.TOTAL_TRANSMISSIONS_FIRST)
        total_transmissions_second = driver.get_text_xpath(TabXpath.TOTAL_TRANSMISSIONS_SECOND)

        descr_selections = driver.get_text_xpath(TabXpath.DESCR_SELECTIONS)
        selections_first = driver.get_text_xpath(TabXpath.SELECTIONS_FIRST)
        selections_second = driver.get_text_xpath(TabXpath.SELECTIONS_SECOND)

        descr_attack = driver.get_text_xpath(TabXpath.DESCR_ATTACK)
        attack_first = driver.get_text_xpath(TabXpath.ATTACK_FIRST)
        attack_second = driver.get_text_xpath(TabXpath.ATTACK_SECOND)

        descr_dangerous_attacks = driver.get_text_xpath(TabXpath.DESCR_DANGEROUS_ATTACKS)
        dangerous_attacks_first = driver.get_text_xpath(TabXpath.DANGEROUS_ATTACKS_FIRST)
        dangerous_attacks_second = driver.get_text_xpath(TabXpath.DANGEROUS_ATTACKS_SECOND)

        result = {
            'expected_goals': (descr_expected_goals, expected_goals_first, expected_goals_second),
            'possession_ball': (descr_possession_ball, possession_ball_first, possession_ball_second),
            'blows': (descr_blows, blows_first, blows_second),
            'shots_on_target': (descr_shots_on_target, shots_on_target_first, shots_on_target_second),
            'blows_by': (descr_blows_by, blows_by_first, blows_by_second),
            'penalties': (descr_penalties, penalties_first, penalties_second),
            'corner': (descr_corner, corner_first, corner_second),
            'offsides': (descr_offsides, offsides_first, offsides_second),
            'face_offs': (descr_face_offs, face_offs_first, face_offs_second),
            'saves': (descr_saves, saves_first, saves_second),
            'fouls': (descr_fouls, fouls_first, fouls_second),
            'total_transmissions': (descr_total_transmissions, total_transmissions_first, total_transmissions_second),
            'selections': (descr_selections, selections_first, selections_second),
            'attack': (descr_attack, attack_first, attack_second),
            'dangerous_attacks': (descr_dangerous_attacks, dangerous_attacks_first, dangerous_attacks_second),
        }

        return result

    @classmethod
    @working_time(active=st.work_time_methods)
    def get_review_game(cls, driver: SeleniumDriver) -> dict:
        """
        Get all info in review menu
        """
        first_time_score = None
        second_time_score = None
        info_goals = []
        info_substitution = []
        info_yellow_cards = []

        yellow_cards = driver.get_text_or_null(ReviewGameXpath.YELLOW_CARDS, pause=1.5)
        red_cards = driver.get_text_or_null(ReviewGameXpath.RED_CARDS)
        test_info = driver.get_elements('//*[@id="detail"]/div[9]/div/div[*]', while_not_element=False)
        test_info = test_info if len(test_info) != 0 else driver.get_elements('//*[@id="detail"]/div[10]/div/div[*]',
                                                                              while_not_element=False)
        for row in test_info:
            print('info')
            info = row.text.split('\n')
            print(info)

            check_black_list = [text for text in cls.BLACK_LIST if text in ''.join(info)]
            if len(check_black_list) > 0:
                print(f'Find exception - {check_black_list}')
                continue

            if '1-Й ТАЙМ' in info:
                first_time_score = info[-1].split(' - ')

            elif '2-Й ТАЙМ' in info:
                second_time_score = info[-1].split(' - ')

            elif '-' in info[1] and 5 <= len(info[1]) <= 7:
                info_goals.append({'time': info[0].replace("'", ''),
                                   'who_scored': info[2],
                                   'game_score': info[1]})

            elif len(info) == 3 and ('(' in info[2] and ')' in info[2] and info[2].count('.') == 0):
                info_yellow_cards.append({'time': info[0].replace("'", ''),
                                          'Person': info[1]})

            elif len(info) == 3 and (info[1].count('.') in [1, 2] or info[1].count(',') in [1, 2]) == 1 or \
                    (info[2].count('.') in [1, 2] or info[2].count(',') in [1, 2]):
                info_substitution.append({'time': info[0].replace("'", ''),
                                          'come': info[1],
                                          'has_left': info[2]})

        result = {
            'first_time_score': first_time_score,
            'second_time_score': second_time_score,
            'info_cards': {'red_cards': len(red_cards), 'yellow_cards': len(yellow_cards), 'info': info_yellow_cards},
            'substitution': {'count': len(info_substitution), 'info': info_substitution},
            'info_goals': {'count': len(info_goals), 'info': info_goals},
        }
        import pprint
        pprint.pprint(result)
        return result

    @classmethod
    def __get_info_from_season(cls,
                               driver: SeleniumDriver,
                               number_season: int):
        """
        Get info about selected number season
        """

        season_xpath = f'//*[@id="tournament-page-archiv"]/div[{number_season}]/div[1]/a'
        season_obj = driver.click_xpath(season_xpath, click=False)
        season_name = season_obj.get_attribute('textContent').strip()
        season_obj.click()
        print(season_name)
        cls.open_all_season_games(driver)
        matches = driver.get_elements('//*[@title="Подробности матча!"]')
        print(len(matches))

        for match in matches:
            match.click()
            windows = driver.get_driver.window_handles
            driver.get_driver.switch_to.window(windows[1])
            driver.click_xpath(TabXpath.STATISTIC_BUTTON)

            cls.get_review_game(driver)
            break

            import pprint
            driver.click_xpath(TabXpath.STATISTIC_BUTTON)
            main_info = cls.__get_main_info_match(driver)
            pprint.pprint(main_info)

            all_statistics = cls.get_all_statistics_game(driver)
            pprint.pprint(all_statistics)

            break

    @classmethod
    def get_archives(cls,
                     driver: SeleniumDriver,
                     numbers_of_seasons: int = 1):
        """
        Get info about football statistics with selected season
        """
        driver.click_xpath(BasicXpaths.ARCHIVE)
        for i in range(3, 3 + numbers_of_seasons):
            cls.__get_info_from_season(driver, i)
