# Ethereum Dataset Kaggle Auto Updater

This project automatically updates Ethereum historical datasets on Kaggle using data from the Binance API.

## Features

- **Automated Data Fetching**: Fetches latest Ethereum (ETH/USDT) data from Binance
- **Multiple Timeframes**: Supports 15m, 1h, 4h, and 1d intervals
- **Kaggle Integration**: Automatically uploads updated datasets to Kaggle
- **GitHub Actions**: Runs daily via GitHub Actions workflow
- **Retry Logic**: Built-in retry mechanisms for robust operation
- **Proxy Support**: Uses Tor proxy for reliable API access

## Setup

### Prerequisites

- Python 3.10+
- Poetry for dependency management
- Kaggle API credentials
- Binance API credentials

### Installation

1. Clone the repository
2. Install dependencies with Poetry:
      ```bash
      poetry install
      ```

### Configuration

Create a `.env` file in the project root with:

```env
KAGGLE_USERNAME=your_kaggle_username
KAGGLE_KEY=your_kaggle_api_key
BINANCE_API_KEY=your_binance_api_key
BINANCE_API_SECRET=your_binance_api_secret
```

### GitHub Secrets

For GitHub Actions to work, add the following secrets to your repository:

- `KAGGLE_USERNAME`
- `KAGGLE_KEY`
- `BINANCE_API_KEY`
- `BINANCE_API_SECRET`

## Usage

### Local Testing

```bash
poetry run python ethereum_dataset_kaggle_auto_updater/kaggle_update_ethereum.py
```

### GitHub Actions

The workflow runs automatically every day at midnight UTC. You can also trigger it manually from the Actions tab.

## Dataset Structure

The dataset includes the following timeframes:

- `eth_15m_data_2020_to_2025.csv` - 15-minute intervals
- `eth_1h_data_2020_to_2025.csv` - 1-hour intervals
- `eth_4h_data_2020_to_2025.csv` - 4-hour intervals
- `eth_1d_data_2020_to_2025.csv` - Daily intervals

Each file contains:

- Open time
- Open, High, Low, Close prices
- Volume
- Quote asset volume
- Number of trades
- Taker buy volumes

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.
