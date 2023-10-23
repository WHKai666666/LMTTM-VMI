from torch.utils.tensorboard import SummaryWriter
import os

log = "./log"
if os.path.exists(log) == False:
    os.mkdir(log)


class logger():
    def __init__(self, name) -> None:
        self.log_dir = os.path.join(log, name)
        self.writer = SummaryWriter(log_dir=self.log_dir)

    def get(self):
        return self.writer
