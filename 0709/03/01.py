import pygsheets
import pandas as pd

gc = pygsheets.authorize(service_account_file='crested-sentry-428902-d8-69499e73e869.json')

survey_url = 'https://docs.google.com/spreadsheets/d/1zKaM6ZD5RwR_7s-tYwdsQzrQ5BsUzf2JuidSaHcsPz4/edit?gid=0#gid=0/'


sh = gc.open_by_url(survey_url)

ws = sh.worksheet_by_title('工作表1')
ws.update_value('A1', '新尖兵')
ws.update_value('B1', '影像處理')
df1 = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
ws.set_dataframe(df1, 'A3', copy_index=True, nan='')