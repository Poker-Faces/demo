# coding:utf-8
city = {
    '北京': '101010100',
    '海淀': '101010200',
    '朝阳': '101010300',
    '顺义': '101010400',
    '怀柔': '101010500',
    '通州': '101010600',
    '昌平': '101010700',
    '延庆': '101010800',
    '丰台': '101010900',
    '石景山': '101011000',
    '大兴': '101011100',
    '房山': '101011200',
    '密云': '101011300',
    '门头沟': '101011400',
    '平谷': '101011500',
    '八达岭': '101011600',
    '佛爷顶': '101011700',
    '汤河口': '101011800',
    '密云上甸子': '101011900',
    '斋堂': '101012000',
    '霞云岭': '101012100',
    '上海': '101020100',
    '闵行': '101020200',
    '宝山': '101020300',
    '嘉定': '101020400',
    '南汇': '101020500',
    '金山': '101020600',
    '青浦': '101020800',
    '松江': '101020800',
    '奉贤': '101020900',
    '崇明': '101021000',
    '天津': '101030100',
    '武清': '101030200',
    '宝坻': '101030300',
    '东丽': '101030400',
    '西青': '101030500',
    '北辰': '101030600',
    '宁河': '101030700',
    '汉沽': '101030800',
    '静海': '101030900',
    '津南': '101031000',
    '塘沽': '101031100',
    '大港': '101031200',
    '蓟县': '101031300',
    '重庆': '101040100',
    '永川': '101040200',
    '合川': '101040300',
    '南川': '101040400',
    '江津': '101040500',
    '万盛': '101040600',
    '渝北': '101040700',
    '北碚': '101040800',
    '巴南': '101040900',
    '长寿': '101041000',
    '黔江': '101041100',
    '万州天城': '101041200',
    '万州龙宝': '101041300',
    '涪陵': '101041400',
    '开县': '101041500',
    '城口': '101041600',
    '云阳': '101041700',
    '巫溪': '101041800',
    '奉节': '101041900',
    '巫山': '101042000',
    '潼南': '101042100',
    '垫江': '101042200',
    '梁平': '101042300',
    '忠县': '101042400',
    '石柱': '101042500',
    '大足': '101042600',
    '荣昌': '101042700',
    '铜梁': '101042800',
    '璧山': '101042900',
    '丰都': '101043000',
    '武隆': '101043100',
    '彭水': '101043200',
    '綦江': '101043300',
    '酉阳': '101043400',
    '秀山': '101043600',
    '哈尔滨': '101050101',
    '双城': '101050102',
    '呼兰': '101050103',
    '阿城': '101050104',
    '宾县': '101050105',
    '依兰': '101050106',
    '巴彦': '101050107',
    '通河': '101050108',
    '方正': '101050109',
    '延寿': '101050110',
    '尚志': '101050111',
    '五常': '101050112',
    '木兰': '101050113',
    '齐齐哈尔': '101050201',
    '讷河': '101050202',
    '龙江': '101050203',
    '甘南': '101050204',
    '富裕': '101050205',
    '依安': '101050206',
    '拜泉': '101050207',
    '克山': '101050208',
    '克东': '101050209',
    '泰来': '101050210',
    '牡丹江': '101050301',
    '海林': '101050302',
    '穆棱': '101050303',
    '林口': '101050304',
    '绥芬河': '101050305',
    '宁安': '101050306',
    '东宁': '101050307',
    '长春': '101060101',
    '农安': '101060102',
    '德惠': '101060103',
    '九台': '101060104',
    '榆树': '101060105',
    '双阳': '101060106',
    '吉林': '101060201',
    '舒兰': '101060202',
    '永吉': '101060203',
    '蛟河': '101060204',
    '磐石': '101060205',
    '桦甸': '101060206',
    '延吉': '101060301',
    '敦化': '101060302',
    '安图': '101060303',
    '汪清': '101060304',
    '和龙': '101060305',
    '天池': '101060306',
    '龙井': '101060307',
    '珲春': '101060308',
    '图们': '101060309',
    '松江': '101060310',
    '沈阳': '101070101',
    '苏家屯': '101070102',
    '辽中': '101070103',
    '康平': '101070104',
    '法库': '101070105',
    '新民': '101070106',
    '新城子': '101070107',
    '大连': '101070201',
    '瓦房店': '101070202',
    '金州': '101070203',
    '普兰店': '101070204',
    '旅顺': '101070205',
    '长海': '101070206',
    '庄河': '101070207',
    '皮口': '101070208',
    '鞍山': '101070301',
    '台安': '101070302',
    '岫岩': '101070303',
    '海城': '101070304',
    '呼和浩特': '101080101',
    '土默特左旗': '101080102',
    '托克托': '101080103',
    '和林格尔': '101080104',
    '清水河': '101080105',
    '呼和浩特市郊区': '101080106',
    '武川': '101080107',
    '包头': '101080201',
    '白云鄂博': '101080202',
    '满都拉': '101080203',
    '土默特右旗': '101080204',
    '固阳': '101080205',
    '达尔罕茂明安联合旗': '101080206',
    '乌海': '101080301',
    '石家庄': '101090101',
    '井陉': '101090102',
    '正定': '101090103',
    '栾城': '101090104',
    '行唐': '101090105',
    '灵寿': '101090106',
    '高邑': '101090107',
    '深泽': '101090108',
    '赞皇': '101090109',
    '无极': '101090110',
    '平山': '101090111',
    '元氏': '101090112',
    '赵县': '101090113',
    '辛集': '101090114',
    '藁城': '101090115',
    '晋洲': '101090116',
    '新乐': '101090117',
    '保定': '101090201',
    '满城': '101090202',
    '阜平': '101090203',
    '徐水': '101090204',
    '唐县': '101090205',
    '高阳': '101090206',
    '容城': '101090207',
    '紫荆关': '101090208',
    '涞源': '101090209',
    '望都': '101090210',
    '安新': '101090211',
    '易县': '101090212',
    '涞水': '101090213',
    '曲阳': '101090214',
    '蠡县': '101090215',
    '顺平': '101090216',
    '雄县': '101090217',
    '涿州': '101090218',
    '定州': '101090219',
    '安国': '101090220',
    '高碑店': '101090221',
    '张家口': '101090301',
    '宣化': '101090302',
    '张北': '101090303',
    '康保': '101090304',
    '沽源': '101090305',
    '尚义': '101090306',
    '蔚县': '101090307',
    '阳原': '101090308',
    '怀安': '101090309',
    '万全': '101090310',
    '怀来': '101090311',
    '涿鹿': '101090312',
    '赤城': '101090313',
    '崇礼': '101090314',
    '太原': '101100101',
    '清徐': '101100102',
    '阳曲': '101100103',
    '娄烦': '101100104',
    '太原古交区': '101100105',
    '太原北郊': '101100106',
    '太原南郊': '101100107',
    '大同': '101100201',
    '阳高': '101100202',
    '大同县': '101100203',
    '天镇': '101100204',
    '广灵': '101100205',
    '灵邱': '101100206',
    '浑源': '101100207',
    '左云': '101100208',
    '阳泉': '101100301',
    '盂县': '101100302',
    '平定': '101100303',
    '西安': '101110101',
    '长安': '101110102',
    '临潼': '101110103',
    '蓝田': '101110104',
    '周至': '101110105',
    '户县': '101110106',
    '高陵': '101110107',
    '咸阳': '101110200',
    '三原': '101110201',
    '礼泉': '101110202',
    '永寿': '101110203',
    '淳化': '101110204',
    '泾阳': '101110205',
    '武功': '101110206',
    '乾县': '101110207',
    '彬县': '101110208',
    '长武': '101110209',
    '旬邑': '101110210',
    '兴平': '101110211',
    '延安': '101110300',
    '延川': '101110302',
    '子长': '101110303',
    '延长': '101110301',
    '宜川': '101110304',
    '富县': '101110305',
    '志丹': '101110306',
    '安塞': '101110307',
    '甘泉': '101110308',
    '洛川': '101110309',
    '黄陵': '101110310',
    '黄龙': '101110311',
    '吴起': '101110312',
    '济南': '101120101',
    '长清': '101120102',
    '商河': '101120103',
    '章丘': '101120104',
    '平阴': '101120105',
    '济阳': '101120106',
    '青岛': '101120201',
    '崂山': '101120202',
    '即墨': '101120204',
    '胶州': '101120204',
    '胶南': '101120205',
    '莱西': '101120206',
    '平度': '101120207',
    '淄博': '101120301',
    '淄川': '101120302',
    '博山': '101120303',
    '高青': '101120304',
    '周村': '101120305',
    '沂源': '101120306',
    '桓台': '101120307',
    '临淄': '101120308',
    '乌鲁木齐': '101130101',
    '蔡家湖': '101130102',
    '小渠子': '101130103',
    '巴仑台': '101130104',
    '达坂城': '101130105',
    '十三间房气象站': '101130106',
    '乌鲁木齐牧试站': '101130107',
    '天池': '101130108',
    '克拉玛依': '101130201',
    '石河子': '101130301',
    '炮台': '101130302',
    '莫索湾': '101130303',
    '乌兰乌苏': '101130304',
    '拉萨': '101140101',
    '当雄': '101140102',
    '尼木': '101140103',
    '墨竹贡卡': '101140104',
    '日喀则': '101140201',
    '拉孜': '101140202',
    '南木林': '101140203',
    '聂拉木': '101140204',
    '定日': '101140205',
    '江孜': '101140206',
    '帕里': '101140207',
    '山南': '101140301',
    '贡嘎': '101140302',
    '琼结': '101140303',
    '加查': '101140304',
    '浪卡子': '101140305',
    '错那': '101140306',
    '隆子': '101140307',
    '西宁': '101150101',
    '大通': '101150102',
    '湟源': '101150103',
    '湟中': '101150104',
    '海东': '101150201',
    '乐都': '101150202',
    '民和': '101150203',
    '互助': '101150204',
    '化隆': '101150205',
    '循化': '101150206',
    '冷湖': '101150207',
    '黄南': '101150301',
    '尖扎': '101150302',
    '泽库': '101150303',
    '兰州': '101160101',
    '皋兰': '101160102',
    '永登': '101160103',
    '榆中': '101160104',
    '定西': '101160201',
    '通渭': '101160202',
    '陇西': '101160203',
    '渭源': '101160204',
    '临洮': '101160205',
    '漳县': '101160206',
    '岷县': '101160207',
    '平凉': '101160301',
    '泾川': '101160302',
    '灵台': '101160303',
    '崇信': '101160304',
    '华亭': '101160305',
    '庄浪': '101160306',
    '静宁': '101160307',
    '银川': '101170101',
    '永宁': '101170102',
    '灵武': '101170103',
    '贺兰': '101170104',
    '石嘴山': '101170201',
    '惠农': '101170202',
    '平罗': '101170203',
    '陶乐': '101170204',
    '石炭井': '101170205',
    '吴忠': '101170301',
    '同心': '101170302',
    '盐池': '101170303',
    '韦州': '101170304',
    '麻黄山': '101170305',
    '青铜峡': '101170306',
    '郑州': '101180101',
    '巩义': '101180102',
    '荥阳': '101180103',
    '登封': '101180104',
    '新密': '101180105',
    '新郑': '101180106',
    '中牟': '101180107',
    '安阳': '101180201',
    '汤阴': '101180202',
    '滑县': '101180203',
    '内黄': '101180204',
    '林州': '101180205',
    '新乡': '101180301',
    '获嘉': '101180302',
    '原阳': '101180303',
    '辉县': '101180304',
    '卫辉': '101180305',
    '延津': '101180306',
    '封丘': '101180307',
    '长垣': '101180308',
    '南京': '101190101',
    '溧水': '101190102',
    '高淳': '101190103',
    '江宁': '101190104',
    '六合': '101190105',
    '江浦': '101190106',
    '无锡': '101190201',
    '江阴': '101190202',
    '宜兴': '101190203',
    '镇江': '101190301',
    '丹阳': '101190302',
    '扬中': '101190303',
    '句容': '101190304',
    '丹徒': '101190305',
    '武汉': '101200101',
    '蔡甸': '101200102',
    '黄陂': '101200103',
    '新洲': '101200104',
    '江夏': '101200105',
    '襄樊': '101200201',
    '襄阳': '101200202',
    '保康': '101200203',
    '南漳': '101200204',
    '宜城': '101200205',
    '老河口': '101200206',
    '谷城': '101200207',
    '枣阳': '101200208',
    '鄂州': '101200301',
    '杭州': '101210101',
    '萧山': '101210102',
    '桐庐': '101210103',
    '淳安': '101210104',
    '建德': '101210105',
    '昌化': '101210106',
    '临安': '101210107',
    '富阳': '101210108',
    '湖州': '101210201',
    '长兴': '101210202',
    '安吉': '101210203',
    '德清': '101210204',
    '嘉兴': '101210301',
    '嘉善': '101210302',
    '海宁': '101210303',
    '桐乡': '101210304',
    '平湖': '101210305',
    '海盐': '101210306',
    '合肥': '101220101',
    '长丰': '101220102',
    '肥东': '101220103',
    '肥西': '101220104',
    '蚌埠': '101220201',
    '怀远': '101220202',
    '固镇': '101220203',
    '五河': '101220204',
    '芜湖': '101220301',
    '繁昌': '101220302',
    '芜湖县': '101220303',
    '南陵': '101220304',
    '福州': '101230101',
    '闽清': '101230102',
    '闽侯': '101230103',
    '罗源': '101230104',
    '连江': '101230105',
    '马祖': '101230106',
    '永泰': '101230107',
    '平潭': '101230108',
    '福州郊区': '101230109',
    '长乐': '101230110',
    '福清': '101230111',
    '平潭海峡大桥': '101230112',
    '厦门': '101230201',
    '同安': '101230202',
    '宁德': '101230301',
    '古田': '101230302',
    '霞浦': '101230303',
    '寿宁': '101230304',
    '周宁': '101230305',
    '福安': '101230306',
    '柘荣': '101230307',
    '福鼎': '101230308',
    '屏南': '101230309',
    '南昌': '101240101',
    '新建': '101240102',
    '南昌县': '101240103',
    '安义': '101240104',
    '进贤': '101240105',
    '九江': '101240201',
    '瑞昌': '101240202',
    '庐山': '101240203',
    '武宁': '101240204',
    '德安': '101240205',
    '永修': '101240206',
    '湖口': '101240207',
    '彭泽': '101240208',
    '星子': '101240209',
    '都昌': '101240210',
    '棠荫': '101240211',
    '修水': '101240212',
    '上饶': '101240301',
    '波阳': '101240302',
    '婺源': '101240303',
    '康山': '101240304',
    '余干': '101240305',
    '万年': '101240306',
    '德兴': '101240307',
    '上饶县': '101240308',
    '弋阳': '101240309',
    '横峰': '101240310',
    '铅山': '101240311',
    '玉山': '101240312',
    '广丰': '101240313',
    '长沙': '101250101',
    '宁乡': '101250102',
    '浏阳': '101250103',
    '马坡岭': '101250104',
    '湘潭': '101250201',
    '韶山': '101250202',
    '湘乡': '101250203',
    '株洲': '101250301',
    '攸县': '101250302',
    '醴陵': '101250303',
    '株洲县': '101250304',
    '茶陵': '101250305',
    '炎陵': '101250306',
    '贵阳': '101260101',
    '白云': '101260102',
    '花溪': '101260103',
    '乌当': '101260104',
    '息烽': '101260105',
    '开阳': '101260106',
    '修文': '101260107',
    '清镇': '101260108',
    '遵义': '101260201',
    '遵义县': '101260202',
    '仁怀': '101260203',
    '绥阳': '101260204',
    '湄潭': '101260205',
    '凤冈': '101260206',
    '桐梓': '101260207',
    '赤水': '101260208',
    '习水': '101260209',
    '道真': '101260210',
    '正安': '101260211',
    '务川': '101260212',
    '余庆': '101260213',
    '安顺': '101260301',
    '普定': '101260302',
    '镇宁': '101260303',
    '平坝': '101260304',
    '紫云': '101260305',
    '关岭': '101260306',
    '成都': '101270101',
    '龙泉驿': '101270102',
    '新都': '101270103',
    '温江': '101270104',
    '金堂': '101270105',
    '双流': '101270106',
    '郫县': '101270107',
    '大邑': '101270108',
    '蒲江': '101270109',
    '新津': '101270110',
    '都江堰': '101270111',
    '彭州': '101270112',
    '邛崃': '101270113',
    '崇州': '101270114',
    '攀枝花': '101270201',
    '仁和': '101270202',
    '米易': '101270203',
    '盐边': '101270204',
    '自贡': '101270301',
    '富顺': '101270302',
    '荣县': '101270303',
    '广州': '101280101',
    '番禺': '101280102',
    '从化': '101280103',
    '增城': '101280104',
    '花都': '101280105',
    '韶关': '101280201',
    '乳源': '101280202',
    '始兴': '101280203',
    '翁源': '101280204',
    '乐昌': '101280205',
    '仁化': '101280206',
    '南雄': '101280207',
    '新丰': '101280208',
    '惠州': '101280301',
    '博罗': '101280302',
    '惠东': '101280304',
    '龙门': '101280305',
    '昆明': '101290101',
    '昆明农试站': '101290102',
    '东川': '101290103',
    '寻甸': '101290104',
    '晋宁': '101290105',
    '宜良': '101290106',
    '石林': '101290107',
    '呈贡': '101290108',
    '富民': '101290109',
    '嵩明': '101290110',
    '禄劝': '101290111',
    '安宁': '101290112',
    '太华山': '101290113',
    '河口县': '101290114',
    '大理': '101290201',
    '云龙': '101290202',
    '漾鼻': '101290203',
    '永平': '101290204',
    '宾川': '101290205',
    '弥渡': '101290206',
    '祥云': '101290207',
    '巍山': '101290208',
    '剑川': '101290209',
    '洱源': '101290210',
    '鹤庆': '101290211',
    '南涧': '101290212',
    '红河': '101290301',
    '石屏': '101290302',
    '建水': '101290303',
    '弥勒': '101290304',
    '元阳': '101290305',
    '绿春': '101290306',
    '开远': '101290307',
    '个旧': '101290308',
    '蒙自': '101290309',
    '屏边': '101290310',
    '泸西': '101290311',
    '金平': '101290312',
    '南宁': '101300101',
    '邕宁': '101300103',
    '横县': '101300104',
    '隆安': '101300105',
    '马山': '101300106',
    '上林': '101300107',
    '武鸣': '101300108',
    '宾阳': '101300109',
    '崇左': '101300201',
    '天等': '101300202',
    '龙州': '101300203',
    '凭祥': '101300204',
    '大新': '101300205',
    '扶绥': '101300206',
    '宁明': '101300207',
    '柳州': '101300301',
    '柳城': '101300302',
    '鹿寨': '101300304',
    '柳江': '101300304',
    '融安': '101300305',
    '融水': '101300306',
    '三江': '101300307',
    '海口': '101310101',
    '琼山': '101310102',
    '三亚': '101310201',
    '香港': '101320101',
    '澳门': '101330101',
    '台北县': '101340101',
    '高雄': '101340201',
    '台中': '101340401',
}