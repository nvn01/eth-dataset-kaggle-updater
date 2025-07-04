import os
import time
import pandas as pd
from datetime import datetime
from binance.client import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")

# Configure proxy settings (will be used for Binance API calls)
proxies = {
    'http': os.getenv('HTTP_PROXY'),
    'https': os.getenv('HTTPS_PROXY')
}

def create_binance_client(max_retries=3):
    """Create Binance client with retry logic."""
    local_proxies = {
        'http': os.getenv('HTTP_PROXY'),
        'https': os.getenv('HTTPS_PROXY')
    }
    
    for attempt in range(max_retries):
        try:
            client = Client(
                BINANCE_API_KEY, 
                BINANCE_API_SECRET,
                {
                    'proxies': local_proxies,
                    'timeout': 30,
                    'verify': True
                }
            )
            # Test the connection
            client.ping()
            print("Successfully connected to Binance API")
            return client
        except Exception as e:
            print(f"Attempt {attempt + 1}/{max_retries} failed: {str(e)}")
            if attempt < max_retries - 1:
                print("Waiting 10 seconds before retry...")
                time.sleep(10)
                if os.name != 'nt':  # Only restart tor on non-Windows systems
                    os.system('sudo service tor restart')
                    time.sleep(5)
            else:
                raise

def fetch_binance_data(symbol, interval, start_date, end_date, output_file, max_retries=3):
    """Fetch historical data from Binance with retry logic and new timestamp format."""
    for attempt in range(max_retries):
        try:
            client = create_binance_client()
            klines = client.get_historical_klines(symbol, interval, start_date, end_date)
            columns = [
                'Open time', 'Open', 'High', 'Low', 'Close', 'Volume',
                'Close time', 'Quote asset volume', 'Number of trades',
                'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore'
            ]
            df = pd.DataFrame(klines, columns=columns)
            
            # Convert timestamps to UTC datetime explicitly (NEW FORMAT)
            df['Open time'] = pd.to_datetime(df['Open time'], unit='ms', utc=True)
            df['Close time'] = pd.to_datetime(df['Close time'], unit='ms', utc=True)
            
            # Convert to string format with explicit UTC designation for clarity
            df['Open time'] = df['Open time'].dt.strftime('%Y-%m-%d %H:%M:%S.%f UTC')[:-3]  # Remove last 3 digits for milliseconds
            df['Close time'] = df['Close time'].dt.strftime('%Y-%m-%d %H:%M:%S.%f UTC')[:-3]
            
            df.to_csv(output_file, index=False)
            print(f"Fetched data saved to {output_file}")
            return
        except Exception as e:
            print(f"Attempt {attempt + 1}/{max_retries} failed: {str(e)}")
            if attempt < max_retries - 1:
                print("Waiting 20 seconds before retry...")
                time.sleep(20)
                if os.name != 'nt':  # Only restart tor on non-Windows systems
                    os.system('sudo service tor restart')
                    time.sleep(5)
            else:
                raise

def main():
    """Fetch new format Ethereum data for all timeframes."""
    # Create output directory
    output_dir = "ethereum_new_format_data"
    os.makedirs(output_dir, exist_ok=True)
    
    # Fetch complete historical data with new format
    start_date = "2017-08-17"  # Ethereum started trading on Binance
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    timeframes = {
        "15m": Client.KLINE_INTERVAL_15MINUTE,
        "1h": Client.KLINE_INTERVAL_1HOUR,
        "4h": Client.KLINE_INTERVAL_4HOUR,
        "1d": Client.KLINE_INTERVAL_1DAY
    }

    print(f"Fetching Ethereum data from {start_date} to {end_date}")
    print("This will take some time as we're fetching complete historical data...")
    
    for tf_name, tf_interval in timeframes.items():
        output_file = os.path.join(output_dir, f"eth_{tf_name}_data_2017_to_2025.csv")
        print(f"\nFetching {tf_name} data...")
        fetch_binance_data("ETHUSDT", tf_interval, start_date, end_date, output_file)
        print(f"Completed {tf_name} data fetch")

    print(f"\nAll data fetched successfully!")
    print(f"Files saved in: {output_dir}")
    print("\nYou can now upload these files to Kaggle to update your dataset with the new timestamp format.")

if __name__ == "__main__":
    main() 