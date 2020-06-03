"""
校 园 新 闻 爬 取 
@Date 2020.05.30 
pip3 install beautifulsoup4
"""
# 连接数据库出现RuntimeError: cryptography is required for sha256_password or caching_sha2 _password
# 解决办法：安装cryptography即可:pip install cryptography
import requests
from bs4 import BeautifulSoup
import pymysql


def crawl():
    info_list = []
    for num in range(1, 3):
        url = 'http://news.niit.edu.cn/4000/list'+str(num)+'.htm'
        html = requests.get(url).content
        html_doc = str(html, 'utf-8')
        soup = BeautifulSoup(html_doc, 'html.parser')
        title_list = soup.find_all('span', {"class": "news_title"})
        for title in title_list:
            link_node = title.find("a")
            temp_dict = {}
            temp_dict['title'] = link_node['title'].strip()
            date_node = title.parent.find("span", {"class", "news_meta"})
            temp_dict['gmt_create'] = date_node.text
            temp_dict['gmt_modified'] = date_node.text
            temp_dict['is_deleted'] = 1
            temp_dict['is_top'] = 0
            url = 'http://news.niit.edu.cn'+link_node['href']
            html = requests.get(url).content
            html_doc = str(html, 'utf-8')
            soup = BeautifulSoup(html_doc, 'html.parser')
            content_div = soup.find(
                "div", {"class": "wp_articlecontent"})
            temp_dict['content'] = content_div.get_text()
            img_list = content_div.find_all('img')
            if len(img_list) >= 1:
                img_url = img_list[0]['src']
                temp_dict['cover'] = 'http://news.niit.edu.cn'+img_url
            else:
                temp_dict['cover'] = 'http://ww1.sinaimg.cn/large/0074PogOly1gfdqo5j2taj30zk0m8dnd.jpg'
            info_list.append(temp_dict)
    return info_list


def data_insert(info_list):
    # db = pymysql.connect("localhost", "root", "root", "db_python")
    db = pymysql.connect("rm-m5ee476bu350735gjeo.mysql.rds.aliyuncs.com",
                         "root", "XuNiit_#", "first_smart_campus")
    cursor = db.cursor()
    val = []
    for dic in info_list:
        item = (dic['cover'], dic['gmt_create'], dic['gmt_modified'],
                dic['is_deleted'], dic['is_top'], dic['content'], dic['title'])
        val.append(item)
    sql = "INSERT INTO info_manage (cover,gmt_create,gmt_modified,is_deleted,is_top,content,title) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    try:
        # 执行sql语句，批量插入
        cursor.executemany(sql, val)
    # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误，则回滚
        db.rollback()
    finally:
        # 关闭数据库
        db.close()


if __name__ == "__main__":
    list = crawl()
    print(len(list))
    data_insert((list))
