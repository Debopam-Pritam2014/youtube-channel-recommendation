import streamlit as st
import pickle
import pandas as pd
import numpy as np
from helper import recommend
import requests
from io import BytesIO
import time
import streamlit.components.v1 as components


popular_df=pickle.load(open('popular_df.pkl','rb'))
st.header("Youtube Channel Recommendation")

# keywords=st.text_input("Enter your major...")
user_input=st.selectbox(label="Select Channels",options=sorted(list(popular_df['channel_name'].values)))

submit_btn=st.button(label='Recommend')

if submit_btn:
    similar_channels, scores = recommend(user_input)
    count = 0
    for i  in range(len(scores)):
        if scores[i] >= 0.1:
            count += 1
        else:
            break

    if count >= 1:
        # Limit count to 5
        count = min(count, 5)
        
        # Create columns dynamically
        cols = st.columns(count)
        
        # Iterate over similar channels
        for i, col in enumerate(cols):
            with col:
                st.image(f"{similar_channels[i][1]}", use_column_width=True)
                st.write(similar_channels[i][0])
                url = f"https://www.youtube.com/{similar_channels[i][2]}"
                # time.sleep(1)
                
                # Using html component to create button with CSS styling
                components.html(
                    f"""
                    <style>
                        .checkout-button {{
                            background-color: #4CAF50;
                            color: #fff;
                            padding: 10px 20px;
                            border: none;
                            border-radius: 5px;
                            cursor: pointer;
                        }}
                        
                        .checkout-button:hover {{
                            background-color: #3e8e41;
                        }}
                        
                        .checkout-button:active {{
                            transform: scale(0.9);
                        }}
                    </style>
                    
                    <a href="{url}" target="_blank">
                        <button class="checkout-button">Checkout</button>
                    </a>
                    """,
                    height=70,
                )
                        
    else:
        st.write("Sorry 😒 No similar Channel Found.")