from bs4 import BeautifulSoup

html = """
<table>
    <tr>
        <th>船名</th>
        <th>航次</th>
        <th>提单号</th>
        <th>箱号</th>
        <th>报关单号</th>
        <th>作业码头</th>
        <th>海关放行状态</th>
        <th>EDI中心接收时间</th>
        <th>序列号</th>
    </tr>
    <tr>
        <td>CSCL OSAKA</td>
        <td>8197W</td>
        <td>KTSNSHA9AA003</td>
        <td>CSLU1106216</td>
        <td>220120161011282136</td>
        <td>外二期</td>
        <td>已放行</td>
        <td>201611161013</td>
        <td>400094490047</td>
    </tr>
    <tr>
        <td>CSCL OSAKA</td>
        <td>8197W</td>
        <td>KTSNSHA9AA003</td>
        <td>CSLU1374965</td>
        <td>220120161011282136</td>
        <td>外二期</td>
        <td>已放行</td>
        <td>201611161013</td>
        <td>400094490047</td>
    </tr>
</table>
"""
def spiderFile():
    soup = BeautifulSoup(html, 'html5lib')
    data_list = []  # 结构: [dict1, dict2, ...], dict结构{'船名': ship_name, '航次': voyage, '提单号': bill_num, '作业码头': wharf}
    for idx, tr in enumerate(soup.find_all('tr')):
        if idx != 0:
            tds = tr.find_all('td')
            data_list.append({
                '船名': tds[0].contents[0],
                '航次': tds[1].contents[0],
                '提单号': tds[2].contents[0],
                '作业码头': tds[5].contents[0]
            })
    print(data_list)
if __name__ =='__main__':
    spiderFile()
