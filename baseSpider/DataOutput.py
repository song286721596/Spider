# -*-coding:utf-8-*-
#@Author: Songzq
#@Time: 2020年03月12日17时
import codecs

class DataOutput(object):
    def __init__(self):
        self.datas = []
    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)
        print(self.datas)

    def output_html(self):
        fout = codecs.open('bake.html', 'w',encoding='utf-8')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")
            #self.datas.remove(data) # 不知道是作者笔误，还是怎样这个地方是需要注释掉，要不然存储的文件只有一条记录
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()
