import pandas as pd
import os
import json
df_esc50=pd.read_csv("esc50.csv")

human_sounds_ids=[]
nature_ids=[]
natural_ids=[]
animal_ids=[]
nature_sound=['rain','wind','thunderstorm']
natural_sounds=['rain','sea_waves','crackling_fire','crickets','chirping_birds','water_drops','wind','pouring_water','thunderstorm']
animal_sounds=['dog','cat','crow','frog','insects_flying']
human_sound=['laughing','snoring','drinking_sipping','coughing','sneezing','breathing','sipping','footsteps','clapping']
for i in range(2000):
 if(df_esc50['category'].iloc[i] in human_sound):
  human_sounds_ids.append(df_esc50['filename'].iloc[i])
 if(df_esc50['category'].iloc[i] in nature_sound):
  nature_ids.append(df_esc50['filename'].iloc[i])
 if(df_esc50['category'].iloc[i] in natural_sounds):
  natural_ids.append(df_esc50['filename'].iloc[i])
 if(df_esc50['category'].iloc[i] in natural_sounds):
  animal_ids.append(df_esc50['filename'].iloc[i])

audio_location=[]
from os.path import exists
sound_labels = [
    "Dog", "Rain", "Crying_baby", "Door_wood_knock", "Helicopter", "Rooster",
    "Sea_waves", "Sneezing", "Mouse_click", "Chainsaw", "Pig", "Crackling_fire",
    "Clapping", "Keyboard_typing", "Siren", "Cow", "Crickets", "Breathing",
    "Door_wood_creaks", "Car_horn", "Frog", "Chirping_birds", "Coughing",
    "Can_opening", "Engine", "Cat", "Water_drops", "Footsteps", "Washing_machine",
    "Train", "Hen", "Wind", "Laughing", "Vacuum_cleaner", "Church_bells",
    "Insects", "flying", "Pouring_water", "Brushing_teeth", "Clock_alarm", "Airplane",
    "Sheep", "Toilet_flush", "Snoring", "Clock_tick", "Fireworks", "Crow",
    "Thunderstorm", "Drinking_sipping", "Glass_breaking", "Hand_saw", "Park",
    "Traffic", "Public_Square","Street_pedestrian","Bus","Tram","Metro","airport","metro_station",
    "shopping_mall"
]

sound_id_map = {}
next_id = 0  # Keep track of the next available ID

for label in sound_labels:
  # Assign unique ID to each label
  sound_id_map[label.lower()] = "/m/0"+str(next_id)
  next_id += 1
# Get the sound labels and IDs from the dictionary
sound_labels = list(sound_id_map.keys())
sound_ids = list(sound_id_map.values())
from pydub import AudioSegment
import os
# Load the foreground audio
custom_json=[]
# Outdoor sounds public sqaure, traffic,pedastrians
len_public_sq=len(os.listdir("dataset/outdoor/public_square"))
for i,file in enumerate(os.listdir("dataset/outdoor/public_square")):
    for wav in os.listdir('esc50'):
        if(wav in human_sounds_ids):
         foreground_audio = AudioSegment.from_file('esc50/'+wav, format="wav")
         background_audio = AudioSegment.from_file("dataset/outdoor/public_square/"+file, format="wav")
         combined_audio = background_audio[:4000].overlay(foreground_audio, position=0)
         wav_data=df_esc50[df_esc50['filename']==wav]
         dict={"wav":"custom_dataset/custom_human_with_public_square/"+str(i)+'_custom_human_with_public_square_'+wav,
           "labels":sound_id_map[wav_data['category'].values[0]]+",/m/053",
           "caption":wav_data['category'].values[0] + " with the sound of public square in background"}
         if(exists('esc50/'+wav)):
          custom_json.append(dict)
         if not os.path.exists('custom_dataset/custom_human_with_public_square'):
            os.makedirs('custom_dataset/custom_human_with_public_square')
         combined_audio.export('custom_dataset/custom_human_with_public_square/'+str(i)+'_custom_human_with_public_square_'+wav, format="wav")
    print('Completed Public sqaure with human:'+str(int((i+1)/len_public_sq)*100)+'%')

