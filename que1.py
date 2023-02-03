from bs4 import BeautifulSoup
import requests
import csv

headers= ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})
domain='https://www.amazon.in'

fields=['Name','ASIN NO.','URL','RATING','TOTAL REVIEW','PRICE']

filename='product.csv'

csvfile=open(filename,'w',encoding='utf-8') 
csvwriter= csv.writer(csvfile)

csvwriter.writerow(fields)
    


# product_urls=[]

#this function will collect the urls of 20 listing page 
def collect_listing_urls():
    
    count=1
    url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1'
    print("URL : "+url)
    get_product_details(url)

    

    while count<=20:
        webpage = requests.get(url,headers=headers)
        # print(html_text)

        soup = BeautifulSoup(webpage.content,'lxml')

        spans = soup.find_all('span',class_='s-pagination-strip')

        for tag in spans:
            all_a = tag.find_all('a')
            for a in all_a:
                if a.text == 'Next':
                    # print(a['href'])
                    temp = domain+a['href']
                    print("URL : "+temp)
                    get_product_details(temp)
                    count+=1







#here this function will collect all the product details from the listing page urls

def get_product_details(line):
    
    

    url = line.strip()
    # print("URL : "+line)
    webpage= requests.get(url,headers=headers)

    soup = BeautifulSoup(webpage.content,'lxml')

    product_divs = soup.find_all('div',class_='a-section a-spacing-small a-spacing-top-small')

    # print(product_divs)
    for div in product_divs:
        name_and_links = div.find('a',class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
        rating = div.find('span',class_='a-icon-alt')
        total_review= div.find('span',class_='a-size-base s-underline-text')
        price=div.find('span',class_='a-offscreen')
        # print(name_and_links)
        if name_and_links is None:
            product_name=''
            product_url=''
            continue
        else:
            product_name = name_and_links.text
            product_url=  name_and_links['href']
        
        if rating is None:
            rating =0 
            continue
        else:
            rating =rating.text

        if total_review is None:
            total_review=0
            continue
        else:
            total_review= total_review.text
        
        if price is None:
            price=0
            continue
        else:
            price = price.text
        
        product_url = domain+product_url

        #here we are solving the problem given in the second question 

        
        # product_webpage = requests.get(product_url,headers=headers)
        # product_soup = BeautifulSoup(product_webpage.content,'lxml')                

        # #here we are extracting the description of item in detailed form
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
        l= product_url.rfind('/dp/')
        ASIN= product_url[l+4:l+14]


        #here we are writing data in the csv file 
        data_list=[product_name,ASIN,product_url,rating,total_review,price]
        csvwriter.writerow(data_list)

        
        # product_urls.append(domain+product_urls)



collect_listing_urls()

