#!/bin/bash
# Start KrishiShakti with Real Blynk Data

echo "╔════════════════════════════════════════════════════════╗"
echo "║  KrishiShakti - Starting with Real Blynk Data        ║"
echo "╚════════════════════════════════════════════════════════╝"
echo ""
echo "🚀 Starting KrishiShakti Server..."
python3 app.py &
SERVER_PID=$!

echo "⏳ Waiting for server to start..."
sleep 5

echo "📡 Starting Blynk Bridge..."
python3 blynk_bridge.py &
BRIDGE_PID=$!

echo ""
echo "✅ Everything is running!"
echo ""
echo "📊 Open your dashboard:"
echo "   http://localhost:5001/dashboard.html"
echo ""
echo "🤖 Try the AI chatbot:"
echo "   http://localhost:5001/chatbot.html"
echo ""
echo "📈 View history:"
echo "   http://localhost:5001/history.html"
echo ""
echo "Press Ctrl+C to stop everything"
echo ""

# Wait for Ctrl+C
trap "echo ''; echo '🛑 Stopping...'; kill $SERVER_PID $BRIDGE_PID 2>/dev/null; echo '✅ Stopped'; exit" INT

wait
