# Test plan

Unit tests mock the exchange-rate API (`app.rates.fetch_rate`) so they are fast and deterministic.
One live integration test (`tests/integration/test_rates_live.py`) calls the real API and runs only when `RATES_LIVE=1`, in the nightly CI job.
