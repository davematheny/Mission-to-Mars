#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


# Visit the Mars news site
url = 'https://redplanetscience.com/'
browser.visit(url)


# In[ ]:


# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[ ]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')


# In[ ]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[ ]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# In[ ]:


# ## JPL Space Images Featured Image

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[ ]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[ ]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[ ]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[ ]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[ ]:


# ## Mars Facts

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()

df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df

df.to_html()

#browser.quit()


# In[ ]:





# In[122]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[131]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
html = browser.html
hemisphere_soup = soup(html, 'html.parser')

hemisphere_titles = hemisphere_soup.find_all('h3')
#hemisphere_images = hemisphere_soup.find('img', class_='thumb').get('src')
#loop 
for a in hemisphere_titles:
    #hemisphere_soup = soup(html, 'html.parser')
    if a.text != 'Back':
        title = a.text
        #print(title)
        hemisphere_images = url+hemisphere_image_soup.find('img', alt=title+' thumbnail').get('src')
        #print(hemisphere_images)
        hemisphere_both = {'img_url': hemisphere_images,'title': title}
        #print(hemisphere_both)
        hemisphere_image_urls.append(hemisphere_both)


# In[132]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[134]:


# 5. Quit the browser
browser.quit()


# In[87]:





# In[126]:





# In[90]:





# In[125]:





# In[ ]:




