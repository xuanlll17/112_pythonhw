import requests
import sqlite3
from datetime import date

__all__=['update_sqlite_data']

#download data-----------------------------------------------------------------
def __download_aqi_data()->list[dict]:
    aqi_url = 'https://data.moenv.gov.tw/api/v2/aqx_p_07?api_key=f1ef64e9-395c-44b2-9bf1-0b714fca448b'
    response = requests.get(aqi_url)
    response.raise_for_status()
    print('下載成功')
    return response.json()      #轉成python資料結構

def parse_json(w):
    location = w['records']
    weather_list = []
    for item in location:
        city_item = {}
        city_item['城市'] = item['locationName']
        city_item['起始時間'] = item['weatherElement'][1]['time'][0]['startTime']
        city_item['結束時間'] = item['weatherElement'][1]['time'][0]['endTime']
        city_item['最高溫度'] = float(item['weatherElement'][1]['time'][0]['parameter']['parameterName'])
        city_item['最低溫度'] = float(item['weatherElement'][1]['time'][0]['parameter']['parameterName'])
        city_item['感覺'] = item['weatherElement'][3]['time'][0]['parameter']['parameterName']
        weather_list.append(city_item)
    return weather_list


#create sql table--------------------------------------------------------------
def __create_table(conn:sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute(
        '''
		CREATE TABLE IF NOT EXISTS 空氣品質(
            "id" INTEGER,
			"測站編號"	INTEGER,
			"測站名稱"	TEXT NOT NULL,
            "測站英文名稱"	TEXT NOT NULL,
			"空品區"	TEXT NOT NULL,
			"更新時間"	TEXT DEFAULT CURRENT_TIMESTAMP,
			"城市"	TEXT NOT NULL,
            "鄉鎮"	TEXT NOT NULL,
            "測站地址"	TEXT NOT NULL,
			"經度"	INTEGER,
			"緯度"	INTEGER,
			"測站類型"	TEXT NOT NULL,
			PRIMARY KEY("id" AUTOINCREMENT),
            UNIQUE(測站名稱,更新時間) ON CONFLICT REPLACE
		);
		'''
    )
    conn.commit()


def __insert_data(conn:sqlite3.Connection,values:list[any])->None:
    cursor = conn.cursor()
    #REPLACE 沒有重建一筆(insert),有就更新
    sql = '''
		REPLACE INTO 空氣品質(測站編號,測站名稱,測站英文名稱,空品區,城市,鄉鎮,測站地址,經度,緯度,測站類型)
		VALUES(?,?,?,?,?,?,?,?,?,?)
	'''
    cursor.execute(sql,values)
    conn.commit()

def update_sqlite_data()->None:
    data = __download_aqi_data()
    conn = sqlite3.connect("空氣品質.db")
    __create_table(conn)
    for item in data:
        print(item)
        __insert_data(conn,values=[item['siteid'],item['sitename'],item['siteengname'],item['areaname'],item['tot'],item['county'],item['township'],item['siteaddress'],item['twd97lon'],item['twd97lat'],item['sitetype']])
    conn.close()
