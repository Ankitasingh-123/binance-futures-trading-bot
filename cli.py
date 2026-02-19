import argparse
import logging
from bot.client import BinanceFuturesClient
from bot.orders import place_market_order, place_limit_order
from bot.validators import *
from bot.logging_config import setup_logging
from binance.exceptions import BinanceAPIException

API_KEY = "jcQUjDqO06q3oIrFuyvJAKgkIT8Dqd1ChhXlFUfctlqFXC22FinOPnKHwCl4iwzP"
API_SECRET = "N2GDQCnvX8vePUTWa7kuYGoVFxTUEGIiRrQwWxy1pPB02oNRUXVtYZTT1RCMbWmC"


def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)
        validate_price(args.type, args.price)

        client_wrapper = BinanceFuturesClient(API_KEY, API_SECRET)
        client = client_wrapper.get_client()

        print("\n--- Order Request Summary ---")
        print(vars(args))

        if args.type == "MARKET":
            order = place_market_order(client, args.symbol, args.side, args.quantity)
        else:
            order = place_limit_order(client, args.symbol, args.side, args.quantity, args.price)

        print("\n--- Order Response ---")
        print(f"Order ID: {order.get('orderId')}")
        print(f"Status: {order.get('status')}")
        print(f"Executed Qty: {order.get('executedQty')}")
        print(f"Avg Price: {order.get('avgPrice')}")

        print("\n✅ Order placed successfully!")

    except ValueError as ve:
        logging.error(str(ve))
        print(f"\n❌ Input Error: {ve}")

    except BinanceAPIException as be:
        logging.error(str(be))
        print(f"\n❌ Binance API Error: {be}")

    except Exception as e:
        logging.error(str(e))
        print(f"\n❌ Unexpected Error: {e}")


if __name__ == "__main__":
    main()
