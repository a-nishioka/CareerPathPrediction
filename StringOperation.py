import string
import unicodedata
import re


class StringOperation:
    prefecture_list = []
    region_list = []
    city_list = []

    def __init__(self):
        self.prefecture_list = ['愛知', '青森', '秋田', '秋田', '石川', '茨城', '岩手', '愛媛', '大分', '大阪', '岡山', '沖縄', '香川', '鹿児島', '神奈川', '岐阜', '京都', '熊本', '群馬', '高知', '埼玉', '佐賀',
                                '滋賀', '静岡', '島根', '千葉', '東京', '徳島', '栃木', '鳥取', '富山', '長崎', '長野', '奈良', '新潟', '兵庫', '広島', '福井', '福岡', '福島', '北海道', '三重', '宮城', '宮崎', '山形', '山口', '山梨', '和歌山']
        self.region_list = ['北海道', '東北', '関東', '中部', '近畿', '中国', '四国', '九州', '首都圏', '北関東', '南関東',
                            '甲信越', '北陸', '東海', '関西', '北信越', '中京', '瀬戸内', '山陰', '山陽', '北四国', '南四国', '北部九州', '南九州']
        self.city_list = ['札幌', '函館', '小樽', '旭川', '室蘭', '釧路', '帯広',
                          '北見', '夕張', '岩見沢', '網走', '留萌', '苫小牧', '稚内', '美唄',
                          '芦別', '江別', '赤平', '紋別', '士別', '名寄', '三笠', '根室', '千歳',
                          '滝川', '砂川', '歌志内', '深川', '富良野', '登別', '恵庭', '伊達',
                          '北広島', '石狩', '北斗', '当別', '新篠津', '松前', '福島', '知内',
                          '木古内', '七飯', '鹿部', '森', '八雲', '長万部', '江差', '上ノ国',
                          '厚沢部', '乙部', '奥尻', '今金', 'せたな', '島牧', '寿都', '黒松内',
                          '蘭越', 'ニセコ', '真狩', '留寿都', '喜茂別', '京極', '倶知安', '共和',
                          '岩内', '泊', '神恵内', '積丹', '古平', '仁木', '余', '赤井川', '南幌',
                          '奈井江', '上砂川', '由仁', '長沼', '栗山', '月形', '浦臼', '新十津川',
                          '妹背牛', '秩父別', '雨竜', '北竜', '沼田', '鷹栖', '東神楽', '当麻',
                          '比布', '愛別', '上川', '東川', '美瑛', '上富良野', '中富良野',
                          '南富良野', '占冠', '和寒', '剣淵', '下川', '美深', '音威子府', '中川',
                          '幌加内', '増毛', '小平', '苫前', '羽幌', '初山別', '遠別', '天塩',
                          '猿払', '浜頓別', '中頓別', '枝幸', '豊富', '礼文', '利尻', '利尻富士',
                          '幌延', '美幌', '津別', '斜里', '清里', '小清水', '訓子府', '置戸',
                          '佐呂間', '遠軽', '湧別', '滝上', '興部', '西興部', '雄武', '大空',
                          '豊浦', '壮瞥', '白老', '厚真', '洞爺湖', '安平', 'むかわ', '日高',
                          '平取', '新冠', '浦河', '様似', 'えりも', '新ひだか', '音更', '士幌',
                          '上士幌', '鹿追', '新得', '清水', '芽室', '中札内', '更別', '大樹',
                          '広尾', '幕別', '池田', '豊頃', '本別', '足寄', '陸別', '浦幌', '釧路',
                          '厚岸', '浜中', '標茶', '弟子屈', '鶴居', '白糠', '別海', '中標津',
                          '標津', '羅臼', '色丹', '泊', '留夜別', '留別', '紗那', '蘂取', '青森',
                          '弘前', '八戸', '黒石', '五所川原', '十和田', '三沢', 'むつ', 'つがる',
                          '平川', '平内', '今別', '蓬田', '外ヶ浜', '鰺ヶ沢', '深浦', '西目屋',
                          '藤崎', '大鰐', '田舎館', '板柳', '鶴田', '中泊', '野辺地', '七戸',
                          '六戸', '横浜', '東北', '六ヶ所', 'おいらせ', '大間', '東通', '風間浦',
                          '佐井', '三戸', '五戸', '田子', '南部', '階上', '新郷', '盛岡', '宮古',
                          '大船渡', '花巻', '北上', '久慈', '遠野', '一関', '陸前高田', '釜石',
                          '二戸', '八幡平', '奥州', '滝沢', '雫石', '葛巻', '岩手', '紫波', '矢巾',
                          '西和賀', '金ケ崎', '平泉', '住田', '大槌', '山田', '岩泉', '田野畑',
                          '普代', '軽米', '野田', '九戸', '洋野', '一戸', '仙台', '石巻', '塩竈',
                          '気仙沼', '白石', '名取', '角田', '多賀城', '岩沼', '登米', '栗原',
                          '東松島', '大崎', '富谷', '蔵王', '七ヶ宿', '大河原', '村田', '柴田',
                          '川崎', '丸森', '亘理', '山元', '松島', '七ヶ浜', '利府', '大和', '大郷',
                          '大衡', '色麻', '加美', '涌谷', '美里', '女川', '南三陸', '秋田', '能代',
                          '横手', '大館', '男鹿', '湯沢', '鹿角', '由利本荘', '潟上', '大仙',
                          '北秋田', 'にかほ', '仙北', '小坂', '上小阿仁', '藤里', '三種', '八峰',
                          '五城目', '八郎潟', '井川', '大潟', '美郷', '羽後', '東成瀬', '山形',
                          '米沢', '鶴岡', '酒田', '新庄', '寒河江', '上山', '村山', '長井', '天童',
                          '東根', '尾花沢', '南陽', '山辺', '中山', '河北', '西川', '朝日', '大江',
                          '大石田', '金山', '最上', '舟形', '真室川', '大蔵', '鮭川', '戸沢',
                          '高畠', '川西', '小国', '白鷹', '飯豊', '三川', '庄内', '遊佐', '福島',
                          '会津若松', '郡山', 'いわき', '白河', '須賀川', '喜多方', '相馬',
                          '二本松', '田村', '南相馬', '伊達', '本宮', '桑折', '国見', '川俣',
                          '大玉', '鏡石', '天栄', '下郷', '檜枝岐', '只見', '南会津', '北塩原',
                          '西会津', '磐梯', '猪苗代', '会津坂下', '湯川', '柳津', '三島', '金山',
                          '昭和', '会津美里', '西郷', '泉崎', '中島', '矢吹', '棚倉', '矢祭', '塙',
                          '鮫川', '石川', '玉川', '平田', '浅川', '古殿', '三春', '小野', '広野',
                          '楢葉', '富岡', '川内', '大熊', '双葉', '浪江', '葛尾', '新地', '飯舘',
                          '水戸', '日立', '土浦', '古河', '石岡', '結城', '龍ケ崎', '下妻', '常総',
                          '常陸太田', '高萩', '北茨城', '笠間', '取手', '牛久', 'つくば',
                          'ひたちなか', '鹿嶋', '潮来', '守谷', '常陸大宮', '那珂', '筑西',
                          '坂東', '稲敷', 'かすみがうら', '桜川', '神栖', '行方', '鉾田',
                          'つくばみらい', '小美玉', '茨城', '大洗', '城里', '東海', '大子',
                          '美浦', '阿見', '河内', '八千代', '五霞', '境', '利根', '宇都宮',
                          '足利', '栃木', '佐野', '鹿沼', '日光', '小山', '真岡', '大田原', '矢板',
                          '那須塩原', 'さくら', '那須烏山', '下野', '上三川', '益子', '茂木',
                          '貝', '芳賀', '壬生', '野木', '塩谷', '高根沢', '那須', '那珂川', '前橋',
                          '高崎', '桐生', '伊勢崎', '太田', '沼田', '館林', '渋川', '藤岡', '富岡',
                          '安中', 'みどり', '榛東', '吉岡', '上野', '神流', '下仁田', '南牧',
                          '甘楽', '中之条', '長野原', '嬬恋', '草津', '高山', '東吾妻', '片品',
                          '川場', '昭和', 'みなかみ', '玉村', '板倉', '明和', '千代田', '大泉',
                          '邑楽', 'さいたま', '川越', '熊谷', '川口', '行田', '秩父', '所沢',
                          '飯能', '加須', '本庄', '東松山', '春日部', '狭山', '羽生', '鴻巣',
                          '深谷', '上尾', '草加', '越谷', '蕨', '戸田', '入間', '朝霞', '志木',
                          '和光', '新座', '桶川', '久喜', '北本', '八潮', '富士見', '三郷', '蓮田',
                          '坂戸', '幸手', '鶴ヶ島', '日高', '吉川', 'ふじみ野', '白岡', '伊奈',
                          '三芳', '毛呂山', '越生', '滑川', '嵐山', '小川', '川島', '吉見', '鳩山',
                          'ときがわ', '横瀬', '皆野', '長瀞', '小鹿野', '東秩父', '美里', '神川',
                          '上里', '寄居', '宮代', '杉戸', '松伏', '千葉', '銚子', '市川', '船橋',
                          '館山', '木更津', '松戸', '野田', '茂原', '成田', '佐倉', '東金', '旭',
                          '習志野', '柏', '勝浦', '市原', '流山', '八千代', '我孫子', '鴨川',
                          '鎌ケ谷', '君津', '富津', '浦安', '四街道', '袖ケ浦', '八街', '印西',
                          '白井', '富里', '南房総', '匝瑳', '香取', '山武', 'いすみ', '大網白里',
                          '酒々井', '栄', '神崎', '多古', '東庄', '九十九里', '芝山', '横芝光',
                          '一宮', '睦沢', '長生', '白子', '長柄', '長南', '大多喜', '御宿', '鋸南',
                          '千代田', '中央', '港', '新宿', '文京', '台東', '墨田', '江東', '品川',
                          '目黒', '大田', '世田谷', '渋谷', '中野', '杉並', '豊島', '北', '荒川',
                          '板橋', '練馬', '足立', '葛飾', '江戸川', '八王子', '立川', '武蔵野',
                          '三鷹', '青梅', '府中', '昭島', '調布', '町田', '小金井', '小平', '日野',
                          '東村山', '国分寺', '国立', '福生', '狛江', '東大和', '清瀬', '東久留米',
                          '武蔵村山', '多摩', '稲城', '羽村', 'あきる野', '西東京', '瑞穂',
                          '日の出', '檜原', '奥多摩', '大島', '利島', '新島', '神津島', '三宅',
                          '御蔵島', '八丈', '青ヶ島', '小笠原', '横浜', '川崎', '相模原',
                          '横須賀', '平塚', '鎌倉', '藤沢', '小田原', '茅ヶ崎', '逗子', '三浦',
                          '秦野', '厚木', '大和', '伊勢原', '海老名', '座間', '南足柄', '綾瀬',
                          '葉山', '寒川', '大磯', '二宮', '中井', '大井', '松田', '山北', '開成',
                          '箱根', '真鶴', '湯河原', '愛川', '清川', '新潟', '長岡', '三条', '柏崎',
                          '新発田', '小千谷', '加茂', '十日', '見附', '村上', '燕', '糸魚川',
                          '妙高', '五泉', '上越', '阿賀野', '佐渡', '魚沼', '南魚沼', '胎内',
                          '聖籠', '弥彦', '田上', '阿賀', '出雲崎', '湯沢', '津南', '刈羽', '関川',
                          '粟島浦', '富山', '高岡', '魚津', '氷見', '滑川', '黒部', '砺波',
                          '小矢部', '南砺', '射水', '舟橋', '上市', '立山', '入善', '朝日',
                          '金沢', '七尾', '小松', '輪島', '珠洲', '加賀', '羽咋', 'かほく', '白山',
                          '能美', '野々市', '川北', '津幡', '内灘', '志賀', '宝達志水', '中能登',
                          '穴水', '能登', '福井', '敦賀', '小浜', '大野', '勝山', '鯖江', 'あわら',
                          '越前', '坂井', '永平寺', '池田', '南越前', '越前', '美浜', '高浜',
                          'おおい', '若狭', '甲府', '富士吉田', '都留', '山梨', '大月', '韮崎',
                          '南アルプス', '北杜', '甲斐', '笛吹', '上野原', '甲州', '中央',
                          '市川三郷', '早川', '身延', '南部', '富士川', '昭和', '道志', '西桂',
                          '忍野', '山中湖', '鳴沢', '富士河口湖', '小菅', '丹波山', '長野', '松本',
                          '上田', '岡谷', '飯田', '諏訪', '須坂', '小諸', '伊那', '駒ヶ根', '中野',
                          '大', '飯山', '茅野', '塩尻', '佐久', '千曲', '東御', '安曇野', '小海',
                          '川上', '南牧', '南相木', '北相木', '佐久穂', '軽井沢', '御代田', '立科',
                          '青木', '長和', '下諏訪', '富士見', '原', '辰野', '箕輪', '飯島',
                          '南箕輪', '中川', '宮田', '松川', '高森', '阿南', '阿智', '平谷',
                          '根羽', '下條', '売木', '天龍', '泰阜', '喬木', '豊丘', '大鹿', '上松',
                          '南木曽', '木祖', '王滝', '大桑', '木曽', '麻績', '生坂', '山形', '朝日',
                          '筑北', '池田', '松川', '白馬', '小谷', '坂城', '小布施', '高山',
                          '山ノ内', '木島平', '野沢温泉', '信濃', '小川', '飯綱', '栄', '岐阜',
                          '大垣', '高山', '多治見', '関', '中津川', '美濃', '瑞浪', '羽島', '恵那',
                          '美濃加茂', '土岐', '各務原', '可児', '山県', '瑞穂', '飛騨', '本巣',
                          '郡上', '下呂', '海津', '岐南', '笠松', '養老', '垂井', '関ケ原', '神戸',
                          '輪之内', '安八', '揖斐川', '大野', '池田', '北方', '坂祝', '富加',
                          '川辺', '七宗', '八百津', '白川', '東白川', '御嵩', '白川', '静岡',
                          '浜松', '沼津', '熱海', '三島', '富士宮', '伊東', '島田', '富士', '磐田',
                          '焼津', '掛川', '藤枝', '御殿場', '袋井', '下田', '裾野', '湖西', '伊豆',
                          '御前崎', '菊川', '伊豆の国', '牧之原', '東伊豆', '河津', '南伊豆',
                          '松崎', '西伊豆', '函南', '清水', '長泉', '小山', '吉田', '川根本',
                          '森', '名古屋', '豊橋', '岡崎', '一宮', '瀬戸', '半田', '春日井', '豊川',
                          '津島', '碧南', '刈谷', '豊田', '安城', '西尾', '蒲郡', '犬山', '常滑',
                          '江南', '小牧', '稲沢', '新城', '東海', '大府', '知多', '知立', '尾張旭',
                          '高浜', '岩倉', '豊明', '日進', '田原', '愛西', '清須', '北名古屋',
                          '弥富', 'みよし', 'あま', '長久手', '東郷', '豊山', '大口', '扶桑',
                          '大治', '蟹江', '飛島', '阿久比', '東浦', '南知多', '美浜', '武豊',
                          '幸田', '設楽', '東栄', '豊根', '津', '四日市', '伊勢', '松阪', '桑名',
                          '鈴鹿', '名張', '尾鷲', '亀山', '鳥羽', '熊野', 'いなべ', '志摩', '伊賀',
                          '木曽岬', '東員', '菰野', '朝日', '川越', '多気', '明和', '大台', '玉城',
                          '度会', '大紀', '南伊勢', '紀北', '御浜', '紀宝', '大津', '彦根', '長浜',
                          '近江八幡', '草津', '守山', '栗東', '甲賀', '野洲', '湖南', '高島',
                          '東近江', '米原', '日野', '竜王', '愛荘', '豊郷', '甲良', '多賀', '京都',
                          '福知山', '舞鶴', '綾部', '宇治', '宮津', '亀岡', '城陽', '向日',
                          '長岡京', '八幡', '京田辺', '京丹後', '南丹', '木津川', '大山崎',
                          '久御山', '井手', '宇治田原', '笠置', '和束', '精華', '南山城',
                          '京丹波', '伊根', '与謝野', '大阪', '堺', '岸和田', '豊中', '池田',
                          '吹田', '泉大津', '高槻', '貝塚', '守口', '枚方', '茨木', '八尾',
                          '泉佐野', '富田林', '寝屋川', '河内長野', '松原', '大東', '和泉',
                          '箕面', '柏原', '羽曳野', '門真', '摂津', '高石', '藤井寺', '東大阪',
                          '泉南', '四條畷', '交野', '大阪狭山', '阪南', '島本', '豊能', '能勢',
                          '忠岡', '熊取', '田尻', '岬', '太子', '河南', '千早赤阪', '神戸', '姫路',
                          '尼崎', '明石', '西宮', '洲本', '芦屋', '伊丹', '相生', '豊岡', '加古川',
                          '赤穂', '西脇', '宝塚', '三木', '高砂', '川西', '小野', '三田', '加西',
                          '丹波篠山', '養父', '丹波', '南あわじ', '朝来', '淡路', '宍粟', '加東',
                          'たつの', '猪名川', '多可', '稲美', '播磨', '川', '福崎', '神河', '太子',
                          '上郡', '佐用', '香美', '新温泉', '奈良', '大和高田', '大和郡山', '天理',
                          '橿原', '桜井', '五條', '御所', '生駒', '香芝', '葛城', '宇陀', '山添',
                          '平群', '三郷', '斑鳩', '安堵', '川西', '三宅', '田原本', '曽爾', '御杖',
                          '高取', '明日香', '上牧', '王寺', '広陵', '河合', '吉野', '大淀', '下市',
                          '黒滝', '天川', '野迫川', '十津川', '下北山', '上北山', '川上', '東吉野',
                          '和歌山', '海南', '橋本', '有田', '御坊', '田辺', '新宮', '紀の川', '岩出',
                          '紀美野', 'かつらぎ', '九度山', '高野', '湯浅', '広川', '有田川', '美浜',
                          '日高', '由良', '印南', 'みなべ', '日高川', '白浜', '上富田', 'すさみ',
                          '那智勝浦', '太地', '古座川', '北山', '串本', '鳥取', '米子', '倉吉',
                          '境港', '岩美', '若桜', '智頭', '八頭', '三朝', '湯梨浜', '琴浦', '北栄',
                          '日吉津', '大山', '南部', '伯耆', '日南', '日野', '江府', '松江', '浜田',
                          '出雲', '益田', '大田', '安来', '江津', '雲南', '奥出雲', '飯南', '川本',
                          '美郷', '邑南', '津和野', '吉賀', '海士', '西ノ島', '知夫', '隠岐の島',
                          '岡山', '倉敷', '津山', '玉野', '笠岡', '井原', '総社', '高梁', '新見',
                          '備前', '瀬戸内', '赤磐', '真庭', '美作', '浅口', '和気', '早島', '里庄',
                          '矢掛', '新庄', '鏡野', '勝央', '奈義', '西粟倉', '久米南', '美咲',
                          '吉備中央', '広島', '呉', '竹原', '三原', '尾道', '福山', '府中', '三次',
                          '庄原', '大竹', '東広島', '廿日市', '安芸高田', '江田島', '府中', '海田',
                          '熊野', '坂', '安芸太田', '北広島', '大崎上島', '世羅', '神石高原',
                          '下関', '宇部', '山口', '萩', '防府', '下松', '岩国', '光', '長門', '柳井',
                          '美祢', '周南', '山陽小野田', '周防大島', '和木', '上関', '田布施',
                          '平生', '阿武', '徳島', '鳴門', '小松島', '阿南', '吉野川', '阿波',
                          '美馬', '三好', '勝浦', '上勝', '佐那河内', '石井', '神山', '那賀',
                          '牟岐', '美波', '海陽', '松茂', '北島', '藍住', '板野', '上板', 'つるぎ',
                          '東みよし', '高松', '丸亀', '坂出', '善通寺', '観音寺', 'さぬき',
                          '東かがわ', '三豊', '土庄', '小豆島', '三木', '直島', '宇多津', '綾川',
                          '琴平', '多度津', 'まんのう', '松山', '今治', '宇和島', '八幡浜',
                          '新居浜', '西条', '大洲', '伊予', '四国中央', '西予', '東温', '上島',
                          '久万高原', '松前', '砥部', '内子', '伊方', '松野', '鬼北', '愛南',
                          '高知', '室戸', '安芸', '南国', '土佐', '須崎', '宿毛', '土佐清水',
                          '四万十', '香南', '香美', '東洋', '奈半利', '田野', '安田', '北川',
                          '馬路', '芸西', '本山', '大豊', '土佐', '大川', 'いの', '仁淀川',
                          '中土佐', '佐川', '越知', '梼原', '日高', '津野', '四万十', '大月',
                          '三原', '黒潮', '北九州', '福岡', '大牟田', '久留米', '直方', '飯塚',
                          '田川', '柳川', '八女', '筑後', '大川', '行橋', '豊前', '中間', '小郡',
                          '筑紫野', '春日', '大野城', '宗像', '太宰府', '古賀', '福津', 'うきは',
                          '宮若', '嘉麻', '朝倉', 'みやま', '糸島', '那珂川', '宇美', '篠栗',
                          '志免', '須恵', '新宮', '久山', '粕屋', '芦屋', '水巻', '岡垣', '遠賀',
                          '小竹', '鞍手', '桂川', '筑前', '東峰', '大刀洗', '大木', '広川', '香春',
                          '添田', '糸田', '川崎', '大任', '赤', '福智', '苅田', 'みやこ', '吉富',
                          '上毛', '築上', '佐賀', '唐津', '鳥栖', '多久', '伊万里', '武雄', '鹿島',
                          '小城', '嬉野', '神埼', '吉野ヶ里', '基山', '上峰', 'みやき', '玄海',
                          '有田', '大町', '江北', '白石', '太良', '長崎', '佐世保', '島原', '諫早',
                          '大村', '平戸', '松浦', '対馬', '壱岐', '五島', '西海', '雲仙', '南島原',
                          '長与', '時津', '東彼杵', '川棚', '波佐見', '小値賀', '佐々', '新上五島',
                          '熊本', '八代', '人吉', '荒尾', '水俣', '玉名', '山鹿', '菊池', '宇土',
                          '上天草', '宇城', '阿蘇', '天草', '合志', '美里', '玉東', '南関', '長洲',
                          '和水', '大津', '菊陽', '南小国', '小国', '産山', '高森', '西原',
                          '南阿蘇', '御船', '嘉島', '益城', '甲佐', '山都', '氷川', '芦北',
                          '津奈木', '錦', '多良木', '湯前', '水上', '相良', '五木', '山江', '球磨',
                          'あさぎり', '苓北', '大分', '別府', '中津', '日田', '佐伯', '臼杵',
                          '津久見', '竹田', '豊後高田', '杵築', '宇佐', '豊後大野', '由布',
                          '国東', '姫島', '日出', '九重', '玖珠', '宮崎', '都城', '延岡', '日南',
                          '小林', '日向', '串間', '西都', 'えびの', '三股', '高原', '国富', '綾',
                          '高鍋', '新富', '西米良', '木城', '川南', '都農', '門川', '諸塚', '椎葉',
                          '美郷', '高千穂', '日之影', '五ヶ瀬', '鹿児島', '鹿屋', '枕崎', '阿久根',
                          '出水', '指宿', '西之表', '垂水', '薩摩川内', '日置', '曽於', '霧島',
                          'いちき串木野', '南さつま', '志布志', '奄美', '南九州', '伊佐', '姶良',
                          '三島', '十島', 'さつま', '長島', '湧水', '大崎', '東串良', '錦江',
                          '南大隅', '肝付', '中種子', '南種子', '屋久島', '大和', '宇検', '瀬戸内',
                          '龍郷', '喜界', '徳之島', '天城', '伊仙', '和泊', '知名', '与論', '那覇',
                          '宜野湾', '石垣', '浦添', '名護', '糸満', '沖縄', '豊見城', 'うるま',
                          '宮古島', '南城', '国頭', '大宜味', '東', '今帰仁', '本部', '恩納',
                          '宜野座', '金武', '伊江', '読谷', '嘉手納', '北谷', '北中城', '中城',
                          '西原', '与那原', '南風原', '渡嘉敷', '座間味', '粟国', '渡名喜',
                          '南大東', '北大東', '伊平屋', '伊是名', '久米島', '八重瀬', '多良間',
                          '竹富', '与那国']
        return

    def __del__(self):
        del self.prefecture_list
        del self.region_list
        del self.city_list
        return

    def get_forward(self, target, text):
        idx = text.find(target)
        if(idx > 0):
            return text[idx+1:]
        else:
            return ""

    def get_back(self, target, text):
        idx = text.find(target)
        if(idx > 0):
            return text[:idx]
        else:
            return ""

    def replace(self, target, replaced, text):
        return text.replace(target, replaced)

    def remove_punctuation(self, text):
        text = unicodedata.normalize("NFKC", text)
        result = text.translate(str.maketrans(
            '', '', string.punctuation + "「」、。','"))
        return result

    def remove_hiragana(self, text):
        result = re.sub('[ぁ-ん]', '', text)
        return result

    def remove_prefecture(self, text):
        result = text.translate(str.maketrans(
            '', '', ''.join(self.prefecture_list)))
        return result

    def remove_region(self, text):
        for each in self.region_list:
            if(text == each):
                return ""
        return text

    def remove_city(self, text):
        for each in self.city_list:
            if(text == each):
                return ""
        return text

    # 正規化
    def normalize(self, text):
        unicodedata.normalize("NFKC", text)
        return text
