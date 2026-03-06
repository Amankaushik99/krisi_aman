# 🤖 Full AI Chatbot Setup Guide

## Quick Setup (2 Minutes)

### Step 1: Get Your FREE OpenRouter API Key

1. **Visit**: https://openrouter.ai/
2. **Sign Up**: Click "Sign In" → Sign up with Google/GitHub/Email (FREE)
3. **Get Key**: 
   - Go to "Keys" section: https://openrouter.ai/keys
   - Click "Create Key"
   - Copy your key (starts with `sk-or-v1-...`)

### Step 2: Run Setup Script

```bash
python3 setup_openrouter.py
```

When prompted, paste your API key and press Enter.

### Step 3: Restart Server

```bash
# Stop current server (Ctrl+C)
# Then start again:
python3 app.py
```

### Step 4: Test Your AI Chatbot

Open: http://localhost:5001/chatbot.html

Ask questions like:
- "What should I do about my soil moisture?"
- "मेरी फसल की सेहत कैसी है?" (Hindi)
- "ਮੈਨੂੰ ਪਾਣੀ ਕਦੋਂ ਦੇਣਾ ਚਾਹੀਦਾ ਹੈ?" (Punjabi)

## ✅ What You Get

### AI-Powered Features
- 🧠 **Intelligent Responses**: Natural language understanding
- 🌍 **Multi-Language**: English, Hindi, Punjabi auto-detection
- 📊 **Context-Aware**: Uses your real sensor data
- 🎯 **Personalized**: Advice specific to Landran, Punjab
- ⚡ **Fast**: Responses in 2-3 seconds
- 🔄 **Reliable**: Falls back to demo mode if AI fails

### Current Sensor Integration
```
📍 Location: Landran, Punjab, India
🌡️  Temperature: 15°C (real-time)
💧 Humidity: 65%
🌱 Soil Moisture: 45%
💨 Air Quality: 84 ppm
🌫️  PM2.5: 35 µg/m³
```

## 🆓 Free Tier Details

OpenRouter free tier includes:
- ✅ Multiple free AI models
- ✅ No credit card required
- ✅ Generous rate limits (enough for farming use)
- ✅ Fast response times
- ✅ No expiration

**Models Available (FREE):**
- `meta-llama/llama-3.1-8b-instruct:free` (Default)
- `google/gemma-2-9b-it:free`
- `mistralai/mistral-7b-instruct:free`

## 📝 Manual Setup (Alternative)

If you prefer to edit manually:

1. Open `ai_chat.py`
2. Find this line:
   ```python
   OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY', 'YOUR_API_KEY_HERE')
   ```
3. Replace `YOUR_API_KEY_HERE` with your actual key:
   ```python
   OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY', 'sk-or-v1-YOUR_ACTUAL_KEY')
   ```
4. Save and restart server

## 🧪 Test Your Setup

### Test from Command Line:
```bash
python3 ai_chat.py
```

### Test from Web:
1. Open: http://localhost:5001/chatbot.html
2. Ask: "What should I do about my soil moisture?"
3. You should get an AI-powered response in 2-3 seconds

## 🎯 Example Conversations

### English Example:
**You**: "My soil moisture is 45%. What should I do?"

**AI**: "With 45% soil moisture and current temperature of 15°C in Landran, your soil is moderately dry. I recommend watering within the next 4-6 hours. Apply 15-20mm of water (about 1.5-2 liters per square meter) early morning between 6-8 AM. Use drip irrigation or water at soil level to avoid leaf wetness. The cooler temperature means less evaporation, so this watering should last 2-3 days."

### Hindi Example:
**You**: "मेरी मिट्टी में 45% नमी है। मुझे क्या करना चाहिए?"

**AI**: "लांद्रां में 15°C तापमान और 45% मिट्टी की नमी के साथ, आपकी मिट्टी मध्यम रूप से सूखी है। मैं अगले 4-6 घंटों में पानी देने की सलाह देता हूं। सुबह 6-8 बजे के बीच 15-20mm पानी (लगभग 1.5-2 लीटर प्रति वर्ग मीटर) दें। ड्रिप सिंचाई का उपयोग करें या मिट्टी के स्तर पर पानी दें।"

