import phonenumbers
from phonenumbers import geocoder, carrier, timezone

# تحقق مما إذا كان رقم الهاتف صالحًا
def is_valid_phone_number(number):
    try:
        parsed_number = phonenumbers.parse(number, None)
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.phonenumberutil.NumberFormatException:
        return False

# الحصول على معلومات عن رقم الهاتف
def get_phone_info(number):
    parsed_number = phonenumbers.parse(number, None)
    country = geocoder.description_for_number(parsed_number, 'en')
    carrier_name = carrier.name_for_number(parsed_number, 'en')
    time_zones = timezone.time_zones_for_number(parsed_number)
    return country, carrier_name, time_zones

# الدالة الرئيسية
def main():
    print("""
           _           _       _    
     _ __ | |__   ___ | | ___ | | __
    | '_ \| '_ \ / _ \| |/ _ \| |/ /
    | |_) | | | | (_) | | (_) |   < 
    | .__/|_| |_|\___/|_|\___/|_|\_\
    |_|                             
                                    by *Mousavi*
    """)

    while True:
        print('x' * 50)

        inp_1 = input('Enter your numbers (1 to search, or any other key to exit): ')
        
        if inp_1 == '1':
            entered_num = input('Please enter a phone number : ')
            
            if is_valid_phone_number(entered_num):
                country, carrier_name, time_zones = get_phone_info(entered_num)
                print(f"Country: {country}")
                print(f"Carrier: {carrier_name}")
                print(f"Time Zones: {', '.join(time_zones)}")
            else:
                print("Invalid phone number. Please enter a valid phone number.")
        else:
            print("""
            Thank you for using this tool!
            Contact us for any questions or concerns.
            """)

if __name__ == "__main__":
    main()

    
