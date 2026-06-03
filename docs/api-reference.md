# Api Reference


### Rate Limiting (2026-06-04)

- 429 responses should trigger exponential backoff starting at 1s
- Max 5 retries before surfacing error to caller
- Idempotency keys required on all POST /transactions calls
