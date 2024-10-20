import pandas as pd
import os
import random

# File paths
affiliation_file = 'affiliation-categories.csv'  # Path to the affiliation file
directory = 'arsondata-fulltimeline'  # Path to the directory containing the CSV files

# Load the affiliation data
affiliation_data = pd.read_csv(affiliation_file)

# Filter the rows for opposers and supporters
opposer_accounts = affiliation_data[affiliation_data['Category'] == 'Opposer']['ID'].tolist()
supporter_accounts = affiliation_data[affiliation_data['Category'] == 'Supporter']['ID'].tolist()

# Initialize lists to store selected tweets for opposers and supporters
opposer_tweets = []
supporter_tweets = []

# Shuffle the opposer and supporter accounts to pick them randomly
random.shuffle(opposer_accounts)
random.shuffle(supporter_accounts)

# Helper function to collect tweets
def collect_tweets(account_list, tweet_list, max_tweets=30):
    for account_number in account_list:
        account_file = os.path.join(directory, f"{account_number}.csv")
        
        if os.path.exists(account_file):
            # Load the tweets from the file
            tweets_data = pd.read_csv(account_file)
            
            # Find tweets containing #ArsonEmergency
            matching_tweets = tweets_data[tweets_data['created_at'].str.contains('#ArsonEmergency', case=False, na=False)]

            # Record up to 30 tweets from this account
            for tweet in matching_tweets['created_at'].head(max_tweets):
                tweet_list.append({
                    'account_number': account_number,
                    'tweet': tweet
                })
                
                if len(tweet_list) >= max_tweets:
                    break
        if len(tweet_list) >= max_tweets:
            break

# Collect tweets for opposers
collect_tweets(opposer_accounts, opposer_tweets, max_tweets=30)

# Collect tweets for supporters
collect_tweets(supporter_accounts, supporter_tweets, max_tweets=30)

# Create DataFrames from the selected tweets
opposer_seed_data = pd.DataFrame(opposer_tweets)
supporter_seed_data = pd.DataFrame(supporter_tweets)

# Save the seed data to new CSV files
opposer_seed_data.to_csv('opposer_seed_data.csv', index=False)
supporter_seed_data.to_csv('supporter_seed_data.csv', index=False)

print("Opposer seed data saved to 'opposer_seed_data.csv'.")
print("Supporter seed data saved to 'supporter_seed_data.csv'.")
