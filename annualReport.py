import subprocess
import sys
from count import count as count_data
from juan import juan

if __name__ == '__main__':  
    subprocess.run([sys.executable, './stopwords/sort_stopwords_addition.py'], check=True) # 将停用词_addition自动排序
    subprocess.run([sys.executable, './extract_log.py'], check=True) # 提取log里面的元素
    subprocess.run([sys.executable, './getWordCloud.py'], check=True) # 生成词云

    sender, count = count_data()
    
    rank = []
    for i in count:
        index = 0
        min = int(i)
        for j in count:
            if (min < int(j)):
                index += 1
        rank.append(str(index + 1))

    month_latest, date_latest, hour_latest, minute_latest, hour_latest_morning, minute_latest_morning, month_earliest, date_earliest, hour_earliest, minute_earliest = juan()
    all_data = zip(sender, count, rank, month_latest, date_latest, hour_latest, minute_latest, hour_latest_morning, minute_latest_morning, month_earliest, date_earliest, hour_earliest, minute_earliest)

    with open('./juan.txt', 'w', encoding='utf-8') as f: # 个人数据
        for obj in all_data:
            print(' '.join(obj))
            f.write(' '.join(obj) + '\n')
    
    # 以下为js代码源码
    # const seedID = data.user_id + new String(2021);
    # let count_ARKsanlin = 9258;
    # let pfmList = [];

    # if (count <= 100) pfmList = ['潜海员', '$数据丢失$灵喵喵不认识这个人捏', '不活跃成员会资深会员', '您完全不社交是吗'];
    # else if (count <= 500) pfmList = ['水群，到底是一种怎么样的存在', '零元水', '学水群，认识水群，你学会了吗？', '我好不容易水一次群，你却把我伤的这么彻底'];
    # else if (count <= 1000) pfmList = [`当年${sender[0]}老师退出文坛我是极力反对的`, '这群保熟吗', 'tnnd！为什么不水！水！'];
    # else if (count <= 3000) pfmList = ['喷射战士', '水群你都要卷？', '再水亿句', '你这么水你朋友知道吗？啊对对对'];
    # else pfmList = ['汐灵本体', '宁就是天天龙王？', '你上一秒这么水，还是在上秒'];
    # const randomNum = seedRandom.getRandomIntInclusive(seedID, 0, pfmList.length - 1);
    # let pfm = pfmList[randomNum];

    # let replyObj = `${sender} 的2021年度水群报告(今年只从9.28开始统计)：

    # 这一年，你一共水了${count}条消息，在群友中排行第${rank}`
    # if (rank == '1') replyObj += `，恭迎龙神大人！！！`;
    # else if (count >= 100) {
    #     if (count <= 500) replyObj += `，你水了${(count / 64).toFixed(2)}组消息！`;
    #     else if (count <= 1000) replyObj += `，足足有${(count / 154).toFixed(2)}倍的官号粉丝。`;
    #     else if (count <= 3000) replyObj += `，大概能达到${(count / 255).toFixed(2)}次附魔上限。`;
    #     else replyObj += `，你水了${(count / count_ARKsanlin).toFixed(2)}个汐灵了，再接再厉！`;
    # }
    
    # replyObj += `
    # ${month_latest}月${date_latest}号，你卷到很晚，${hour_latest}:${minute_latest}还在发消息`;
    # if (Number(hour_latest_morning) - Number(hour_latest) == 1) replyObj += `，你是直接通宵了吧！`;
    # else replyObj += `。`;
    # replyObj += `
    # ${month_earliest}月${date_earliest}号，你${hour_earliest}:${minute_earliest}在群里打卡，你起的真早`;
    # if (Number(hour_earliest) >= 6 && Number(hour_earliest) <= 7) replyObj += `，这天大家都卷不过你。`;
    # else replyObj += `。`;
    # replyObj += `\n
    # 你的年度喷水形象是：
    # ${pfm}`;

    # if (ifSenderExist === false) replyObj = `${sender} 的2021年度水群报告(今年只从9.28开始统计)：
    
    # 对不起，暂时没有你的数据呢`;

    # data.reply(replyObj);