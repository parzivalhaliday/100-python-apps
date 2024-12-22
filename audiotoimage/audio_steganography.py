import wave
import numpy as np
from PIL import Image
from PIL.ImageEnhance import Sharpness

def encode_image_to_audio(image_path, output_path):
    try:
        # Read image and convert to grayscale with higher resolution
        img = Image.open(image_path).convert('L')  # Convert image to grayscale
        img = img.resize((256, 256))  # Resize image to 256x256 pixels
        img_array = np.array(img)  # Convert image to numpy array
        
        # Initialize audio file with parameters
        audio = wave.open(output_path, 'w')  # Create new WAV file
        audio.setnchannels(1)  # Set to mono channel
        audio.setsampwidth(2)  # Set sample width to 2 bytes
        audio.setframerate(96000)  # Set sample rate to 96kHz
        
        # Process each pixel and convert to audio signal
        for pixel in img_array.flatten():  # Iterate through each pixel value
            # Convert pixel value to frequency
            frequency = 200 + float(pixel * 2)  # Map pixel value (0-255) to frequency range (200-710 Hz)
            duration = 0.005  # Set duration for each pixel tone
            t = np.linspace(0, duration, int(96000 * duration))  # Create time array
            wave_data = (np.sin(2 * np.pi * frequency * t) * 32767).astype(np.int16)  # Generate sine wave
            audio.writeframes(wave_data.tobytes())  # Write audio data to file
        
        audio.close()  # Close the audio file
        print(f"Image converted to audio: {output_path}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

def decode_audio_to_image(audio_path, output_path):
    try:
        # Read audio file
        audio = wave.open(audio_path, 'r')  # Open WAV file for reading
        frames = audio.readframes(audio.getnframes())  # Read all audio frames
        audio_data = np.frombuffer(frames, dtype=np.int16)  # Convert to numpy array
        
        # Calculate samples per pixel based on duration
        samples_per_pixel = int(96000 * 0.005)  # Number of samples for each pixel
        pixels = []  # Store decoded pixel values
        
        # Process audio chunks to extract pixel values
        for i in range(0, len(audio_data), samples_per_pixel):
            chunk = audio_data[i:i + samples_per_pixel]  # Get chunk of audio data
            if len(chunk) == samples_per_pixel:
                fft = np.fft.fft(chunk)  # Perform FFT on chunk
                freqs = np.fft.fftfreq(len(chunk), 1/96000)  # Get frequency array
                peak_freq = freqs[np.argmax(np.abs(fft))]  # Find peak frequency
                pixel = int((abs(peak_freq) - 200) / 2)  # Convert frequency back to pixel value
                pixels.append(min(255, max(0, pixel)))  # Ensure pixel value is in valid range
        
        # Reconstruct image from pixel values
        img_array = np.array(pixels[:256*256]).reshape(256, 256).astype(np.uint8)  # Create 2D image array
        img = Image.fromarray(img_array)  # Convert array to image
        
        # Enhance image quality
        enhancer = Sharpness(img)  # Create sharpness enhancer
        img = enhancer.enhance(2.0)  # Apply sharpness enhancement
        
        img.save(output_path)  # Save the decoded image
        print(f"Audio converted to image: {output_path}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

# Example usage of the encoding and decoding functions
encode_image_to_audio("input.jpg", "secret.wav")
decode_audio_to_image("secret.wav", "decoded.png") 