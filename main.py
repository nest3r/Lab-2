import xml.etree.ElementTree as ET

def parse_currency_xml(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()

    date = root.attrib['Date']

    currencies = []
    for currency in root.findall('Valute'):
        nominal = int(currency.find('Nominal').text)
        if nominal == 10 or nominal == 100:
            char_code = currency.find('CharCode').text
            name = currency.find('Name').text

            year = None
            if date is not None:
                year = int(date.split('.')[-1])

            if year is not None and (year == 2015 or year == 2018):
                currency_data = {
                    'CharCode': char_code,
                    'Name': name,
                    'Year': year
                }
                currencies.append(currency_data)

    return date, currencies

file_name = 'currency.xml'
date, currencies = parse_currency_xml(file_name)

print("Date:", date)
for currency in currencies:
    print(f"CharCode: {currency['CharCode']}")
    print(f"Name: {currency['Name']}")
    print(f"Year: {currency['Year']}")
    print()