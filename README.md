# FreeKassa - Api

## Intallation

```json
pip install freekassa
```

## Usage

### Generate link payment

```python
merchant = Merchant(shop_id=123456789,
                    secret1="secret1",
                    secret2="secret2",
                    api_key="api_key")
payment_link = merchant.get_payment_form_url(amount=100, order_id="Product 1", us_={'token':'token1',"token2":"token2"})
```

### Check balance

```python
balance = merchant.get_balance()
```