import json

routes_data = {
    'wugongshan': {
        'name': '武功山',
        'location': '江西省萍乡市',
        'elevation': '金顶 1918m',
        'featured': '高山草甸、云海、星空',
        'description': '武功山以高山草甸闻名，是中国十大徒步路线之一。连绵不绝的万亩草甸在山顶铺展，日出云海和星空露营是其最大亮点。适合新手入门，基础设施完善。',
        'best_season': '3-5月（杜鹃花）、9-11月（金黄草甸、晴朗天气）',
        'difficulty': '⭐⭐（初级）',
        'duration': '2-3天',
        'distance_km': 35,
        'total_ascent_m': 1400,
        'routes': [
            {
                'name': '经典徒步线（发云界-金顶）',
                'type': '主力路线',
                'start_point': '萍乡市芦溪县发云界（乘车至沈子村驿站约2小时）',
                'end_point': '武功山金顶',
                'distance_km': 28,
                'ascent_m': 1300,
                'time_hours': '2天1夜',
                'waypoints': [
                    {'name': '发云界入口', 'elevation': '500m', 'note': '大巴到达处，需换乘中巴至沈子村'},
                    {'name': '沈子村', 'elevation': '600m', 'note': '徒步起点，有客栈补给'},
                    {'name': '吊马庄', 'elevation': '900m', 'note': '中途休息点，约3小时'},
                    {'name': '观音宕', 'elevation': '1200m', 'note': '大片草甸营地，风景绝佳'},宕'},
                    {'name': '华顶', 'elevation': '1400m', 'note': '扎营点，可看日出'},
                    {'name': '金顶（龙王山）', 'elevation': '1918m', 'note': '最高点，标志性建筑'}
                ],
                'emergency_exit': [
                    {'name': '吊马庄下撤点', 'desc': '可沿原路返回沈子村，约4小时'},
                    {'name': '观光索道', 'desc': '从西坑站乘坐索道下山，耗时约20分钟'}
                ],
                'camping': '观音宕（免费营地，草甸平坦）、华顶（收费营地，有水源）',
                'supply': '沈子村有小店，山上金顶和游客中心有商店但价格较高'
            },
            {
                'name': '索道轻松线',
                'type': '休闲路线',
                'start_point': '游客中心',
                'end_point': '金顶',
                'distance_km': 5,
                'ascent_m': 300,
                'time_hours': '半天',
                'waypoints': [
                    {'name': '游客中心', 'elevation': '400m', 'note': '购票乘车至索道下站'},
                    {'name': '索道下站', 'elevation': '600m', 'note': '乘坐索道上山'},
                    {'name': '金顶', 'elevation': '1918m', 'note': '山顶观景'}
                ],
                'emergency_exit': [{'name': '索道下行', 'desc': '随时可乘索道下山'}],
                'camping': '无',
                'supply': '山顶有餐厅和小卖部'
            }
        ],
        'transport': {
            '到达': '高铁至萍乡北站，转乘大巴至芦溪县，再打车到武功山游客中心（约3小时）',
            '住宿': '山上客栈20-80元/人（床位），金顶酒店200-500元；山下客栈80-200元/晚'
        },
        'tips': [
            '山顶温差大，即使是夏天也要带冲锋衣或薄羽绒服',
            '草甸路段无遮挡，务必做好防晒',
            '旺季（国庆、五一）山上住宿紧张且涨价，提前预订',
            '建议自带干粮和水，山上物价较高',
            '星空摄影爱好者建议选择晴天夜晚扎营'
        ]
    },
    
    'genie_nanxian': {
        'name': '格聂南线',
        'location': '四川省甘孜州理塘县',
        'elevation': '格聂峰 6204m（周边穿越）',
        'featured': '藏区神山、冷古寺、热梯温泉、原始森林、高山海子',
        'description': '格聂南线被誉为"川藏线上最后的净土"，环绕格聂神峰的徒步线路，沿途经过原始森林、高山草甸、冰川海子和藏寨，风景壮美且游客稀少，是进阶徒步者的天堂。',
        'best_season': '5-6月（花海）、9-10月（秋色）',
        'difficulty': '⭐⭐⭐⭐（高阶）',
        'duration': '5-7天',
        'distance_km': 120,
        'total_ascent_m': 3500,
        'routes': [
            {
                'name': '格聂南线环线（理塘-格聂-理塘）',
                'type': '主力环线',
                'start_point': '理塘县',
                'end_point': '理塘县',
                'distance_km': 120,
                'ascent_m': 3500,
                'time_hours': '6天5夜',
                'waypoints': [
                    {'name': '理塘（起点）', 'elevation': '4014m', 'note': '世界highest城市，适应海拔第一天'},
                    {'name': '贡嘎岭', 'elevation': '4200m', 'note': '第二天抵达，经冷古寺，海拔适应关键点'},
                    {'name': '沙溪牧场', 'elevation': '4300m', 'note': '第三天，高山草甸，牛群成群'},
                    {'name': '格聂之眼', 'elevation': '4400m', 'note': '第四天，标志性景点，俯瞰河谷'},
                    {'name': '热梯温泉', 'elevation': '4100m', 'note': '第五天，天然温泉恢复体力'},
                    {'name': '獐子坝', 'elevation': '3800m', 'note': '第六天，原始森林，徒步终点附近'},
                    {'name': '理塘（终点）', 'elevation': '4014m', 'note': '返回理塘县城'}
                ],
                'emergency_exit': [
                    {'name': '贡嘎岭下撤', 'desc': '如遇恶劣天气可从贡嘎岭骑马返回理塘（约半天）'},
                    {'name': '沙溪牧场骑马点', 'desc': '部分路段可雇佣马帮驮运物资'}
                ],
                'camping': '沙溪牧场（高山草甸营地）、格聂之眼附近（视野开阔）、獐子坝（林区营地）',
                'supply': '理塘县城物资充足；贡嘎岭有小卖部；途中需自带全部食物和燃料'
            }
        ],
        'transport': {
            '到达': '成都新南门车站坐大巴到理塘（约7小时），或飞抵甘孜格聂机场（季节性航班）',
            '住宿': '理塘县城宾馆100-300元/晚；途中仅能露营'
        },
        'tips': [
            '海拔4000m+，务必预留1-2天适应高原，预防高反',
            '建议找当地藏族向导带队，部分路段无明显路径',
            '夏季可能有暴雨，备好防水装备和保暖衣物',
            '尊重藏区宗教习俗，不要随意触碰玛尼堆和经幡',
            '带上卫星通讯设备，全程大部分区域无信号',
            '高热量食物要多带，高海拔消耗大'
        ]
    },
    
    'yubeng': {
        'name': '雨崩村',
        'location': '云南省迪庆州德钦县梅里雪山脚下',
        'elevation': '雨崩村 3150m / 冰湖 4100m',
        'featured': '梅里雪山日照金山、神瀑、冰湖、藏寨风情',
        'description': '雨崩被称为"藏在梅里雪山中的世外桃源"，是一个只有几百人的藏族小村落。徒步进入雨崩是经典线路，途经神瀑和冰湖两条支线，沿途欣赏梅里雪山十三峰，是入门级高山徒步的首选。',
        'best_season': '3-5月（春暖花开）、10-11月（秋高气爽、看日照金山最佳）',
        'difficulty': '⭐⭐⭐（中级）',
        'duration': '4-5天',
        'distance_km': 40,
        'total_ascent_m': 1600,
        'routes': [
            {
                'name': '进雨崩线（西当温泉-雨崩）',
                'type': '进山路线',
                'start_point': '西当温泉',
                'end_point': '雨崩上村',
                'distance_km': 14,
                'ascent_m': 900,
                'time_hours': '6-7小时（徒步）/ 1小时（越野车）',
                'waypoints': [
                    {'name': '西当温泉', 'elevation': '2400m', 'note': '进山起点，可乘越野车或徒步'},
                    {'name': '南宗垭口', 'elevation': '3500m', 'note': '翻越山口，俯瞰整个雨崩和梅里雪山全景'},
                    {'name': '雨崩上村', 'elevation': '3150m', 'note': '抵达第一站，客栈聚集地'}
                ],
                'emergency_exit': [{'name': '原路返回西当', 'desc': '约5小时下撤'}],
                'camping': '无（全程有客栈）',
                'supply': '雨崩村内有多家客栈和餐馆，物资靠牦牛运输，价格略高'
            },
            {
                'name': '雨崩内线（雨崩-神瀑-冰湖）',
                'type': '徒步支线',
                'start_point': '雨崩上村',
                'end_point': '雨崩上村',
                'distance_km': 20,
                'ascent_m': 700,
                'time_hours': '全天（往返）',
                'waypoints': [
                    {'name': '雨崩上村', 'elevation': '3150m', 'note': '出发点'},
                    {'name': '雨崩下村', 'elevation': '3000m', 'note': '经过下村，抄近道去神瀑'},
                    {'name': '神瀑', 'elevation': '3600m', 'note': '藏族圣地，穿越瀑布祈福'},
                    {'name': '冰湖', 'elevation': '4100m', 'note': '梅里雪山冰碛湖，沿途经森林草甸'},
                    {'name': '笑农大本营', 'elevation': '3800m', 'note': '台湾登山队旧址，中途休息点'}
                ],
                'emergency_exit': [
                    {'name': '神瀑原路返回', 'desc': '约2小时'},
                    {'name': '笑农大本营下撤', 'desc': '如遇身体不适应立即下撤至雨崩'}
                ],
                'camping': '无',
                'supply': '沿途无补给点，自带水和干粮'
            }
        ],
        'transport': {
            '到达': '丽江客运站→香格里拉→德钦→飞来寺→西当温泉（全程约8-10小时，需换乘）',
            '住宿': '雨崩村内客栈200-500元/晚，条件简陋但风景绝佳'
        },
        'tips': [
            '进山的越野车约80元/人，节省体力推荐乘车',
            '看日照金山推荐飞来寺观景点（进雨崩前住一晚）',
            '神瀑路线相对轻松，冰湖路线爬升较大量力而行',
            '雨季（7-8月）山路泥泞且有落石风险，谨慎前往',
            '尊重藏族文化，顺时针转经，不要踩门槛'
        ]
    },
    
    'huangshan': {
        'name': '黄山徒步线',
        'location': '安徽省黄山市',
        'elevation': '莲花峰 1864m',
        'featured': '奇松、怪石、云海、温泉四绝',
        'description': '黄山是中国最著名的山岳风景区之一，"五岳归来不看山，黄山归来不看岳"。相比景区索道的轻松游，徒步上下黄山能更深度体验奇松怪石的壮丽。适合周末短途出行。',
        'best_season': '全年皆宜，11-3月看雾凇，6-8月看云海概率高',
        'difficulty': '⭐⭐（初级）',
        'duration': '1-2天',
        'distance_km': 20,
        'total_ascent_m': 1200,
        'routes': [
            {
                'name': '云谷寺-白鹅岭线（后山上）',
                'type': '经典上山路',
                'start_point': '云谷寺',
                'end_point': '北海景区',
                'distance_km': 10,
                'ascent_m': 700,
                'time_hours': '4-5小时',
                'waypoints': [
                    {'name': '云谷寺', 'elevation': '650m', 'note': '后山入口，乘大巴至索道下站'},
                    {'name': '白鹅岭', 'elevation': '1000m', 'note': '索道上站，始信峰方向'},
                    {'name': '始信峰', 'elevation': '1580m', 'note': '黄山奇松集中地'},
                    {'name': '清凉台', 'elevation': '1660m', 'note': '观日出绝佳点'},
                    {'name': '北海宾馆', 'elevation': '1650m', 'note': '中途休息点'}
                ],
                'emergency_exit': [{'name': '云谷索道下行', 'desc': '随时可乘索道下山'}],
                'camping': '山上宾馆（价格较高）或指定露营区',
                'supply': '山顶有多个餐厅和便利店'
            },
            {
                'name': '慈光阁-玉屏楼线（前山上）',
                'type': '前山上山路',
                'start_point': '慈光阁',
                'end_point': '玉屏楼',
                'distance_km': 8,
                'ascent_m': 600,
                'time_hours': '3-4小时',
                'waypoints': [
                    {'name': '慈光阁', 'elevation': '350m', 'note': '前山入口'},
                    {'name': '朱砂峰', 'elevation': '800m', 'note': '沿途风景渐入佳境'},
                    {'name': '玉屏楼', 'elevation': '1650m', 'note': '迎客松所在地'}
                ],
                'emergency_exit': [{'name': '玉屏索道下行', 'desc': '约10分钟'}],
                'camping': '无',
                'supply': '玉屏楼有餐厅'
            }
        ],
        'transport': {
            '到达': '高铁至黄山北站，转乘大巴至黄山风景区南大门（约1小时）',
            '住宿': '山顶宾馆300-800元/晚（建议提前预订），山下汤口镇80-200元/晚'
        },
        'tips': [
            '推荐后山上（云谷寺）前山下（慈光阁），坡度较缓省力',
            '山顶住宿紧俏，旺季务必提前一周预订',
            '带一根登山杖减轻膝盖压力',
            '清晨看日出推荐清凉台或狮子峰',
            '门票190元（含景交车90元），有效期4天'
        ]
    },
    
    'meili_xue Shan': {
        'name': '梅里雪山·白马雪山穿越',
        'location': '云南省迪庆州德钦县-西藏自治区芒康市',
        'elevation': '白马雪山垭口 4400m',
        'featured': '藏区神山群、太子十三峰、盐井古盐田',
        'description': '梅里雪山以"日照金山"闻名，这里是藏区八大神山之首。徒步线路从飞来寺出发，穿越太子十三峰，经白马雪山垭口进入西藏，沿途有原始森林、高山草甸、冰川和藏族村落，是一条极具挑战性的经典线路。',
        'best_season': '4-5月、10-11月（避开雨季和冬季大雪）',
        'difficulty': '⭐⭐⭐⭐⭐（专家级）',
        'duration': '5-7天',
        'distance_km': 80,
        'total_ascent_m': 3200,
        'routes': [
            {
                'name': '飞来寺-盐井线（梅里穿越）',
                'type': '主力穿越线',
                'start_point': '德钦飞来寺',
                'end_point': '西藏盐井古盐田',
                'distance_km': 80,
                'ascent_m': 3200,
                'time_hours': '5-7天',
                'waypoints': [
                    {'name': '飞来寺', 'elevation': '3400m', 'note': '起点，观日照金山最佳位置'},
                    {'name': '雾浓顶', 'elevation': '3500m', 'note': '十三峰观景台'},
                    {'name': '雨崩村', 'elevation': '3150m', 'note': '途经藏寨休整'},
                    {'name': '沙力龙坝', 'elevation': '4000m', 'note': '高山草甸营地'},
                    {'name': '白马雪山垭口', 'elevation': '4400m', 'note': '最高点，穿越滇藏界线'},
                    {'name': '同乐村', 'elevation': '3200m', 'note': '下坡进入西藏芒康境内'},
                    {'name': '盐井古盐田', 'elevation': '2500m', 'note': '终点，千年手工制盐工艺'}
                ],
                'emergency_exit': [
                    {'name': '雨崩村下撤', 'desc': '原路返回飞来寺或从西当温泉出山'},
                    {'name': '沙力龙坝骑马', 'desc': '部分路段可雇马帮'}
                ],
                'camping': '沙力龙坝（高山草甸）、同乐村附近（林区）',
                'supply': '飞来寺和雨崩有补给点，途中需自带3-4天食物'
            }
        ],
        'transport': {
            '到达': '丽江→香格里拉→德钦→飞来寺（约8小时），盐井终点需从芒康乘车返回',
            '住宿': '飞来寺观景客栈200-500元/晚；途中仅能露营'
        },
        'tips': [
            '需要高海拔徒步经验，建议跟专业户外团队',
            '需办理边防证（德钦县公安局办理）',
            '垭口风雪大，备好防风防水装备',
            '尊重藏区信仰，不要逆时针转经',
            '卫星电话必备，部分路段无信号',
            '秋季（10-11月）能见度最佳，看日照金山概率最高'
        ]
    },
    
    'dalai_river_crossing': {
        'name': '大朝山·老君山九十九弯',
        'location': '云南省丽江市玉龙纳西族自治县',
        'elevation': '老君山 4247m',
        'featured': '丹霞地貌、高山湖泊、茶马古道',
        'description': '老君山黎明丹霞风景区拥有壮观的红色丹霞地貌和高山湖泊群。九十九弯是经典的徒步爬升路段，登顶后可俯瞰整个玉龙雪山山脉。适合有一定经验的徒步爱好者。',
        'best_season': '3-5月、9-11月',
        'difficulty': '⭐⭐⭐（中级）',
        'duration': '2-3天',
        'distance_km': 30,
        'total_ascent_m': 2000,
        'routes': [
            {
                'name': '九十九弯-黎明丹霞线',
                'type': '主力路线',
                'start_point': '剑川县沙溪镇',
                'end_point': '老君山黎明乡',
                'distance_km': 30,
                'ascent_m': 2000,
                'time_hours': '2天1夜',
                'waypoints': [
                    {'name': '沙溪镇', 'elevation': '2400m', 'note': '茶马古道古镇，徒步起点'},
                    {'name': '九十九弯', 'elevation': '3200m', 'note': '连续盘山弯道，爬升最陡路段'},
                    {'name': '高山草甸营地', 'elevation': '3800m', 'note': '中途扎营点'},
                    {'name': '老君山山顶', 'elevation': '4247m', 'note': '丹霞地貌奇观'},
                    {'name': '黎明乡', 'elevation': '2600m', 'note': '下山终点，丹霞峡谷'}
                ],
                'emergency_exit': [
                    {'name': '九十九弯下撤', 'desc': '沿原路返回沙溪镇'},
                    {'name': '黎明乡车辆接应', 'desc': '可提前安排车辆在黎明乡等候'}
                ],
                'camping': '高山草甸营地（需自带帐篷）',
                'supply': '沙溪镇有餐馆和超市，途中无补给'
            }
        ],
        'transport': {
            '到达': '丽江客运站→剑川→沙溪镇（约4小时）',
            '住宿': '沙溪镇民宿80-200元/晚；途中露营'
        },
        'tips': [
            '丹霞地貌区域植被稀疏，注意防晒',
            '九十九弯路段陡峭，建议使用登山杖',
            '雨季（7-8月）山路湿滑，谨慎前往',
            '可结合虎跳峡徒步一起安排'
        ]
    },
    
    'huabaoshan': {
        'name': '哈巴雪山',
        'location': '云南省丽江市香格里拉市宁蒗县',
        'elevation': '哈巴雪山主峰 5396m',
        'featured': '入门级5000米雪山、垂直植被带谱、冰川遗迹',
        'description': '哈巴雪山是中国最适合入门的高山之一，5396米的海拔对于有体能的普通人来说是可以挑战的高度。从丽江出发，沿途经历热带雨林到高山草甸到冰川带的完整垂直景观变化，是雪山入门首选。',
        'best_season': '10月-次年5月（旱季，天气稳定）',
        'difficulty': '⭐⭐⭐⭐（进阶）',
        'duration': '2天1夜',
        'distance_km': 16,
        'total_ascent_m': 2100,
        'routes': [
            {
                'name': '哈巴雪山攀登线（丽江-玉湖村-一营地-二营地-顶峰-返回）',
                'type': '攀登主力线',
                'start_point': '丽江古城→玉湖村',
                'end_point': '丽江古城',
                'distance_km': 16,
                'ascent_m': 2100,
                'time_hours': '2天1夜',
                'waypoints': [
                    {'name': '玉湖村', 'elevation': '3100m', 'note': '丽江出发，车程约2小时，徒步起点'},
                    {'name': '一营地', 'elevation': '3600m', 'note': '原始森林段，约3小时'},
                    {'name': '二营地', 'elevation': '4200m', 'note': '高山草甸段，约2小时'},
                    {'name': '4800m垭口', 'elevation': '4800m', 'note': '冲顶出发点是凌晨1-2点'},
                    {'name': '哈巴雪山顶峰', 'elevation': '5396m', 'note': '冲顶登顶约3-4小时'}
                ],
                'emergency_exit': [
                    {'name': '一营地下撤', 'desc': '冲顶过程中如有不适立即下撤至一营地'},
                    {'name': '4800m垭口下撤', 'desc': '最快下撤路线，约4小时回玉湖村'}
                ],
                'camping': '一营地（森林营地）、二营地（草甸营地）',
                'supply': '玉湖村有客栈，途中需自带全部食物和氧气'
            }
        ],
        'transport': {
            '到达': '丽江包车/拼车至玉湖村（约2小时，费用150-300元）',
            '住宿': '玉湖村纳西族客栈80-200元/晚；途中露营'
        },
        'tips': [
            '必须跟随有资质的户外公司报名攀登（政府规定）',
            '需要提前进行体能训练，建议有4000米以上山峰经验',
            '冲顶凌晨出发需头灯，山顶温度可达-20℃',
            '备好冰爪、冰镐（通常由公司提供）',
            '预防高反，携带氧气瓶',
            '攀登许可证约600元/人，含保险和向导'
        ]
    },
    
    'hutiao_gorge': {
        'name': '虎跳峡·上虎跳',
        'location': '云南省丽江市玉龙县虎跳峡镇',
        'elevation': '峡谷底部 1800m / 崖顶 2500m',
        'featured': '世界最深峡谷之一、金沙江怒涛、玉龙雪山与哈巴雪山对峙',
        'description': '虎跳峡是世界三大峡谷之一，江水从200多米深的峡谷中奔腾而过，气势磅礴。上虎跳路线短平快适合新手，中虎跳-白水台线是经典半日徒步，Full虎跳（2天）则穿越玉龙哈巴雪山分水岭。',
        'best_season': '全年可去，春秋最佳',
        'difficulty': '⭐⭐（初级）',
        'duration': '半天-2天',
        'distance_km': 18,
        'total_ascent_m': 600,
        'routes': [
            {
                'name': 'Full虎跳线（上虎跳-中虎跳-白水台-CD客栈-28道拐-下虎跳）',
                'type': '经典穿越线',
                'start_point': '上虎跳景区',
                'end_point': '下虎跳',
                'distance_km': 18,
                'ascent_m': 600,
                'time_hours': '2天1夜（或一天暴走）',
                'waypoints': [
                    {'name': '上虎跳', 'elevation': '1800m', 'note': '起点，可看虎跳石'},
                    {'name': '中虎跳', 'elevation': '1800m', 'note': '最壮观的江面收窄处'},
                    {'name': '白水台', 'elevation': '2200m', 'note': '中途休息点，有客栈'},
                    {'name': 'CD客栈', 'elevation': '2600m', 'note': '著名徒步者歇脚点，夜景极佳'},
                    {'name': '28道拐', 'elevation': '2800m', 'note': '连续之字形陡坡，最后挑战'},
                    {'name': '下虎跳', 'elevation': '1800m', 'note': '终点，可远眺虎跳石'}
                ],
                'emergency_exit': [
                    {'name': '白水台下撤', 'desc': '可乘车返回虎跳峡镇'},
                    {'name': 'CD客栈车辆接应', 'desc': '部分路段可开车绕行'}
                ],
                'camping': 'CD客栈附近可露营（收费）',
                'supply': '白水台和CD客栈有简餐和住宿'
            }
        ],
        'transport': {
            '到达': '丽江客运中心→虎跳峡镇（约2小时，30元）',
            '住宿': '虎跳峡镇客栈50-150元/晚；CD客栈200-400元/晚'
        },
        'tips': [
            '28道拐是精华也是难点，建议清晨出发避开午后高温',
            '峡谷内风大，注意固定帐篷',
            '雨季（7-8月）注意江水暴涨，不要在江边扎营',
            '可结合玉龙雪山行程安排'
        ]
    }
}

import os
data_path = r'D:\大学课程\大三小学期\实训\codex学习\项目测试\outdoor_guide\data\routes_db.json'
with open(data_path, 'w', encoding='utf-8') as f:
    json.dump(routes_data, f, ensure_ascii=False, indent=2)
print("路线数据库已生成:", len(routes_data), "条路线")
for k, v in routes_data.items():
    print(f"  - {v['name']}：{v['location']} | {v['difficulty']} | {v['duration']}")
