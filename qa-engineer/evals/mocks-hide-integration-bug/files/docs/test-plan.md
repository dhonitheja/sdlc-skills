# Test plan

Unit tests mock the exchange-rate API (`app.rates.fetch_rate`) so they are fast and deterministic.

One live integration test (`tests/integration/test_rates_live.py`) calls the rates service over HTTP and runs only when `RATES_LIVE=1`. In CI and locally it targets the stand-in service in `stub/rates_server.py` (port 8201), whose response contract is documented in `stub/README.md`. The nightly job points `RATES_BASE_URL` at the vendor's sandbox instead.
