import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import streamlit as st
from app import get_gemini_response

# Mock the `get_gemini_response` function to avoid real API calls
def mock_get_gemini_response(question):
    return "Mocked response to: " + question

# Use monkeypatch to replace the real function with the mock
def test_get_gemini_response():
    question = "What is the capital of France?"
    response = mock_get_gemini_response(question)
    assert response == "Mocked response to: What is the capital of France?"

def test_app_flow(monkeypatch):
    # Simulate a Streamlit test flow using monkeypatch to mock the user input
    monkeypatch.setattr(st, 'text_input', lambda label, key: "What is the capital of France?")
    monkeypatch.setattr(st, 'button', lambda label: True)
    
    # Mock get_gemini_response directly
    monkeypatch.setattr('app.get_gemini_response', mock_get_gemini_response)
    
    response = get_gemini_response(st.text_input("Input:", "input"))
    assert response == "Mocked response to: What is the capital of France?"
