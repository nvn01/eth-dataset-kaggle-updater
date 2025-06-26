# Ethereum Dataset Kaggle Auto Updater

An automated Python script that fetches Ethereum (ETH/USDT) historical price data from the Binance API and updates a Kaggle dataset daily. This project ensures that the Ethereum price dataset stays current with the latest market data.

## Features

- **Automated Daily Updates**: GitHub Actions workflow runs every day at midnight (UTC)
- **Multiple Timeframes**: Supports 15-minute, 1-hour, 4-hour, and daily intervals
- **Data Merging**: Automatically merges new data with existing historical data
- **Error Handling**: Robust retry mechanisms and proxy support for stability
- **Kaggle Integration**: Seamlessly uploads updated datasets to Kaggle

### GitHub Actions

The project includes a GitHub Actions workflow that:

- Runs automatically every day at midnight (UTC)
- Updates the Kaggle dataset at https://www.kaggle.com/datasets/novandraanugrah/ethereum-price-data-binance-api-2017now
- Uses proxy configuration (Tor + Privoxy) for enhanced stability
- Includes retry mechanisms for handling API failures

## Dataset Structure

The script maintains four CSV files with different timeframes:

- `eth_15m_data_2017_to_2025.csv` (15-minute intervals)
- `eth_1h_data_2017_to_2025.csv` (1-hour intervals)
- `eth_4h_data_2017_to_2025.csv` (4-hour intervals)
- `eth_1d_data_2017_to_2025.csv` (daily intervals)

Each file contains the following columns:

- Open time
- Open
- High
- Low
- Close
- Volume
- Close time
- Quote asset volume
- Number of trades
- Taker buy base asset volume
- Taker buy quote asset volume

## Installation

### Prerequisites

- Python 3.10+
- Poetry (for dependency management)
- Binance API credentials
- Kaggle API credentials

### Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd eth-dataset-kaggle-updater
```

2. Install dependencies using Poetry:

```bash
poetry install
```

3. Create a `.env` file in the root directory with your credentials:

```env
BINANCE_API_KEY=your_binance_api_key
BINANCE_API_SECRET=your_binance_api_secret
KAGGLE_USERNAME=your_kaggle_username
KAGGLE_KEY=your_kaggle_api_key
```

## Usage

### Manual Execution

To run the updater manually:

```bash
poetry run python ethereum_dataset_kaggle_auto_updater/kaggle_update_ethereum.py
```

### Fetch Full Historical Data

To fetch complete historical data from the beginning:

```bash
python fetch_full_eth_data.py
```

### GitHub Actions Setup

For automated execution, set up the following secrets in your GitHub repository:

- `BINANCE_API_KEY`: Your Binance API key
- `BINANCE_API_SECRET`: Your Binance API secret
- `KAGGLE_USERNAME`: Your Kaggle username
- `KAGGLE_KEY`: Your Kaggle API key

## Project Structure

```
eth-dataset-kaggle-updater/
├── ethereum_dataset_kaggle_auto_updater/
│   ├── data/                    # Downloaded Kaggle dataset
│   ├── new_data/               # Newly fetched data from Binance
│   ├── merged_data/            # Merged datasets for upload
│   └── kaggle_update_ethereum.py
├── .github/workflows/
│   └── main.yml                # GitHub Actions workflow
├── fetch_full_eth_data.py      # Script to fetch complete historical data
├── poetry.lock
├── pyproject.toml
└── README.md
```

## How It Works

1. **Download Current Dataset**: Downloads the existing dataset from Kaggle
2. **Fetch New Data**: Retrieves the latest Ethereum price data from Binance API
3. **Merge Data**: Combines new data with existing historical data, removing duplicates
4. **Upload to Kaggle**: Updates the Kaggle dataset with the merged data
5. **Cleanup**: Removes temporary files after successful upload

## Error Handling

The script includes comprehensive error handling:

- **Retry Logic**: Automatic retries for failed API calls
- **Proxy Support**: Uses Tor and Privoxy for enhanced connection stability
- **Connection Testing**: Validates API connections before data fetching
- **Global Retry Loop**: Attempts the entire process multiple times if needed

## Data Coverage

- **Start Date**: August 17, 2017 (ETH/USDT pair launch on Binance)
- **End Date**: Current date (updated daily)
- **Update Frequency**: Daily at midnight UTC
- **Data Source**: Binance API

## Dependencies

Key Python packages used:

- `binance-connector`: For Binance API integration
- `kaggle`: For Kaggle dataset operations
- `pandas`: For data manipulation
- `python-dotenv`: For environment variable management

## License

This project is licensed under the CC BY 4.0 License - see the dataset metadata for details.

## Acknowledgments

- Binance for providing the cryptocurrency data API
- Kaggle for hosting the dataset platform
- The open-source community for the tools and libraries used

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please open an issue in the GitHub repository.
