# Rates stand-in service

`python stub/rates_server.py` serves on 127.0.0.1:8201 (override with `STUB_PORT`).

`GET /v1/<CUR>` returns JSON:

```json
{"data": {"currency": "EUR", "rate": 2.0}}
```

This mirrors the vendor's documented response shape. It is a local stand-in, not the vendor's real service.
