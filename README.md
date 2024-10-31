# YouTube Channel Recommendation System


A content-based recommendation system built using Python, Streamlit, and scikit-learn.

<img src="images/youtube recommendation.png" alt="YouTube Channel Recommender System" width="600">

## Live Demo

👉 [Live Demo](https://youtube-channel-recommendation.streamlit.app/)

## Table of Contents
-----------------

1. [Overview](#overview)
2. [Features](#features)
3. [Technical Requirements](#technical-requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Dataset](#dataset)
7. [Model](#model)
8. [Deployment](#deployment)
9. [Contributing](#contributing)
10. [License](#license)
11. [Challenges/Limitations](#challenges-limitations)


## Overview
------------

This project aims to develop a content-based YouTube channel recommendation system. The system uses natural language processing (NLP) techniques to analyze channel descriptions and recommend similar channels.


## Features
------------

* Content-based filtering using CountVectorizer
* Cosine similarity calculation for recommendation
* Streamlit application for user-friendly interface
* Deployment on Streamlit Cloud


## Technical Requirements
----------------------

* Python 3.8+
* scikit-learn
* Streamlit
* Pandas
* NumPy
* Pickle


## Installation
------------

1. Clone the repository: `git clone https://github.com/Debopam-Pritam2014/youtube-channel-recommendation.git`
2. Create Virtual Environment: `conda create venv python==3.10 -y`
3. Install required libraries: `pip install -r requirements.txt`
4. Run the application: `streamlit run app.py`


## Usage
-----

1. Open the Streamlit application
2. Select a YouTube channel name
3. Click "Recommend" to get similar channel suggestions


## Dataset
---------

* Collected from Kaggle
* Preprocessed and cleaned for analysis


## Model
------

* CountVectorizer for text vectorization
* Cosine similarity calculation for recommendation


## Deployment
-------------

* Deployed on Streamlit Cloud


## Contributing
------------

Contributions are welcome! Please fork the repository, make changes, and submit a pull request.


## License
-------

MIT License

Copyright (c) 2023 Debopam Dey(Pritam)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:


The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.


THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## Challenges/Limitations
----------------------

### 1. Memory Issues

Calculating the similarity matrix for a large dataset resulted in memory issues. To mitigate this, only Indian YouTube channels were included in the dataset.

### 2. Large Similarity Matrix

The similarity matrix size became approximately 2GB, which posed storage and computation challenges. To address this, a dictionary was created where:

* Keys: Channel indices
* Values: Similar channel indices and similarity scores

This optimization reduced storage requirements and improved computation efficiency.


Future improvements will focus on:


* Scaling the model to accommodate larger datasets
* Exploring alternative similarity calculation methods
* Integrating additional features (e.g., video content analysis)