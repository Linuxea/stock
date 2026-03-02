with open('20260303/us_stock_report.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 简单替换
content = content.replace('<title>2026年2月27日 美股市场行情报告</title>', 
                          '<title>2026年3月3日 美股市场行情报告</title>')
content = content.replace('2026年2月27日 星期四 | 美国东部时间',
                          '2026年3月3日 星期二 | 美国东部时间')
content = content.replace('2026-02-27 16:00 ET', '2026-03-02 16:00 ET')
content = content.replace('48,977.92', '48,904.78')
content = content.replace('▼ 521.28', '▼ 73.14')
content = content.replace('-1.05%', '-0.15%')
content = content.replace('PPI数据高于预期，道指大幅下挫超500点，创近期最大跌幅',
                          '中东局势紧张，道指小幅下跌，能源股走强提供支撑')
content = content.replace('6,878.88', '6,881.62')
content = content.replace('▼ 29.98', '▲ 2.74')
content = content.replace('-0.43%', '+0.04%')
content = content.replace('通胀担忧升温，科技股拖累标普500指数下跌，2月整体转负',
                          '能源股走强助标普500指数企稳，中东冲突影响发酵')
content = content.replace('22,668.21', '22,748.86')
content = content.replace('▼ 210.17', '▲ 80.65')
content = content.replace('-0.92%', '+0.36%')
content = content.replace('科技股承压，英伟达等AI龙头延续跌势，纳斯达克跌近1%',
                          '科技股反弹，投资者逢低买入，纳斯达克收涨')

# 写入文件
with open('20260303/us_stock_report.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('基本更新完成')
