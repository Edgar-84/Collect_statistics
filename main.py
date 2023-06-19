import time

from utils.basic_decorators import working_time
from utils.SeleniumModule import SeleniumDriver
from FlashScoreActions.FlashScoreModule import FlashScore


url = 'https://www.flashscore.com.ua/football/england/premier-league/#/nunhS7Vn/table/overall'


@working_time(active=True)
def main(url):

    driver_object = SeleniumDriver()
    FlashScore.open_football_leagues(driver_object, url=url)
    FlashScore.get_archives(driver_object)
    time.sleep(10)
    driver_object.close_driver()


if __name__ == '__main__':
    main(url)
