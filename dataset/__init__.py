from .zjumocap import ZJUMoCapDataset
from .people_snapshot import PeopleSnapshotDataset
from .fd_dress import FDressDataset

def load_dataset(cfg, split='train'):
    dataset_dict = {
        'zjumocap': ZJUMoCapDataset,
        'people_snapshot': PeopleSnapshotDataset,
        '4Dress': FDressDataset,
    }
    return dataset_dict[cfg.name](cfg, split)
