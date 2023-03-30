import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import RenderType, ThemeType

path = "E:\\pythonProject\\Creation\\datas\\salary_city.xlsx"

df = pd.read_excel(path)
area = df['区'].tolist()
salary = df['工资'].tolist()

bar = (
    Bar(
        # 配置项
        init_opts=opts.InitOpts(
            # 初始化画布大小
            width='700px',
            height='400px',
            # 渲染风格
            renderer=RenderType.CANVAS,
            page_title="网页标题",
            # 设置表格主题
            theme=ThemeType.LIGHT,
            # 背景颜色
            bg_color='white'
        )
    )
        .add_xaxis(area)
        .add_yaxis("工资", salary)
        # 全局配置项
        .set_global_opts(
        # TitleOpts: 标题配置项
        title_opts=opts.TitleOpts(
            # 主标题
            title='北京各区薪资图',
            # 跳转链接
            title_link='https://www.baidu.com',
            # blank在新窗口打开 self在当前窗口打开
            title_target='blank',
            # 副标题
            subtitle='副标题',
            subtitle_link="",
            subtitle_target="self",
            # 位置
            # pos_left='center',
            # pos_right=
            # pos_bottom=
            # padding= 边距
        ),
        # DataZoomOpts: 区域缩放配置项
        datazoom_opts=opts.DataZoomOpts(
            is_show=True,

        )

    )

)
bar.render()
