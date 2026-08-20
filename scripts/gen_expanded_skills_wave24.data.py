SKILLS = [
    {
        "name": "ai-for-computer-graphics",
        "title": "AI for Computer Graphics",
        "description": "Neural rendering, differentiable rendering, inverse rendering, geometry and material estimation, and generative image synthesis for photorealistic graphics.",
        "devin_body": r'''
## When to use

You are synthesizing or editing photorealistic images, reconstructing scenes from observations, or integrating learned components into a traditional rendering pipeline.

## Key concepts

- **Neural radiance fields (NeRF)**: implicit 3D scene representations via MLPs and volume rendering.
- **3D Gaussian splatting**: explicit point-based scene representation with fast rasterization.
- **Differentiable rendering**: propagate gradients through light transport for inverse rendering.
- **Material and lighting estimation**: recover reflectance, illumination, and geometry from images.
- **Generative image synthesis**: diffusion and GAN-based texture/material generation.

## Code pattern

```python
import torch
import torch.nn as nn


class NeRFMLP(nn.Module):
    def __init__(self, pos_dim=3, hidden=256):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(pos_dim, hidden),
            nn.ReLU(),
            nn.Linear(hidden, hidden),
            nn.ReLU(),
            nn.Linear(hidden, hidden),
            nn.ReLU(),
            nn.Linear(hidden, 4)  # RGB + density
        )

    def forward(self, x):
        return self.net(x)
```

## Tuning notes

- Combine positional encoding for high-frequency details.
- Use coarse plus fine sampling for efficient ray marching.
- Differentiable rendering is expensive; use efficient samplers and cache radiance fields.
- Validate synthesized views against held-out camera poses.

## Verification

1. Fit a small NeRF to a synthetic multi-view cube and render novel views.
2. Compare PSNR and SSIM of rendered views to ground truth.
3. Estimate a simple BRDF from flash/no-flash image pairs.
''',
        "references": [
            "https://arxiv.org/abs/2111.05849",
            "https://arxiv.org/abs/2504.01402",
            "https://arxiv.org/abs/2501.13104",
            "https://doi.org/10.48550/arxiv.2402.00028",
        ],
    },
    {
        "name": "ai-for-animation",
        "title": "AI for Animation",
        "description": "Motion synthesis, inbetweening, character retargeting, physics-based animation, and style transfer for animated content.",
        "devin_body": r'''
## When to use

You are producing character motion, automating inbetween frames, retargeting across skeletons, or blending styles in games and film.

## Key concepts

- **Motion capture and cleanup**: denoise and segment motion data.
- **Motion inbetweening**: generate plausible intermediate frames between key poses.
- **Motion diffusion models**: generate diverse, controllable character movements.
- **Retargeting**: transfer motion between skeletons with different topologies.
- **Physics-based animation**: combine deep networks with simulation for realistic contact.

## Code pattern

```python
import torch
import torch.nn as nn


class MotionInbetweener(nn.Module):
    def __init__(self, n_joints, hidden=256):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(n_joints * 3 * 2, hidden),
            nn.ReLU(),
            nn.Linear(hidden, hidden),
            nn.ReLU(),
            nn.Linear(hidden, n_joints * 3)
        )

    def forward(self, start, end):
        return self.net(torch.cat([start, end], dim=-1))
```

## Tuning notes

- Normalize joint rotations and positions to root-relative coordinate frames.
- Train with diverse skeleton topologies to improve retargeting.
- Use foot-contact losses for ground-adherent locomotion.
- Evaluate with FID-like motion metrics and perceptual studies.

## Verification

1. Generate inbetween frames and measure pose smoothness and foot slide.
2. Retarget a walk cycle to a skeleton with different limb lengths.
3. Condition a motion-diffusion model on a text prompt and compare to a reference.
''',
        "references": [
            "https://arxiv.org/abs/2404.13680",
            "https://arxiv.org/abs/2404.15121",
            "https://arxiv.org/abs/2406.00960",
            "https://arxiv.org/abs/2405.11126",
            "https://arxiv.org/abs/2410.10306",
        ],
    },
    {
        "name": "ai-for-games",
        "title": "AI for Games",
        "description": "Procedural content generation, game-playing agents via reinforcement learning, NPC behavior, and generative AI for game assets and narratives.",
        "devin_body": r'''
## When to use

You are generating levels, items, or quests, training agents to play, designing NPC behavior, or augmenting game design with AI.

## Key concepts

- **Procedural content generation (PCG)**: search-based, learning-based, and LLM-driven level and asset generation.
- **Reinforcement learning for games**: train policies for playing or content generation.
- **Behavior trees and planning**: combine learned modules with symbolic AI.
- **LLM-driven design**: use large language models to generate quests, dialogues, and rules.
- **Player modeling and difficulty adaptation**: predict player skill and adjust content.

## Code pattern

```python
from stable_baselines3 import PPO
import gymnasium as gym

env = gym.make("CartPole-v1")  # proxy for a game environment
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=100_000)
```

## Tuning notes

- Balance exploration and exploitation for sparse game rewards.
- Use procedural environments to improve generalization.
- Combine RL with human demonstrations or imitation learning.
- Validate generated content with playability checks and player tests.

## Verification

1. Train an RL agent to reach a target in a procedural level.
2. Generate a set of playable platformer levels and check solvability.
3. Compare an LLM-generated quest to hand-written baselines for coherence.
''',
        "references": [
            "https://arxiv.org/abs/2410.15644",
            "https://arxiv.org/abs/2407.09013",
            "https://arxiv.org/abs/1702.00539",
            "https://arxiv.org/abs/2010.04548",
            "https://arxiv.org/abs/2408.12525",
        ],
    },
    {
        "name": "ai-for-virtual-reality",
        "title": "AI for Virtual Reality",
        "description": "Natural interaction, intent recognition, multimodal input, foveated rendering, virtual agents, and AI-driven content creation for VR.",
        "devin_body": r'''
## When to use

You are building immersive VR experiences that need gesture, gaze, voice, or intent-driven interaction, or AI-generated virtual worlds.

## Key concepts

- **Multimodal interaction**: combine hand tracking, eye tracking, and speech.
- **Intent recognition**: map low-level input streams to high-level user goals.
- **Foveated and gaze-contingent rendering**: optimize quality at the fixation point.
- **Virtual agents and avatars**: LLM-driven embodied characters in VR.
- **AI-assisted 3D scene editing**: natural language or sketch-based scene manipulation.

## Code pattern

```python
from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

result = classifier(
    "grab the red cube",
    candidate_labels=["grab", "move", "scale", "delete"]
)
```

## Tuning notes

- Calibrate trackers to each user and environment.
- Reduce latency for real-time interaction; prefer on-device inference.
- Use gaze plus hand fusion to resolve ambiguous commands.
- Test usability with target user groups in head-mounted displays.

## Verification

1. Build a classifier that maps speech to VR actions and report accuracy.
2. Implement gaze and hand fusion for object selection and measure selection time.
3. Generate a simple 3D scene from a natural language prompt in VR.
''',
        "references": [
            "https://arxiv.org/abs/2402.15083",
            "https://arxiv.org/abs/2410.21091",
            "https://arxiv.org/abs/2405.11537",
            "https://doi.org/10.48550/arxiv.2410.22177",
        ],
    },
    {
        "name": "ai-for-augmented-reality",
        "title": "AI for Augmented Reality",
        "description": "SLAM, scene understanding, depth completion, registration, occlusion handling, and semantic AR with deep learning.",
        "devin_body": r'''
## When to use

You are building AR applications that need accurate tracking, environment understanding, or realistic placement of virtual objects.

## Key concepts

- **Visual SLAM**: simultaneous localization and mapping for AR tracking.
- **Depth estimation and completion**: infer dense depth for occlusion and placement.
- **Plane and object detection**: identify surfaces for virtual object anchoring.
- **Semantic SLAM**: fuse object labels and geometry for context-aware AR.
- **Neural scene representations**: NeRF and 3D Gaussian splatting for AR.

## Code pattern

```python
import cv2
import numpy as np

sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(marker_img, None)
kp2, des2 = sift.detectAndCompute(camera_frame, None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)
good = [m for m, n in matches if m.distance < 0.75 * n.distance]
```

## Tuning notes

- Use robust feature matching or learned descriptors for low-texture scenes.
- Ensure real-time performance on mobile or AR glasses.
- Fuse IMU and visual measurements to handle fast motion.
- Validate tracking drift and re-localization on representative scenes.

## Verification

1. Track a planar marker or natural feature map and report reprojection error.
2. Estimate dense depth for a scene and compare to LiDAR ground truth.
3. Place a virtual object on a detected plane and check stability over time.
''',
        "references": [
            "https://arxiv.org/abs/2404.11419",
            "https://arxiv.org/abs/2402.03246",
            "https://arxiv.org/abs/2404.17876",
            "https://arxiv.org/abs/2404.04377",
            "https://arxiv.org/abs/2411.10940",
        ],
    },
    {
        "name": "ai-for-speech",
        "title": "AI for Speech",
        "description": "Automatic speech recognition, text-to-speech, speaker verification, speech synthesis, and self-supervised speech models.",
        "devin_body": r'''
## When to use

You need to transcribe, synthesize, verify speakers, or process spoken language in apps, assistants, or accessibility tools.

## Key concepts

- **End-to-end ASR**: CTC, RNN-T, attention, Conformer, and Whisper.
- **Text-to-speech (TTS)**: Tacotron, FastSpeech, and neural vocoders.
- **Speaker recognition and verification**: embeddings and anti-spoofing.
- **Self-supervised speech models**: wav2vec 2.0, HuBERT, and WavLM.
- **Streaming and on-device ASR**: latency, quantization, and memory optimization.

## Code pattern

```python
from transformers import WhisperProcessor, WhisperForConditionalGeneration

processor = WhisperProcessor.from_pretrained("openai/whisper-base")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-base")

inputs = processor(audio, sampling_rate=16000, return_tensors="pt")
predicted_ids = model.generate(inputs.input_features)
transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)
```

## Tuning notes

- Fine-tune on domain-specific data for named entities and jargon.
- Use SpecAugment and robust training for noise and reverberation.
- Calibrate confidence scores for human-in-the-loop transcription.
- Evaluate with WER on in-domain and out-of-domain test sets.

## Verification

1. Fine-tune Whisper on a small labeled dataset and compare WER.
2. Build a speaker verification pipeline and report equal error rate.
3. Synthesize speech with a TTS model and run MOS listening tests.
''',
        "references": [
            "https://arxiv.org/abs/2303.03329",
            "https://arxiv.org/abs/2111.01690",
            "https://arxiv.org/abs/2408.14991",
            "https://arxiv.org/abs/2410.09456",
            "https://arxiv.org/abs/2006.11477",
        ],
    },
    {
        "name": "ai-for-audio",
        "title": "AI for Audio",
        "description": "Audio enhancement, source separation, music generation, audio event detection, and speech enhancement.",
        "devin_body": r'''
## When to use

You are restoring, separating, generating, or analyzing audio for music, communications, or ambient sensing.

## Key concepts

- **Speech enhancement and denoising**: mask-based and generative approaches.
- **Source separation**: music demixing and speech separation.
- **Audio event detection and classification**: weakly supervised and transformer models.
- **Music generation**: symbolic and audio-domain diffusion and transformer models.
- **Audio super-resolution and bandwidth extension**: AERO, AEROMamba, and flow matching.

## Code pattern

```python
import torch
import torchaudio

waveform, sr = torchaudio.load("noisy.wav")
spec = torchaudio.transforms.Spectrogram(n_fft=512)(waveform)

mask = torch.sigmoid(model(spec))
enhanced = torchaudio.transforms.GriffinLim(n_fft=512)(spec * mask)
```

## Tuning notes

- Use loss functions aligned with human perception (PESQ, STOI, DNSMOS).
- Train on diverse noise and reverberation conditions.
- Avoid over-suppression of desired signals like music.
- Evaluate generalization on out-of-domain noise and speakers.

## Verification

1. Denoise speech and measure PESQ and STOI improvement over input.
2. Separate vocals from a music track and compute SDR.
3. Detect a set of audio events and compare F1 to a labeled test set.
''',
        "references": [
            "https://arxiv.org/abs/2409.09642",
            "https://arxiv.org/abs/2501.15417",
            "https://arxiv.org/abs/2504.09381",
            "https://arxiv.org/abs/2502.02942",
            "https://arxiv.org/abs/2505.19476",
        ],
    },
    {
        "name": "ai-for-video",
        "title": "AI for Video",
        "description": "Video understanding, action recognition, video generation, temporal modeling, video captioning, and multimodal video models.",
        "devin_body": r'''
## When to use

You are analyzing, generating, editing, or captioning video for content understanding, media, or robotics.

## Key concepts

- **Action recognition and localization**: 3D CNNs, transformers, and SlowFast.
- **Video generation and editing**: video diffusion and autoregressive models.
- **Temporal modeling**: long-range dependencies, optical flow, and motion.
- **Video-language models**: joint text-video understanding and retrieval.
- **Video pretraining**: contrastive, masked, and generative objectives.

## Code pattern

```python
import torch
import torch.nn as nn

video = torch.randn(2, 3, 16, 112, 112)  # (B, C, T, H, W)
model = nn.Conv3d(
    3, 64, kernel_size=(3, 7, 7), padding=(1, 3, 3)
)
features = model(video)
```

## Tuning notes

- Sample clips and augment spatial and temporal crops.
- Use sparse attention or factorized convolutions for long videos.
- Balance frame resolution, clip length, and batch size.
- Evaluate with video-specific metrics (FVD, IS, video mAP).

## Verification

1. Train an action-recognition model on a small video dataset.
2. Generate a short clip with a video diffusion model and compute FVD.
3. Build a video captioning pipeline and compare captions to references.
''',
        "references": [
            "https://arxiv.org/abs/2503.09642",
            "https://arxiv.org/abs/2502.04363",
            "https://arxiv.org/abs/2412.10255",
            "https://arxiv.org/abs/2504.12027",
            "https://arxiv.org/abs/2408.15241",
        ],
    },
    {
        "name": "ai-for-3d-vision",
        "title": "AI for 3D Vision",
        "description": "3D reconstruction, point cloud processing, NeRF and Gaussian splatting, depth estimation, 3D detection, and scene understanding.",
        "devin_body": r'''
## When to use

You need to reconstruct, represent, or interpret 3D geometry from images, point clouds, or depth sensors.

## Key concepts

- **Point cloud deep learning**: PointNet, PointNet++, DGCNN, and Point Transformer.
- **Neural radiance fields and 3D Gaussian splatting**: implicit and explicit scene representations.
- **Depth estimation**: monocular and stereo depth and completion.
- **3D object detection and segmentation**: VoteNet, PointRCNN, and 3D instance segmentation.
- **Surface reconstruction and registration**: traditional and learning-based methods.

## Code pattern

```python
import open3d as o3d

pcd = o3d.io.read_point_cloud("scene.ply")
pcd.estimate_normals(
    search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30)
)
o3d.io.write_point_cloud("scene_normals.ply", pcd)
```

## Tuning notes

- Normalize point clouds and handle varying density.
- Use multi-view consistency for depth and reconstruction.
- Combine geometric and photometric cues.
- Validate with Chamfer distance, F-score, or mAP on 3D benchmarks.

## Verification

1. Reconstruct a small object from multi-view images with NeRF or Gaussian splatting and render novel views.
2. Segment or classify a point cloud and report mIoU or accuracy.
3. Estimate depth from a monocular image and compare to ground truth.
''',
        "references": [
            "https://arxiv.org/abs/2210.00379",
            "https://doi.org/10.1007/s00371-023-03237-7",
            "https://arxiv.org/abs/2306.03000",
            "https://arxiv.org/abs/2301.13656",
            "https://arxiv.org/abs/2404.00714",
        ],
    },
    {
        "name": "ai-for-computer-vision",
        "title": "AI for Computer Vision",
        "description": "Image classification, detection, segmentation, vision-language models, generative vision, and efficient deep learning deployment.",
        "devin_body": r'''
## When to use

You are building visual perception systems for images: classification, detection, segmentation, vision-language, or image generation.

## Key concepts

- **Convolutional and transformer backbones**: ResNet, ViT, ConvNeXt, and EfficientNet.
- **Object detection and segmentation**: Faster R-CNN, YOLO, Mask R-CNN, and SAM.
- **Vision-language models**: CLIP, Flamingo, LLaVA, and Qwen-VL.
- **Generative vision**: GANs, diffusion models, and image editing.
- **Efficient deployment**: quantization, pruning, knowledge distillation, and NAS.

## Code pattern

```python
import torchvision
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from PIL import Image
import torchvision.transforms as T

model = fasterrcnn_resnet50_fpn(weights="DEFAULT").eval()
image = Image.open("scene.jpg").convert("RGB")
tensor = T.ToTensor()(image)
predictions = model([tensor])
```

## Tuning notes

- Use strong augmentations and pretrained backbones for small datasets.
- Choose model scale based on latency and accuracy trade-offs.
- Leverage foundation models with few-shot prompting or fine-tuning.
- Evaluate with mAP, mIoU, accuracy, and fairness metrics.

## Verification

1. Fine-tune an object detector on a custom dataset and report mAP.
2. Run a vision-language model on image QA and compare to a captioning baseline.
3. Apply a segmentation foundation model to a novel object category.
''',
        "references": [
            "https://arxiv.org/abs/2308.13998",
            "https://arxiv.org/abs/2403.17561",
            "https://arxiv.org/abs/2304.00685",
            "https://arxiv.org/abs/2111.07624",
            "https://arxiv.org/abs/2402.16369",
        ],
    },
    {
        "name": "ai-for-nlp",
        "title": "AI for NLP",
        "description": "Large language models, text classification, machine translation, question answering, information extraction, and prompt engineering.",
        "devin_body": r'''
## When to use

You are processing, generating, or understanding text for chatbots, search, translation, summarization, or information extraction.

## Key concepts

- **Transformer language models**: BERT, GPT, T5, and LLaMA.
- **Prompting and in-context learning**: zero and few-shot, chain-of-thought, and RAG.
- **Fine-tuning and alignment**: instruction tuning, RLHF, and DPO.
- **Information extraction and semantic parsing**: NER, relation extraction, and parsing.
- **Evaluation and safety**: perplexity, BLEU, ROUGE, toxicity, and bias.

## Code pattern

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf")

inputs = tokenizer("Summarize the following:", return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=128)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Tuning notes

- Use instruction and chat templates for dialog models.
- Combine retrieval augmentation to reduce hallucination.
- Balance context length, batch size, and learning rate for fine-tuning.
- Evaluate on task-specific benchmarks and human judgments.

## Verification

1. Fine-tune an LLM on a domain QA dataset and measure exact match and F1.
2. Build a RAG pipeline and compare answer accuracy to a pure LLM.
3. Run a prompt-engineering ablation and track performance across prompts.
''',
        "references": [
            "https://doi.org/10.48550/arxiv.2405.12819",
            "https://arxiv.org/abs/2402.06196",
            "https://arxiv.org/abs/2501.04040",
            "https://arxiv.org/abs/2503.06072",
        ],
    },
    {
        "name": "ai-for-human-robot-interaction",
        "title": "AI for Human-Robot Interaction",
        "description": "Multimodal interfaces, natural language instructions, shared autonomy, social robotics, and embodied AI for human-robot collaboration.",
        "devin_body": r'''
## When to use

You are designing robots that understand, plan, or communicate with humans via language, gestures, gaze, or shared control.

## Key concepts

- **Natural language and gesture understanding**: map multimodal commands to robot actions.
- **Task planning and grounding**: LLM and VLM agents that plan and perceive.
- **Shared autonomy and intent prediction**: adapt robot behavior to human intent.
- **Social and affective HRI**: trust, engagement, and personalization.
- **Safety and explainability**: legible motion, uncertainty, and human oversight.

## Code pattern

```python
from transformers import pipeline

qa = pipeline("question-answering")
context = "The mug is on the table next to the robot."
result = qa(question="Where is the mug?", context=context)
print(result["answer"])
```

## Tuning notes

- Ground language in the robot's perception and action space.
- Use feedback loops for clarification and error recovery.
- Consider cultural and individual differences in interaction.
- Evaluate with task success, human effort, and subjective trust.

## Verification

1. Build a system that maps a natural language command to a robot plan and execute it in simulation.
2. Run a user study comparing speech-only versus multimodal command success.
3. Implement an intent-prediction model and report accuracy in a shared workspace.
''',
        "references": [
            "https://arxiv.org/abs/2405.00693",
            "https://arxiv.org/abs/2401.03217",
            "https://arxiv.org/abs/2401.15174",
            "https://doi.org/10.48550/arxiv.2401.11838",
            "https://arxiv.org/abs/2307.10897",
        ],
    },
]