len_traffic=len(os.listdir("dataset/outdoor/traffic"))
for i,file in enumerate(os.listdir("dataset/outdoor/traffic")):
    for wav in os.listdir('esc50'):
        if(wav in human_sounds_ids):
         foreground_audio = AudioSegment.from_file('esc50/'+wav, format="wav")
         background_audio = AudioSegment.from_file("dataset/outdoor/traffic/"+file, format="wav")
         combined_audio = background_audio[:4000].overlay(foreground_audio, position=0)
         wav_data=df_esc50[df_esc50['filename']==wav]
         dict={"wav":"custom_dataset/custom_human_with_traffic/"+str(i)+'_custom_human_with_traffic_'+wav,
           "labels":sound_id_map[wav_data['category'].values[0]]+",/m/052",
           "caption":wav_data['category'].values[0] + " with the sound of street traffic in background"}
         if(exists('esc50/'+wav)):
          custom_json.append(dict)
         if not os.path.exists('custom_dataset/custom_human_with_traffic'):
            os.makedirs('custom_dataset/custom_human_with_traffic')
         combined_audio.export('custom_dataset/custom_human_with_traffic/'+str(i)+'_custom_human_with_traffic_'+wav, format="wav")
    print('Completed traffic with human:'+str(int((i+1)/len_traffic)*100)+'%')

len_pedestrians=len(os.listdir("dataset/outdoor/pedastrians"))
for i,file in enumerate(os.listdir("dataset/outdoor/pedastrians")):
    for wav in os.listdir('esc50'):
        if(wav in human_sounds_ids):
         foreground_audio = AudioSegment.from_file('esc50/'+wav, format="wav")
         background_audio = AudioSegment.from_file("dataset/outdoor/pedastrians/"+file, format="wav")
         combined_audio = background_audio[:4000].overlay(foreground_audio, position=0)
         wav_data=df_esc50[df_esc50['filename']==wav]
         dict={"wav":"custom_dataset/custom_human_with_pedastrains/"+str(i)+'_custom_human_with_pedastrains_'+wav,
           "labels":sound_id_map[wav_data['category'].values[0]]+",/m/054",
           "caption":wav_data['category'].values[0] + " with the sound of street pedastrians in background"}
         if(exists('esc50/'+wav)):
          custom_json.append(dict)
         if not os.path.exists('custom_dataset/custom_human_with_pedastrains'):
            os.makedirs('custom_dataset/custom_human_with_pedastrains')
         combined_audio.export('custom_dataset/custom_human_with_pedastrains/'+str(i)+'_custom_human_with_pedastrains_'+wav, format="wav")
    print('Completed street pedestrians  with human:'+str(int((i+1)/len_pedestrians)*100)+'%')

len_park=len(os.listdir("dataset/outdoor/park"))
for i,file in enumerate(os.listdir("dataset/outdoor/park")):
    for wav in os.listdir('esc50'):
        if(wav in human_sounds_ids):
         foreground_audio = AudioSegment.from_file('esc50/'+wav, format="wav")
         background_audio = AudioSegment.from_file("dataset/outdoor/park/"+file, format="wav")
         combined_audio = background_audio[:4000].overlay(foreground_audio, position=0)
         wav_data=df_esc50[df_esc50['filename']==wav]
         dict={"wav":"custom_dataset/custom_human_with_park/"+str(i)+'_custom_human_with_park_'+wav,
           "labels":sound_id_map[wav_data['category'].values[0]]+",/m/051",
           "caption":wav_data['category'].values[0] + " with the sound of park in background"}
         if(exists('esc50/'+wav)):
          custom_json.append(dict)
         if not os.path.exists('custom_dataset/custom_human_with_park'):
            os.makedirs('custom_dataset/custom_human_with_park')
         combined_audio.export('custom_dataset/custom_human_with_park/'+str(i)+'_custom_human_with_park_'+wav, format="wav")
    print('Completed park with human:'+str(int((i+1)/len_park)*100)+'%')

natural_sounds=['rain','sea_waves','crackling_fire','crickets','chirping_birds','water_drops','wind','pouring_water','thunderstorm']
animal_sounds=['dog','cat','crow','frog','insects_flying']
for i,file in enumerate(os.listdir("dataset/outdoor/park")):
    for wav in os.listdir('esc50'):
        if(wav in natural_ids):
         foreground_audio = AudioSegment.from_file('esc50/'+wav, format="wav")
         background_audio = AudioSegment.from_file("dataset/outdoor/park/"+file, format="wav")
         combined_audio = background_audio[:4000].overlay(foreground_audio, position=0)
         wav_data=df_esc50[df_esc50['filename']==wav]
         dict={"wav":"custom_dataset/custom_natural_with_park/"+str(i)+'_custom_natural_with_park_'+wav,
           "labels":sound_id_map[wav_data['category'].values[0]]+",/m/051",
           "caption":wav_data['category'].values[0] + " with the sound of park in background"}
         if(exists('esc50/'+wav)):
          custom_json.append(dict)
         if not os.path.exists('custom_dataset/custom_natural_with_park'):
            os.makedirs('custom_dataset/custom_natural_with_park')
         combined_audio.export('custom_dataset/custom_natural_with_park/'+str(i)+'_custom_natural_with_park_'+wav, format="wav")
    print('Completed park with nature sounds:'+str(int((i+1)/len_park)*100)+'%')

