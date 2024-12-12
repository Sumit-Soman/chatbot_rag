
# E-Commerce Chatbot Project

## Overview
This project is an advanced Retrieval-Augmented Generation (RAG)-based chatbot designed for e-commerce. The chatbot utilizes LangChain's vector stores and OpenAI's GPT models to provide accurate, context-aware responses to customer queries using a predefined set of prompts stored in `prompts.txt`.

### Features
- **RAG Integration**: Combines prompt-based retrieval with GPT-based generative responses for enhanced accuracy.
- **Customizable Prompts**: Accepts input prompts from `prompts.txt` for tailored query handling.
- **Comprehensive Testing**: Includes test cases to validate functionality, response quality, and performance.
- **Detailed HTML Report**: Generates `report.html`, summarizing execution metrics, response timings, and test outcomes.

## Setup and Usage

### Prerequisites
- Python 3.9 or later
- OpenAI API key
- Required Python packages:
  ```bash
  pip install -r requirements.txt
  ```

### Environment Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Set up your environment:
   ```bash
   python -m venv chatbot_env
   source chatbot_env/bin/activate  # On Windows: chatbot_env\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Add your OpenAI API key in a `.env` file:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

### Running the Chatbot
1. Ensure your prompts are placed in `data/prompts.txt`.
2. Run the chatbot:
   ```bash
   python chatbot.py
   ```

### Running Tests
To execute tests to validate Chatbot and generate the HTML report:
```bash
pytest --html=report.html --self-contained-html
```

## Project Structure

```
project/
├── chatbot.py               # Main chatbot implementation
├── conftest.py              # Pytest configuration with custom hooks
├── tests/
│   ├── test_data.json       # Test cases for response validation
│   ├── test_pref_data.json  # Test cases for performance testing
│   ├── test_chatbot.py      # Test scripts
├── data/
│   └── prompts.txt          # Prompts for chatbot
├── report.html              # HTML test report
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── .env                     # Environment variables (OpenAI API key)
```

---

## Key Features

1. **Dynamic Query Handling**:
   - Uses FAISS vector stores for efficient prompt retrieval.
   - Provides context-aware, accurate responses based on user input.

2. **Robust Testing Framework**:
   - **Function Tests**:
     - Validates responses against expected outputs defined in `data\prompts.txt`.
     - Example:
       - **Input Query**: "What is the return policy?"
       - **Expected Response**: "Our return policy allows returns within 30 days."
       - **Criteria**: Ensures that the response contains clear, policy-related information.
   - **Performance Tests**:
     - Evaluates response times for various queries.
     - Examples:
       - **Simple Query**: "What are your store hours?" (Expected <1s response time).
       - **Complex Query**: "What are the shipping policies for international orders placed during holidays?" (Expected <2s response time).
   - Ensures chatbot meets performance thresholds and handles edge cases effectively.

3. **Validated Quality and Exit Criteria**:
   - Ensures all responses are accurate, contextually relevant, and adhere to expected criteria.
   - Exit criteria:
     - All test cases pass.
     - Response times remain within acceptable limits.
     - Quality of responses validated against predefined standards.

4. **Detailed Reporting**:
   - Generates a comprehensive HTML report (`report.html`) summarizing test results and performance metrics.

## Performance Highlights
- Average response time: Under 2 seconds for most queries.
- High accuracy in returning relevant and precise answers.
- Successfully handles edge cases, ensuring robust operation.

## Future Enhancements
- Add multi-turn conversational support for complex interactions.
- Implement real-time prompt updates without restarting the application.
- Enhance error-handling mechanisms for better fault tolerance.

## Contributors
- **Sumit Soman**: Project Developer