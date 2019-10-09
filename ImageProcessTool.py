# -*- coding:utf-8 -*-
import wx
from PIL import Image

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, u'CM升级工具', size=(600, 400))

        # 创建面板

        panel = wx.Panel(self)

        # 创建按钮
        self.bt_FlipHoriz = wx.Button(panel, label='水平翻转')
        self.bt_FlipVert = wx.Button(panel, label='垂直翻转')
        self.bt_MidBase = wx.Button(panel, label='居中白底')  # 确定白底像素
        self.bt_AddWrite = wx.Button(panel, label='添加白底')

        # 创建文本

        self.lb_FilePath = wx.StaticText(panel, 0, u"文件路径：", style=wx.TE_LEFT)
        self.lb_Pixel = wx.StaticText(panel, 0, u"像      素：", style=wx.TE_LEFT)
        self.txt_FilePath = wx.TextCtrl(panel, style=wx.TE_LEFT, value=u'请选择图片目录')
        self.txt_Pixel = wx.TextCtrl(panel, style=wx.TE_LEFT, value=u'请输入像素')
        # 创建文本内容框，多行，垂直滚动条
        self.text_contents = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.HSCROLL)

        # 添加容器
        bsizer_top = wx.BoxSizer(wx.HORIZONTAL)

        bsizer_center = wx.BoxSizer(wx.HORIZONTAL)

        bsizer_botton1 = wx.BoxSizer(wx.VERTICAL)
        bsizer_botton2 = wx.BoxSizer(wx.VERTICAL)
        bsizer_content = wx.BoxSizer(wx.HORIZONTAL)

        # 容器中添加控件
        bsizer_top.Add(self.lb_FilePath, proportion=0, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, border=5)
        bsizer_top.Add(self.txt_FilePath, proportion=2, flag=wx.EXPAND | wx.ALL, border=5)

        bsizer_center.Add(self.lb_Pixel, proportion=0, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT,
                          border=5)
        bsizer_center.Add(self.txt_Pixel, proportion=2, flag=wx.EXPAND | wx.ALL, border=5)

        bsizer_botton1.Add(self.bt_FlipHoriz, proportion=1, flag=wx.ALL, border=5)
        bsizer_botton1.Add(self.bt_FlipVert, proportion=1, flag=wx.ALL, border=5)
        bsizer_botton1.Add(self.bt_MidBase, proportion=1, flag=wx.ALL, border=5)
        bsizer_botton2.Add(self.bt_AddWrite, proportion=1, flag=wx.ALL, border=5)
        bsizer_content.Add(self.text_contents, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

        # wx.VERTICAL 横向分割
        bsizer_all = wx.BoxSizer(wx.VERTICAL)
        # 添加顶部sizer，proportion=0 代表bsizer_top大小不可变化
        bsizer_all.Add(bsizer_top, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
        bsizer_all.Add(bsizer_center, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
        # 添加底部sizer，proportion=1 代表bsizer_bottom大小变化
        bsizer_botoom = wx.BoxSizer(wx.HORIZONTAL)
        bsizer_all.Add(bsizer_botoom, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
        bsizer_botoom.Add(bsizer_botton1, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
        bsizer_botoom.Add(bsizer_botton2, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
        bsizer_botoom.Add(bsizer_content, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
        self.Bind(wx.EVT_BUTTON, self.update, self.bt_FlipHoriz)
        self.Bind(wx.EVT_BUTTON, self.zipweb, self.bt_FlipVert)
        self.Bind(wx.EVT_BUTTON, self.addwrite, self.bt_AddWrite)
        panel.SetSizer(bsizer_all)

    def copyFiles(self, sourceDir, targetDir):
        pass

    def update(self, event):

        # build
        self.text_contents.AppendText('升级结束\n')

    # 生成网站升级包
    def zipweb(self, event):
        pass

    def addwrite(self, event):
        try:
            sourceFile = self.txt_FilePath.GetValue()
            image = Image.open(sourceFile)
            image = image.convert('RGBA')

            imagewidth = image.size[0]  # 图片宽度
            imageheight = image.size[1]  # 图片高度

            whiteimage = Image.open('白底.jpg')
            whiteimage = whiteimage.convert('RGB')

            whiteimage = whiteimage.resize((imagewidth, imageheight))

            whiteimage.paste(image, (0, 0), mask=image)
            whiteimage.save(sourceFile)
            self.text_contents.AppendText('白底转换成功\n')
        except Exception as e:
            self.text_contents.AppendText('报错：{0}\n'.format(e))
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    frame.Center()
    app.MainLoop()
