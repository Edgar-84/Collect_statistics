import time

from config import settings as st
from utils.basic_decorators import working_time
from utils.SeleniumModule import SeleniumDriver
from FlashScoreActions.FlashScoreXpaths import BasicXpaths, TableResultsXpaths as TabXpath, ReviewGameXpath


class FlashScore:
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
        # data = [
        #     ('expected_goals', TabXpath.DESCR_EXPECTED_GOALS, TabXpath.EXPECTED_GOALS_FIRST, TabXpath.EXPECTED_GOALS_SECOND),
        #         ]
        # result = {}

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

    @staticmethod
    @working_time(active=st.work_time_methods)
    def get_review_game(driver: SeleniumDriver) -> dict:
        """
        Get all info in review menu
        """

        all_score = driver.get_elements(ReviewGameXpath.ALL_SCORE)
        yellow_cards = len(driver.get_text_or_null(ReviewGameXpath.YELLOW_CARDS))
        red_cards = len(driver.get_text_or_null(ReviewGameXpath.RED_CARDS))
        substitution = len(driver.get_text_or_null(ReviewGameXpath.SUBSTITUTION))
        score = []

        for row in all_score:
            if 'тайм' in row.get_attribute('textContent').strip():
                data = row.get_attribute('textContent').strip().split('тайм')
                score.append((data[1].split(' - ')))

        first_time_score, second_time_score = score[0], score[1]

        result = {
            'first_time_score': first_time_score,
            'second_time_score': second_time_score,
            'yellow_cards': yellow_cards,
            'red_cards': red_cards,
            'substitution': substitution,
        }

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
        # cls.open_all_season_games(driver)
        matches = driver.get_elements('//*[@title="Подробности матча!"]')
        print(len(matches))

        for match in matches:
            match.click()
            windows = driver.get_driver.window_handles
            driver.get_driver.switch_to.window(windows[1])
            # driver.click_xpath(TabXpath.STATISTIC_BUTTON)

            cls.get_review_game(driver)
            break

            import pprint
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
