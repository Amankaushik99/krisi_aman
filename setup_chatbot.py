#!/usr/bin/env python3
"""
Setup OpenRouter API for the chatbot
"""

import os
import sys

def main():
    print("╔════════════════════════════════════════════════════════╗")
    print("║  KrishiShakti Chatbot Setup                          ║")
    print("╚════════════════════════════════════════════════════════╝\n")
    
    print("🤖 Setting up AI Chatbot with OpenRouter\n")
    
    print("📋 Steps to get your FREE API key:")
    print("1. Go to: https://openrouter.ai/")
    print("2. Click 'Sign In' (top right)")
    print("3. Sign up with Google/GitHub/Email")
    print("4. Go to 'Keys' section")
    print("5. Click 'Create Key'")
    print("6. Copy your API key (starts with 'sk-or-v1-')\n")
    
    print("💡 Free tier includes:")
    print("   • Multiple free models (Llama, Mistral, etc.)")
    print("   • No credit card required")
    print("   • Generous rate limits\n")
    
    api_key = input("👉 Paste your OpenRouter API key here (or press Enter to skip): ").strip()
    
    if not api_key:
        print("\n⚠️  No API key provided.")
        print("\n💡 The chatbot will work in DEMO mode (fallback responses)")
        print("   To enable AI features, run this script again with your API key.\n")
        return
    
    if not api_key.startswith('sk-or-v1-'):
        print("\n❌ Invalid API key format!")
        print("   OpenRouter keys should start with 'sk-or-v1-'")
        print("   Please check and try again.\n")
        return
    
    # Update ai_chat.py with the API key
    try:
        with open('ai_chat.py', 'r') as f:
            content = f.read()
        
        # Replace the placeholder key
        content = content.replace(
            "OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY', 'sk-or-v1-d41d8cd98f00b204e9800998ecf8427e')",
            f"OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY', '{api_key}')"
        )
        
        with open('ai_chat.py', 'w') as f:
            f.write(content)
        
        print("\n✅ API key saved successfully!")
        print("\n🧪 Testing the chatbot...")
        
        # Test the chatbot
        from ai_chat import ask_ai
        
        test_data = {
            'dht22': {'temperature': 28.5, 'humidity': 65.2},
            'fc28': {'value': 45.3},
            'mq135': {'value': 125.5},
            'pms5003': {'pm25': 32.1, 'pm10': 45.6},
            'location': {'city': 'Lāndrān', 'country': 'India'}
        }
        
        response = ask_ai("What should I do about my soil moisture?", test_data)
        
        if "⚠️" in response and "API" in response:
            print("\n❌ Test failed!")
            print(response)
        else:
            print("\n✅ Test successful!")
            print("\n🤖 Sample Response:")
            print("-" * 60)
            print(response)
            print("-" * 60)
        
        print("\n" + "="*60)
        print("✅ CHATBOT SETUP COMPLETE!")
        print("="*60)
        print("\n📊 Try the chatbot:")
        print("   http://localhost:5001/chatbot.html")
        print("\n💡 The chatbot now supports:")
        print("   • Real-time sensor data integration")
        print("   • Multi-language (English, Hindi, Punjabi)")
        print("   • Context-aware farming advice")
        print("   • Free AI-powered responses\n")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("Please try again or manually edit ai_chat.py\n")

if __name__ == '__main__':
    main()
