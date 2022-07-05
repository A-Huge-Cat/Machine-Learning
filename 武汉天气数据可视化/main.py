import Spider
import Draw


GraphMaker = Draw.LineGraph()
yearlist = []
for year in ["2019", "2020", "2021", "2022"]:
    monthList = []
    for month in ["{}04".format(year), "{}05".format(year), "{}06".format(year)]:
        wp = Spider.WebSpider(url="https://lishi.tianqi.com/wuhan/{}.html".format(month))
        bsobj = wp.collect_data()
        datelist = Spider.WebSpider.get_data(bsobj=bsobj, classify="日期")
        templist = Spider.WebSpider.get_data(bsobj=bsobj, classify="温度")
        monthList.append(GraphMaker.draw(x_data=datelist, y_data=templist))
    GraphMaker.add_month_timeline(monthList, year)


