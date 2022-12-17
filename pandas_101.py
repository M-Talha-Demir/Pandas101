import numpy as np
import pandas as pd

############################################################
# # Series
############################################################

# my_dict = {'atil': 50, 'zeynep': 40, 'Mehmet': 30}
# my_series = pd.Series(my_dict)
# print(my_series)
#
# my_ages = [50, 40, 30]
# my_names = ['Atil', 'Zeynep', 'Mehmet']
# my_series = pd.Series(data=my_ages, index=my_names)
# print(my_series)
#
# np_array = np.array([50, 40, 30])
# print(np_array)
# my_series = pd.Series(np_array)
# print(my_series)
# my_series = pd.Series(np_array, my_names)
# print(my_series)

############################################################
# # Series Features
############################################################

# my_series = pd.Series(['Atil', 'Zeynep', 'Mehmet'])
# print(my_series)
# my_series = pd.Series(['Atil', 'Zeynep', 'Mehmet'], [1, 2, 3])
# result_war_1 = pd.Series([100, 20, 30], ['Atil', 'Zeynep', 'Mehmet'])
# result_war_2 = pd.Series([10, 20, 30], ['Atil', 'Zeynep', 'Mehmet'])
# # result_war_3 = pd.Series([100, 200, 60], ['Atil', 'Zeynep', 'Ayşe'])
#
# result_war_ = result_war_1 + result_war_2
# # result_war_ = result_war_1 + result_war_2 + result_war_3
# print(result_war_)


############################################################
# # Data Frame
############################################################

# random_array = np.random.randn(4, 3)
# print(random_array)
#
# df = pd.DataFrame(random_array)
# print(df)
#
# new_df = pd.DataFrame(random_array, index=['Taha', 'Rumeysa', 'Hasan', 'Aynur'], columns=['Maaş', 'Yaş', 'Çalışma Saati'])
# print(new_df)
# print(new_df['Yaş'])
# print(new_df['Çalışma Saati'])
# print(new_df[['Maaş', 'Çalışma Saati']])
# print(new_df.loc['Taha'])
# print(new_df.iloc[0])

############################################################
# # Data Frame İ n d e x
############################################################

# new_df['Emeklilik Yaşı'] = new_df['Yaş'] + new_df['Yaş']
# print(new_df)
#
# print(new_df.drop('Emeklilik Yaşı', axis=1))
# print(new_df.drop('Taha'))
# print(new_df)
# print(new_df.drop('Emeklilik Yaşı', axis=1, inplace=True))
# print(new_df)
# print(new_df.loc['Aynur']['Maaş'])
# print(new_df.loc['Taha']['Yaş'])
# print(new_df < 0)
# tt =new_df < 0
# print(tt)
# print(new_df[tt])
# print(new_df[new_df['Yaş'] > 0])
# print(new_df[new_df['Çalışma Saati'] > 0])
# print(new_df.reset_index())
# new_index_list = ['Ta', 'Ru', 'Ha', 'Ay']
# new_df['yeni index'] = new_index_list
# print(new_df.set_index('yeni index'))
# print(new_df)
# print(new_df.set_index('yeni index', inplace=True))
# print(new_df)

############################################################
# # Data Frame Multi İ n d e x
###########################################################

# first_index = ["Demir", "Demir", "Demir", "Demir", "Demir", 'Türe', 'Türe', 'Deniz']
#
# in_index = ['Taha', 'Rumeysa', 'Hasan', 'Aynur', 'Talha', 'İbrahim', 'Kemal', 'Belgin']
#
# multi_index = list(zip(first_index, in_index))
#
# print(multi_index)
#
# multi_index = pd.MultiIndex.from_tuples(multi_index)
#
# print(multi_index)
#
# family_list = [[20, 'A'], [13, 'B'], [14, 'C'], [16, 'D'], [17, 'G'], [15, 'H'], [19, 'J'], [18, 'K']]
#
# family_list_np = np.array(family_list)
#
# family_list_df = pd.DataFrame(family_list_np, index=multi_index, columns=['Yaş', "Meslek"])
#
# print(family_list_df)
# print(family_list_df.loc['Demir'])
# print(family_list_df.loc['Demir'].loc['Taha'])
# family_list_df.index.names = ['Soyadı', 'İsmi']
# print(family_list_df)


############################################################
# # Missing Data
###########################################################

