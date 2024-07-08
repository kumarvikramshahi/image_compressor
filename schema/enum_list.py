from enum import Enum


class ImageProcessingStatus(str, Enum):
    STARTED_COMPRESSION = "started_compression"
    COMPRESSING = "compressing"
    STORING_COMPRESSED = "storing_compressed"
    COMPLETED = "completed"
    FAILED = "failed"
