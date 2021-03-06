from torch import nn
from baseline.models.MobileLiteNet import MobileLiteNet54, MobileLiteNet54_se
from .fishnet import FishNet150
from baseline.models.FeatherNet import FeatherNetA, FeatherNetB
from torchvision.models import MobileNetV2


class Ensemble(nn.Module):
    def __init__(self, device, num_classes=2):
        super(Ensemble, self).__init__()

        self.num_classes = num_classes
        self.models = [FeatherNetA().to(device),
                       FeatherNetB().to(device),
                       FishNet150(num_cls=self.num_classes).to(device),
                       MobileNetV2(num_classes=self.num_classes).to(device),
                       MobileLiteNet54().to(device),
                       MobileLiteNet54_se().to(device)]
        self.device = device

    def forward(self, x):
        return sum(map(lambda m: m(x), self.models))
