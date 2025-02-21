# Sentiment Analysis API  
![Demo](https://user-images.githubusercontent.com/57702598/90991088-264c8880-e56c-11ea-9895-90029d3c2139.gif)  

## Overview  
This project is a **Sentiment Analysis API** that takes user input text and predicts its sentiment using **Hugging Face Hub**. It is built with **FastAPI** for the backend and deployed on **Koyeb**.  

## Technologies Used  
- **FastAPI** – Backend framework  
- **Hugging Face Hub** – Sentiment analysis model  
- **Koyeb** – Deployment platform  

## Installation and Setup  
### 1. Clone the Repository  
```bash
git clone https://github.com/your-username/sentiment-analysis-api.git
cd sentiment-analysis-api
```

### 2. Create a Virtual Environment (Optional but Recommended)  
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables  
Create a `.env` file and add your **Hugging Face API Token**:  
```
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token_here
```

### 5. Run the FastAPI Server  
```bash
uvicorn main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

## API Usage  
### **Endpoint:**  
`POST /analyze_sentiment/`  

### **Request Body:**  
```json
{
    "text": "I love this product!"
}
```

### **Response:**  
```json
{
    "text": "I love this product!",
    "sentiment": "5 stars"
}
```

## Frontend  
A simple HTML frontend is provided in `index.html`, which sends a request to the API and displays the sentiment result.

## Deployment on Koyeb  
The API is deployed on **Koyeb**, a serverless platform for easy deployment. Steps to deploy:  
1. Create a new service on **Koyeb**.  
2. Connect your GitHub repository.  
3. Set environment variables in **Koyeb**.  
4. Deploy and get the API URL.

---

🚀 **Enjoy building with FastAPI and Hugging Face!**  
