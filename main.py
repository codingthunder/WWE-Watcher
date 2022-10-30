from logging import raiseExceptions
import pandas as pd
import numpy as np
import json
import web_navigator as nav
import sys

#I admit, I was a bit lazy in setting this up. 

class show_runner:
        save_Location = "save_spot.json"
        currentIndex : int = 0
        blacklisted_show_classes = None
        chrome_profile_path = None
        df = pd.read_excel('.\WWE Network Peacock.xlsx')
        driver = None

        def setup(chromeProfilePath : str = None):
                show_runner.chrome_profile_path = chromeProfilePath

                with open(show_runner.save_Location,"r") as openfile:
                        json_object = json.load(openfile)
                        show_runner.currentIndex = json_object["current_episode"]
                        show_runner.blacklisted_show_classes = json_object["blacklisted_classes"]
                        if show_runner.chrome_profile_path is None and "profile_path" in json_object and json_object["profile_path"]:
                                show_runner.chrome_profile_path = json_object["profile_path"]
                
                show_runner.driver = nav.open_browser(show_runner.chrome_profile_path)

        def run_episode() -> bool:

                sr = show_runner

                while True:
                        showClass = sr.df.iloc[sr.currentIndex]['Class']
                        if showClass in sr.blacklisted_show_classes:
                                sr.currentIndex += 1
                                continue
                        break

                destinationUrl = sr.df.iloc[sr.currentIndex]['Link']
                #nextUrl = df.iloc[currentIndex + 1]['Link']



                driver = show_runner.driver
                nav.go_to_page(driver,destinationUrl)
                
                chromeResult = nav.wait_for_url_to_change(driver)

                if chromeResult == True or chromeResult == None:
                        return False

                sr.currentIndex += 1

                if chromeResult == "":
                        sr.blacklisted_show_classes += showClass
                
                return True




        def run_series(chromeProfilePath : str = None):
                show_runner.setup(chromeProfilePath)
                
                iterations = 0

                while (show_runner.run_episode()):
                        iterations += 1
                        if iterations > 4:
                                break


                saveData = {"current_episode": int(show_runner.currentIndex), "blacklisted_classes": show_runner.blacklisted_show_classes}

                if show_runner.chrome_profile_path:
                        saveData["profile_path"] = show_runner.chrome_profile_path

                with open(show_runner.save_Location, "w") as outfile:
                        json.dump(saveData,outfile)




profile_path=None

try:
        profile_path = sys.argv[1]
except:
        pass

show_runner.run_series(chromeProfilePath=profile_path)




