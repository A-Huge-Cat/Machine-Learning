import Spider
import Draw

# 获取历史上武汉天气数据
def history_wuhan():
    GraphMaker = Draw.LineGraph()
    return_data = []
    for year in ["2019", "2020", "2021", "2022"]:
        monthList = []
        for month in ["{}04".format(year), "{}05".format(year), "{}06".format(year)]:
            wp = Spider.WebSpider(url="https://lishi.tianqi.com/wuhan/{}.html".format(month))
            bsobj = wp.collect_data()
            datelist = Spider.WebSpider.get_data(bsobj=bsobj, classify="日期")
            templist = Spider.WebSpider.get_data(bsobj=bsobj, classify="温度")
            templist.append(month)
            return_data.append(templist)
            monthList.append(GraphMaker.draw(x_data=datelist, y_data=templist))
        GraphMaker.add_month_timeline(monthList, year)
    return return_data



# 获取今年成都天气数据
def Now_NeiJiang():
    GraphMaker = Draw.LineGraph()
    return_data = []
    monthList = []
    for month in ["202204", "202205", "202206"]:
        wp = Spider.WebSpider(url="https://lishi.tianqi.com/neijiang/{}.html".format(month))
        bsobj = wp.collect_data()
        datelist = Spider.WebSpider.get_data(bsobj=bsobj, classify='日期')
        templist = Spider.WebSpider.get_data(bsobj=bsobj, classify="温度")
        templist.append(month)
        return_data.append(templist)
        monthList.append(GraphMaker.draw(x_data=datelist, y_data=templist))

    GraphMaker.add_month_timeline(monthList, "2022", city="内江")
    return return_data

Now_NeiJiang()
