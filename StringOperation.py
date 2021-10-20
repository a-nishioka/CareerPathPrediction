import string
import unicodedata
import re

class StringOperation:
    
    def __init__(self):
        return

    def __del__(self):
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
        result = text.translate(str.maketrans( '', '', string.punctuation + "「」、。','"))
        return result

    def remove_hiragana(self, text):
        result = re.sub('[ぁ-ん]', '', text)
        return result

    def remove_prefecture(self, text):
        prefecture_list = ['愛知','青森','秋田','秋田','石川','茨城','岩手','愛媛','大分','大阪','岡山','沖縄','香川','鹿児島','神奈川','岐阜','京都','熊本','群馬','高知','埼玉','佐賀','滋賀','静岡','島根','千葉','東京','徳島','栃木','鳥取','富山','長崎','長野','奈良','新潟','兵庫','広島','福井','福岡','福島','北海道','三重','宮城','宮崎','山形','山口','山梨','和歌山']
        result = text.translate(str.maketrans( '', '', ''.join(prefecture_list)))
        return result

    def remove_region(self, text):
        region_list = ['北海道','東北','関東','中部','近畿','中国','四国','九州','首都圏','北関東','南関東','甲信越','北陸','東海','関西','北信越','中京','瀬戸内','山陰','山陽','北四国','南四国','北部九州','南九州']
        result = text.translate(str.maketrans( '', '', ''.join(region_list)))
        return result