for i,file in enumerate(os.listdir("dataset/outdoor/park")):
    for wav in os.listdir('esc50'):
        if(wav in animal_ids):
         foreground_audio = AudioSegment.from_file('esc50/'+wav, format="wav")
         background_audio = AudioSegment.from_file("dataset/outdoor/park/"+file, format="wav")
         combined_audio = background_audio[:4000].overlay(foreground_audio, position=0)
         wav_data=df_esc50[df_esc50['filename']==wav]
         dict={"wav":"custom_dataset/custom_animals_with_park/"+str(i)+'_custom_animals_with_park_'+wav,
           "labels":sound_id_map[wav_data['category'].values[0]]+",/m/051",
           "caption":wav_data['category'].values[0] + " with the sound of park in background"}
         if(exists('esc50/'+wav)):
          custom_json.append(dict)
         if not os.path.exists('custom_dataset/custom_animals_with_park'):
            os.makedirs('custom_dataset/custom_animals_with_park')
         combined_audio.export('custom_dataset/custom_animals_with_park/'+str(i)+'_custom_animals_with_park_'+wav, format="wav")
    print('Completed park with animal sounds:'+str(int((i+1)/len_park)*100)+'%')

for i,file in enumerate(os.listdir("dataset/outdoor/public_square")):
    for wav in os.listdir('esc50'):
        if(wav in nature_ids):
         foreground_audio = AudioSegment.from_file('esc50/'+wav, format="wav")
         background_audio = AudioSegment.from_file("dataset/outdoor/public_square/"+file, format="wav")
         combined_audio = background_audio[:4000].overlay(foreground_audio, position=0)
         wav_data=df_esc50[df_esc50['filename']==wav]
         dict={"wav":"custom_dataset/custom_nature_with_public_square/"+str(i)+'_custom_nature_with_public_square_'+wav,
           "labels":sound_id_map[wav_data['category'].values[0]]+",/m/053",
           "caption":wav_data['category'].values[0] + " with the sound of public square in background"}
         if(exists('esc50/'+wav)):
          custom_json.append(dict)
         if not os.path.exists('custom_dataset/custom_nature_with_public_square'):
            os.makedirs('custom_dataset/custom_nature_with_public_square')
         combined_audio.export('custom_dataset/custom_nature_with_public_square/'+str(i)+'_custom_nature_with_public_square_'+wav, format="wav")
    print('Completed Public sqaure with nature:'+str(int((i+1)/len_public_sq)*100)+'%')


for i,file in enumerate(os.listdir("dataset/outdoor/traffic")):
    for wav in os.listdir('esc50'):
        if(wav in nature_ids):
         foreground_audio = AudioSegment.from_file('esc50/'+wav, format="wav")
         background_audio = AudioSegment.from_file("dataset/outdoor/traffic/"+file, format="wav")
         combined_audio = background_audio[:4000].overlay(foreground_audio, position=0)
         wav_data=df_esc50[df_esc50['filename']==wav]
         dict={"wav":"custom_dataset/custom_nature_with_traffic/"+str(i)+'_custom_nature_with_traffic_'+wav,
           "labels":sound_id_map[wav_data['category'].values[0]]+",/m/052",
           "caption":wav_data['category'].values[0] + " with the sound of street traffic in background"}
         if(exists('esc50/'+wav)):
          custom_json.append(dict)
         if not os.path.exists('custom_dataset/custom_nature_with_traffic'):
            os.makedirs('custom_dataset/custom_nature_with_traffic')
         combined_audio.export('custom_dataset/custom_nature_with_traffic/'+str(i)+'_custom_nature_with_traffic_'+wav, format="wav")
    print('Completed traffic with nature:'+str(int((i+1)/len_traffic)*100)+'%')


