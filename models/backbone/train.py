import os
from random import seed

import numpy as np
import torch

from config import cfg

# seed随便赋一个值
seed = 42  # 设置一个随机数种子值

# ------------prepare enviroment------------
if seed is not None:
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)

gpus = cfg.GPU_ID
if len(gpus) == 1:
    torch.cuda.set_device(gpus[0])

torch.backends.cudnn.benchmark = True

# ------------prepare data loader------------
data_mode = cfg.DATASET
if data_mode is 'SHHA':
    from datasets.SHHA.loading_data import loading_data
    from datasets.SHHA.setting import cfg_data
elif data_mode is 'SHHB':
    from datasets.SHHB.loading_data import loading_data
    from datasets.SHHB.setting import cfg_data
elif data_mode is 'QNRF':
    from datasets.QNRF.loading_data import loading_data
    from datasets.QNRF.setting import cfg_data
elif data_mode is 'UCF50':
    from datasets.UCF50.loading_data import loading_data
    from datasets.UCF50.setting import cfg_data

# ------------Prepare Trainer------------
net = cfg.NET
if net in ['MCNN', 'Res50', 'CSRNet']:
    from trainer import Trainer

# ------------Start Training------------
pwd = os.path.split(os.path.realpath(__file__))[0]
cc_trainer = Trainer(loading_data, cfg_data, pwd)
cc_trainer.forward()
