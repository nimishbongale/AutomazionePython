from selenium import webdriver


def showit(stringval):
    browser.get(stringval)


text = input("Satellite Imagery of India in grayscale(gsl) or color(clr)?")
browser = webdriver.Chrome()
browser.maximize_window()

if text == 'gsl':
    showit('http://oiswww.eumetsat.org/IPPS/html/latestImages/EUMETSAT_MSGIODC_IR039_SouthernAsia.jpg')
elif text == 'clr':
    showit('http://oiswww.eumetsat.org/IPPS/html/latestImages/EUMETSAT_MSGIODC_IR039Color_SouthernAsia.jpg')
else:
    showit('about:blank')





