import os
import shutil

path = "C:\\Users\\queyo\\Desktop\\音乐\\"
#path = "F:\\music"
new_folder_path = os.path.join(path,"日语名字")
n#ew_folder_path = os.path.join(path,"中文名字")
if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)

def check_contain_jp(check_str):
    for s in check_str:
        if u'\u4e00' <= s <= u'\u9fff':
        #http://xuehaipeng.iteye.com/blog/613825 #日文编码
        #if u'\u3040' <= s <= u'\u309f' or u'\u30a0' <= s <= u'\u30ff':
            return True
    return False

ky = ["op", "ed","神田沙也加", "米津玄師", "AKB48", "akb48", "ELISA", "Lia", "LiSA", "小林未郁", 
      "mizuki", "Mizuki", "Trident", "中孝介", "南條愛乃", "堀江由衣", "平沢進", "数码宝贝",
      "戸松遥", "96", "梶浦由記", "水樹", "石川智晶", "AKINO", "Aimer", "fripSide",
      "魔法少女", "魔法禁书", "澤野弘之", "平野綾", "山村響", "宮崎歩", "宇浦冴香", 
      "家庭教师", "寄生兽", "水野佐彩", "池頼広", "鋼兵", "赤飯", "千本桜", "高梨康治",
      "高橋広樹", "麻枝准", "黒崎真音", "龙猫", "茅原実里", "花澤香菜", "科学超电磁炮",
      "宮崎誠", "大谷幸", "大黒摩季", "坂本真綾", "多田葵", "唐沢美帆", "和田光司", 
      "伊藤祥平", "仓木麻衣", "井内舞子", "橋本由香利", "久石让", "宫崎骏", "安室奈美恵",
      "YUI", "RADWIMPS", "Ray", "Gemie", "GARNiDELiA", "Dream", "CHEMISTRY", "BUMP OF CHICKEN", 
      "Booing Day", "Angela", "99radioservice", "MYTH & ROID", "RIPE", "OLIVIA", 
      "OKAMOTO", "SPLAY", "STEREO DIVE", "T.M.Revolution", "THE ORAL CIGARETTES", 
      "THE STREET BEATS", "TRUSTRICK", "V.A.", "V6", "Yosh", "yoshiki", "lisa",
      "ZAQ", "可憐Girl", "哥特萝莉", "喜多村英梨", "岸田教団", "LoveLive", "渕上舞", 
      "沼倉愛美", "稲村優奈", "吉田仁美", "azusa", "OxT", "TV", "3L", "BABYMETAL",
      "BAAD", "KOKIA", "Lisa", "Op", "OP", "ED", "Ed", "亜咲花", "佐倉綾音", "倉木麻衣", 
      "初音", "加藤有加利", "地狱少女", "奥井雅美", "安野希世乃", "小倉唯", "早見沙織,", 
      "日本", "東山奈央", "柯南", "柴田淳", "水树", "滨崎步", "火影", "KOKIA", "EGOIST", 
      "ClariS", "中島美嘉", "奥井雅美", "奥田真子", "玉置浩二", "玉置成実", "神曲", "罪恶王冠", 
      "高达", 
      ]

def check_ky(ky, name):
    for i in ky:
        if i in name:
            return True
    return False

#列出文档
file_list = os.listdir(path)
#提取出文档名称内的数字，并根据数字决定将问价发往那个文件夹
for i in file_list:
    old_file_path = os.path.join(path,i)
    new_file_path = os.path.join(path,"日语名字")
    #new_file_path = os.path.join(path,"中文名字")
    if os.path.isdir(old_file_path):
        pass
    elif not os.path.exists(old_file_path):
        pass
    elif ".mp3" not in i:
        os.remove(old_file_path)
    
    elif check_contain_jp(i):
            shutil.move(old_file_path,new_file_path)
    
    else:
        if check_ky(ky, i):
            shutil.move(old_file_path,new_file_path)
        
