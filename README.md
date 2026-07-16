# Outdoor Gear Guide - 户外装备入门指南

一个帮助户外新手了解装备、选择品牌、根据预算推荐的Web应用。

## 功能特性

- **装备分类浏览** - 12大类装备：登山包、登山杖、冲锋衣、登山鞋、帐篷、睡袋、徒步鞋、睡垫、炉头套锅、净水设备、头灯、导航装备
- **品牌详细介绍** - 每个品类涵盖多个知名品牌（始祖鸟、Osprey、Gregory、Salomon等）
- **预算智能推荐** - 输入预算，自动生成装备推荐清单
- **装备对比工具** - 同品类不同品牌横向对比
- **新手入门指南** - 从活动类型到安全须知，系统化学习
- **装备清单生成器** - 根据活动类型和季节自动生成必备清单

## 快速开始

### 环境要求
- Python 3.8+
- Flask 3.0+

### 安装
`ash
cd outdoor_guide
pip install flask
`

### 运行
`ash
python app.py
`

然后在浏览器中打开 http://127.0.0.1:5000

## 项目结构

`
outdoor_guide/
├── app.py                 # Flask主应用
├── requirements.txt       # 依赖列表
├── data/
│   ├── equipment_db.json  # 装备数据库
│   └── models.py          # 数据读写工具
├── templates/             # HTML模板
│   ├── base.html          # 基础布局
│   ├── index.html         # 首页
│   ├── category.html      # 品类详情
│   ├── guide.html         # 新手指南
│   ├── compare.html       # 装备对比
│   └── checklist.html     # 清单生成器
└── static/
    ├── css/
    │   └── style.css      # 样式表
    └── js/
        └── main.js        # 前端交互
`

## API接口

- GET / - 首页
- GET /category/<id> - 品类详情
- GET /guide - 新手指南
- GET /compare - 装备对比
- GET /checklist - 清单生成器
- GET /api/categories - 获取所有装备数据
- POST /api/recommend - 获取推荐（JSON: {budget: 5000}）

## 覆盖品牌

- **国际品牌**: Arc'teryx, Osprey, Gregory, Deuter, Patagonia, MSR, Big Agnes, Mammut, LEKI, Black Diamond, Scarpa, Salomon, Merrell, Lowa, Petzl, Jetboil, Katadyn, Therm-a-Rest, Sea to Summit, Marmot, Snow Peak, Garmin
- **国产品牌**: 凯乐石(KAILAS), 探路者(Toread), 牧高笛(Mobi Garden), 黑冰(Black Ice), 火枫(Fire-Maple), 两步路

##  License

MIT
