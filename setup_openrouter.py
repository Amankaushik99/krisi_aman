#!/usr/bin/env python3
"""
Easy OpenRouter API Key Setup
"""

import os
import sys

def main():
    print("╔════════════════════════════════════════════════════════╗")
    print("║  KrishiShakti - OpenRouter API Setup                 ║")
    print("╚════════════════════════════════════════════════════════╝\n")
    
    print("🤖 Setting up AI-Powered Chatbot\n")
    
    print("📋 Get your FREE OpenRouter API key:")
    print("1. Visit: https://openrouter.ai/")
    print("2. Click 'Sign In' (top right)")
    print("3. Sign up with Google/GitHub/Email")
    print("4. Go to 'Keys' section: https://openrouter.ai/keys")
    print("5. Click 'Create Key'")
    print("6. Copy your key (starts with 'sk-or-v1-')\n")
    
    print("💡 Free tier includes:")
    print("   • Multiple free AI models")
    print("   • No credit card required")
    print("   • Generous rate limits")
    print("   • Fast responses\n")
    
    api_key = input("👉 Paste your OpenRouter API key here: ").strip()
    
    if not api_key:
        print("\n❌ No API key provided!")
        print("Run this script again when you have your key.\n")
        return False
    
    if not api_key.startswith('sk-or-v1-'):
        print("\n⚠️  Warning: Key doesn't start with 'sk-or-v1-'")
        confirm = input("Continue anyway? (y/n): ").strip().lower()
        if confirm != 'y':
            print("\n❌ Setup cancelled.")
            return False
    
    # Update ai_chat.py
    try:
        print("\n🔄 Updating ai_chat.py...")
        
        with open('ai_chat.py', 'r') as f:
            content = f.read()
        
        # Replace the API key line
        import re
        pattern = r"OPENROUTER_API_KEY = os\.environ\.get\('OPENROUTER_API_KEY', '[^']*'\)"
        replacement = f"OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY', '{api_key}')"
        
        new_content = re.sub(pattern, replacement, content)
        
        with open('ai_chat.py', 'w') as f:
            f.write(new_content)
        
        print("✅ API key saved!\n")
        
        # Test the chatbot
        print("🧪 Testing chatbot with your API key...\n")
        
        from ai_chat import ask_ai
        
        test_data = {
            'dht22': {'temperature': 15.0, 'humidity': 65.0},
            'fc28': {'value': 45.0},
            'mq135': {'value': 84.0},
            'pms5003': {'pm25': 35.0, 'pm10': 50.0},
            'location': {'city': 'Landran', 'country': 'India'}
        }
        
        print("📍 Test Location: Landran, Punjab, India")
        print("🌡️  Temperature: 15°C")
        print("💧 Humidity: 65%")
        print("🌱 Soil Moisture: 45%\n")
        print("❓ Test Question: What should I do about my soil moisture?\n")
        print("🤖 AI Response:")
        print("-" * 60)
        
        response = ask_ai("What should I do about my soil moisture?", test_data)
        print(response)
        print("-" * 60)
        
        if "⚠️" in response or "Error" in response:
            print("\n⚠️  Test completed but got an error response.")
            print("This might be normal if:")
            print("  • API key needs activation (wait a few minutes)")
            print("  • Rate limit reached (try again later)")
            print("  • Network issue (check internet connection)")
            print("\nThe chatbot will fall back to demo mode if AI fails.")
        else:
            print("\n✅ Test successful! AI is working!")
        
        print("\n" + "="*60)
        print("✅ SETUP COMPLETE!")
        print("="*60)
        
        print("\n🎉 Your AI-powered chatbot is ready!")
        print("\n📊 Try it now:")
        print("   http://localhost:5001/chatbot.html")
        
        print("\n💡 Features enabled:")
        print("   ✅ AI-powered intelligent responses")
        print("   ✅ Natural language understanding")
        print("   ✅ Context-aware farming advice")
        print("   ✅ Multi-language support (English, Hindi, Punjabi)")
        print("   ✅ Real-time sensor data integration")
        print("   ✅ Fallback to demo mode if AI fails")
        
        print("\n🔄 Restart your server to apply changes:")
        print("   Press Ctrl+C to stop")
        print("   Run: python3 app.py\n")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("Please try again or manually edit ai_chat.py\n")
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
