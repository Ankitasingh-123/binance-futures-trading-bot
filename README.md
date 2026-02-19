# Binance Futures Testnet Trading Bot

## Setup

1. Create and activate virtual environment
2. Install dependencies:
   pip install -r requirements.txt
3. Add your Binance Testnet API keys inside cli.py

## Run Examples

Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 70000

## Assumptions

- Minimum notional $100 enforced by Binance
- Using Binance Futures Testnet

## Features
- Market and Limit order support
- CLI-based trading
- Input validation & error handling
- Logging to `bot.log`
