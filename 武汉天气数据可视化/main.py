import numpy as np

import Spider
import Draw


# 获取历史上武汉天气数据
def history_wuhan():
    GraphMaker = Draw.LineGraph()
    PieMaker = Draw.PieGraph()
    return_data = []
    for year in ["2019", "2020", "2021", "2022"]:
        monthList = []
        Pielist = []
        for month in ["{}04".format(year), "{}05".format(year), "{}06".format(year)]:
            wp = Spider.WebSpider(url="https://lishi.tianqi.com/wuhan/{}.html".format(month))
            bsobj = wp.collect_data()
            datelist = Spider.WebSpider.get_data(bsobj=bsobj, classify="日期")
            templist = Spider.WebSpider.get_data(bsobj=bsobj, classify="温度")
            _, rate = cut(templist[0])
            label = ["热到死", "很热", "热"]
            Pielist.append([PieMaker.draw(label, rate), month])
            templist.append(month)
            return_data.append(templist)
            monthList.append(GraphMaker.draw(x_data=datelist, y_data=templist))
        GraphMaker.add_month_timeline(monthList, year)
        GraphMaker.add_month_timeline(Pielist, year)
    return return_data


# 获取今年内江天气数据
def Now_chengdu():
    GraphMaker = Draw.LineGraph()
    return_data = []
    monthList = []
    for month in ["202204", "202205", "202206"]:
        wp = Spider.WebSpider(url="https://lishi.tianqi.com/chengdu/{}.html".format(month))
        bsobj = wp.collect_data()
        datelist = Spider.WebSpider.get_data(bsobj=bsobj, classify='日期')
        templist = Spider.WebSpider.get_data(bsobj=bsobj, classify="温度")
        templist.append(month)
        return_data.append(templist)
        monthList.append(GraphMaker.draw(x_data=datelist, y_data=templist))

    GraphMaker.add_month_timeline(monthList, "2022", city="内江")
    return return_data


# 分段数据
def cut(max_tem):
    hot_to_die, too_hot, hot, rate = [], [], [], []
    for element in max_tem:
        if element > 30:
            hot_to_die.append(element)
        elif element > 25:
            too_hot.append(element)
        else:
            hot.append(element)

    rate.append(len(hot_to_die) / (len(hot_to_die) + len(too_hot) + len(hot)))
    rate.append(len(too_hot) / (len(hot_to_die) + len(too_hot) + len(hot)))
    rate.append(len(hot) / (len(hot_to_die) + len(too_hot) + len(hot)))

    # print(rate)
    return [hot_to_die, too_hot, hot], rate



history_wuhan()
