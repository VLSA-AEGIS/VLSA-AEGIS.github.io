import os
from moviepy.editor import VideoFileClip


def crop_mute_compress():
    # 1. 定义你的两个文件夹路径
    base_dirs = {
        "Baseline": "./real_world/baseline",
        "Ours": "./real_world/ours"
    }

    # 2. 定义需要处理的文件名列表
    target_files = [
        "freecompress-cup_I.mp4",
        "freecompress-cup_II.mp4",
        "freecompress-apple_I.mp4",
        "freecompress-apple_II.mp4"
    ]

    print("🚀 开始处理：裁剪 + 去音 + 强力压缩 (Web兼容模式)...")

    for label, folder_path in base_dirs.items():
        if not os.path.exists(folder_path):
            print(f"⚠️ 跳过: 找不到文件夹 {folder_path}")
            continue

        for filename in target_files:
            input_path = os.path.join(folder_path, filename)

            # 检查源文件是否存在
            if not os.path.exists(input_path):
                print(f"⚠️ 缺失: {filename} 在 {label} 中没找到")
                continue

            # 定义输出文件名 (例如 freecompress-cup_I_cropped.mp4)
            # 注意：这里直接覆盖你之前生成的那个 40M 的大文件，或者你可以改名
            output_filename = filename.replace(".mp4", "_cropped.mp4")
            output_path = os.path.join(folder_path, output_filename)

            print(f"\n🎥 正在处理 [{label}] {filename} ...")

            try:
                # --- 核心步骤 ---

                # 1. 加载视频
                clip = VideoFileClip(input_path)

                # 2. 裁剪 (x从0到1111, 高度保持不变)
                cropped_clip = clip.crop(x1=0, x2=1111)

                # 3. 保存
                # codec="libx264": 网页通用编码，体积小
                # audio=False: **彻底移除声音**
                # preset="slow": 压缩率更高 (文件更小)
                # threads=4: 加快处理速度
                cropped_clip.write_videofile(
                    output_path,
                    codec="libx264",
                    audio=False,  # <--- 这里去掉声音
                    preset="slow",  # <--- 这里保证体积小
                    verbose=False,
                    logger=None  # 不显示乱七八糟的进度条，只看结果
                )

                # 释放内存
                clip.close()
                cropped_clip.close()

                print(f"✅ 成功: {output_filename} (已静音)")

            except Exception as e:
                print(f"❌ 失败: {e}")

    print("\n🎉 全部搞定！现在的视频应该是体积小、无声且网页可播放的了。")


if __name__ == "__main__":
    crop_mute_compress()