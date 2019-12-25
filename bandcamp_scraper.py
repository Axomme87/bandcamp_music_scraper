from __future__ import print_function
from selenium import webdriver
import os
import time
import urllib
import re
from utils.colorfy import Colors

colorfy = Colors()
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
CHROME_DRIVER_PATH = str(CURRENT_PATH) + str('/utils/chromedriver')


class Selenium:

    def __init__(self, driver_path):
        chrome_options = webdriver.ChromeOptions()
        prefs = {'intl.accept_languages': 'en,en_US'}
        chrome_options.add_experimental_option('prefs', prefs)
        chrome_options.add_argument('headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("start-maximized")

        # setting up the class variables and the Chrome Driver
        self.__driver = webdriver.Chrome(driver_path, chrome_options=chrome_options)

    def run(self):
        try:
            self.__driver.get('https://bandcamp.com/cmgriffing')
            self.__driver.implicitly_wait(10)

            songs_count = self.__driver.find_element_by_class_name('count').text
            print(colorfy.info('Playlist total songs count: ' + str(songs_count)))

            print(colorfy.warn('...loading all songs...'))

            count_items = len(self.__driver.find_elements_by_xpath('//*[@id="collection-items"]/ol/li'))
            print(colorfy.debug('Loaded ' + str(count_items) + ' of ' + str(songs_count)))

            self.__driver.find_element_by_class_name('show-more').click()
            time.sleep(15)
            count_items = len(self.__driver.find_elements_by_xpath('//*[@id="collection-items"]/ol/li'))
            print(colorfy.debug('Loaded ' + str(count_items) + ' of ' + str(songs_count)))
            self.__driver.execute_script('window.scrollBy(0,5000)')
            time.sleep(15)
            count_items = len(self.__driver.find_elements_by_xpath('//*[@id="collection-items"]/ol/li'))
            print(colorfy.debug('Loaded ' + str(count_items) + ' of ' + str(songs_count)))

            items = self.__driver.find_elements_by_xpath('//*[@id="collection-items"]/ol/li')

            counter = 0

            for song in items:
                counter += 1
                print(colorfy.warn('>>> Song No. ' + str(counter) + ' <<<'))
                song_title = song.find_element_by_class_name('collection-item-title').text
                print(colorfy.info(song_title))
                song_title_arr = []
                for word in song_title.split():
                    song_title_arr += re.split('[^a-zA-Z0-9]', word)
                song_title = '-'.join([word for word in song_title_arr if word != ''])
                print(colorfy.debug(song_title))

                song_artist = song.find_element_by_class_name('collection-item-artist').text
                print(colorfy.info(song_artist))
                song_artist_arr = []
                for word in song_artist[3:].split():
                    song_artist_arr += re.split('[^a-zA-Z0-9]', word)
                song_artist = '-'.join([word for word in song_artist_arr if word != ''])
                print(colorfy.debug(song_artist))

                song.click()
                time.sleep(5)
                song_url = self.__driver.find_element_by_xpath('/html/body/audio').get_attribute('src')
                print(song_url)

                mp3_file = urllib.urlopen(song_url)
                output = open('music/' + song_artist + '_' + song_title + '.mp3', 'wb')
                output.write(mp3_file.read())
                output.close()
                print('\n')

            self.__driver.quit()
        except Exception as e:
            self.__driver.quit()


selenium = Selenium(CHROME_DRIVER_PATH)
selenium.run()
