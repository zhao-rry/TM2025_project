## Project Members
Ada Mainetti, Kevin Warnakulasuriya, and Harry Zhao
## Title
Child Speech Age Prediction
## Abstract
Our project focuses on predicting a child’s age based on a snippet of transcribed speech. First Language Acquisition is topical in our understanding of language, and we wish to use Text Mining to attempt to find patterns in speech development. Our research focuses on English transcripts of children in North America and the UK between the ages of 2-15 taken from the CHILDES database. 
## Research questions
** Main Research Question: **

How accurately can you predict a child’s age based on their speech?

** Secondary Research Questions: **

- What ages, if any, have the most identifiable speech patterns? What do they consist of?
- Are there English Language mistakes often made by a certain age category?
- What quantifiable characteristics can be seen develop as a child ages? E.g., vocabulary size, average sentence length
- How much of a child’s conversation is necessary to reasonably accurately judge their age?

## Dataset
We plan to source most of our data from the publicly available CHILDES database, which contains multiple corpora of transcribed children's and caretakers' speech in various languages. We will combine these corpora into a larger dataset in order to have enough samples to work with for our predictive model, as they individually only contain transcripts from a handful for children. Additionally, most of the dialogues are spoken by adults, which we are not interested in, so we will need to get as much raw data as possible.
From our initial survey of the data, they do not have a standard way of transcribing information, meaning that we will have to extract and standardise the information during our preprocessing step. We will need to find a method for processing extra-verbal symbols (such as tags, intonation markers, pauses, etc.) or eliminating them.

## Timeline
By April 25
- Read related literature
- Preprocessing:
- Downloaded and merging all the data from CHILDES
- Extracting the child’s speech and labelling conversations by child’s age
- Normalization and Lemmatization
- (maybe) PoS Tagging
- Models
- Selecting what models to use

By May 9
- Preprocessing 2:
- Vectorizing the data
- N-gram splits
- Have at least one model trained
- Refine secondary research questions
- Refine hyperparameters

By May 23
- Evaluate the model and evaluate the model’s functioning
- Finish paper 
- Finish presentation

## Documentation
TBD
