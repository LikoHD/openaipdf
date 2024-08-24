
# 📚 Books Counter

Book Counter 是一个简单的网页应用，用于统计 PDF 文件中提到的其他书籍。
体验地址：www.bookinbook.top/
![WechatIMG166](https://github.com/user-attachments/assets/65e70e22-f182-40cd-94e3-8fe592cc3315)
![screenshot-20240824-180032](https://github.com/user-attachments/assets/0e631e1e-3f1d-44a8-9d8e-b406fc8377fa)



## 功能特点

- 上传 PDF 文件
- 分析 PDF 内容，识别书名
- 统计每本书出现的次数和页码
- 以表格形式展示统计结果

## 技术栈

- HTML5
- JavaScript
- Tailwind CSS
- PDF.js

## 使用方法

1. 打开应用页面
2. 点击"选择文件"按钮，选择要分析的 PDF 文件
3. 点击"上传并查看 PDF 中提及的书籍"按钮
4. 等待分析完成，查看统计结果

## 统计结果展示

- 总计提及的书籍数量
- 每本书的详细信息：
  - 书名
  - 出现页数
  - 出现页码（最多显示前 5 页，超过则显示总页数）

## 本地运行

1. 克隆仓库到本地
2. 使用支持 CORS 的本地服务器运行 `index.html`（例如 Live Server）
3. 在浏览器中打开应用

## 注意事项

- 请确保上传的是有效的 PDF 文件
- 大型 PDF 文件可能需要较长的处理时间
- 统计结果按书籍出现次数降序排列

## 贡献

欢迎提交 Issues 和 Pull Requests 来改进这个项目。

## 许可证

[MIT License](LICENSE)