# data_dict = {'İstanbul': [30, 29, np.nan], 'Amasya': [20, np.nan, 25], 'İzmir': [40, 39, 37]}
# weather_df = pd.DataFrame(data_dict)
#
# print(weather_df)
# print(weather_df.dropna())
# print(weather_df.dropna(axis=1))
#
# data_dict = {'İstanbul': [30, 29, np.nan], 'Amasya': [20, np.nan, 25], 'İzmir': [40, 39, 37], 'Samsun': [np.nan, np.nan, 35]}
# weather_df = pd.DataFrame(data_dict)
#
# print(weather_df)
# print(weather_df.dropna(axis=1, thresh=2))
# print(weather_df.fillna(20))


############################################################
# # group by
###########################################################

# data_dict = {'Departman': ['Yazılım', 'Satış', "pazar", "pazar", "Yazılım", "hukuk", "hukuk", "hukuk"],
#              'Çalışan İsmi': ['Taha', 'Rumeysa', 'Hasan', 'Aynur', 'Talha', 'İbrahim', 'Kemal', 'Belgin'],
#              'Maaş': [40, 39, 37, 40, 39, 37, 40, 39]}
# weather_df = pd.DataFrame(data_dict)
#
# print(weather_df)
# gruoup = weather_df.groupby('Departman')
# print(gruoup.count())
# print(gruoup.mean())
# print(gruoup.max())
# print(gruoup.describe())

############################################################
# # concat
###########################################################

# data_dict_1 = {'İsim': ['Taha', 'Rumeysa', 'Hasan', 'Aynur'],
#              'Spor': ['Koşu', 'Yüzme', 'Koşu', 'Basketbol'],
#              'Kalori': [200,100,50,300]}
# df_1 = pd.DataFrame(data_dict_1)
# data_dict_2 = {'İsim': ['Talha', 'İbrahim', 'Kemal', 'Belgin'],
#              'Spor': ['Voleybol', 'Yüzme', 'Koşu', 'Basketbol'],
#              'Kalori': [200,100,50,300]}
# df_2 = pd.DataFrame(data_dict_2, index=[4, 5, 6, 7])
# data_dict_3 = {'İsim': ['Osman', 'Mehmed', 'Muhammed', 'Ahmed'],
#              'Spor': ['Koşu', 'Yüzme', 'Voleybol', 'Basketbol'],
#              'Kalori': [200,100,50,300]}
# df_3 = pd.DataFrame(data_dict_3, index=[8, 9, 10, 11])
#
# print(pd.concat([df_1, df_2, df_3], axis=0))
# df_conc = pd.concat([df_1, df_2, df_3], axis=0)
# print(df_conc)

############################################################
# # merge
###########################################################

# data_dict_1 = {'İsim': ['Taha', 'Rumeysa', 'Hasan', 'Aynur'],
#              'Spor': ['Koşu', 'Yüzme', 'Koşu', 'Basketbol']}
# merge_data_df_1 = pd.DataFrame(data_dict_1)
# print(merge_data_df_1)
#
# data_dict_2 = {'İsim': ['Taha', 'Rumeysa', 'Hasan', 'Aynur'],
#              'Kalori': [200,100,50,300]}
# merge_data_df_2 = pd.DataFrame(data_dict_2)
#
# print(merge_data_df_2)
# print(pd.merge(merge_data_df_1,merge_data_df_2, on='İsim'))

############################################################
# # Pandas ++
###########################################################

# data_dict = {'Departman': ['Yazılım', 'Satış', "pazar", "pazar", "Yazılım", "hukuk", "hukuk", "hukuk", 'Yazılım'],
#              'Çalışan İsmi': ['Taha', 'Rumeysa', 'Hasan', 'Aynur', 'Talha', 'İbrahim', 'Kemal', 'Belgin', 'Talha'],
#              'Maaş': [40, 39, 37, 40, 39, 37, 40, 39, 88]}
#
# df = pd.DataFrame(data_dict)
# print(df)
# print(df['Departman'].unique())
# print(df['Departman'].nunique())
# print(df['Departman'].value_counts())
#
#
# def brut_to_net(maas):
#     return maas*0.66
#
#
# print(df['Maaş'].apply(brut_to_net))
# print(df.isnull())
#
#
# print(df.pivot_table(values='Maaş', index=['Departman', 'Çalışan İsmi']))
# print(df.pivot_table(values='Maaş', index=['Departman', 'Çalışan İsmi'], aggfunc=np.sum))

############################################################
# # Pandas ++ Excel
###########################################################

df = pd.read_excel('pandas_.xlsx')
df = pd.DataFrame(df)
print(df)
print(df.dropna())
dolu_excel = df.dropna()
print(dolu_excel)
dolu_excel.to_excel("new_pandas.xlsx")