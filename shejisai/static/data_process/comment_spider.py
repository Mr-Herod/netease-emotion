import requests,json
from fake_useragent import UserAgent
import threading

class MySpider(threading.Thread):
    def __init__(self,song_id,s_num,e_num):
        threading.Thread.__init__(self)
        self.song_id = song_id
        self.s_num = s_num
        self.e_num = e_num
        self.comments = []
    
    def run(self):
        self.get_comment(self.song_id,self.s_num,self.e_num )
    
    
    def get_comment(self,song_id,s_num,e_num):
        comments = []
        ua = UserAgent()
        for page_num in range(s_num,e_num):
            url = "http://music.163.com/api/v1/resource/comments/R_SO_4_"+str(song_id)+"?offset="+str(page_num)+"&limit=20"
            data = json.loads(requests.get(url,headers = {"User-Agent":ua.random}).text)
            if data.get('comments'):
                comm = data['comments']
                if comm == []:
                    break
                for item in comm:
                    comm_data = {
                        'nickname': item['user']['nickname'],
                        'content': item['content'].replace('\r', ' '),
                        'like': item['likedCount'],
                        'time': item['time']
                    }
                    comments.append(comm_data)
            # print("now: ",page_num," Last comment: ",comments[-1]['content'])
            page_num += 1
        self.comments = comments

        
def get_songid(url):
    return url.split('=')[1]

def get_comments(song_id):
    spiders = []
    for i in range(10):
        spiders.append(MySpider(song_id,i*10,i*10+10))
    comments = []
    print("Spiders begin....")
    for i in range(10):
        spiders[i].start()
    for i in range(10):
        spiders[i].join()
    for i in range(10):
        comments += spiders[i].comments
    print("Spiders done....")
    with open("/home/ubuntu/shejisai/static/data_process/comments/"+str(song_id)+".txt","w",encoding = "utf-8") as f:
        f.write(str(comments))
    return comments

def draw_wordpic(song_id,comments):
    from wordcloud import WordCloud
    from PIL import Image
    import matplotlib.pyplot as plt
    import jieba
    import numpy as np
    words = jieba.cut(",".join([comment['content'] for comment in comments]))
    words = list(words)
    bgimg = np.array(Image.open("/home/ubuntu/shejisai/static/image/"+'music_bg.png'))
    wc_img = WordCloud(mask = bgimg,scale=4,max_font_size = 80,random_state=20,background_color ="white",font_path = '/home/ubuntu/shejisai/static/fonts/msyh.ttc').generate(" ".join(words))

    plt.figure(figsize = (4,5)) 
    plt.axis('off')
    plt.imshow(wc_img)
    plt.tight_layout()
    plt.savefig("/home/ubuntu/shejisai/static/image/"+str(song_id)+".jpg",dpi=300)

if __name__ == "__main__":
    url = input()
    song_id = get_songid(url)
    draw_wordpic(song_id,get_comments(song_id))
