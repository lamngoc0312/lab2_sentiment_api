# Sentiment Analysis API

## 1. Student Information

- **Full Name:** Lâm Như Ngọc
- **Student ID:** 25127214
- **Class:** 25C09
- **Course:** Computational Thinking
- **Assignment:** Lab 2 - API

## 2. Project Introduction

This project is a Sentiment Analysis API developed using FastAPI and a pretrained Hugging Face model.

The system accepts English text as input and predicts whether the sentiment is positive or negative.

The API returns the predicted sentiment label and a confidence score in JSON format.

## 3. Hugging Face Model

- **Model:** distilbert/distilbert-base-uncased-finetuned-sst-2-english
- **Model URL:** https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english
- **Task:** Text Classification / Sentiment Analysis
- **Output:** POSITIVE or NEGATIVE

The pretrained DistilBERT model is used through the Hugging Face Transformers library.

## 4. Technologies Used

- Python
- FastAPI
- Uvicorn
- Hugging Face Transformers
- PyTorch
- Requests
- Pydantic

## 5. Installation

Clone or download the repository and open the project directory.

Create a virtual environment:

```powershell
py -3.13 -m venv .venv
```

Install the required dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## 6. Running the Application

Start the FastAPI server:

```powershell
.\.venv\Scripts\python.exe -m uvicorn main:app --reload
```

Open the API documentation:

http://127.0.0.1:8000/docs

The Hugging Face model may need to be downloaded during the first run.

## 7. API Endpoints

### GET /

Returns information about the API and its available endpoints.

### GET /health

Checks whether the API service is running.

### POST /predict

Accepts English text and returns a sentiment prediction.

**Example 1: Positive Sentiment**

Request:

```json
{
  "text": "I love studying programming!"
}
```

Response:

```json
{
  "input": "I love studying programming!",
  "label": "POSITIVE",
  "score": 0.9994,
  "model": "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
}
```

**Example 2: Negative Sentiment**

Request:

```json
{
  "text": "This is the worst experience ever."
}
```

Response:

```json
{
  "input": "This is the worst experience ever.",
  "label": "NEGATIVE",
  "score": 0.9998,
  "model": "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
}
```

## 8. Input Validation and Error Handling

The API implements input validation and error handling.

- Missing text field: HTTP 422
- Empty or whitespace-only text: HTTP 422
- Valid text: HTTP 200
- AI model not ready: HTTP 503
- Model inference failure: HTTP 500

Input text must contain between 1 and 1000 characters.
Whitespace is removed from the beginning and end of the input.

## 9. Testing

The project includes test_api.py, which uses the
Python requests library to test the API.

The test cases include:

1. GET / - HTTP 200
2. GET /health - HTTP 200
3. POST /predict with positive text - HTTP 200
4. POST /predict with negative text - HTTP 200
5. POST /predict with missing input - HTTP 422
6. POST /predict with blank input - HTTP 422

The script checks HTTP status codes and displays
the returned JSON responses.

Run the tests:

    python test_api.py

Expected message:

    All API tests passed!

## 10. Demonstration Video

The demonstration video includes:
- Introduction to the Hugging Face DistilBERT model.
- Explanation of the project structure and source code.
- Running the FastAPI application.
- Testing the prediction endpoint with positive and negative inputs.
- Running automated API tests and explaining the results.

**Watch the demonstration video:** [https://youtu.be/avxg-eBgKro]