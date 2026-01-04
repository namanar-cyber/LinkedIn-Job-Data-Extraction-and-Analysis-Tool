LinkedIn Job Scraper
🎯 Project Title
LinkedIn Job Data Extraction and Analysis Tool

📝 Description
A robust Python-based web scraping tool that automatically extracts job listings from LinkedIn. This tool is specifically designed to gather program management and related positions in Delhi, India, with built-in error handling, retry mechanisms, and data formatting capabilities.

✨ Key Features
Automated scraping of LinkedIn job postings
Intelligent retry mechanism with exponential backoff
Multiple search term support for comprehensive results
Clean data formatting and structure
CSV export with timestamp-based naming
Duplicate removal and result limitation
Detailed error handling and user feedback
🛠️ Technologies Used
Python 3.x
pandas
jobspy
csv
datetime

📋 Prerequisites
pip install pandas jobspy
🚀 Installation & Setup
Clone the repository
git clone https://github.com/yourusername/linkedin-job-scraper.git
cd linkedin-job-scraper
Install required packages
pip install -r requirements.txt
💻 Usage
Run the script using:

python job_scraper.py
📊 Output
The script generates a CSV file with the following information:

Job site
Job title
Company name
City
State
Job type
Salary interval
Minimum salary
Maximum salary
Job URL
Job description
🔄 Process Flow
Initial scraping attempt for Program Manager positions
Fallback to alternative search terms if needed
Data cleaning and formatting
Removal of duplicates
Export to CSV with timestamp
⚠️ Error Handling
Multiple retry attempts for failed scraping
Random delays between attempts
Comprehensive error messages and suggestions
VPN usage recommendations
📝 requirements.txt
pandas>=1.3.0
jobspy>=1.0.0

👤 Developer
Your Name : Naman Arora
Linkedin : https://www.linkedin.com/in/naman-arora-94b17b154/


GitHub: @yourusername
LinkedIn: Your Name