### Punjabi Example:
**You**: "ਮੇਰੀ ਮਿੱਟੀ ਵਿੱਚ 45% ਨਮੀ ਹੈ। ਮੈਨੂੰ ਕੀ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ?"

**AI**: "ਲਾਂਦਰਾਂ ਵਿੱਚ 15°C ਤਾਪਮਾਨ ਅਤੇ 45% ਮਿੱਟੀ ਦੀ ਨਮੀ ਦੇ ਨਾਲ, ਤੁਹਾਡੀ ਮਿੱਟੀ ਮੱਧਮ ਸੁੱਕੀ ਹੈ। ਮੈਂ ਅਗਲੇ 4-6 ਘੰਟਿਆਂ ਵਿੱਚ ਪਾਣੀ ਦੇਣ ਦੀ ਸਲਾਹ ਦਿੰਦਾ ਹਾਂ। ਸਵੇਰੇ 6-8 ਵਜੇ ਦੇ ਵਿਚਕਾਰ 15-20mm ਪਾਣੀ (ਲਗਭਗ 1.5-2 ਲੀਟਰ ਪ੍ਰਤੀ ਵਰਗ ਮੀਟਰ) ਦਿਓ।"

## 🔧 Troubleshooting

### "API key not configured"
- Run: `python3 setup_openrouter.py`
- Or manually edit `ai_chat.py`

### "API returned status 401"
- Invalid API key
- Check you copied the complete key
- Verify key is active on OpenRouter dashboard

### "API returned status 429"
- Rate limit exceeded (rare on free tier)
- Wait a few minutes
- Chatbot will automatically use demo mode

### "Connection error"
- Check internet connection
- Verify firewall isn't blocking openrouter.ai
- Chatbot will automatically use demo mode

### Chatbot still shows demo mode
- Make sure you restarted the server after adding API key
- Check `ai_chat.py` has your actual key (not 'YOUR_API_KEY_HERE')
- Test with: `python3 ai_chat.py`

## 🎨 Customize Your AI

### Change AI Model

Edit `ai_chat.py`, find this line:
```python
"model": "meta-llama/llama-3.1-8b-instruct:free",
```

Replace with:
- `"google/gemma-2-9b-it:free"` - Google's Gemma (good for technical)
- `"mistralai/mistral-7b-instruct:free"` - Mistral (balanced)
- `"meta-llama/llama-3-8b-instruct:free"` - Llama 3 (creative)

### Adjust Response Length

Edit `ai_chat.py`, find:
```python
"max_tokens": 500
```

Change to:
- `300` - Shorter responses
- `800` - Longer, detailed responses

### Adjust Creativity

Edit `ai_chat.py`, find:
```python
"temperature": 0.7
```

Change to:
- `0.3` - More focused, factual
- `0.9` - More creative, varied

## 📊 Usage Stats

After setup, you can monitor:
- API usage: https://openrouter.ai/activity
- Credits remaining
- Response times
- Model performance

## 🚀 Next Steps

1. ✅ Get API key from https://openrouter.ai/keys
2. ✅ Run `python3 setup_openrouter.py`
3. ✅ Restart server
4. ✅ Test at http://localhost:5001/chatbot.html
5. ✅ Ask farming questions in any language!

## 💡 Pro Tips

1. **Ask Specific Questions**: "What fertilizer for wheat in February?" is better than "Tell me about fertilizer"

2. **Use Your Language**: The AI understands Hindi and Punjabi perfectly

3. **Reference Sensors**: "My temperature is 15°C, is this good for wheat?" - AI will use your actual sensor data

4. **Follow-up Questions**: Have a conversation! Ask follow-ups for more details

5. **Trust the Fallback**: If AI fails, demo mode is still very smart and uses your sensor data

---

**Ready to get started?** Run `python3 setup_openrouter.py` now! 🚀
