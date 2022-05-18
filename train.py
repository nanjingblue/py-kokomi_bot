# 导入库
from model.model import *
from model.pre_process import *
import torch

# 读入数据
dataClass = Corpus('data/genshin.tsv', maxSentenceWordsNum=25)
# dataClass = Corpus('data/genshin.tsv', maxSentenceWordsNum=18)



device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 指定模型和一些超参
model = Seq2Seq(dataClass, featureSize=256, hiddenSize=256,
                attnType='L', attnMethod='concat',
                encoderNumLayers=5, decoderNumLayers=3,
                encoderBidirectional=True,
                device=device)
                # device=torch.device('cuda'))

# 训练
model.train(batchSize=1000, epoch=5000)
# model.train(batchSize=512, epoch=500)

# 保存模型
model.save('modelGenShin.pkl')
