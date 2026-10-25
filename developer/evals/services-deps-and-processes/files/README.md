# Shop services

Two small services. `inventory` listens on 8101 and `orders` on 8102.
`GET /stock/<item>` on inventory returns stock. `POST /order/<item>` on orders returns 200 if the item is in stock, else 409.
