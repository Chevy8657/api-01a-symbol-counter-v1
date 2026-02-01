# Symbol Counter

Single-purpose API. Stateless. Deterministic. Returns JSON only.

## Endpoints
- GET `/health`
- GET `/v1/symbol-count?text=`

## Example

Request:
`/v1/symbol-count?text=Hello%20%40%23%24World%21`

Response:
```json
{
  "input": "Hello @#$World!",
  "symbol_count": 4
}
