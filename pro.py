import csv
import pandas as pd
from jobspy import scrape_jobs
from datetime import datetime
import time
import random

def attempt_scraping(attempts=3):
    for attempt in range(attempts):
        try:
            if attempt > 0:
                time.sleep(random.uniform(5, 10))
            
            print(f"Attempt {attempt + 1} for LinkedIn scraping...")
            
            return scrape_jobs(
                site_name=["linkedin"],
                search_term="Program Manager",
                location="Delhi, IN",
                results_wanted=50
            )
        except Exception as e:
            if attempt == attempts - 1:
                raise e
            print(f"Attempt {attempt + 1} failed: {str(e)}. Retrying...")
            time.sleep(random.uniform(10, 15))
            continue

def format_dataframe(df):
    """Format the dataframe to match the desired structure"""
    # Define the desired columns and their order
    desired_columns = [
        'site',
        'title',
        'company',
        'city',
        'state',
        'job_type',
        'interval',
        'min_amount',
        'max_amount',
        'job_url',
        'description'
    ]

    # Create new columns if they don't exist
    for col in desired_columns:
        if col not in df.columns:
            df[col] = None

    # Extract city and state from location if possible
    if 'location' in df.columns:
        df[['city', 'state']] = df['location'].str.extract(r'(.*?),\s*(.+)$')

    # Ensure all columns are present and in the right order
    df = df[desired_columns]

    return df

def main():
    try:
        print("\nStarting LinkedIn job scraping...")
        
        # First attempt
        jobs = attempt_scraping()
        
        # If we don't get enough results, try with alternative search terms
        alternative_terms = ["Program Manager", "Assistant Manager", "Senior Subject Matter"]

        for term in alternative_terms:
            if len(jobs) < 20:
                print(f"\nTrying with alternative search term: {term}")
                time.sleep(5)
                new_jobs = scrape_jobs(
                    site_name=["linkedin"],
                    search_term=term,
                    location="Delhi, IN",
                    results_wanted=50
                )
                jobs = pd.concat([jobs, new_jobs], ignore_index=True)
                jobs = jobs.drop_duplicates(subset=['job_url'])

        if not jobs.empty:
            # Format the dataframe
            jobs = format_dataframe(jobs)
            
            # Sort by date if available
            if 'date_posted' in jobs.columns:
                jobs = jobs.sort_values('date_posted', ascending=False)
            
            # Take the first 20 jobs
            jobs = jobs.head(20)

            # Generate timestamp for filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            # Save to CSV with specific formatting
            csv_filename = f"job_listings_{timestamp}.csv"
            jobs.to_csv(csv_filename, 
                       quoting=csv.QUOTE_NONNUMERIC, 
                       escapechar="\\", 
                       index=False,
                       encoding='utf-8')
            
            print(f"\nFound {len(jobs)} jobs")
            print(f"Data saved to {csv_filename}")

            # Display formatted results
            pd.set_option('display.max_columns', None)
            pd.set_option('display.width', None)
            pd.set_option('display.max_colwidth', None)
            print("\nJob Listings Preview:")
            print(jobs.to_string())

    except Exception as e:
        print("\nError occurred during scraping.")
        print(f"Error details: {str(e)}")
        print("\nSuggestions:")
        print("1. Try using a VPN service")
        print("2. Wait for a few minutes before trying again")
        print("3. Check your internet connection")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nMain program error: {str(e)}")
    finally:
        print("\nScript execution completed")
