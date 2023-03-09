def lambda_handler(event, context):
    main()


def main():
    pass


if __name__ == "__main__":
    main()

"""
pip install -t dist/lambda .
cd dist/lambda
zip -x '*.pyc' -r ../lambda.zip .
https://binx.io/2022/05/23/poetry-lambda/
"""
