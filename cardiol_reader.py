import json
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


VLINE_KWARGS = { "color": "red", "linestyle": "--"}
DATA_PATH = Path("data")
RESULT_PATH = Path("results")


def plot_ecg(signal, revision):
    ecg_id = revision["ECG_ID"]
    reviewer_id = revision["reviewer_id"]

    plt.title(f"{ecg_id} by {reviewer_id}")
    plt.xlim(0, revision["episodes"][-1]["offset"])
    plt.plot(signal)


    episodes = revision["episodes"]
    rhythm_name_pos_y = min(signal)
    episode_offsets = [episode["offset"] for episode in episodes]
    for episode in episodes:
        plt.axvline(episode["onset"], **VLINE_KWARGS)
        plt.axvline(episode["offset"], **VLINE_KWARGS)

        rhythm_name_pos_x = (episode["onset"] + episode["offset"]) / 2
        plt.text(rhythm_name_pos_x, rhythm_name_pos_y,
                 episode["rhythm_name"], horizontalalignment="center", verticalalignment="bottom", rotation=0)


def save_fig(ecg_id, reviewer_id):
    if not RESULT_PATH.exists():
        RESULT_PATH.mkdir()

    ecg_id_path = RESULT_PATH / ecg_id
    if not ecg_id_path.exists():
        ecg_id_path.mkdir()
       
    file_path = ecg_id_path / str(reviewer_id)
    plt.savefig(file_path)
    print(f"\tRevision from reviewer {reviewer_id} was saved as {file_path}.png")



if __name__ == "__main__":
    ecg_files_paths = DATA_PATH.glob("*.ecg")
    ecg_ids = [file_name.stem for file_name in ecg_files_paths]
    print("Found ECGs files:\n" + '\n'.join(map(str, ecg_ids)), end="\n\n")

    for ecg_id in ecg_ids:
        ecg_file_content = np.fromfile(DATA_PATH.joinpath(f"{ecg_id}.ecg"), dtype="int16")
        
        print(f"Start saving ECGs revisions for {ecg_id}")
        revisions_files_paths = DATA_PATH.glob(f"{ecg_id}*.json")
        for revision_file_path in revisions_files_paths:
            with open(revision_file_path, "r") as rev_file:
                ecg_revision = json.load(rev_file)

            plot_ecg(ecg_file_content, ecg_revision)
            save_fig(ecg_id, ecg_revision["reviewer_id"])
            plt.close()

        print(f"ECGs revisions for {ecg_id} was saved", end="\n\n")
