# ---------previous---------##
# from bs4 import BeautifulSoup
# import requests

# headers= ({'User-Agent':
#                 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
#                 'Accept-Language': 'en-US, en;q=0.5'})
# domain='https://www.amazon.in'
# product_url='https://www.amazon.in/dp/B09B277CR5/ref=sspa_dk_detail_7?psc=1&pd_rd_i=B09B277CR5&pd_rd_w=0gLPi&content-id=amzn1.sym.b3dfef88-30a1-490c-be36-e990ef384667&pf_rd_p=b3dfef88-30a1-490c-be36-e990ef384667&pf_rd_r=ZYDY7XZ1716CWD331W12&pd_rd_wg=UYXLW&pd_rd_r=e73f48a5-6a45-4908-ab23-7c5f89bab8fa&s=apparel&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw'


# product_webpage = requests.get(product_url,headers=headers)
# product_soup = BeautifulSoup(product_webpage.content,'lxml')                

# print(product_soup.prettify())
#here we are extracting the description of item in detailed form
# description = product_soup.find('ul',class_='a-unordered-list a-vertical a-spacing-mini')
# list_of_description=[]
# description_li = description.find_all('li')
# # print(description_li)
# for s in description_li:
#     text=s.span.text
#     # print("TEXT : "+text)
#     list_of_description.append(text)


# for li  in list_of_description:
#     print("text : "+li)


#here we are fetching the product details 
# product_details=product_soup.find_all('ul',class_='a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list')

# product_details_span= product_details.find_all('span',class_='a-list-item')
# ASIN=''
# manufacturer=''


# print(product_details_span)


#NOW WE WILL TRY TO EXTRACT THE ASIN NUMBER AND THE INFORMATION OF THE MANUFACTURER

# product_details= product_soup.find('div',class_='a-section feature detail-bullets-wrapper bucket')
# print(product_details)




####---------------------------------new----------------------####

from bs4 import BeautifulSoup
import requests

headers= ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})

domain='https://www.amazon.in'

product_url='https://www.amazon.in/Safari-Spartan-Water-Resistant-Backpack/dp/B09B26MB5M/ref=sr_1_36?crid=2M096C61O4MLT&keywords=bags&qid=1675332392&sprefix=ba%2Caps%2C283&sr=8-36'

product_webpage = requests.get(product_url,headers=headers)

product_soup = BeautifulSoup(product_webpage.content,'lxml') 

# print(product_soup.prettify())

ASIN=''
manufacturer=''

product_details= product_soup.find('ul',class_="a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list")
# print(product_details)
if product_details is not None:

    for li in product_details:
        
        # print(li)
        for span in li:
            # print(span)
            flag=True
            bool_asin=False
            bool_manufacture=False
            for inspan in span:
                print(inspan)

                if flag:
                    flag=False
                    if 'ASIN' in span.text:
                        bool_asin=True
                    elif 'Manufacturer' in span.text:
                        bool_manufacture=True

                else:
                    if bool_asin:
                        ASIN=span.text
                    elif bool_manufacture:
                        manufacturer=span.text
            
    print('ASIN : '+ASIN)
    print('MANUFACTURER  : '+manufacturer)
