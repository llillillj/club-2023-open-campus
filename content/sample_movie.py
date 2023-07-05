from moviepy.editor import VideoFileClip
from make_gray import convert_folder_images_to_grayscale
from tqdm import tqdm
import os
current_path = os.path.dirname(os.path.abspath(__file__))
def extract_frames(video_path, output_folder, frames_per_second):
    clip = VideoFileClip(video_path)

    # ビデオの長さとフレームレートを取得
    duration = clip.duration
    fps = clip.fps

    # 指定したフレームレートに合わせてフレームを抽出する間隔を計算
    interval = max(round(fps / frames_per_second), 1)

    # 出力フォルダが存在しない場合は作成
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, frame in tqdm(enumerate(clip.iter_frames())):
        # 指定したフレーム間隔でフレームを保存
        if i % interval == 0:
            output_path = os.path.join(output_folder, f"frame_{i:03d}.jpg")
            clip.save_frame(output_path, t=i/fps)  # 指定したタイムスタンプでフレームを保存

        if (i + 1) / fps > duration:
            break

# 使用例
video_path = os.path.join(current_path, "10seconds_waterfall.mp4")  # 入力ビデオのパス
output_folder = os.path.join(current_path, "output_folder")  # 出力フォルダのパス
frames_per_second = 100  # 1秒間に抽出するフレーム数

extract_frames(video_path, output_folder, frames_per_second)
convert_folder_images_to_grayscale("output_folder")
