import matplotlib.pyplot as plt

import Draw
import Spider


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
    return return_data, datelist


# 获取今年成都天气数据
def history_chengdu():
    GraphMaker = Draw.LineGraph()
    PieMaker = Draw.PieGraph()
    Pielist = []
    return_data = []
    monthList = []
    for month in ["202204", "202205", "202206"]:
        wp = Spider.WebSpider(url="https://lishi.tianqi.com/chengdu/{}.html".format(month))
        bsobj = wp.collect_data()
        datelist = Spider.WebSpider.get_data(bsobj=bsobj, classify='日期')
        templist = Spider.WebSpider.get_data(bsobj=bsobj, classify="温度")
        _, rate = cut(templist[0])
        label = ["热到死", "很热", "热"]
        Pielist.append([PieMaker.draw(label, rate), month])
        templist.append(month)
        return_data.append(templist)
        monthList.append(GraphMaker.draw(x_data=datelist, y_data=templist))
    GraphMaker.add_month_timeline(Pielist, "2022", city="成都")
    GraphMaker.add_month_timeline(monthList, "2022", city="成都")
    return return_data, datelist


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


# 两个城市的比较
def compare(yearmonth):
    data_wuhan, date_wuhan = history_wuhan()
    data_chengdu, date_chengdu = history_chengdu()
    for data in data_wuhan:
        if data[-1] == yearmonth:
            max_temp_wuhan, min_temp_wuhan, _ = data
    for data in data_chengdu:
        if data[-1] == yearmonth:
            max_temp_chengdu, min_temp_chengdu, _ = data

    return [max_temp_wuhan, max_temp_chengdu], [min_temp_wuhan, min_temp_chengdu], date_wuhan


def main():
    max_temp_list, min_temp_list, date = compare("202206")
    plt.figure()
    plt.plot(date, max_temp_list[0], "r--")
    plt.plot(date, max_temp_list[1], "b--")
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
    plt.xticks(rotation=90)
    plt.xlabel("日期")
    plt.ylabel("温度")
    plt.legend(["武汉最高气温", "成都最高温度"])
    plt.show()

if __name__ == '__main__':
    main()
