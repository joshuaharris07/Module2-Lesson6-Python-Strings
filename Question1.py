# Product Review Analysis

# Task 1: Keyword Highlighter

# Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average". 
# We want you to capitalize those keywords then print out each review. 
# Print out each review with the keywords in uppercase so they stand out.
#     reviews = [
#         "This product is really good. I'm impressed with its quality.",
#         "The performance of this product is excellent. Highly recommended!",
#         "I had a bad experience with this product. It didn't meet my expectations.",
#         "Poor quality product. Wouldn't recommend it to anyone.",
#         "The product was average. Nothing extraordinary about it."
#     ]

# So for the first string in the reviews list, we want it to say: "This product is really GOOD. I'm impressed with its quality."

def check_reviews(reviews):
    keywords = ["good", "excellent", "bad", "poor", "average"]
    for review in reviews:
        new_review = review.split()
        i = -1
        for word in new_review:
            i += 1
            for keyword in keywords:
                if word[0:len(keyword)] == keyword:
                    word = word.upper()
                    new_review[i] = word.upper()
        print(" ".join(new_review))

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

check_reviews(reviews)


# Task 2: Sentiment Tally

# Develop a function that tallies the number of positive and negative words in each review.  
# The function should return the total count of positive and negative words.
#     positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
#     negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def check_reviews(reviews):
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    neutral_words = ["average", "mediocre", "okay"]
    keywords = positive_words + negative_words + neutral_words
    negative_word_count = 0
    positive_word_count = 0
    print(keywords)
    for review in reviews:
        new_review = review.split()
        i = -1
        for word in new_review:
            i += 1
            for keyword in keywords:
                if word[0:len(keyword)].lower() == keyword:
                    word = word.upper()
                    new_review[i] = word.upper()
                    if word[0:len(keyword)].lower() in positive_words:
                        positive_word_count += 1
                    elif word[0:len(keyword)].lower() in negative_words:
                        negative_word_count += 1
        print(" ".join(new_review))
    print(f"Total positive sentiments: {positive_word_count}")
    print(f"Total negative sentiments: {negative_word_count}")

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

check_reviews(reviews)


# Task 3: Review Summary

# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. 
# Ensure that the summary does not cut off in the middle of a word.

# Example: "This product is really good. I'm...",

def review_summary(reviews):
    for review in reviews:
        cutoff = 30
        while review[cutoff] != " ":
            cutoff += 1
        print(review[0:cutoff] + "...")

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

review_summary(reviews)