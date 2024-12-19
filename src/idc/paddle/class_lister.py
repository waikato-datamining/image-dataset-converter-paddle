from typing import List, Dict


def list_classes() -> Dict[str, List[str]]:
    return {
        "seppl.io.Reader": [
            "idc.paddle.reader.imgcls",
        ],
        "seppl.io.Writer": [
            "idc.paddle.writer.imgcls",
        ],
    }
