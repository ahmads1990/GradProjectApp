import time
import pyaudio
import wave

class Recorder:
    def __init__(self):
        self.is_recording = False
        self.frames = []
        self.sample_rate = 50000  # Sample rate
        self.chunk = 1024  # Record in chunks of 1024 samples
        self.sample_format = pyaudio.paInt16  # 16 bits per sample
        self.channels = 1
        self.current_record_length = 0
        self.max_record_length = 30  # Maximum recording length in seconds
        self.path = 'Audio/'

    def start_recording(self, filename):
        """
        Starts recording audio from the default input device and saves it to a WAV file.
        
        Args:
            path (str): The path where the output file will be saved.
            filename (str): The name of the output file.
        """
        self.is_recording = True
        self.frames = []
        
        # Create an interface to PortAudio
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(
            format=self.sample_format,
            channels=self.channels,
            rate=self.sample_rate,
            input=True,
            frames_per_buffer=self.chunk)
        
        start = time.time()

        while self.is_recording:
            data = self.stream.read(self.chunk)
            self.frames.append(data)

            # Calcualte time elapsed from starting the record
            self.current_record_length = time.time() - start
            # Check duration if bigger allowed stop the recording
            if self.current_record_length >= self.max_record_length:
                self.is_recording = False
                break
            
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
        
        # Save the recorded audio to a WAV file
        wf = wave.open(self.path + filename + ".wav", 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.audio.get_sample_size(self.sample_format))
        wf.setframerate(self.sample_rate)
        wf.writeframes(b''.join(self.frames))
        wf.close() 
        
    def stop_recording(self):
        """Stops the current recording."""
        self.is_recording = False
