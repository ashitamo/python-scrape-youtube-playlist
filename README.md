# Python Scrape Youtube Playlist
 Scrape playlist with beautifulsoup and request.
 
## How to run it?
### put yt.py in same of main.py folder
main.py
    
    form yt import YT
    link='https://www.youtube.com/watch?v=iRK4AAIOtVg&list=PLsfoPiT3bicYtFMKQm3rrhk4I6uxjfxvs'
    
    title,playlist=YT.yt(link)
    print(title)
    print(playlist)
    #playlist is a list. if you want to scrape the first videoId,you will do it. like:
    print(playlist[0][0])#videoId
    print(playlist[0][1])#name
    print(playlist[0][2])#duration
    
 output
    
    04 #title
    [['iRK4AAIOtVg', '【戴上耳機♪用心聆聽】在那樣的時刻與你相遇，那一刻想馬上將這份感情傳達給你！', '5:11'], ['CEhXQOsSdAo', '【戴上耳機♪用心聆聽】請讓我守護你的全部，無論你多麼的迷茫！', '4:50'], ['0HTAKT-JIaA', '【單曲推薦】【僕が死 
    のうと思ったのは】【薇爾莉特】', '6:18'], ['dpMVLrdzhuY', '超好聽的日語歌曲——《君だったら》HAPPY BIRTHDAY', '5:21'], ['180xCt99Lec', '一首好聽的日語歌——《生きていたんだよな》她曾經活過啊 あいみょん', '3:16'], ['gLyAp9mBo0E', '『イ 
    ンタビュア | Interviewer』【鹿乃(かの)】中英日羅字幕', '4:27'], ['owyCtb21Lws', '『オレンジ Orange』【花たん】中日字幕', '4:07'], ['4RClfyQh5Ow', '已刪除影片', '4:07'], ['YaLdJc7l7O0', '已刪除影片', '4:07'], ['_nzEkpVuNF4', '已刪除
    影片', '4:07'], ['1n5FL9eOefg', '♡.おねがいダーリン\u3000ver.柊優花', '3:13'], ['ZGtBKChPmkM', 'そばかす (JUDY AND MARY) \u3000song by Lon', '4:13'], ['skPEvdls_9k', 'やがて君になる ED【hectopascal】/ 小糸 侑 , 七海 燈子', '4:29'], ['2mBRwwNA8zw', '【戴上耳機♪一秒沉淪】那天遇上了你，從此改變了我！', '4:11'], ['xN_SJE-B-TQ', '花降らし acoustic cover / pazi', '2:21'], ['rQ73KgimPxY', 'Nightcore - Koi ni Koishite 「 Mai Kuraki 」', '3:39'], ['GQ3V50XoLOM', '美 
    波「紫丁香」MV', '5:03'], ['zAKYiZyEOdc', 'Yunomi & nicamoq - インドア系ならトラックメイカー (Fdby Remix)【中日歌詞Lyrics】', '3:29'], ['fbJiRfIp_cU', '【小野崎人】TouhouMAD - Touhou & Nitori Get Down! (+lyrics) 【HD】', '5:40'], ['0YF8vecQWYs', '美波「聲嘶力竭」MV', '4:14'], ['HJpF72ht41Y', '已刪除影片', '4:14'], ['c9lGNuLiRr8', '【中文字幕】DOUBLE RAINBOW DREAMS feat.澤村·史賓瑟·英梨梨・霞之丘詩羽(CV：大西沙織・茅野愛衣)【不起眼女主角培育法♭】', '4:37'], ['Fd9AOs4BMVM', 'Yunomi - ダンスフロアの果実 (feat. nicamoq)', '3:56'], ['YSRsw0eAkNc', '[偽戀]西野加奈 - 好想見你 好想見你 (附中日歌詞)', '4:39'], ['6C2g065JKvk', '人渣的本願 ED - 平行線 (中文字幕)', '5:00'], ['clU8c2fpk2s', '【女 
    版翻唱】Lemon/米津玄師(Full Covered by コバソロ & 春茶)', '4:32'], ['4YHUamjfJ0k', 'ryo (supercell) × やなぎなぎ\u3000メルト 10th ANNIVERSARY MIX', '5:09'], ['GSpdPn14lno', '創聖のアクエリオン - AKINO（フル）', '4:42'], ['k0KqXYfkjEU', 'Sword Art Online: Ordinal Scale - Ubiquitous dB -Special Ver.- // アスナ x シリカ', '4:50'], ['sDFHITaq-XY', '♫ 擅長捉弄人的高木同學 ED 1- 気まぐれロマンティック【日中歌詞】【FULL】✕', '4:52'], ['1kYE_aeDxcY', '已刪除影片', '4:52'], ['2cgQrUVRCg0', '已刪除影片', '4:52'], ['dpMVLrdzhuY', '超好聽的日語歌曲——《君だったら》HAPPY BIRTHDAY', '5:21'], ['7_UW6acbdyU', 'SAKURA - いきものがかり (Ikimonogakari)(カヴァー)', '5:58'], ['45uSYC7335U', '《僕が死のうと
    思ったのは》/《曾經我也想過一了百了》【中/日歌詞】(hess Cover)', '6:18'], ['q2cmyLLwVu8', 'プラスティックメモリーズ「好きなので。」', '4:30'], ['-tKVN2mAKRI', 'DAOKO × 米津玄師『打上花火』MUSIC VIDEO', '4:53'], ['lLnUpHa8n1k', 'rionos - Viator (ウィアートル) [Maquia Theme Song - HD]', '4:53'], ['W_IkBXSyC_4', '當山みれい 『願い～あの頃のキミへ～』', '5:52'], ['eBhNSdxjjms', 'Karakai Jouzu no Takagi-san 2 ED3 - 「 キセキ Kiseki 」by Takahashi Rie (FULL VER.)', '5:04'], ['fmQRhPSpGdQ', '【MV】夏恋慕 - Harucha / Koba Solo（“ 富城物産” CM歌曲）', '4:36'], ['DS2sP8CDLas', "あたしが隣にいるうちに／藤川千愛\u3000アニメ『盾の勇者の成り上がり』エンディングテーマ   (''The Rising of the Shield Hero'' Ending Theme )", '5:55'], ['AN6EcOyqHao', "Baby don't cry / 安室奈美恵(full covered by コバソロ & 藤川千愛)", '4:46'], ['60V_ns2HukE', 'Kie Kitano →「 Hazakura 」', '5:19'], ['6su62xI2x2Q', "きみの名前 / 藤川千愛 (「盾の勇者 
    の成り上がり」エンディングテーマ）Music Video (''The Rising of the Shield Hero'' Ending Theme )", '5:01'], ['TLWkm-SNDS8', '超好听的日语歌曲——《太陽と向日葵》FLOWER', '4:27'], ['D7cW3x6cDQA', '一首好聽的日語歌《モトカレ》Juliet【中
    日歌詞Lyrics】', '4:42'], ['A_1t2Dkd2Io', 'AAA / 「恋音と雨空」Music Video', '5:19'], ['oeCveS4UidE', '[ Chihiro ] - Home ( Lyrics )', '4:41'], ['Iuajy8LBjAQ', '一首好聽的日語歌《トランスルーセント》やなぎなぎ【中日歌詞Lyrics】', '4:15'], ['FE40N7DOPAQ', '【鬼滅之刃】LiSA - 紅蓮華 (中日文字幕)-鬼滅の刃KimetsunoYaiba OP Full Lyrics', '3:58'], ['0_01XNdmJSw', '已刪除影片', '3:58'], ['RUwsujdyq5U', '已刪除影片', '3:58'], ['SVxyPoT9pl0', '已刪除影片', '3:58'], ['OrfkBaqiktY', '【一首超好聽的日語歌】- 舞花『New World』', '4:10'], ['uKw0CN7dwKc', 'ULTIMATE♭ /  加藤恵   ( CV 安野希世乃 )「Saenai Heroine no Sodatekata Fine」 ( Lyrics  )', '4:37'], ['4ZP_U28H54g', '一首好聽的日語歌《*菜乃 - 夢
    花火》【中日歌詞Lyrics】', '4:26'], ['s-O_JV8j8wc', 'back number - 「瞬き」Music Video', '2:41']]
    #playlist
    
    iRK4AAIOtVg #videoId
    
    【戴上耳機♪用心聆聽】在那樣的時刻與你相遇，那一刻想馬上將這份感情傳達給你！ #name
    
    5:11# duration
    
