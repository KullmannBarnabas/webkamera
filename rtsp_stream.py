import cv2
import subprocess

# Configuration
rtsp_server_url = "rtsp://127.0.0.1:8554/proba"
ffmpeg_path = "ffmpeg"  # Ensure ffmpeg is installed and in your PATH
frame_width = 640
frame_height = 480
fps = 30

# Open webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
cap.set(cv2.CAP_PROP_FPS, fps)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()
# FFmpeg command to stream video
ffmpeg_command = [
    ffmpeg_path,
    '-y',  # Overwrite output files
    '-f', 'rawvideo',  # Input format is raw video
    '-pix_fmt', 'bgr24',  # Pixel format
    '-s', f"{frame_width}x{frame_height}",  # Frame size
    '-r', str(fps),  # Frame rate
    '-i', '-',  # Input from stdin
    '-c:v', 'libx264',  # Video codec
    '-preset', 'ultrafast',  # Encoding speed/quality tradeoff
    '-f', 'rtsp',  # Output format
    '-rtsp_transport', 'tcp',  # RTSP transport protocol
    rtsp_server_url
]

# Start FFmpeg process

process = subprocess.Popen(ffmpeg_command, stdin=subprocess.PIPE)

print(f"Streaming webcam to {rtsp_server_url}")

try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame from webcam.")
            break

        # Write frame to FFmpeg stdin
        process.stdin.write(frame.tobytes())
except KeyboardInterrupt:
    print("Streaming stopped.")
finally:
    # Release webcam and terminate FFmpeg process
    cap.release()
    process.stdin.close()
    process.terminate()
    process.wait()
