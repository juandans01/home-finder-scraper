from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def scrap():

    DRIVER_PATH = './driver/chromedriver'
    print('* STARTED SCRAPPING')
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)
    driver.get('https://www.soloduenos.com/BusquedaGeneral.asp?cmbZona=1&veraneo=&image333.x=11&image333.y=8')

    # CHECK HOUSE
    driver.find_element_by_xpath("//input[@name='chkProp'][@value='1']").click()
    # CHECK PH
    driver.find_element_by_xpath("//input[@name='chkProp'][@value='10']").click()
    # CHECK DEPT
    driver.find_element_by_xpath("//input[@name='chkProp'][@value='2']").click()
    # CHECK LOFT
    driver.find_element_by_xpath("//input[@name='chkProp'][@value='9']").click()

    #CHECK TYPE
    driver.find_element_by_xpath("//input[@name='chkAlquiler']").click()

    #SELECT MONEY TYPE
    driver.find_element_by_xpath("//select[@name='cmbMonedaAlq']//option[@value='2']").click()
    # SELECT MAX MONEY
    driver.find_element_by_xpath("//input[@name='aMaximo']").send_keys('60000')

    # SELECT NEIGHBORHOODS
    driver.find_element_by_xpath("//select[@name='CmbBarrio1']//option[@value='9']").click()
    driver.find_element_by_xpath("//select[@name='CmbBarrio2']//option[@value='22']").click()
    driver.find_element_by_xpath("//select[@name='CmbBarrio3']//option[@value='3']").click()
    driver.find_element_by_xpath("//select[@name='CmbBarrio4']//option[@value='63']").click()

    # SUBMIT FIRST PAGE
    driver.find_element_by_xpath("//input[@type='submit']").click()
    print('* FINISHED FIRST OPTIONS PAGE')

    # GET ALL AMB COUNT OPTIONALS 
    ambList = driver.find_elements_by_xpath("//input[@type='radio'][contains(@name, 'optAmbientes')][string-length(@name)='13'][@value='3']")
    for amb in ambList:
      amb.click()

    # SUBMIT SECOND PAGE
    driver.find_element_by_xpath("//input[@type='submit']").click()
    print('* FINISHED SECOND OPTIONS PAGE')

    results = driver.find_elements_by_xpath("//img[@alt='Propiedad ingresada en los últimos 15 días']")

    to_save = []
    names_list = open('saved_properties.txt', 'r').read().split('\n')
    
    for result in results:
      link = result.find_element_by_xpath("./ancestor::tr[@bgcolor='#FFDEA2']//td//div//a")
      property_link = link.get_attribute('href')        
      if not property_link in names_list:
        to_save.append(property_link)
    


    with open('saved_properties.txt', 'a') as f:
      for save_item in to_save:
        print('* NEW -> ' + save_item)
        f.write(save_item + '\n')

    if len(to_save) == 0:
      print('* NO NEW PROPERTIES :(')  
    print('* FINISHED SCRAPPING')
    driver.quit()