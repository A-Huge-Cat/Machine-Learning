import requests
from bs4 import BeautifulSoup


# 爬虫类
class WebSpider:
    def __init__(self, url="https://lishi.tianqi.com/wuhan/202206.html"):
        self.url = url
        self.headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}

    # 获取网页前端代码
    def collect_data(self):
        try:
            html_data = requests.get(self.url, headers=self.headers)
            bsobj = BeautifulSoup(html_data.text)
            return bsobj
        except:
            return "发生了一些错误"

    # 获取指定类别的代码
    @staticmethod
    def get_data(bsobj, classify):
        # 获取日期

        if classify == "日期":
            datelist = []
            date_data = bsobj.findAll('div', {"class": "th200"})

            for date in date_data:
                datelist.append(date.text)
            return datelist[1:]

        # 获取温度
        if classify == "温度":
            max_list, min_list = [], []
            temp_data = bsobj.findAll('div', {"class": "th140"})

            i = 0
            while i < len(temp_data):
                if '℃' in temp_data[i].text:
                    max_list.append(int(str(temp_data[i].text)[:-1]))
                    min_list.append(int(str(temp_data[i + 1].text)[:-1]))
                    i += 4
                else:
                    i += 1
            return [max_list, min_list]


if __name__ == "__main__":
    print(WebSpider.get_data(WebSpider().collect_data(), "日期"))
