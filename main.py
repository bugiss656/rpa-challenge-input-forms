import time
import pandas as pd
from selenium.webdriver import Chrome


def main():
    excel_df = pd.read_excel('challenge.xlsx', sheet_name='Sheet1')
    excel_data = excel_df.to_dict(orient='records')

    driver = Chrome()
    driver.get('http://www.rpachallenge.com/')

    start_button = driver.find_element_by_tag_name('button')
    start_button.click()

    for item in excel_data:
        first_name_input = driver.find_element_by_css_selector('input[ng-reflect-name="labelFirstName"]')
        last_name_input = driver.find_element_by_css_selector('input[ng-reflect-name="labelLastName"]')
        company_name_input = driver.find_element_by_css_selector('input[ng-reflect-name="labelCompanyName"]')
        role_in_company_input = driver.find_element_by_css_selector('input[ng-reflect-name="labelRole"]')
        address_input = driver.find_element_by_css_selector('input[ng-reflect-name="labelAddress"]')
        email_input = driver.find_element_by_css_selector('input[ng-reflect-name="labelEmail"]')
        phone_number_input = driver.find_element_by_css_selector('input[ng-reflect-name="labelPhone"]')

        submit_button = driver.find_element_by_css_selector('input[type="submit"]') 

        form_inputs = [first_name_input, last_name_input, company_name_input, role_in_company_input, address_input, email_input, phone_number_input]
        
        for index, (key, value) in enumerate(item.items()):
            form_inputs[index].send_keys(value)

        submit_button.click()

    time.sleep(5)
    driver.close()
    

if __name__ == '__main__':
    main()