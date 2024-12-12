import json
import pytest
import time
import warnings
from src.chatbot import setup_chatbot, get_response

warnings.filterwarnings("ignore", category=DeprecationWarning, module="langchain")
"""
    Fixture to set up the chatbot.

    This fixture initializes the chatbot by setting up the language model (LLM)
    and retriever components. It is scoped to the module level, ensuring the
    chatbot setup is reused across all tests in the module.

    Returns:
    tuple: A tuple containing the LLM and retriever instances.
"""
@pytest.fixture(scope="module")
def chatbot_setup():
    llm, retriever = setup_chatbot()
    return llm, retriever

"""
    Load test cases from a JSON file.

    This function reads a JSON file containing test cases and returns the
    parsed data as a Python dictionary.

    Args:
    file_path (str): Path to the JSON file containing test cases.

    Returns:
    list: A list of test cases, where each test case is a dictionary.
"""
def load_test_cases(file_path="tests/test_data.json"):
    with open(file_path, "r") as file:
        return json.load(file)


"""
    Test chatbot responses for predefined queries.

    This test validates the chatbot's response against predefined expectations
    for various input queries. It also customizes the test title for each query.

    Args:
    chatbot_setup (tuple): The chatbot setup fixture providing LLM and retriever.
    test_case (dict): A single test case containing input query, expected output,
        and validation criteria.
    request (Fixture): Pytest request fixture for customizing test titles.
"""
@pytest.mark.parametrize("test_case", load_test_cases(file_path="tests/test_data.json"))
def test_chatbot_response(chatbot_setup, test_case, request):
    llm, retriever = chatbot_setup
    query = test_case["input_query"]
    expected = test_case["expected_output"]
    validation = test_case["validation_criteria"]

    # Customize test title
    request.node._nodeid = f"Input query: {query}"

    start_time = time.time()
    response = get_response(llm, retriever, query)
    elapsed_time = time.time() - start_time

    print(f"Query: {query}\nResponse: {response}\nExpected: {expected}\nResponse Time: {elapsed_time:.2f}s\n")
    assert expected in response, f"Validation failed: {validation}"

"""
    Test chatbot response time for predefined queries.

    This test validates the chatbot's response against predefined expectations
    and ensures that the response time is below a specified threshold.

    Args:
    chatbot_setup (tuple): The chatbot setup fixture providing LLM and retriever.
    test_case (dict): A single test case containing input query, expected output,
        and validation criteria.
    request (Fixture): Pytest request fixture for customizing test titles.
"""
@pytest.mark.parametrize("test_case", load_test_cases(file_path="tests/test_pref_data.json"))
def test_chatbot_response_time(chatbot_setup, test_case, request):
    """Test chatbot responses for predefined queries."""
    llm, retriever = chatbot_setup
    query = test_case["input_query"]
    expected = test_case["expected_output"]
    validation = test_case["validation_criteria"]

    # Customize test title
    request.node._nodeid = f"Input query: {query}"

    start_time = time.time()
    response = get_response(llm, retriever, query)
    elapsed_time = time.time() - start_time

    print(f"Query: {query}\nResponse: {response}\nExpected: {expected}\nResponse Time: {elapsed_time:.2f}s\n")
    assert expected in response, f"Validation failed: {validation}"
    assert elapsed_time < 2, f"Validation failed: {validation}. Time taken: {elapsed_time}"
