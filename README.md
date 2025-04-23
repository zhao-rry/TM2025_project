## Project Members
Ada Mainetti, Kevin Warnakulasuriya, and Harry Zhao
## Title
Analysis of World War I Letters
## Abstract
Our project focuses on applying text mining techniques to analyse a collection of transcribed letters sent during the First World War, between 1914 and 1918. By doing so, we hope to discover if the events of the war could be reflected in the contents and sentiments of these letters sent to and from the frontline. To do so, we approach this task using three different frameworks: sentiment analysis, topic modelling, and quantitative analysis.

## Research questions
**Main Research Question:**

How can we use computational methods to learn about lived experiences of World War I from transcribed letters?

**Secondary Research Questions:**

- What are the main topics written about in these letters? Can we identify them using topic modelling?
- What were the predominant sentiments of soldiers on the frontline and how did they change over time?
- How much can quantitative measures of the textual data inform us about letter-writing practices during the war?

## Dataset
We obtained 60 transcribed letters from a public dataset hosted on kaggle.com at [this link](https://www.kaggle.com/datasets/anthaus/world-war-i-letters). This repository contains a JSON file of letters in both English and French. Other relevant metadata, such as the year and place of writing, being stored in a separate CSV file.

To supplement our dataset, we manually inserted 32 more letters taken from the [UK National Archives](https://www.nationalarchives.gov.uk/education/resources/letters-first-world-war-1915) into the original JSON file. This gives us a total of roughly 90 letters, each with roughly two pages of text.

## Timeline
By April 25
- Read related literature
- Preprocessing
    - Downloaded and merging datasets from Kaggle and the National Archives
    - Normalization and Lemmatization
    - (maybe) PoS Tagging
- Selecting what models to use

By May 9
- Preprocessing
- Apply pretrained sentiment analysis
- Have at least one model trained
- Refine secondary research questions
- Refine hyperparameters

By May 23
- Extras
    - Extract more letters from other wars, run same processing steps and compare results
- Qualitative analysis
- Finish paper
- Finish presentation

## Documentation
TBD
