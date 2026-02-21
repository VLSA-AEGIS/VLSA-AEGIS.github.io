import os
from moviepy.editor import VideoFileClip
import moviepy.video.fx.all as vfx  # 引入特效模块

folder_path = '.'

# --- 参数设置 ---
TARGET_WIDTH = 400  # 锁定宽度 400 像素
TARGET_FPS = 8  # 每秒 8 帧
SPEED_FACTOR = 3  # 播放速度设为 3 倍速


def convert_all_mp4_to_gif():
    mp4_files = [f for f in os.listdir(folder_path) if f.endswith('.mp4')]

    if not mp4_files:
        print("当前目录下没有找到 MP4 文件。")
        return

    print(f"找到 {len(mp4_files)} 个 MP4 文件，开始转换为 3倍速 GIF...")

    for filename in mp4_files:
        input_path = os.path.join(folder_path, filename)
        output_path = os.path.join(folder_path, filename.replace('.mp4', '.gif'))

        print(f"正在处理: {filename} ...")

        try:
            # 1. 加载原视频
            clip = VideoFileClip(input_path)

            # 2. 关键步：应用 3 倍速特效
            fast_clip = clip.fx(vfx.speedx, SPEED_FACTOR)

            # 3. 缩放分辨率（限制宽度）
            resized_clip = fast_clip.resize(width=TARGET_WIDTH)

            # 4. 导出 GIF
            resized_clip.write_gif(output_path, fps=TARGET_FPS, logger=None)

            # 5. 释放内存
            clip.close()
            fast_clip.close()
            resized_clip.close()

            print(f"✅ 完成: {filename}")

        except Exception as e:
            print(f"❌ 转换 {filename} 失败，错误信息: {e}")


if __name__ == "__main__":
    convert_all_mp4_to_gif()
    print("所有转换任务结束！")