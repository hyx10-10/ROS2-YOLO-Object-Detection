import cv2
import os
# 1. 自动创建多级数据目录
save_dir = "dataset/images/raw_capture"
os.makedirs(save_dir, exist_ok=True)
# 2. 挂载摄像头 (通常 0 为笔记本自带，外接可能为 2 或 4)
cap = cv2.VideoCapture(0)
# 设置分辨率以匹配推理要求 (可选)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
idx = 0
print("=== 采集程序启动 ===")
print("[S] 键保存当前帧 | [Q] 键安全退出")
while True:
    ret, frame = cap.read()
    if not ret:
        print("[Error] 无法从摄像头读取画面，请检查物理连接。")
        break
    # 镜像翻转画面 (便于人类直观操作，若不需要可注释)
    # frame = cv2.flip(frame, 1) 
    
    cv2.imshow("Robot Vision Capture", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("s"):
        # 使用 5 位定长数字格式化文件名，如 img_00042.jpg
        name = os.path.join(save_dir, f"img_{idx:05d}.jpg")
        cv2.imwrite(name, frame)
        print(f"[Success] 已保存关键帧: {name}")
        idx += 1
    elif key == ord("q"):
        print("=== 采集结束 ===")
        break
# 3. 释放底层硬件资源
cap.release()
cv2.destroyAllWindows()