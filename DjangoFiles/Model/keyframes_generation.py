
from diffusers import StableDiffusionPipeline,StableDiffusionControlNetPipeline,ControlNetModel
import os
os.makedirs("/generated_keyframes", exist_ok=True)

def generate_keyframes(common_scene,keyframes):
    control_net=ControlNetModel.from_pretrained("lllyasviel/control_v11p_sd15_canny")
    pipeline = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1",controlnet=control_net,torch_dtype=torch.float16)


    pipeline.to("cuda")  # Ensure GPU usage

    negative_prompt = "blurry, duplicate, low quality, cropped, extra hands, extra faces, messy background"

    key_frames = []
    for frame in keyframes:
        image = pipeline(frame[1],negative_prompt=negative_prompt,num_inference_steps=30).images[0]
        key_frames.append(image)


    output_dir = "./generated_keyframes/output"
    os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist

    # Save keyframes
    for i, frame in enumerate(key_frames):
        frame.save(f"{output_dir}/keyframe_{i}.png")