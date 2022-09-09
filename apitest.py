import requests
from datetime import date, datetime, timedelta


# 讯飞语音内置墨迹天气API接口测试及结果

# 环境变量
city = "武汉"
nowtime = datetime.utcnow() + timedelta(hours=8)  # 东八区时间
today = datetime.strptime(str(nowtime.date()), "%Y-%m-%d") #今天的日期

# 天气查询
def get_weather():
  if city is None:
    print('请设置城市')
    return None
  url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
  res = requests.get(url).json()
  if res is None:
    return None
  weather = res['data']['list'][0]
  return weather

# 获取当前日期为星期几
def get_week_day():
  week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
  week_day = week_list[datetime.date(today).weekday()]
  return week_day


print(get_weather())
print(get_week_day())


# 天气API查询结果
response_1 = {
    'city': '武汉', 
    'lastUpdateTime': '2022-09-09 20:55:08', 
    'date': '2022-09-09', 
    'weather': '多云', 
    'temp': 25.0, 
    'humidity': '63%', 
    'wind': '东北风2级', 
    'pm25': 20.0, 
    'pm10': 27.0, 
    'low': 24.0, 
    'high': 33.0, 
    'airData': '32', 
    'airQuality': '优', 
    'dateLong': 1662652800000, 
    'weatherType': 1, 
    'windLevel': 2, 
    'province': '湖北'
}