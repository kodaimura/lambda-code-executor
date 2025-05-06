import json
import uuid
import os
import subprocess

def lambda_handler(event, context):
    body = json.loads(event["body"])
    code_def = body["code_def"]
    code_call = body["code_call"]
    
    file_id = str(uuid.uuid4())
    code_path = f"/tmp/{file_id}.py"

    try:
        with open(code_path, "w") as f:
            f.write(code_def + "\n")
            f.write(f"__result__ = {code_call}\n")
            f.write("print(__result__, end='')\n")

        result = subprocess.run(
            ["python3", code_path],
            capture_output=True,
            text=True,
            timeout=5
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                "output": result.stdout,
                "error": result.stderr
            })
        }

    except subprocess.TimeoutExpired:
        return {
            'statusCode': 408,
            'body': json.dumps({"error": "Execution timed out"})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)})
        }

    finally:
        if os.path.exists(code_path):
            os.remove(code_path)
