import cv2
import os


def crop_videos_cv2():
    # 需要处理的文件列表
    files = [
        "freecompress-cup_I.mp4",
        "freecompress-cup_II.mp4",
        "freecompress-apple_I.mp4",
        "freecompress-apple_II.mp4"
    ]

    current_dir = os.getcwd()  # 获取当前工作目录
    crop_w = 1111  # 目标裁剪宽度

    print(f"当前工作目录: {current_dir}")

    for filename in files:
        input_path = os.path.join(current_dir, filename)

        # 1. 检查文件是否存在
        if not os.path.exists(input_path):
            print(f"⚠️ 跳过: 找不到文件 {input_path}")
            continue

        # 2. 初始化视频读取
        cap = cv2.VideoCapture(input_path)

        if not cap.isOpened():
            print(f"❌ 无法打开视频: {filename}")
            continue

        # 获取原视频参数
        original_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        original_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # 3. 设置输出参数
        # 如果原视频宽度小于1111，则只裁剪到原视频宽度（防止报错）
        actual_crop_w = min(crop_w, original_w)

        output_filename = filename.replace(".mp4", "_cropped.mp4")
        output_path = os.path.join(current_dir, output_filename)

        # 视频编码格式：'mp4v' 是 mp4 的通用编码，在 Windows 上兼容性较好
        fourcc = cv2.VideoWriter_fourcc(*'avc1')
        out = cv2.VideoWriter(output_path, fourcc, fps, (actual_crop_w, original_h))

        print(f"正在处理: {filename} ({total_frames} 帧)...")
        print(f"  - 原始尺寸: {original_w}x{original_h}")
        print(f"  - 裁剪尺寸: {actual_crop_w}x{original_h}")

        frame_count = 0

        # 4. 逐帧处理
        while True:
            ret, frame = cap.read()
            if not ret:
                break  # 视频结束

            # [y_start:y_end, x_start:x_end]
            # 保留高度 0到h (全部)，宽度 0到1111
            cropped_frame = frame[0:original_h, 0:actual_crop_w]

            out.write(cropped_frame)
            frame_count += 1

            # 每100帧打印一次进度，防止看起来像卡死了
            if frame_count % 100 == 0:
                print(f"    已处理: {frame_count}/{total_frames}", end='\r')

        # 5. 释放资源
        cap.release()
        out.release()
        print(f"\n✅ 完成: {output_filename}\n")

    print("所有任务处理完毕。")


if __name__ == "__main__":
    crop_videos_cv2()