# draft
resource "aws_lambda_function" "my_function" {
  filename      = "lambda_function.zip"
  function_name = "my-function"
  role          = "arn:aws:iam::123456789012:role/my-role"
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.8"
}
