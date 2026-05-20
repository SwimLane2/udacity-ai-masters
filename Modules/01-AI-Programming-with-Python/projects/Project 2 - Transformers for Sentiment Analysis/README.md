# Project 2 – Transformers for Movie Review Sentiment Analysis

## Overview
In this project, I built a sentiment analysis model using a transformer-based architecture to classify IMDB movie reviews as positive or negative. The goal of the project was to understand how transformers can be adapted for classification tasks and to train a model that achieves good performance on unseen data.

---------------------------------------------------------------------------------------------------

## Dataset
The IMDB movie review dataset was used for this project. It consists of:
- 25,000 training reviews
- 25,000 test reviews
- Binary labels:
  - 1 = Positive review
  - 0 = Negative review

The dataset was loaded from raw text files and converted into Pandas DataFrames for easier handling.

-----------------------------------------------------------------------------------------------------

## Approach

### 1. Data Loading and Exploration
- Loaded raw text reviews from folder structure
- Created training, validation, and test splits
- Explored label distribution and review lengths

### 2. Tokenization
- Used Hugging Face’s `bert-base-uncased` tokenizer
- Applied subword tokenization
- Padded and truncated reviews to a fixed length

### 3. Dataset and DataLoader
- Implemented a custom PyTorch `Dataset` class
- Used PyTorch `DataLoader` for batching and shuffling
- Ensured correct tensor shapes for training

### 4. Model Architecture
- Built a custom transformer model from scratch
- Included:
  - Token embeddings
  - Positional embeddings
  - Multi-head self-attention
  - Feed-forward layers
- Added a classification head for binary sentiment prediction

### 5. Training and Evaluation
- Used Cross Entropy Loss
- Optimized using AdamW
- Trained the model for multiple epochs
- Monitored validation accuracy during training

### 6. Testing and Inference
- Evaluated the trained model on the test dataset
- Achieved over **75% accuracy** on unseen test data
- Implemented a simple inference function to predict sentiment for new reviews

## Results
- Test Accuracy: **>75%**
- Model performance improved with additional training epochs
---

## Example Inference
```python
sample_reviews = [
    "This movie was amazing and I really enjoyed it.",
    "The movie was boring and a complete waste of time."
]

predictions = predict_sentiment(sample_reviews, model, tokenizer, device)
# Output: [1, 0]
```

