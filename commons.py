import io

import torch
import torch.nn as nn
from torchvision import models
from PIL import Image
import torchvision.transforms as transforms

def get_model():
	checkpoint_path = '/Users/julia_kaplan/flask-skin/templates/.ipynb_checkpoints/Project2CodeForNewImage-checkpoint.ipynb'
	model = models. densenet161(pretrained=True)
	model.classifier = nn.Linear(2208, 102)
	model.load_state_dict(torch.load(
		checkpoint_path, map_location='cpu'), strict=False)
	model.eval()
	return model

def get_tensor(image_bytes):
	my_transforms = transforms.Compose([transforms.Resize(224),
        				    transforms.CenterCrop(224),
        				    transforms.ToTensor(),
        				    transforms.Normalize(mean=[0.4914, 0.4822, 0.4465], 
                             					  std=[0.2023, 0.1994, 0.2010])])
	image = Image.open(io.BytesIO(image_bytes))
	return my_transforms(image).unsqueeze(0)
