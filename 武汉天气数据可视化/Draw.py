import time

import pyecharts.options as opts
from pyecharts.charts import Line, Pie
from pyecharts.charts import Timeline
import numpy as np


class LineGraph:
    def __init__(self):
        self.text = "折线图"

    @staticmethod
    def draw(x_data, y_data):
        """

        :param x_data: 日期
        :param y_data: 温度
        :return:1:success 0 fail
        """

        year_month = x_data[0][:7]
        max_temp, min_temp, _ = y_data
        Lines = (
            Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
                series_name="最高气温",
                y_axis=max_temp,
                markpoint_opts=opts.MarkPointOpts(
                    data=[
                        opts.MarkPointItem(type_="max", name="最大值"),
                        opts.MarkPointItem(type_="min", name="最小值"),
                    ]
                ),
                markline_opts=opts.MarkLineOpts(
                    data=[opts.MarkLineItem(type_="average", name="平均值")]
                ),
            )
            .add_yaxis(
                series_name="最低气温",
                y_axis=min_temp,
                markpoint_opts=opts.MarkPointOpts(
                    data=[opts.MarkPointItem(value=-2, name="周最低", x=1, y=-1.5)]
                ),
                markline_opts=opts.MarkLineOpts(
                    data=[
                        opts.MarkLineItem(type_="average", name="平均值"),
                        opts.MarkLineItem(symbol="none", x="90%", y="max"),
                        opts.MarkLineItem(symbol="circle", type_="max", name="最高点"),
                    ]
                ),
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="", subtitle=""),
                tooltip_opts=opts.TooltipOpts(trigger="axis"),
                toolbox_opts=opts.ToolboxOpts(is_show=True),
                xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
            )
        )
        return [Lines, year_month]

    def add_month_timeline(self, linelist, year="", city="武汉"):
        tl = Timeline()
        for graph, year_month in linelist:
            tl.add(graph, str(year_month))

        tl.render("{}-{}{}的鬼天气.html".format(str(time.time()), year, city))


class PieGraph:
    def __init__(self):
        self.text = "大饼"

    @staticmethod
    def draw(item, rate):
        c = (
            Pie()
            .add("", [list(z) for z in zip(item, rate)])
            .set_colors(["blue", "green", "red"])
            .set_global_opts(title_opts=opts.TitleOpts(title="气温状况"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            # .render("pie_set_color.html")
        )
        return c
