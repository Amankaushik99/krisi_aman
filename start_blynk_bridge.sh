#!/bin/bash
# Start Blynk Bridge to show real sensor data on dashboard

echo "╔════════════════════════════════════════════════════════╗"
echo "║  Starting Blynk to KrishiShakti Bridge                ║"
echo "╚════════════════════════════════════════════════════════╝"
echo ""
echo "📡 This will fetch real data from your Blynk device"
echo "🔄 And display it on your KrishiShakti dashboard"
echo ""
echo "Make sure your KrishiShakti server is running!"
echo "If not, open another terminal and run: python3 app.py"
echo ""
echo "Press Ctrl+C to stop the bridge"
echo ""

python3 blynk_bridge.py
