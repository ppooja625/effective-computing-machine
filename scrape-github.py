
import sys
import requests
from bs4 import BeautifulSoup


base_url='https://github.com/topics/'
def get_top_repositories(doc):
    article_tags=doc.find_all('article',class_='border rounded color-shadow-small color-bg-subtle my-4')
    top_repos=[parse_repository(tag) for tag in article_tags]
    return top_repos

def get_topic_page(topic):
    topic_url=base_url+topic
    response=requests.get(topic_url)
    if not response.ok:
        print('response status:',response.status_code)
        raise Exception('failed to fetch the webpage'+topic_url)
    doc=BeautifulSoup(response.text)
    return doc
    
def parse_repository(article_tags):
    a_tag=article_tags.h3.find_all('a')
    username=a_tag[0].text.strip()
    repo_name=a_tag[1].text.strip()
    repo_url=base_url+a_tag[1]['href'].strip()
    star_tag=article_tags.find('span',class_='Counter js-social-count')
    star_count=parse_star_count(star_tag.text.strip())
    return {'repository_name': repo_name, 'owner_username': username, 'stars': star_count, 'repository_url': repo_url}

def parse_star_count(star_str):
    star_str=star_str.strip()
    if star_str[-1]=="k":
        return int(float(star_str[:-1]))*1000
    else:
        int(star_str)
    
def write_csv(items,path):
    with open(path,'w') as f:
        if len(items)==0:
            return
        headers=list(items[0].keys())
        f.write(','.join(headers)+'\n')

        for item in items:
            values=[]
            for header in headers:
                values.append(str(item.get(header,' ')))
            f.write(','.join(values)+'\n')
                
def scrap_topic_reperositories(topic,path=None):
    if path is None:
        path=topic+'.csv'
        
    topic_page_doc=get_topic_page(topic)
    topic_repositories=get_top_repositories(topic_page_doc)
    write_csv(topic_repositories,path)
    print('Top repositiories for {} written to path {} is'.format(topic,path))
    return path
        

            

if __name__=="__main__":
    #print(sys.argv[1])
    #topic=sys.argv[1]
   scrap_topic_reperositories('Azure')
