## Project Members
Ada Mainetti, Kevin Warnakulasuriya, and Harry Zhao
## Title
Exploration of World War I Letters Through Text Mining

## Abstract
The first World War was among the most significant events of the 20th century. An important form of communication between soldiers and their loved ones were written letters, many of which have since been preserved and digitized. We aim to analyze such letters using text mining techniques to understand wartime experiences. 

## Research questions
**Main Research Question:**

How can we use computational methods to learn about lived experiences of World War I from transcribed letters?

**Secondary Research Questions:**

- What are the main topics written about in these letters? Can we identify them using topic modelling?
- What were the predominant sentiments of soldiers on the frontline and how did they change over time?
- How much can quantitative measures of the textual data inform us about letter-writing practices during the war?

## Repository Organization

There are 3 subfolders:

- [BERT Emotion Classifier](./bert_emotion_classifier/): contains the model used in the sentiment analysis.

- [Data](./data/): contains the raw and the data preprocessed in the general_stats notebook.

- [Gimmie](./gimmie/): contains the code used for web scraping during the data analysis process.

The code is organized into 3 main notebooks

- [General Statistics](./general_stats.ipynb): Preprocessing and preliminary data analysis.

- [Topic Modelling](./topicmodelling.ipynb): Topic Modelling.

- [Sentiment Analysis](./sentiment_analysis_final.ipynb): Sentiment Analysis.

Final Analysis and Data Visualization is in:

- [Final Report](./FinalReport.pdf)

- [Presentation](./ww1letterspresent.pptx)
