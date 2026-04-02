[Prev](/context00002.md) | [Next](/context00004.md)

# Raspberry Pi Camera Streaming Guide (Debian 13 / Bookworm+)

This guide provides the latest working commands for streaming video from a Raspberry Pi (Debian 13 "Trixie" or Raspberry Pi OS Bookworm) to a Mac or other computer with low latency.

## 1. Installation
Ensure the necessary camera applications are installed on your Raspberry Pi:

```bash
sudo apt update
sudo apt install rpicam-apps
```

## 2. Start Streaming (Raspberry Pi)
Run this command on the Pi to start a persistent stream. The `while` loop ensures the stream automatically restarts if the connection is closed or fails.

```bash
while true; do rpicam-vid -t 0 --inline --listen -o tcp://0.0.0.0:5000 --width 640 --height 480 --framerate 30; sleep 1; done
```
- **-t 0**: Run forever.
- **--inline**: Forces header information (SPS/PPS) with every keyframe (essential for streaming).
- **--listen**: Wait for a client to connect.
- **-o tcp://0.0.0.0:5000**: Output to TCP port 5000.
- **--width 640 --height 480 --framerate 30**: Optimized for low latency over Wi-Fi.

## 3. Viewing the Stream (Mac / Client)

### Option A: ffplay (Lowest Latency)
If you have `ffmpeg` installed (`brew install ffmpeg`), run this command in your Mac terminal:

```bash
ffplay -fflags nobuffer -flags low_delay -framedrop tcp://192.168.1.45:5000
```
*(Replace `192.168.1.45` with your Pi's actual IP, e.g., 192.168.1.45)*

### Option B: VLC Media Player
1. Open VLC.
2. Go to **File -> Open Network...** (Cmd + N).
3. Enter the URL: `tcp/h264://192.168.1.45:5000`
4. Click **Show More Options** and set **Network Caching** to `200ms` for lower lag.

## 4. Troubleshooting
- **Command not found**: Ensure you use `rpicam-*` instead of `libcamera-*` on newer OS versions.
- **Connection Refused**: Ensure the Pi command is running and you are using the correct IP address.
- **Broken Socket/Aborted**: This is normal when a TCP client disconnects. The `while` loop provided above automatically handles this and restarts the listener.

[Prev](/context00002.md) | [Next](/context00004.md)
