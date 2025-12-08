from moviepy.editor import VideoFileClip


def change_video_speed(input_path, output_path, speed_factor):
    # 加载视频
    clip = VideoFileClip(input_path)

    # 变速 (speed_factor > 1 是加速, < 1 是减速)
    # 例如：2.0 是 2倍速，0.5 是 0.5倍速(慢放)
    final_clip = clip.speedx(speed_factor)

    # 保存视频
    final_clip.write_videofile(output_path, codec="libx264")


for episode in [3]:
    # 使用示例：把机器人视频加速 4 倍
    change_video_speed(f"task2/{episode}/openvla.mp4", f"task2/{episode}/openvla_3x.mp4", 3.0)
    change_video_speed(f"task2/{episode}/pi05.mp4", f"task2/{episode}/pi05_3x.mp4", 3.0)
    change_video_speed(f"task2/{episode}/ours.mp4", f"task2/{episode}/ours_3x.mp4", 3.0)