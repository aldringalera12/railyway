#!/usr/bin/env python3
"""
Compare responses between original chatbot and FastAPI version
"""

import requests
import json
from chatbot import VectorDatabaseChatbot

def test_original_chatbot(question):
    """Test the original chatbot directly."""
    print(f"🔍 Testing original chatbot with: '{question}'")
    
    # Initialize original chatbot
    chatbot = VectorDatabaseChatbot(
        api_key="F2kIZdCtAAHnfVYlPCfCdLBtEtxLyEzGQqTiRVnt",
        db_path="./vector_db",
        collection_name="definitions"
    )
    
    # Get response using same methods as single_question
    search_results = chatbot.search_relevant_context(question)
    response = chatbot.generate_response(question, search_results)
    
    print(f"✅ Original response: {response[:100]}...")
    print(f"📚 Sources found: {len(search_results)}")
    
    return response, search_results

def test_fastapi_chatbot(question):
    """Test the FastAPI chatbot via HTTP."""
    print(f"🌐 Testing FastAPI chatbot with: '{question}'")
    
    try:
        response = requests.post(
            "http://localhost:8000/chat",
            json={"question": question, "max_results": 8},
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ FastAPI response: {data['answer'][:100]}...")
            print(f"📚 Sources found: {len(data['sources'])}")
            return data['answer'], data['sources']
        else:
            print(f"❌ FastAPI error: {response.status_code}")
            return None, None
            
    except Exception as e:
        print(f"❌ FastAPI connection error: {e}")
        return None, None

def compare_responses(question):
    """Compare responses from both versions."""
    print("=" * 80)
    print(f"🧪 COMPARING ENHANCED RESPONSES FOR: '{question}'")
    print("=" * 80)

    # Test original
    original_response, original_sources = test_original_chatbot(question)
    print()

    # Test FastAPI
    fastapi_response, fastapi_sources = test_fastapi_chatbot(question)
    print()

    # Compare
    if fastapi_response:
        print("🔍 COMPARISON RESULTS:")
        print(f"   Response length - Original: {len(original_response)}, FastAPI: {len(fastapi_response)}")
        print(f"   Sources count - Original: {len(original_sources)}, FastAPI: {len(fastapi_sources)}")

        # Check for truncation in both
        orig_complete = original_response.strip().endswith(('.', '!', '?', ':', '%'))
        fast_complete = fastapi_response.strip().endswith(('.', '!', '?', ':', '%'))

        print(f"   Truncation check - Original: {'✅ Complete' if orig_complete else '⚠️ Truncated'}, FastAPI: {'✅ Complete' if fast_complete else '⚠️ Truncated'}")

        # Check if responses are similar (allowing for minor differences)
        if original_response.strip() == fastapi_response.strip():
            print("✅ IDENTICAL: Responses are exactly the same!")
        elif len(original_response) > 0 and len(fastapi_response) > 0:
            # Check similarity by comparing first 300 characters
            orig_start = original_response[:300].strip()
            fast_start = fastapi_response[:300].strip()
            if orig_start == fast_start:
                print("✅ VERY SIMILAR: Response beginnings are identical")
            else:
                print("⚠️  DIFFERENT: Responses differ")
                print(f"   Original: {orig_start}...")
                print(f"   FastAPI:  {fast_start}...")
        else:
            print("❌ ERROR: One or both responses are empty")

        # Check for specific improvements
        if "what law" in question.lower():
            orig_has_law = "11015" in original_response and "2018" in original_response
            fast_has_law = "11015" in fastapi_response and "2018" in fastapi_response
            print(f"   Law details - Original: {'✅' if orig_has_law else '❌'}, FastAPI: {'✅' if fast_has_law else '❌'}")

        elif "four types" in question.lower():
            types = ["inbound", "outbound", "in-campus", "out-campus"]
            orig_types = sum(1 for t in types if t in original_response.lower())
            fast_types = sum(1 for t in types if t in fastapi_response.lower())
            print(f"   Cross-enrolment types - Original: {orig_types}/4, FastAPI: {fast_types}/4")

        elif "student assistant" in question.lower():
            orig_rate = "₱25" in original_response or "25.00" in original_response
            fast_rate = "₱25" in fastapi_response or "25.00" in fastapi_response
            print(f"   Correct rate (₱25) - Original: {'✅' if orig_rate else '❌'}, FastAPI: {'✅' if fast_rate else '❌'}")

    else:
        print("❌ Cannot compare - FastAPI request failed")

    print()

def main():
    """Run comparison tests."""
    print("🧪 ENHANCED CHATBOT RESPONSE COMPARISON TEST")
    print("This will compare responses between ENHANCED original chatbot.py and FastAPI version")
    print("Both versions now include all the fixes and improvements!")
    print()

    # Test questions - including the problematic ones that were fixed
    test_questions = [
        "What does PRMSU stand for?",
        "What law officially established PRMSU in 2018?",
        "What are the four types of cross-enrolment recognized by PRMSU?",
        "What is the maximum number of hours per month a student assistant is allowed to work, and at what hourly rate?",
        "What is the penalty for a first offense of being caught under the influence of liquor on campus?",
        "What honors can be awarded to graduating students based on their GWA?"
    ]
    
    for question in test_questions:
        compare_responses(question)
        print("Press Enter to continue to next test...")
        input()
    
    print("🎉 Comparison tests completed!")

if __name__ == "__main__":
    main()
