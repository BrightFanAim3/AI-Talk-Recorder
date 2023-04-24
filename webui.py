import whisper
import gradio as gr

def caption(audio):
  # Use whisper to transcribe the audio file
  transcript = whisper.transcribe(audio.name, "--language zh-CN")
  # Return the transcript as output
  return transcript

# Create a gradio interface for our function
iface = gr.Interface(
  fn=caption, # our function
  inputs=gr.inputs.Audio(type="file", label="Upload an audio file"), # audio input
  outputs=gr.outputs.Textbox(label="Caption"), # text output
  title="Audio Captioning Tool", # title of the app
  description="A simple tool to generate captions for audio files using whisper and gradio.", # description of the app
  examples=[["example.wav"]], # some example audio files to test
)

# Launch the app
iface.launch()