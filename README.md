# lambda-code-executor

下記言語のプログラムを実行し、結果を返すAPI
- Python
- Racket

### Python
```bash
curl -X POST https://<API-GatewayID>.execute-api.ap-northeast-1.amazonaws.com/exec/python \
  -H "Content-Type: application/json" \
  -d '{
    "code_def": "def square(x):\n  return x * x",
    "code_call": "square(5)"
  }'
```

### Racket
```bash
curl -X POST https://<API-GatewayID>.execute-api.ap-northeast-1.amazonaws.com/exec/racket \
  -H "Content-Type: application/json" \
  -d '{
    "code_def": "(define (square x) (* x x))",
    "code_call": "(square 5)"
  }'
```
  