for i,file in enumerate(os.listdir("dataset/outdoor/traffic")):
    for wav in os.listdir('esc50'):
        if(wav in nature_ids):
         foreground_audio = AudioSegment.from_file('esc50/'+wav, format="wav")
         background_audio = AudioSegment.from_file("dataset/outdoor/traffic/"+file, format="wav")
         combined_audio = background_audio[:4000].overlay(foreground_audio, position=0)
         wav_data=df_esc50[df_esc50['filename']==wav]
         dict={"wav":"custom_dataset/custom_nature_with_pedastrains/"+str(i)+'_custom_nature_with_pedastrains_'+wav,
           "labels":sound_id_map[wav_data['category'].values[0]]+",/m/054",
           "caption":wav_data['category'].values[0] + " with the sound of street pedastrains in background"}
         if(exists('esc50/'+wav)):
          custom_json.append(dict)
         if not os.path.exists('custom_dataset/custom_nature_with_pedastrains'):
            os.makedirs('custom_dataset/custom_nature_with_pedastrains')
         combined_audio.export('custom_dataset/custom_nature_with_pedastrains/'+str(i)+'_custom_nature_with_pedastrains_'+wav, format="wav")
    print('Completed street pedestrians  with nature:'+str(int((i+1)/len_pedestrians)*100)+'%')

#  Vechicle
len_bus=len(os.listdir("dataset/vehicle/bus"))
for i,file in enumerate(os.listdir("dataset/vehicle/bus")):
    for wav in os.listdir('esc50'):
        if(wav in human_sounds_ids):
         foreground_audio = AudioSegment.from_file('esc50/'+wav, format="wav")
         background_audio = AudioSegment.from_file("dataset/vehicle/bus/"+file, format="wav")
         combined_audio = background_audio[:4000].overlay(foreground_audio, position=0)
         wav_data=df_esc50[df_esc50['filename']==wav]
         dict={"wav":"custom_dataset/custom_human_with_bus/"+str(i)+'_custom_human_with_bus_'+wav,
           "labels":sound_id_map[wav_data['category'].values[0]]+",/m/055",
           "caption":wav_data['category'].values[0] + " with the sound of bus in background"}
         if(exists('esc50/'+wav)):
          custom_json.append(dict)
         if not os.path.exists('custom_dataset/custom_human_with_bus'):
            os.makedirs('custom_dataset/custom_human_with_bus')
         combined_audio.export('custom_dataset/custom_human_with_bus/'+str(i)+'_custom_human_with_bus_'+wav, format="wav")
    print('Completed bus with human:'+str(int((i+1)/len_bus)*100)+'%')

len_metro=len(os.listdir("dataset/vehicle/metro"))
for i,file in enumerate(os.listdir("dataset/vehicle/metro")):
    for wav in os.listdir('esc50'):
        if(wav in human_sounds_ids):
         foreground_audio = AudioSegment.from_file('esc50/'+wav, format="wav")
         background_audio = AudioSegment.from_file("dataset/vehicle/metro/"+file, format="wav")
         combined_audio = background_audio[:4000].overlay(foreground_audio, position=0)
         wav_data=df_esc50[df_esc50['filename']==wav]
         dict={"wav":"custom_dataset/custom_human_with_metro/"+str(i)+'_custom_human_with_metro_'+wav,
           "labels":sound_id_map[wav_data['category'].values[0]]+",/m/057",
           "caption":wav_data['category'].values[0] + " with the sound of metro in background"}
         if(exists('esc50/'+wav)):
          custom_json.append(dict)
         if not os.path.exists('custom_dataset/custom_human_with_metro'):
            os.makedirs('custom_dataset/custom_human_with_metro')
         combined_audio.export('custom_dataset/custom_human_with_metro/'+str(i)+'_custom_human_with_metro_'+wav, format="wav")
    print('Completed metro with human:'+str(int((i+1)/len_metro)*100)+'%')

len_tram=len(os.listdir("dataset/vehicle/tram"))
for i,file in enumerate(os.listdir("dataset/vehicle/tram")):
    for wav in os.listdir('esc50'):
        if(wav in human_sounds_ids):
         foreground_audio = AudioSegment.from_file('esc50/'+wav, format="wav")
         background_audio = AudioSegment.from_file("dataset/vehicle/tram/"+file, format="wav")
         combined_audio = background_audio[:4000].overlay(foreground_audio, position=0)
         wav_data=df_esc50[df_esc50['filename']==wav]
         dict={"wav":"custom_dataset/custom_human_with_tram/"+str(i)+'_custom_human_with_tram_'+wav,
           "labels":sound_id_map[wav_data['category'].values[0]]+",/m/056",
           "caption":wav_data['category'].values[0] + " with the sound of tram in background"}
         if(exists('esc50/'+wav)):
          custom_json.append(dict)
         if not os.path.exists('custom_dataset/custom_human_with_pedastrains'):
            os.makedirs('custom_dataset/custom_human_with_pedastrains')
         combined_audio.export('custom_dataset/custom_human_with_pedastrains/'+str(i)+'_custom_human_with_tram_'+wav, format="wav")
    print('Completed tram with human:'+str(int((i+1)/len_pedestrians)*100)+'%')

