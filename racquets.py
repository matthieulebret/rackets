import streamlit as st
import pandas as pd
import numpy as np
import requests



# from bs4 import BeautifulSoup
#
# import re

from st_aggrid import AgGrid

st.set_page_config(layout='wide')

st.title('Head Racquets analysis')

st.header('Head Racquets')


# base_site = 'https://www.head.com/en/tennis/racquets/tour.html'
#
#
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
#
# response = requests.get(base_site)
# html = response.content
# # #
# # ### 2.Choosing a parser
#
# soup = BeautifulSoup(html,'lxml')
#
# allproducts = soup.find_all('a',{'class':'product-item-link'})
# all_links = [product['href'] for product in allproducts[1:]]
# all_names = [product.text for product in allproducts[1:]]
#
# i=1
# totalracquets = 38
# placeholder = st.empty()
# progholder = st.empty()
# mybar = st.progress(0)
# #
# all_desc = []
# for link in all_links:
#     response = requests.get(link)
#     html = response.content
#     soup = BeautifulSoup(html,'lxml')
#     desc = soup.find_all('div',{'id':'tab-description'})
#     desc = [racquet.text for racquet in desc]
#     all_desc.append(desc[0])
#     # time.sleep(random.randint(1,4))
#     with placeholder:
#         st.write('Racquet #{0} complete '.format(i)+'/ '+str(totalracquets)+'.')
#     with progholder:
#         pct_complete = '{:,.2%}'.format(i/totalracquets)
#         st.write(pct_complete,' complete.' )
#         try:
#             mybar.progress(i/totalracquets)
#         except:
#             mybar.progress(1)
#     i=i+1
#
# df = pd.DataFrame({'Name':all_names,'Link':all_links,'Description':all_desc})


# df=pd.read_excel('racquets.xlsx').iloc[:,1:]

# all_links = df['Link'].tolist()
#
# i=1
# totalracquets = 38
# placeholder = st.empty()
# progholder = st.empty()
# mybar = st.progress(0)
#
# all_desc = []
#
#
# for link in all_links:
#     response = requests.get(link)
#     html = response.content
#     soup = BeautifulSoup(html,'lxml')
#     desc = soup.find_all('div',{'id':'tab-facts'})
#     desc = [racquet.text for racquet in desc]
#
#
#     all_desc.append(desc[0])
#     # time.sleep(random.randint(1,4))
#     with placeholder:
#         st.write('Racquet #{0} complete '.format(i)+'/ '+str(totalracquets)+'.')
#     with progholder:
#         pct_complete = '{:,.2%}'.format(i/totalracquets)
#         st.write(pct_complete,' complete.' )
#         try:
#             mybar.progress(i/totalracquets)
#         except:
#             mybar.progress(1)
#     i=i+1
#     st.write(desc)
#
# df['Facts']=all_desc
#
# df.to_excel('racquets_all.xlsx')

df = pd.read_excel('racquets_all.xlsx').iloc[:,1:]

# def splitfeature(string,wordstart,wordend):
#     string = string.split(wordstart)[1]
#     string = string.split(wordend)[0]
#     return string
#
# df['CPI'] = df['Facts'].apply(lambda x: int(splitfeature(x,'CPI:','Weight')))
# df['Weight (unstrung)'] = df['Facts'].apply(lambda x: int(splitfeature(x,'(unstrung):',' g /')))
# df['String pattern'] = df['Facts'].apply(lambda x: splitfeature(x,'String pattern:','Head'))
# df['Head size'] = df['Facts'].apply(lambda x: int(splitfeature(x,'Head size:','cm')))
# df['Grip size'] = df['Facts'].apply(lambda x: splitfeature(x,'Grip size:','Balance'))
# df['Balance'] = df['Facts'].apply(lambda x: splitfeature(x,'Balance:','Length'))
# df['Length'] = df['Facts'].apply(lambda x: int(splitfeature(x,'Length:',' mm /')))
# df['Beam'] = df['Facts'].apply(lambda x: x.split('Beam:')[1])
#
#
# links = df['Link'].tolist()

#
# df.drop(['Facts','Link'],inplace=True,axis=1)
# df['Link'] = links

# df.to_excel('racquets_all.xlsx')

df.drop(['Description'],inplace=True,axis=1)

with st.expander('Show CPI table'):
    st.image('https://cdn-magento2-media.head.com/wysiwyg/control_power_index_1.jpg')

st.markdown('https://www.head.com/en_US/tennis/how-tos/how-to-choose-a-tennis-racquet-in-10-steps')

AgGrid(df)
