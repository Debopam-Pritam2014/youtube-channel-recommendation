import pandas as pd
import numpy as np
import pickle
popular_df=pickle.load(open('popular_df.pkl','rb'))
vectorizer=pickle.load(open('vectorizer.pkl','rb'))
similar_dict=pickle.load(open('similar_channels_data.pkl','rb'))

def recommend(channel_name):
#     find the index of the channel name
    indx=np.where(popular_df['channel_name']==channel_name)[0][0]
#     return similar_dict[indx]['similar_channels_indx'],similar_dict[indx]['similarity_score']
    recommended_channels=[]
    scores=similar_dict[indx]['similarity_score']
    for channel in similar_dict[indx]['similar_channels_indx']:
        # print(channel)
        data=[]
        name=popular_df.iloc[channel]['channel_name']
        avatar=popular_df.iloc[channel]['avatar']
        link=popular_df.iloc[channel]['channel_link']
        data.append(name)
        data.append(avatar)
        data.append(link)
        recommended_channels.append(data)
    return recommended_channels,scores
