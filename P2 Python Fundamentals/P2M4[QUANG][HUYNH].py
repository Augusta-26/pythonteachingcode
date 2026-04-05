import os

def weather_program():
    mean_temp_file = open('mean_temp.txt','a+')
    mean_temp_file.write('Rio de Janeiro,Brazil,30.0,18.0\n')
    mean_temp_file.seek(0)
    headings = mean_temp_file.readline()
    headings_list = headings.split(',')

    city_temp = mean_temp_file.readline()
    while city_temp:
        city_temp_list = city_temp.split(',')
        print(headings_list[0].capitalize(),'of',city_temp_list[0],headings_list[2],'is',city_temp_list[2],'Celsius')
        city_temp = mean_temp_file.readline()

    mean_temp_file.close()
    
cmd = "curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt"
os.system(cmd) #download file in Python version, not Jupyter Notebook
print('[QUANG HUYNH]')
weather_program()