#  Indoor
len_airport=len(os.listdir("dataset/indoor/airport"))
for i,file in enumerate(os.listdir("dataset/indoor/airport")):
    for wav in os.listdir('esc50'):
        if(wav in human_sounds_ids):
         foreground_audio = AudioSegment.from_file('esc50/'+wav, format="wav")
         background_audio = AudioSegment.from_file("dataset/indoor/airport/"+file, format="wav")
         combined_audio = background_audio[:4000].overlay(foreground_audio, position=0)
         wav_data=df_esc50[df_esc50['filename']==wav]
         dict={"wav":"custom_dataset/custom_human_with_airport/"+str(i)+'_custom_human_with_airport_'+wav,
           "labels":sound_id_map[wav_data['category'].values[0]]+",/m/058",
           "caption":wav_data['category'].values[0] + " with the sound of airport in background"}
         if(exists('esc50/'+wav)):
          custom_json.append(dict)
         if not os.path.exists('custom_dataset/custom_human_with_airport'):
            os.makedirs('custom_dataset/custom_human_with_airport')
         combined_audio.export('custom_dataset/custom_human_with_airport/'+str(i)+'_custom_human_with_airport_'+wav, format="wav")
    print('Completed airport with human:'+str(int((i+1)/len_airport)*100)+'%')

len_metro_station=len(os.listdir("dataset/indoor/metro_station"))
for i,file in enumerate(os.listdir("dataset/indoor/metro_station")):
    for wav in os.listdir('esc50'):
        if(wav in human_sounds_ids):
         foreground_audio = AudioSegment.from_file('esc50/'+wav, format="wav")
         background_audio = AudioSegment.from_file("dataset/indoor/metro_station/"+file, format="wav")
         combined_audio = background_audio[:4000].overlay(foreground_audio, position=0)
         wav_data=df_esc50[df_esc50['filename']==wav]
         dict={"wav":"custom_dataset/custom_human_with_metro_station/"+str(i)+'_custom_human_with_metro_station_'+wav,
           "labels":sound_id_map[wav_data['category'].values[0]]+",/m/059",
           "caption":wav_data['category'].values[0] + " with the sound of metro station in background"}
         if(exists('esc50/'+wav)):
          custom_json.append(dict)
         if not os.path.exists('custom_dataset/custom_human_with_metro_station'):
            os.makedirs('custom_dataset/custom_human_with_metro_station')
         combined_audio.export('custom_dataset/custom_human_with_metro_station/'+str(i)+'_custom_human_with_metro_station_'+wav, format="wav")
    print('Completed metro station with human:'+str(int((i+1)/len_metro_station)*100)+'%')

len_shop_mall=len(os.listdir("dataset/indoor/shopping_mall"))
for i,file in enumerate(os.listdir("dataset/indoor/shopping_mall")):
    for wav in os.listdir('esc50'):
        if(wav in human_sounds_ids):
         foreground_audio = AudioSegment.from_file('esc50/'+wav, format="wav")
         background_audio = AudioSegment.from_file("dataset/indoor/shopping_mall/"+file, format="wav")
         combined_audio = background_audio[:4000].overlay(foreground_audio, position=0)
         wav_data=df_esc50[df_esc50['filename']==wav]
         dict={"wav":"custom_dataset/custom_human_with_shopping_mall/"+str(i)+'_custom_human_with_shopping_mall_'+wav,
           "labels":sound_id_map[wav_data['category'].values[0]]+",/m/060",
           "caption":wav_data['category'].values[0] + " with the sound of shopping mall in background"}
         if(exists('esc50/'+wav)):
          custom_json.append(dict)
         if not os.path.exists('custom_dataset/custom_human_with_shopping_mall'):
            os.makedirs('custom_dataset/custom_human_with_shopping_mall')
         combined_audio.export('custom_dataset/custom_human_with_shopping_mall/'+str(i)+'_custom_human_with_shopping_mall_'+wav, format="wav")
    print('Completed shopping mall with human:'+str(int((i+1)/len_shop_mall)*100)+'%')

json_data={"data":custom_json}
file_public_json="esc_custom_train.json"
with open(file_public_json, "w") as json_file:
    json.dump(json_data, json_file, indent=4)
    print('Train JSON Created.')

import random
test_data=random.sample(custom_json, 1020)
test_data_json={"data":test_data}
file_test_json="esc_custom_test.json"
with open(file_test_json, "w") as json_file10:
    json.dump(test_data_json, json_file10, indent=4)
    print('Test JSON Created.')