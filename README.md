# Overview

This is a simple python program designed to let you watch WWE in chronological order. It tracks which episode you're on, automatically switches episodes, and lets you blacklist shows you don't want to watch. Right now, it's not exactly user-friendly. You need to be comfortable with using a shell to get it working. I hope to make the program more accessible down the road, but for now, if you've been wanting to watch historic WWF, WCW, and ECW matches in chronological order, with the PPV's, all without having to channel hop and try to keep track of everything, then you'll probably find some use in this.

I originally made this program because I was tired of trying to keep track of where I was at, which episodes I'd already seen, yada yada. And now that it works (mostly), I thought I would share it with you all.

Please see the youtube video below to see how to run it, and how it operates under the hood. It's actually pretty simple, and it really shows just how much heavy lifting Python can do.

[WWE Watcher Walkthrough](https://youtu.be/_bQrioR8uxc)

# Development Environment

I'll be providing links below, but huge shout out to Joshua LaFollette for making the spreadsheet with all this data! If you see this, know you are a saint!
Beyond that, my script relies primarily on the Pandas and Selenium libraries for Python. I use pandas to manage the excel data, and I use Selenium to control the web browser. I've included a requirements.txt file for easy import of dependencies.

# Useful Websites

* [Original Spreadsheet Data](https://docs.google.com/spreadsheets/d/1dRMrHPWNMYW7vQcY2-bbIAY1H06JP5QihMIh8sVwRfI/edit?usp=sharing)
* [Pandas Library for Python](https://pandas.pydata.org/)
* [Fantastic Resource on Selenium for Python](https://selenium-python.readthedocs.io/)
* [How to Get Chromedriver](https://chromedriver.chromium.org/downloads)
* [How to Get Chrome Profile](https://www.howtogeek.com/255653/how-to-find-your-chrome-profile-folder-on-windows-mac-and-linux/)
* [PeacockTV, I Guess](https://www.peacocktv.com/)
