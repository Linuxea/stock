import re

with open('20260228/us_stock_report.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 标题
content = re.sub(r'<title>2026年2月27日 美股市场行情报告</title>', 
                 '<title>2026年3月3日 美股市场行情报告</title>', content)

# 2. 头部日期
content = re.sub(r'2026年2月27日 星期四 \| 美国东部时间', 
                 '2026年3月3日 星期二 | 美国东部时间', content)

# 3. 更新时间
content = re.sub(r'2026-02-27 16:00 ET', '2026-03-02 16:00 ET', content)

# 4. 三大指数数据
# 道琼斯
content = re.sub(r'48,977.92</p>\s*<div class="flex items-center justify-center gap-2">\s*<span class="text-red-600 font-semibold">▼ 521.28</span>\s*<span class="px-2 py-1 rounded-full bg-red-100 text-red-700 text-sm font-medium">-1.05%</span>',
                 '48,904.78</p>\n                        <div class="flex items-center justify-center gap-2">\n                            <span class="text-red-600 font-semibold">▼ 73.14</span>\n                            <span class="px-2 py-1 rounded-full bg-red-100 text-red-700 text-sm font-medium">-0.15%</span>', content)
content = re.sub(r'PPI数据高于预期，道指大幅下挫超500点，创近期最大跌幅',
                 '中东局势紧张，道指小幅下跌，能源股走强提供支撑', content)

# 标普500
content = re.sub(r'6,878.88</p>\s*<div class="flex items-center justify-center gap-2">\s*<span class="text-red-600 font-semibold">▼ 29.98</span>\s*<span class="px-2 py-1 rounded-full bg-red-100 text-red-700 text-sm font-medium">-0.43%</span>',
                 '6,881.62</p>\n                        <div class="flex items-center justify-center gap-2">\n                            <span class="text-green-600 font-semibold">▲ 2.74</span>\n                            <span class="px-2 py-1 rounded-full bg-green-100 text-green-700 text-sm font-medium">+0.04%</span>', content)
content = re.sub(r'通胀担忧升温，科技股拖累标普500指数下跌，2月整体转负',
                 '能源股走强助标普500指数企稳，中东冲突影响发酵', content)

# 纳斯达克
content = re.sub(r'22,668.21</p>\s*<div class="flex items-center justify-center gap-2">\s*<span class="text-red-600 font-semibold">▼ 210.17</span>\s*<span class="px-2 py-1 rounded-full bg-red-100 text-red-700 text-sm font-medium">-0.92%</span>',
                 '22,748.86</p>\n                        <div class="flex items-center justify-center gap-2">\n                            <span class="text-green-600 font-semibold">▲ 80.65</span>\n                            <span class="px-2 py-1 rounded-full bg-green-100 text-green-700 text-sm font-medium">+0.36%</span>', content)
content = re.sub(r'科技股承压，英伟达等AI龙头延续跌势，纳斯达克跌近1%',
                 '科技股反弹，投资者逢低买入，纳斯达克收涨', content)

# 5. 市场要闻 - 更新内容
content = re.sub(r'PPI通胀数据超预期</h4>\s*<p class="text-sm text-gray-600">美国1月生产者物价指数（PPI）高于市场预期，显示通胀压力仍存。市场担忧美联储将维持紧缩货币政策更长时间。</p>',
                 '中东局势紧张推升油价</h4>\n                        <p class="text-sm text-gray-600">美以袭击伊朗引发地缘政治风险，国际油价大涨超6%，能源股走强。市场关注冲突是否会进一步升级。</p>', content)

content = re.sub(r'AI赛道持续分化</h4>\s*<p class="text-sm text-gray-600">英伟达财报后股价延续跌势，市场对AI基础设施支出的可持续性产生怀疑。戴尔因AI服务器需求飙升大涨21.8%。</p>',
                 '能源股逆势走强</h4>\n                        <p class="text-sm text-gray-600">埃克森美孚、雪佛龙等能源股上涨，受益于油价飙升。国防股也获得资金流入，诺斯罗普·格鲁曼涨约4%。</p>', content)

content = re.sub(r'CoreWeave暴跌</h4>\s*<p class="text-sm text-gray-600">云计算公司CoreWeave业绩指引不及预期，股价暴跌18.6%，拖累云计算板块整体走弱。</p>',
                 '科技股反弹收高</h4>\n                        <p class="text-sm text-gray-600">英伟达、微软等科技股从早盘低点反弹，投资者在美以袭击伊朗后逢低买入，推动纳指转涨。</p>', content)

content = re.sub(r'2月回购创新高</h4>\s*<p class="text-sm text-gray-600">尽管市场波动，2月企业回购授权创下2333亿美元纪录，为部分大盘股提供支撑。</p>',
                 '避险资金流入黄金</h4>\n                        <p class="text-sm text-gray-600">地缘政治风险推动黄金价格涨超1.8%，突破5300美元/盎司。投资者寻求避险资产。</p>', content)

# 6. 科技七巨头表现 - 更新数据
# 英伟达
content = re.sub(r'英伟达</p>\s*<p class="text-lg font-bold text-red-600">-4.1%</p>\s*<p class="text-xs text-gray-500">AI支出担忧</p>',
                 '英伟达</p>\n                    <p class="text-lg font-bold text-green-600">+2.0%</p>\n                    <p class="text-xs text-gray-500">逢低买入</p>', content)

# 苹果
content = re.sub(r'苹果</p>\s*<p class="text-lg font-bold text-red-600">-0.8%</p>\s*<p class="text-xs text-gray-500">随大盘调整</p>',
                 '苹果</p>\n                    <p class="text-lg font-bold text-red-600">-0.5%</p>\n                    <p class="text-xs text-gray-500">小幅调整</p>', content)

# 微软
content = re.sub(r'微软</p>\s*<p class="text-lg font-bold text-red-600">-2.5%</p>\s*<p class="text-xs text-gray-500">云计算承压</p>',
                 '微软</p>\n                    <p class="text-lg font-bold text-green-600">+2.2%</p>\n                    <p class="text-xs text-gray-500">反弹强劲</p>', content)

# 亚马逊
content = re.sub(r'亚马逊</p>\s*<p class="text-lg font-bold text-red-600">-1.2%</p>\s*<p class="text-xs text-gray-500">电商板块调整</p>',
                 '亚马逊</p>\n                    <p class="text-lg font-bold text-green-600">+0.8%</p>\n                    <p class="text-xs text-gray-500">温和上涨</p>', content)

# 谷歌
content = re.sub(r'谷歌</p>\s*<p class="text-lg font-bold text-red-600">-1.8%</p>\s*<p class="text-xs text-gray-500">AI竞争加剧</p>',
                 '谷歌</p>\n                    <p class="text-lg font-bold text-green-600">+1.5%</p>\n                    <p class="text-xs text-gray-500">跟随反弹</p>', content)

# Meta
content = re.sub(r'Meta</p>\s*<p class="text-lg font-bold text-red-600">-1.5%</p>\s*<p class="text-xs text-gray-500">广告收入担忧</p>',
                 'Meta</p>\n                    <p class="text-lg font-bold text-green-600">+1.2%</p>\n                    <p class="text-xs text-gray-500">广告业务稳定</p>', content)

# 特斯拉
content = re.sub(r'特斯拉</p>\s*<p class="text-lg font-bold text-green-600">\+0.5%</p>\s*<p class="text-xs text-gray-500">逆势小幅上涨</p>',
                 '特斯拉</p>\n                    <p class="text-lg font-bold text-red-600">-1.0%</p>\n                    <p class="text-xs text-gray-500">电动车需求担忧</p>', content)

# 戴尔
content = re.sub(r'戴尔</p>\s*<p class="text-lg font-bold text-green-600">\+21.8%</p>\s*<p class="text-xs text-gray-500">AI服务器爆发</p>',
                 '戴尔</p>\n                    <p class="text-lg font-bold text-green-600">+3.5%</p>\n                    <p class="text-xs text-gray-500">服务器需求稳</p>', content)

# 7. 板块表现 - 领涨板块
content = re.sub(r'戴尔科技</span>\s*<p class="text-xs text-gray-500">AI服务器需求强劲</p>\s*</div>\s*<span class="text-green-600 font-bold text-lg">\+21.8%</span>',
                 '埃克森美孚</span>\n                                <p class="text-xs text-gray-500">油价大涨推动</p>\n                            </div>\n                            <span class="text-green-600 font-bold text-lg">+4.8%</span>', content)

content = re.sub(r'奈飞</span>\s*<p class="text-xs text-gray-500">退出华纳竞标</p>\s*</div>\s*<span class="text-green-600 font-bold text-lg">\+9.0%</span>',
                 '雪佛龙</span>\n                                <p class="text-xs text-gray-500">能源板块领涨</p>\n                            </div>\n                            <span class="text-green-600 font-bold text-lg">+4.2%</span>', content)

content = re.sub(r'公用事业</span>\s*<p class="text-xs text-gray-500">防御性资金流入</p>\s*</div>\s*<span class="text-green-600 font-bold text-lg">\+0.5%</span>',
                 '诺斯罗普·格鲁曼</span>\n                                <p class="text-xs text-gray-500">国防股受青睐</p>\n                            </div>\n                            <span class="text-green-600 font-bold text-lg">+4.1%</span>', content)

# 领跌板块
content = re.sub(r'半导体</span>\s*<p class="text-xs text-gray-500">英伟达领跌</p>\s*</div>\s*<span class="text-red-600 font-bold text-lg">-3.5%</span>',
                 '旅游休闲</span>\n                                <p class="text-xs text-gray-500">地缘风险冲击</p>\n                            </div>\n                            <span class="text-red-600 font-bold text-lg">-3.2%</span>', content)

content = re.sub(r'云计算</span>\s*<p class="text-xs text-gray-500">CoreWeave拖累</p>\s*</div>\s*<span class="text-red-600 font-bold text-lg">-2.8%</span>',
                 '航空运输</span>\n                                <p class="text-xs text-gray-500">航线风险增加</p>\n                            </div>\n                            <span class="text-red-600 font-bold text-lg">-2.9%</span>', content)

content = re.sub(r'金融服务</span>\s*<p class="text-xs text-gray-500">私人信贷担忧</p>\s*</div>\s*<span class="text-red-600 font-bold text-lg">-2.2%</span>',
                 '消费电子</span>\n                                <p class="text-xs text-gray-500">需求预期下调</p>\n                            </div>\n                            <span class="text-red-600 font-bold text-lg">-1.8%</span>', content)

content = re.sub(r'Block Inc</span>\s*<p class="text-xs text-gray-500">大规模裁员</p>\s*</div>\s*<span class="text-red-600 font-bold text-lg">-8.5%</span>',
                 '波音</span>\n                                <p class="text-xs text-gray-500">供应链担忧</p>\n                            </div>\n                            <span class="text-red-600 font-bold text-lg">-2.5%</span>', content)

# 8. 图表数据 - 更新图表标签和数据数组
content = re.sub(r'labels: \['道琼斯\', \'标普500\', \'纳斯达克\', \'英伟达\', \'微软\', \'谷歌\', \'亚马逊\', \'戴尔\', \'奈飞\'\]',
                 "labels: ['道琼斯', '标普500', '纳斯达克', '英伟达', '微软', '谷歌', '亚马逊', '埃克森美孚', '诺斯罗普']", content)

content = re.sub(r'data: \[-1.05, -0.43, -0.92, -4.1, -2.5, -1.8, -1.2, 21.8, 9.0\]',
                 'data: [-0.15, 0.04, 0.36, 2.0, 2.2, 1.5, 0.8, 4.8, 4.1]', content)

content = re.sub(r"backgroundColor: \['#ef4444', '#ef4444', '#ef4444', '#ef4444', '#ef4444', '#ef4444', '#ef4444', '#22c55e', '#22c55e'\]",
                 "backgroundColor: ['#ef4444', '#22c55e', '#22c55e', '#22c55e', '#22c55e', '#22c55e', '#22c55e', '#22c55e', '#22c55e']", content)

# 9. 市场总结与展望
content = re.sub(r'美股三大指数集体收跌，道指大跌超500点，创近期最大单日跌幅。高于预期的PPI数据打破市场对通胀放缓的乐观预期，强化了美联储维持紧缩政策的预期。科技股成为重灾区，AI产业链持续分化。',
                 '美股周一收盘涨跌不一，道指小幅下跌，标普500和纳指收涨。中东局势紧张推动油价大涨，能源股走强。科技股从早盘低点反弹，投资者在地缘政治风险中逢低买入。', content)

# 风险因素
content = re.sub(r'<li>• 通胀数据高于预期</li>\s*<li>• AI投资可持续性存疑</li>\s*<li>• 美联储政策路径复杂</li>',
                 '<li>• 中东冲突升级风险</li>\n                        <li>• 油价持续上涨压力</li>\n                        <li>• 全球供应链扰动</li>', content)

# 关注要点
content = re.sub(r'<li>• 戴尔AI服务器需求爆发</li>\s*<li>• 企业回购创新高</li>\s*<li>• 防御板块相对抗跌</li>',
                 '<li>• 能源股逆势走强</li>\n                        <li>• 科技股弹性显现</li>\n                        <li>• 避险资产受追捧</li>', content)

# 后市展望
content = re.sub(r'<li>• 关注通胀与利率预期</li>\s*<li>• AI产业兑现度成关键</li>\s*<li>• 震荡分化或成常态</li>',
                 '<li>• 关注地缘政治进展</li>\n                        <li>• 能源与防御板块配置</li>\n                        <li>• 市场波动可能加剧</li>', content)

# 输出到新文件
with open('20260303/us_stock_report.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('美股报告生成完成')
